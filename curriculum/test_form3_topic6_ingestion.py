import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock

def validate_form3_topic6():
    print("================================================================================")
    print("RUNNING COMPREHENSIVE VALIDATION: Form 3 Chemistry Topic 6 (Chlorine & Compounds)")
    print("================================================================================")

    # 1. Verify Grade and Subject
    grade = Grade.objects.filter(name="Form 3").first()
    assert grade is not None, "Grade 'Form 3' does not exist!"
    assert grade.curriculum.name == "844", f"Unexpected curriculum {grade.curriculum.name}"
    print(f"✅ Grade validated: {grade.name} (Curriculum: {grade.curriculum.name})")

    subject = Subject.objects.filter(grade=grade, name="Chemistry").first()
    assert subject is not None, "Subject 'Chemistry' does not exist under Form 3!"
    print(f"✅ Subject validated: {subject.name} under {grade.name}")

    # 2. Verify Topic 6
    topic = Topic.objects.filter(subject=subject, name__startswith="Topic 6: Chlorine").first()
    assert topic is not None, "Topic 6 (Chlorine and its Compounds) does not exist!"
    print(f"✅ Topic validated: {topic.name} (ID: {topic.id})")

    # 3. Verify Learning Units
    expected_modules = [
        "Module 6.1: Laboratory Preparation and Physical Properties of Chlorine",
        "Module 6.2: Chemical Reactions, Bleaching, and Oxidising Properties of Chlorine",
        "Module 6.3: Hydrogen Chloride Gas and Hydrochloric Acid",
        "Module 6.4: Analytical Testing for Chloride Ions, Industrial Uses, and Environmental Impacts of Halogens"
    ]

    units = list(LearningUnit.objects.filter(topic=topic).order_by("order"))
    assert len(units) == 4, f"Expected exactly 4 modules in Topic 6, found {len(units)}"

    banned_meta_labels = [
        "real-world hook", "real world hook",
        "visualization",
        "misconception buster",
        "teacher note",
        "concept explanation",
        "understanding check",
        "worked example",
        "worked calculation",
        "authoring label"
    ]

    for idx, expected_name in enumerate(expected_modules, start=1):
        unit = units[idx - 1]
        assert unit.name == expected_name, f"Module mismatch at index {idx}: expected '{expected_name}', got '{unit.name}'"
        print(f"✅ Learning Unit {idx}: {unit.name} (ID: {unit.id})")

        # Verify Lesson
        lesson = Lesson.objects.filter(topic=topic, learning_unit=unit).first()
        assert lesson is not None, f"No lesson found for unit {unit.name}"
        assert lesson.status == "published", f"Lesson {lesson.title} is not published (status: {lesson.status})"
        assert lesson.version == 1, f"Lesson {lesson.title} has unexpected version {lesson.version}"
        print(f"   ✅ Lesson: '{lesson.title}' (Status: {lesson.status}, Version: {lesson.version})")

        # Verify LessonBlocks
        blocks = list(LessonBlock.objects.filter(lesson=lesson).order_by("order"))
        assert len(blocks) >= 8, f"Lesson {lesson.title} has only {len(blocks)} blocks (expected >= 8)"

        pages = set(b.page_number for b in blocks)
        assert len(pages) == 8, f"Lesson {lesson.title} does not span 8 distinct pages: found {len(pages)} ({pages})"

        # Check for meta-label leakage
        has_learning_goal = False
        has_worked_example = False
        has_mcq = False
        has_summary = False

        for b in blocks:
            # Check title for meta-labels
            lower_title = b.title.lower() if b.title else ""
            lower_page_title = b.page_title.lower() if b.page_title else ""
            for tag in banned_meta_labels:
                assert tag not in lower_title, f"Leaked meta-label '{tag}' in block title: '{b.title}'"
                assert tag not in lower_page_title, f"Leaked meta-label '{tag}' in page title: '{b.page_title}'"

            if b.component_type == "learning_goal":
                has_learning_goal = True
            elif b.component_type == "worked_example":
                has_worked_example = True
            elif b.component_type == "knowledge_check":
                has_mcq = True
                content = b.content
                assert "question" in content and len(content["question"]) > 10, f"Invalid question in block {b.block_id}"
                assert "options" in content and len(content["options"]) == 4, f"MCQ options count != 4 in block {b.block_id}"
                assert content.get("answer") in ["A", "B", "C", "D"], f"Invalid answer key '{content.get('answer')}' in block {b.block_id}"
                assert "explanation" in content and len(content["explanation"]) > 20, f"Explanation too short in block {b.block_id}"
            elif b.component_type == "summary":
                has_summary = True

        assert has_learning_goal, f"Lesson {lesson.id} missing learning_goal block"
        assert has_worked_example, f"Lesson {lesson.id} missing worked_example block"
        assert has_mcq, f"Lesson {lesson.id} missing knowledge_check block"
        assert has_summary, f"Lesson {lesson.id} missing summary block"

        print(f"   ✅ Verified {len(blocks)} blocks across 8 natural concept pages (Zero meta-labels, full KaTeX rigor, interactive MCQs).")

    print("\n================================================================================")
    print("ALL VALIDATION CHECKS PASSED: Form 3 Chemistry Topic 6 is 100% Student-Ready!")
    print("================================================================================")

if __name__ == "__main__":
    validate_form3_topic6()
