import unittest
from unittest.mock import patch, MagicMock
from django.test import TestCase
from django.core.files.base import ContentFile

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.api.serializers import (
    LessonAssetSerializer, LessonAssetBriefSerializer, LessonBlockV2Serializer, LessonV2Serializer
)
from curriculum.media_orchestration.providers.wikimedia import WikimediaProvider
from curriculum.media_orchestration.search_intelligence.models import SearchPayload
from curriculum.media_orchestration.visual_intelligence.models import VisualSpecification
from curriculum.media_orchestration.visual_intelligence.renderer import VisualRenderer
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import (
    validate_svg_structure, sanitize_svg, validate_and_sanitize_svg, save_svg_as_lesson_asset
)


class TestBatch1WikimediaRepairs(unittest.TestCase):
    """Tests for R1, R2, R3 in WikimediaProvider."""

    def test_r1_user_agent_configured(self):
        provider = WikimediaProvider()
        user_agent = provider.session.headers.get('User-Agent', '')
        self.assertTrue(len(user_agent) > 0, "User-Agent header must be set")
        self.assertIn("VLearnEducation", user_agent)
        self.assertIn("contact@vlearn.co.ke", user_agent)

    @patch('curriculum.media_orchestration.providers.wikimedia.requests.Session.get')
    def test_r2_thumbnail_and_r3_metadata_extraction(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "query": {
                "pages": {
                    "12345": {
                        "pageid": 12345,
                        "title": "File:Boyle Law Apparatus 1890.jpg",
                        "imageinfo": [{
                            "url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Boyle_Law_Apparatus_1890.jpg",
                            "thumburl": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Boyle_Law_Apparatus_1890.jpg/800px-Boyle_Law_Apparatus_1890.jpg",
                            "width": 1200,
                            "height": 900,
                            "extmetadata": {
                                "LicenseShortName": {"value": "CC BY-SA 4.0"},
                                "LicenseUrl": {"value": "https://creativecommons.org/licenses/by-sa/4.0"},
                                "Artist": {"value": "<b>John Smith</b>"},
                                "Credit": {"value": "Science History Institute"},
                                "ImageDescription": {"value": "Historical Boyle law apparatus."}
                            }
                        }]
                    }
                }
            }
        }
        mock_get.return_value = mock_response

        provider = WikimediaProvider()
        payload = SearchPayload(
            primary_query="Boyle law apparatus",
            alternate_queries=[],
            preferred_media_category="Real-world Visualization",
            is_suitable_for_wikimedia=True
        )

        assets = provider._execute_search("Boyle law apparatus", "node_1")

        # Verify API request parameters (R2)
        mock_get.assert_called_once()
        _, kwargs = mock_get.call_args
        params = kwargs.get('params', {})
        self.assertIn("thumburl", params.get('iiprop', ''))
        self.assertEqual(params.get('iiurlwidth'), 800)

        # Verify results
        self.assertEqual(len(assets), 1)
        asset = assets[0]

        # R2: URL should prefer the 800px thumbnail
        self.assertEqual(asset.url, "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Boyle_Law_Apparatus_1890.jpg/800px-Boyle_Law_Apparatus_1890.jpg")
        self.assertEqual(asset.metadata.get('raw_url'), "https://upload.wikimedia.org/wikipedia/commons/1/1a/Boyle_Law_Apparatus_1890.jpg")
        self.assertEqual(asset.metadata.get('thumb_url'), "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Boyle_Law_Apparatus_1890.jpg/800px-Boyle_Law_Apparatus_1890.jpg")

        # R3: Commons page URL and attribution metadata preserved
        self.assertEqual(asset.metadata.get('commons_page_url'), "https://commons.wikimedia.org/wiki/File:Boyle_Law_Apparatus_1890.jpg")
        self.assertEqual(asset.author, "John Smith")  # HTML stripped
        self.assertEqual(asset.licensing, "CC BY-SA 4.0")
        self.assertEqual(asset.attribution, "Science History Institute")
        self.assertEqual(asset.metadata.get('author'), "John Smith")
        self.assertEqual(asset.metadata.get('licensing'), "CC BY-SA 4.0")


class TestBatch1SvgSafetyAndStorage(TestCase):
    """Tests for SVG validation, sanitization, and LessonAsset.file storage."""

    def setUp(self):
        self.curriculum = Curriculum.objects.create(name="844", description="Kenyan 8-4-4")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Form 4", level=4)
        self.subject = Subject.objects.create(grade=self.grade, name="Chemistry")
        self.topic = Topic.objects.create(subject=self.subject, name="Acids, Bases and Salts", order=1)
        self.unit = LearningUnit.objects.create(topic=self.topic, name="Unit 1: Electrolytes", order=1)
        self.lesson = Lesson.objects.create(
            topic=self.topic,
            learning_unit=self.unit,
            title="Electrolytic Conduction",
            status="published"
        )
        self.block = LessonBlock.objects.create(
            lesson=self.lesson,
            block_id="block_test_1",
            block_type="suggested_diagram",
            title="Electrolysis Cell Diagram",
            content={"text": "Diagram of electrolysis apparatus"},
            order=1,
            page_number=1,
            page_title="Electrolysis Setup"
        )

    def test_valid_svg_structure(self):
        valid_svg = '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="40" fill="blue"/></svg>'
        is_valid, err = validate_svg_structure(valid_svg)
        self.assertTrue(is_valid)
        self.assertEqual(err, "")

    def test_invalid_svg_structure(self):
        invalid_svg = '<div class="svg-container"><circle cx="50" cy="50" r="40"/></div>'
        is_valid, err = validate_svg_structure(invalid_svg)
        self.assertFalse(is_valid)
        self.assertIn("start with", err)

    def test_svg_sanitization_removes_scripts_and_handlers(self):
        malicious_svg = (
            '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" onload="alert(\'xss\')">'
            '<script>alert("evil")</script>'
            '<foreignObject width="100" height="100"><iframe src="https://evil.com"></iframe></foreignObject>'
            '<a href="javascript:alert(\'hack\')"><rect width="50" height="50" fill="red" onclick="exploit()"/></a>'
            '</svg>'
        )

        is_valid, sanitized, err = validate_and_sanitize_svg(malicious_svg)
        self.assertTrue(is_valid)
        self.assertIsNone(err)

        # Verify dangerous elements were completely stripped
        self.assertNotIn("<script", sanitized)
        self.assertNotIn("onload=", sanitized)
        self.assertNotIn("onclick=", sanitized)
        self.assertNotIn("<foreignObject", sanitized)
        self.assertNotIn("javascript:", sanitized)
        self.assertTrue(sanitized.startswith("<svg"))
        self.assertTrue(sanitized.endswith("</svg>"))

    def test_renderer_with_sanitized_svg(self):
        spec = VisualSpecification(
            node_id="test_node_sec",
            format="svg",
            code='<svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="80" fill="green" onmouseover="attack()"/><script>bad()</script></svg>',
            explanation="Safe circle diagram",
            alt_text="Circle Diagram"
        )
        visual, failure = VisualRenderer.render(spec)
        self.assertIsNotNone(visual)
        self.assertIsNone(failure)
        self.assertNotIn("<script", visual.raw_code)
        self.assertNotIn("onmouseover", visual.raw_code)
        self.assertIn("<circle", visual.raw_code)

    def test_save_svg_as_lesson_asset_file(self):
        svg_code = '<svg viewBox="0 0 100 100"><rect width="80" height="80" fill="purple"/></svg>'
        asset, err = save_svg_as_lesson_asset(
            lesson=self.lesson,
            svg_code=svg_code,
            title="Purple Box Diagram",
            description="A test apparatus diagram",
            metadata={"test_key": "test_value"},
            alt_text="Purple Box"
        )

        self.assertIsNone(err)
        self.assertIsNotNone(asset)
        self.assertEqual(asset.asset_type, "diagram")
        self.assertEqual(asset.source_type, "ai_generated")
        self.assertEqual(asset.storage_type, "file")
        self.assertEqual(asset.status, "attached")
        self.assertTrue(bool(asset.file))
        self.assertIn("lesson_assets", asset.file.name)

        # Link to block and test serializer
        asset.blocks.add(self.block)
        serializer = LessonBlockV2Serializer(self.block)
        data = serializer.data
        self.assertEqual(len(data['assets']), 1)
        brief = data['assets'][0]
        self.assertIsNotNone(brief['file'])
        self.assertTrue("lesson_assets" in brief['file'])
        self.assertEqual(brief['metadata'].get('render_format'), 'svg')
        self.assertTrue(brief['metadata'].get('enrichment_agent'))


class TestBatch1SerializationAndPrefetch(TestCase):
    """Tests for R4 prefetch and serializer contracts."""

    def setUp(self):
        self.curriculum = Curriculum.objects.create(name="844", description="Kenyan 8-4-4")
        self.grade = Grade.objects.create(curriculum=self.curriculum, name="Form 4", level=4)
        self.subject = Subject.objects.create(grade=self.grade, name="Chemistry")
        self.topic = Topic.objects.create(subject=self.subject, name="Electrochemistry", order=1)
        self.unit = LearningUnit.objects.create(topic=self.topic, name="Unit 1: Cells", order=1)
        self.lesson = Lesson.objects.create(
            topic=self.topic,
            learning_unit=self.unit,
            title="Galvanic Cells",
            status="published"
        )
        self.block = LessonBlock.objects.create(
            lesson=self.lesson,
            block_id="block_galvanic_1",
            block_type="suggested_diagram",
            title="Daniell Cell Setup",
            content={"text": "Diagram of Zinc-Copper cell"},
            order=1,
            page_number=1,
            page_title="Daniell Cell"
        )
        self.asset = LessonAsset.objects.create(
            lesson=self.lesson,
            asset_type="image",
            source_type="external",
            storage_type="url",
            status="attached",
            title="Daniell Cell Diagram",
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Daniell_cell.svg/800px-Daniell_cell.svg.png",
            metadata={
                "author": "Science Author",
                "licensing": "CC BY-SA 3.0",
                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Daniell_cell.svg"
            }
        )
        self.asset.blocks.add(self.block)

    def test_lesson_v2_serializer_includes_inline_block_assets(self):
        # Query with prefetch as configured in ActiveLessonView
        lesson = (
            Lesson.objects
            .filter(id=self.lesson.id)
            .prefetch_related('blocks', 'blocks__assets', 'assets')
            .first()
        )

        data = LessonV2Serializer(lesson).data
        self.assertEqual(len(data['blocks']), 1)
        block_data = data['blocks'][0]
        self.assertEqual(len(block_data['assets']), 1)
        asset_data = block_data['assets'][0]

        # Verify attribution metadata survives through serialization
        self.assertEqual(asset_data['url'], "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Daniell_cell.svg/800px-Daniell_cell.svg.png")
        self.assertEqual(asset_data['metadata']['author'], "Science Author")
        self.assertEqual(asset_data['metadata']['licensing'], "CC BY-SA 3.0")
        self.assertEqual(asset_data['metadata']['commons_page_url'], "https://commons.wikimedia.org/wiki/File:Daniell_cell.svg")
