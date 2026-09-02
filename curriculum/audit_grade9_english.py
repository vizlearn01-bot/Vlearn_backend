import os
import sys
import re
import json
import xml.etree.ElementTree as ET
import urllib.request
import urllib.error
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
import django
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

import curriculum.cbc_grade9_english_topic1_svgs as t1_svgs
import curriculum.cbc_grade9_english_topic2_svgs as t2_svgs
import curriculum.cbc_grade9_english_topic3_svgs as t3_svgs
import curriculum.cbc_grade9_english_topic4_svgs as t4_svgs

def audit_svg_modules():
    print("=== 1. AUDITING SVG MODULES & DATABASE ASSETS ===")
    
    topic_modules = [
        ("Topic 1", t1_svgs, 8),
        ("Topic 2", t2_svgs, 7),
        ("Topic 3", t3_svgs, 8),
        ("Topic 4", t4_svgs, 7)
    ]
    
    total_svgs = 0
    svg_errors = []
    
    for t_name, mod, expected_count in topic_modules:
        svg_vars = [k for k in dir(mod) if k.startswith("SVG_")]
        count = len(svg_vars)
        total_svgs += count
        print(f"[{t_name}] Module contains {count} SVG constants (Expected: {expected_count})")
        if count != expected_count:
            svg_errors.append(f"{t_name} count mismatch: got {count}, expected {expected_count}")
            
        for var_name in svg_vars:
            svg_code = getattr(mod, var_name)
            try:
                root = ET.fromstring(svg_code)
                if not root.tag.endswith('svg'):
                    svg_errors.append(f"Root is not <svg> in {t_name} constant {var_name}")
                viewbox = root.attrib.get('viewBox', '')
                if not viewbox.startswith('0 0 800'):
                    svg_errors.append(f"viewBox '{viewbox}' does not start with '0 0 800' in {t_name} constant {var_name}")
            except Exception as e:
                svg_errors.append(f"XML parse error in {t_name} constant {var_name}: {str(e)}")
                
    # Check database LessonAsset records of type 'diagram'
    topics = Topic.objects.filter(subject_id=51).order_by('order')
    lesson_ids = Lesson.objects.filter(topic__in=topics).values_list('id', flat=True)
    db_svgs = LessonAsset.objects.filter(lesson_id__in=lesson_ids, asset_type='diagram')
    print(f"Database contains {db_svgs.count()} 'diagram' LessonAsset records (Expected 30).")
    
    for asset in db_svgs:
        svg_content = asset.metadata.get('svg_content', '') if isinstance(asset.metadata, dict) else ''
        if not svg_content:
            svg_errors.append(f"DB Asset ID {asset.id} ({asset.title}) missing metadata['svg_content']")
            continue
        try:
            root = ET.fromstring(svg_content)
            if not root.tag.endswith('svg'):
                svg_errors.append(f"DB Asset ID {asset.id} root is not <svg>")
            viewbox = root.attrib.get('viewBox', '')
            if not viewbox.startswith('0 0 800'):
                svg_errors.append(f"DB Asset ID {asset.id} viewBox '{viewbox}' does not start with '0 0 800'")
        except Exception as e:
            svg_errors.append(f"DB Asset ID {asset.id} ({asset.title}) XML parse error: {str(e)}")
            
    print(f"Total SVGs verified (Module Constants + DB Records): {total_svgs + db_svgs.count()}. Errors found: {len(svg_errors)}")
    for err in svg_errors:
        print("  - ERROR:", err)
    return svg_errors

def audit_database_structure():
    print("\n=== 2. AUDITING DATABASE STRUCTURE (Grade 9 English, Grade ID 18, Subject ID 51) ===")
    grade = Grade.objects.filter(id=18).first()
    subject = Subject.objects.filter(id=51).first()
    print(f"Grade: {grade.name if grade else 'NOT FOUND'} (ID: {grade.id if grade else 'None'})")
    print(f"Subject: {subject.name if subject else 'NOT FOUND'} (ID: {subject.id if subject else 'None'})")
    
    topics = Topic.objects.filter(subject_id=51).order_by('order')
    print(f"Found {topics.count()} topics for Subject 51.")
    
    structure_errors = []
    total_lessons = 0
    total_pages = 0
    total_blocks = 0
    total_mcqs = 0
    
    expected_topics = {
        1: ("Listening and Speaking", 8),
        2: ("Reading and Literature", 7),
        3: ("Grammar in Use", 8),
        4: ("The Writing Process and Composition", 7)
    }
    
    for topic in topics:
        exp_title, exp_lesson_count = expected_topics.get(topic.order, ("", 0))
        units = LearningUnit.objects.filter(topic=topic).order_by('order')
        lessons = Lesson.objects.filter(topic=topic).order_by('learning_unit__order')
        print(f"Topic {topic.order}: '{topic.name}' -> {units.count()} LearningUnits, {lessons.count()} Lessons (Expected: {exp_lesson_count})")
        
        if lessons.count() != exp_lesson_count:
            structure_errors.append(f"Topic {topic.order} has {lessons.count()} lessons, expected {exp_lesson_count}")
            
        for lesson in lessons:
            total_lessons += 1
            blocks = LessonBlock.objects.filter(lesson=lesson).order_by('page_number', 'order')
            page_numbers = sorted(list(set(b.page_number for b in blocks if b.page_number is not None)))
            total_pages += len(page_numbers)
            total_blocks += blocks.count()
            
            if page_numbers != [1, 2, 3, 4, 5, 6]:
                structure_errors.append(f"Lesson '{lesson.title}' (ID {lesson.id}) has pages {page_numbers}, expected [1, 2, 3, 4, 5, 6]")
                
            # Component type checks
            p1_types = [b.component_type for b in blocks.filter(page_number=1)]
            p2_types = [b.component_type for b in blocks.filter(page_number=2)]
            p3_types = [b.component_type for b in blocks.filter(page_number=3)]
            p4_types = [b.component_type for b in blocks.filter(page_number=4)]
            p5_types = [b.component_type for b in blocks.filter(page_number=5)]
            p6_types = [b.component_type for b in blocks.filter(page_number=6)]
            
            # P1: suggested_image, learning_goal
            if 'suggested_image' not in p1_types or 'learning_goal' not in p1_types:
                structure_errors.append(f"T{topic.order}.L{lesson.learning_unit.order} '{lesson.title}' P1 missing required components: {p1_types}")
            # P2: definition or table
            if 'definition_card' not in p2_types and 'key_definitions' not in p2_types and 'comparison_table' not in p2_types:
                structure_errors.append(f"T{topic.order}.L{lesson.learning_unit.order} '{lesson.title}' P2 missing definitions/table: {p2_types}")
            # P3: diagram / worked example
            if 'suggested_diagram' not in p3_types and 'diagram' not in p3_types and 'worked_example' not in p3_types:
                structure_errors.append(f"T{topic.order}.L{lesson.learning_unit.order} '{lesson.title}' P3 missing diagram/worked_example: {p3_types}")
            # P4: video & practice/real world
            if 'suggested_video' not in p4_types or ('activity_prompt' not in p4_types and 'real_world_example' not in p4_types):
                structure_errors.append(f"T{topic.order}.L{lesson.learning_unit.order} '{lesson.title}' P4 missing suggested_video/activity: {p4_types}")
            # P5: mistakes/misconceptions & step_process/worked_example/guided_practice
            if ('common_misconceptions' not in p5_types and 'common_mistake' not in p5_types and 'common_mistakes' not in p5_types and 'concept_explanation' not in p5_types):
                structure_errors.append(f"T{topic.order}.L{lesson.learning_unit.order} '{lesson.title}' P5 missing common_mistakes: {p5_types}")
            # P6: knowledge_check and summary
            if p6_types.count('knowledge_check') != 2 or ('summary' not in p6_types and 'summary_card' not in p6_types):
                structure_errors.append(f"T{topic.order}.L{lesson.learning_unit.order} '{lesson.title}' P6 missing 2 knowledge_checks or summary: {p6_types}")
                
            # Audit MCQs on Page 6
            mcqs = blocks.filter(page_number=6, component_type='knowledge_check').order_by('order')
            for mcq in mcqs:
                total_mcqs += 1
                c = mcq.content
                opts = c.get('options', [])
                # Could be 'answer', 'correct_answer'
                ans = c.get('answer', c.get('correct_answer', ''))
                exp = c.get('explanation', '')
                
                if len(opts) != 4:
                    structure_errors.append(f"MCQ in T{topic.order}.L{lesson.learning_unit.order} '{lesson.title}' has {len(opts)} options, expected 4")
                
                # Check valid answer representation (either 'A'/'B'/'C'/'D', index 0..3, or matches one of options)
                is_valid_ans = False
                if ans in ['A', 'B', 'C', 'D']:
                    is_valid_ans = True
                elif ans in [0, 1, 2, 3]:
                    is_valid_ans = True
                elif ans in opts:
                    is_valid_ans = True
                    
                if not is_valid_ans:
                    structure_errors.append(f"MCQ in T{topic.order}.L{lesson.learning_unit.order} '{lesson.title}' has invalid answer '{ans}'")
                if not exp or len(str(exp).strip()) == 0:
                    structure_errors.append(f"MCQ in T{topic.order}.L{lesson.learning_unit.order} '{lesson.title}' has empty explanation")

    print(f"Total Lessons: {total_lessons} (Expected: 30)")
    print(f"Total Pages: {total_pages} (Expected: 180)")
    print(f"Total Blocks: {total_blocks} (Expected: 442)")
    print(f"Total MCQs: {total_mcqs} (Expected: 60)")
    print(f"Structure Errors Found: {len(structure_errors)}")
    for err in structure_errors:
        print("  - ERROR:", err)
    return structure_errors

def audit_citation_brackets():
    print("\n=== 3. AUDITING CITATION BRACKETS (e.g., [21], [367]) ===")
    citation_regex = re.compile(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]')
    citation_errors = []
    
    topics = Topic.objects.filter(subject_id=51)
    lessons = Lesson.objects.filter(topic__in=topics)
    blocks = LessonBlock.objects.filter(lesson__in=lessons)
    
    for block in blocks:
        if block.title and citation_regex.search(block.title):
            citation_errors.append(f"Citation bracket in Title: L '{block.lesson.title}' P{block.page_number} Block {block.id}: '{block.title}'")
        
        def check_nested(val, path=""):
            if isinstance(val, str):
                m = citation_regex.search(val)
                if m:
                    citation_errors.append(f"Citation bracket '{m.group(0)}' in L '{block.lesson.title}' P{block.page_number} Block {block.id} at {path}")
            elif isinstance(val, dict):
                for k, v in val.items():
                    check_nested(v, f"{path}.{k}")
            elif isinstance(val, list):
                for idx, item in enumerate(val):
                    check_nested(item, f"{path}[{idx}]")
                    
        check_nested(block.content, "content")
            
    print(f"Citation errors found: {len(citation_errors)}")
    for err in citation_errors:
        print("  - ERROR:", err)
    return citation_errors

def audit_youtube_videos():
    print("\n=== 4. AUDITING YOUTUBE VIDEO ASSETS ===")
    topics = Topic.objects.filter(subject_id=51).order_by('order')
    lesson_ids = Lesson.objects.filter(topic__in=topics).values_list('id', flat=True)
    video_assets = LessonAsset.objects.filter(lesson_id__in=lesson_ids, asset_type='youtube').order_by('lesson__topic__order', 'lesson__learning_unit__order')
    
    print(f"Found {video_assets.count()} YouTube LessonAsset records.")
    
    video_results = []
    
    for asset in video_assets:
        # Check url or metadata
        video_id = asset.metadata.get('youtube_id') if isinstance(asset.metadata, dict) else None
        if not video_id and asset.url:
            # Parse from url: https://www.youtube.com/watch?v=xxx or https://youtu.be/xxx
            if 'watch?v=' in asset.url:
                video_id = asset.url.split('watch?v=')[1].split('&')[0]
            elif 'youtu.be/' in asset.url:
                video_id = asset.url.split('youtu.be/')[1].split('?')[0]
            else:
                video_id = asset.url
        
        title = asset.title
        lesson = asset.lesson
        topic_num = lesson.topic.order
        unit_num = lesson.learning_unit.order
        
        oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
        req = urllib.request.Request(
            oembed_url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    yt_title = data.get('title')
                    author_name = data.get('author_name')
                    video_results.append({
                        "topic_num": topic_num,
                        "unit_num": unit_num,
                        "lesson_title": lesson.title,
                        "video_id": video_id,
                        "asset_title": title,
                        "yt_title": yt_title,
                        "author": author_name,
                        "status": "VALID"
                    })
                    print(f"  [OK] T{topic_num}.L{unit_num:02d} ({video_id}): '{yt_title}' | Channel: {author_name}")
        except urllib.error.HTTPError as e:
            video_results.append({
                "topic_num": topic_num,
                "unit_num": unit_num,
                "lesson_title": lesson.title,
                "video_id": video_id,
                "asset_title": title,
                "status": f"HTTP {e.code}",
                "error": str(e)
            })
            print(f"  [FAIL] T{topic_num}.L{unit_num:02d} ({video_id}): HTTP {e.code}")
        except Exception as e:
            video_results.append({
                "topic_num": topic_num,
                "unit_num": unit_num,
                "lesson_title": lesson.title,
                "video_id": video_id,
                "asset_title": title,
                "status": "ERROR",
                "error": str(e)
            })
            print(f"  [ERROR] T{topic_num}.L{unit_num:02d} ({video_id}): {str(e)}")
            
    return video_results

if __name__ == '__main__':
    audit_svg_modules()
    audit_database_structure()
    audit_citation_brackets()
    results = audit_youtube_videos()
    
    invalid = [r for r in results if r['status'] != 'VALID']
    print(f"\nYouTube Validation Summary: {len(results)-len(invalid)}/{len(results)} VALID.")
    if invalid:
        print(f"Found {len(invalid)} invalid/unavailable videos:")
        for inv in invalid:
            print(f"  - T{inv['topic_num']}.L{inv['unit_num']} '{inv['lesson_title']}' ({inv['video_id']}): {inv['status']}")
