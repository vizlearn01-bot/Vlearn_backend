import os
import sys
import re
import xml.etree.ElementTree as ET
import requests
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

def audit_grade10_business_studies():
    print("=" * 80)
    print("AUDITING GRADE 10 BUSINESS STUDIES TOPICS IN DATABASE")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, level=10).first() or Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    subject = Subject.objects.filter(grade=grade, name="Business Studies").first()

    if not subject:
        print("[-] Subject 'Business Studies' not found!")
        return

    topics = Topic.objects.filter(subject=subject).order_by("order")
    print(f"Found {topics.count()} topics in database.")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    url_cache = {}

    def check_url(url):
        if not url:
            return False, "Empty URL"
        if url in url_cache:
            return url_cache[url]
        try:
            resp = requests.head(url, headers=headers, timeout=5, allow_redirects=True)
            if resp.status_code == 200:
                url_cache[url] = (True, 200)
                return True, 200
            if resp.status_code in [403, 405]:
                # Retry with GET range
                resp = requests.get(url, headers=headers, timeout=5, stream=True)
                url_cache[url] = (resp.status_code == 200, resp.status_code)
                return resp.status_code == 200, resp.status_code
            url_cache[url] = (False, resp.status_code)
            return False, resp.status_code
        except Exception as e:
            url_cache[url] = (False, str(e))
            return False, str(e)

    total_lessons = 0
    total_blocks = 0
    total_mcqs = 0
    total_svgs = 0
    total_images = 0
    total_videos = 0

    issues = []

    for topic in topics:
        print(f"\n--- TOPIC {topic.order}: {topic.name} ---")
        lessons = Lesson.objects.filter(topic=topic).order_by("learning_unit__order")
        print(f"Total Lessons: {lessons.count()}")
        
        t_videos = 0

        for lesson in lessons:
            total_lessons += 1
            blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("page_number", "component_order"))
            total_blocks += len(blocks)

            pages = {}
            has_video = False
            has_diagram = False
            has_image = False

            for b in blocks:
                pages.setdefault(b.page_number, []).append(b)

                # Check block title & content
                if not b.title:
                    issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} missing title")
                if not b.content:
                    issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} missing content")

                # Check bracket citations & prompt leaks in content & title
                text_repr = str(b.content) + " " + str(b.title)
                cites = re.findall(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', text_repr)
                if cites:
                    issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} has citation brackets: {cites[:3]}")

                for leak in ["Prompt:", "JSON Payload", "block_type:", "component_order:"]:
                    if leak in text_repr:
                        issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} has prompt leak: {leak}")

                # Check suggested_image
                if b.block_type == "suggested_image":
                    has_image = True
                    total_images += 1
                    c = b.content or {}
                    url = c.get("url", "")
                    if not url:
                        issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} image missing URL")
                    elif "/thumb/" in url:
                        issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} image uses /thumb/: {url}")
                    else:
                        ok, status = check_url(url)
                        if not ok:
                            issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} image URL failed (HTTP {status}): {url}")

                # Check suggested_diagram
                if b.block_type == "suggested_diagram":
                    has_diagram = True
                    total_svgs += 1
                    c = b.content or {}
                    svg_text = c.get("svg_content", "")
                    if not svg_text:
                        issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} missing svg_content")
                    else:
                        if "viewBox" not in svg_text:
                            issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} SVG missing viewBox")
                        # Try parsing XML
                        try:
                            # Strip namespaces or parse
                            clean_svg = re.sub(r'xmlns="[^"]+"', '', svg_text)
                            ET.fromstring(clean_svg)
                        except Exception as e:
                            issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} SVG XML error: {str(e)[:60]}")

                    # Check asset attachment
                    asset = b.assets.filter(asset_type="diagram").first()
                    if not asset:
                        issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} diagram missing LessonAsset")

                # Check suggested_video
                if b.block_type == "suggested_video":
                    total_videos += 1
                    c = b.content or {}
                    yt_id = c.get("youtube_id", "")
                    if yt_id:
                        has_video = True
                        t_videos += 1
                        asset = b.assets.filter(asset_type="youtube").first()
                        if not asset:
                            issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] Block {b.id} video missing LessonAsset")

                # Check MCQs
                if b.block_type == "knowledge_check":
                    total_mcqs += 1
                    c = b.content or {}
                    q = c.get("question")
                    opts = c.get("options", [])
                    ans = c.get("correct") or c.get("answer")
                    exp = c.get("explanation")
                    if not q:
                        issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] MCQ {b.id} missing question")
                    if len(opts) != 4:
                        issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] MCQ {b.id} has {len(opts)} options, expected 4")
                    if ans not in ["A", "B", "C", "D"]:
                        issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] MCQ {b.id} invalid answer '{ans}'")
                    if not exp:
                        issues.append(f"[Topic {topic.order} L{lesson.learning_unit.order}] MCQ {b.id} missing explanation")

            num_pages = len(pages)
            if num_pages < 7 or num_pages > 8:
                print(f"  [!] Lesson {lesson.learning_unit.order} ({lesson.title[:30]}): {num_pages} pages (Expected 7-8)")
            else:
                print(f"  [+] Lesson {lesson.learning_unit.order} ({lesson.title[:30]}): {num_pages} pages")

        cov = (t_videos / len(lessons) * 100) if len(lessons) > 0 else 0
        print(f"Topic {topic.order} Video Coverage: {t_videos}/{len(lessons)} ({cov:.1f}%)")

    print("\n" + "=" * 80)
    print(f"AUDIT SUMMARY: {len(issues)} ISSUES DETECTED")
    print("=" * 80)
    for iss in issues[:30]:
        print(" - ", iss)
    if len(issues) > 30:
        print(f" ... and {len(issues) - 30} more issues.")

if __name__ == "__main__":
    audit_grade10_business_studies()
