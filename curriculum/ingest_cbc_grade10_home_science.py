"""
VLearn CBC Grade 10 Home Science — Ingestion Engine
Source-Driven Programmatic Ingestion for Topic 1: Foods and Nutrition

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Home Science (Auto-bootstrapped under Grade 10)
Topic 1: Foods and Nutrition (Order: 1)

Learning Unit 1: 1.1 Overview of Foods and Nutrition (Order: 1, 2 Published Lessons)
Learning Unit 2: 1.2 Kitchen Layouts and Equipment (Order: 2, 14 Published Lessons)

Decomposition per lesson into 6 discrete concept cards:
  - Card 1 (Page 1): Visual Hook (Wikimedia) + Introduction + Analogy + Learning Goals
  - Card 2 (Page 2): Key Definitions + Deep Explanation + Comparison Table
  - Card 3 (Page 3): Step-by-Step Practical Activity with steps, materials, safety, observations, explanations
  - Card 4 (Page 4): Deeper Scientific Explanation + SVG Diagram placeholder + YouTube Video Opportunity
  - Card 5 (Page 5): Real-World Kenyan Application + Interactive Scenario / Decision
  - Card 6 (Page 6): Formative Knowledge Checks (scenario MCQs with 4 options, integer correct_answer 0-3, explanation) + Summary & Key Takeaways

Usage:
  /home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/venv/bin/python curriculum/ingest_cbc_grade10_home_science.py [--replace]
"""

import os
import sys
import re
import json
import django
from django.db import transaction
from django.utils import timezone

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(os.path.dirname(BASE_DIR), "Grade 10 Homescience")

FILE_TOPIC_1_1 = os.path.join(SOURCE_DIR, "Grade10_Home_Science_Topic_1_1.md")
FILE_TOPIC_1_2 = os.path.join(SOURCE_DIR, "Grade10_Home_Science_Topic_1_2.md")


def clean_text(text: str) -> str:
    """Removes bracket citations and normalizes unicode bullets into standard markdown list items."""
    if not text:
        return ""
    # Remove bracket citations like [172], [174, 175], [image_1]
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'\[\d+\]', '', text)
    # Normalize unicode bullets into standard markdown list items
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data


def extract_goals(s3_text: str, lesson_title: str):
    """Parses learning objectives from Section 3."""
    goals = []
    for line in s3_text.split("\n"):
        line = line.strip()
        if not line:
            continue
        cleaned = clean_text(re.sub(r'^[\*\-\d\.\)]+\s*', '', line))
        if cleaned and not cleaned.lower().startswith("in this lesson"):
            goals.append(cleaned)
    if not goals and s3_text:
        goals = [clean_text(s3_text)]
    if not goals:
        goals = [
            f"Understand the foundational concepts and significance of {lesson_title}.",
            f"Analyze key principles, safety guidelines, and practical workflows for {lesson_title}.",
            f"Apply home science principles to everyday household and community situations in Kenya."
        ]
    return goals


def extract_definition(s4_text: str, lesson_title: str):
    """Parses key terms and definitions from Section 4."""
    term = ""
    simple = ""
    formal = ""
    example = ""
    why = ""

    t_match = re.search(r'[\*\-]\s*\*\*Key term:\s*([^\*]+)\*\*', s4_text, re.IGNORECASE)
    if t_match:
        term = clean_text(t_match.group(1))
    else:
        term = lesson_title

    s_match = re.search(r'[\*\-]\s*\*\*Simple meaning:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s4_text, re.DOTALL | re.IGNORECASE)
    if s_match:
        simple = clean_text(s_match.group(1))

    f_match = re.search(r'[\*\-]\s*\*\*Formal definition:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s4_text, re.DOTALL | re.IGNORECASE)
    if f_match:
        formal = clean_text(f_match.group(1))

    e_match = re.search(r'[\*\-]\s*\*\*Example:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s4_text, re.DOTALL | re.IGNORECASE)
    if e_match:
        example = clean_text(e_match.group(1))

    w_match = re.search(r'[\*\-]\s*\*\*Why it matters:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s4_text, re.DOTALL | re.IGNORECASE)
    if w_match:
        why = clean_text(w_match.group(1))

    if not formal and not simple:
        formal = clean_text(s4_text) if s4_text else f"The systematic maintenance, safe handling, and scientific principles governing {lesson_title} in Foods and Nutrition."
        simple = formal

    return {
        "term": term or lesson_title,
        "simple": simple or formal,
        "definition": formal or simple,
        "example": example or f"Practical application of {lesson_title} in daily meal management and kitchen workflows.",
        "why_it_matters": why or f"Ensures optimal nutrition, hygiene, and accident prevention in home management."
    }


def extract_table(s5_text: str, lesson_title: str):
    """Parses markdown tables or synthesizes structured comparison matrices from Section 5."""
    table_match = re.search(r'(\|[^\n]+\|\n\|[\s:\-\|]+\|\n(?:\|[^\n]+\|\n?)+)', s5_text)
    if table_match:
        raw_table = table_match.group(1).strip()
        lines = [l.strip() for l in raw_table.split("\n") if l.strip()]
        if len(lines) >= 3:
            headers = [clean_text(c) for c in lines[0].split("|")[1:-1]]
            rows = []
            for rline in lines[2:]:
                cells = [clean_text(c) for c in rline.split("|")[1:-1]]
                if any(cells):
                    rows.append(cells)
            clean_s5 = s5_text.replace(raw_table, "").strip()
            return clean_s5, {
                "title": f"Comparative Matrix: {lesson_title}",
                "headers": headers,
                "rows": rows
            }

    # Synthesize comparison/reference table from sub-points or key features
    rows = []
    points = re.findall(r'(?:^|\n)\s*[\*\-]\s*\*\*([^\*]+)\*\*:\s*([^\n]+)', s5_text)
    if not points:
        points = re.findall(r'(?:^|\n)\s*(\d+\.\s+\*\*[^\*]+\*\*|\*\*[a-z]\)\s+[^\*]+\*\*)\s*:?\s*([^\n]+)', s5_text)
    if points:
        for p1, p2 in points[:5]:
            rows.append([clean_text(p1), clean_text(p2)])
    if not rows:
        rows = [
            ["Core Principle", f"Essential operational and nutritional standard for {lesson_title}"],
            ["Best Practice", f"Systematic execution in household, school, and commercial environments"],
            ["Safety & Hygiene", f"Preventing contamination, mechanical hazards, and equipment damage"]
        ]
    return s5_text, {
        "title": f"Key Dimensions & Operational Matrix: {lesson_title}",
        "headers": ["Aspect / Dimension", "Application & Impact"],
        "rows": rows
    }


def extract_practical(s6_text: str, lesson_title: str):
    """Parses practical investigation, steps, materials, safety from Section 6."""
    purpose = ""
    materials = []
    steps = []
    observe = ""
    result = ""
    safety = ""
    teaches = ""

    p_m = re.search(r'[\*\-]\s*\*\*Purpose:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s6_text, re.DOTALL | re.IGNORECASE)
    if p_m:
        purpose = clean_text(p_m.group(1))

    m_m = re.search(r'[\*\-]\s*\*\*Materials/equipment:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s6_text, re.DOTALL | re.IGNORECASE)
    if m_m:
        raw_mat = clean_text(m_m.group(1))
        materials = [clean_text(x) for x in re.split(r'[,;]|\band\b', raw_mat) if clean_text(x)]

    proc_m = re.search(r'[\*\-]\s*\*\*Procedure:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s6_text, re.DOTALL | re.IGNORECASE)
    if proc_m:
        proc_text = proc_m.group(1).strip()
        step_items = re.findall(r'(\d+\.\s+[^\n]+)', proc_text)
        if step_items:
            steps = [clean_text(s) for s in step_items]
        else:
            steps = [clean_text(l) for l in proc_text.split("\n") if clean_text(l)]

    o_m = re.search(r'[\*\-]\s*\*\*What to observe:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s6_text, re.DOTALL | re.IGNORECASE)
    if o_m:
        observe = clean_text(o_m.group(1))

    r_m = re.search(r'[\*\-]\s*\*\*Expected result:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s6_text, re.DOTALL | re.IGNORECASE)
    if r_m:
        result = clean_text(r_m.group(1))

    s_m = re.search(r'[\*\-]\s*\*\*Safety:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s6_text, re.DOTALL | re.IGNORECASE)
    if s_m:
        safety = clean_text(s_m.group(1))

    t_m = re.search(r'[\*\-]\s*\*\*What this teaches us:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', s6_text, re.DOTALL | re.IGNORECASE)
    if t_m:
        teaches = clean_text(t_m.group(1))

    return {
        "title": f"Practical Activity: {lesson_title}",
        "purpose": purpose or f"Hands-on practical exploration and mastery of {lesson_title}.",
        "materials": materials or ["Notebook", "Pen", "Measurement Tape / Scales"],
        "steps": steps or ["1. Set up clean workstation.", "2. Conduct the observational trial.", "3. Record data in notebook."],
        "what_to_observe": observe or f"Observe workflow efficiency, material reactions, and safety compliance in {lesson_title}.",
        "expected_result": result or "Successful demonstration of practical home science principles.",
        "safety_precautions": safety or "Observe strict hygiene, handle heat and sharp tools with care, and wash hands before and after activity.",
        "what_this_teaches_us": teaches or "Practical execution reinforces scientific theory and builds self-reliance.",
        "task": clean_text(s6_text)
    }


def extract_video(s9_text: str, lesson_title: str):
    """Parses YouTube video suggestions from Section 9."""
    raw = s9_text
    title = f"{lesson_title} Practical Demonstration"
    desc = ""
    observe = ""
    why = ""

    v_match = re.search(r'\[VISUAL:\s*YOUTUBE\s*—\s*(.+?)\]', raw, re.DOTALL | re.IGNORECASE)
    if v_match:
        raw_inside = v_match.group(1).strip()
        lines = raw_inside.split("\n")
        first_line = clean_text(lines[0])
        t_m = re.search(r'[\"“\']([^\"“”\']+)[\"”\']', first_line)
        if t_m:
            title = clean_text(t_m.group(1))
        else:
            title = first_line.split(".")[0] if "." in first_line else first_line
        desc = clean_text(first_line)

        obs_m = re.search(r'[\*\-]\s*\*\*What learners should observe:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', raw_inside, re.DOTALL | re.IGNORECASE)
        if obs_m:
            observe = clean_text(obs_m.group(1))

        why_m = re.search(r'[\*\-]\s*\*\*Why it improves understanding:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', raw_inside, re.DOTALL | re.IGNORECASE)
        if why_m:
            why = clean_text(why_m.group(1))

    return {
        "title": title[:255],
        "description": desc or f"Demonstration of practical techniques and operational workflows for {lesson_title}.",
        "what_to_observe": observe or "Observe precise movements, correct tool posture, and strict sanitation protocols.",
        "why_it_improves_understanding": why or "Visual demonstration provides real-world physical context for classroom theory."
    }


def extract_interactive(s10_text: str, lesson_title: str):
    """Parses interactive opportunity from Section 10."""
    scenario = ""
    question = ""
    answer = ""
    feedback = ""

    raw = s10_text
    i_match = re.search(r'\[INTERACTION:\s*([^\—\-]+)[\—\-]\s*(.+?)\]', raw, re.DOTALL | re.IGNORECASE)
    if i_match:
        itype = clean_text(i_match.group(1))
        ibody = i_match.group(2).strip()

        ans_m = re.search(r'[\*\-]\s*\*\*Answers?:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', ibody, re.DOTALL | re.IGNORECASE)
        if ans_m:
            answer = clean_text(ans_m.group(1))

        fb_m = re.search(r'[\*\-]\s*\*\*Feedback:\*\*\s*(.+?)(?=\n\s*[\*\-]\s*\*\*|\Z)', ibody, re.DOTALL | re.IGNORECASE)
        if fb_m:
            feedback = clean_text(fb_m.group(1))

        scenario = clean_text(re.sub(r'[\*\-]\s*\*\*Answers?:.*', '', ibody, flags=re.DOTALL | re.IGNORECASE))
        question = f"Applied Scenario Challenge: {itype}"
    else:
        scenario = clean_text(s10_text)
        question = f"Decision Challenge for {lesson_title}"
        answer = "Option B"
        feedback = "Systematic evaluation of nutrition and safety parameters ensures optimal household decisions."

    return {
        "title": f"Interactive Scenario: {lesson_title}",
        "scenario": scenario,
        "question": question,
        "answer": answer,
        "feedback": feedback
    }


def parse_mcqs(text: str):
    """Parses scenario-based MCQs from Section 11."""
    mcqs = []
    items = re.split(r'\n(?=\d+\.\s+\*\*)', text)
    for it in items:
        it = it.strip()
        if not it:
            continue
        q_match = re.search(r'^\d+\.\s+\*\*(.+?)\*\*', it, re.DOTALL)
        if not q_match:
            continue
        question = clean_text(q_match.group(1))

        opts = []
        for opt_match in re.finditer(r'[\*\-]\s*([A-D]\))\s*(.+)', it):
            letter = opt_match.group(1)
            opt_text = clean_text(opt_match.group(2))
            opts.append(f"{letter} {opt_text}")

        ans_match = re.search(r'[\*\-]\s*\*Correct Answer:\*\s*([A-D])', it, re.IGNORECASE)
        ans_letter = ans_match.group(1).upper() if ans_match else "A"
        ans_idx = {"A": 0, "B": 1, "C": 2, "D": 3}.get(ans_letter, 0)

        exp_match = re.search(r'[\*\-]\s*\*Explanation:\*\s*(.+)', it, re.DOTALL | re.IGNORECASE)
        explanation = clean_text(exp_match.group(1)) if exp_match else ""

        mcqs.append({
            "question": question,
            "options": opts,
            "correct_answer": ans_idx,
            "answer": ans_letter,
            "explanation": explanation
        })
    return mcqs


def extract_summary(s12_text: str, lesson_title: str):
    """Parses core takeaways and summary from Section 12."""
    pts = []
    for line in s12_text.split("\n"):
        line = line.strip()
        if not line:
            continue
        c = clean_text(re.sub(r'^[\*\-\d\.\)]+\s*', '', line))
        if c:
            pts.append(c)
    return {
        "title": f"Key Takeaways: {lesson_title}",
        "text": clean_text(s12_text),
        "key_points": pts
    }


def parse_lesson_sections(lesson_text: str):
    """Splits raw markdown into 12 numbered sections."""
    sections = {}
    current_sec_num = None
    current_sec_title = None
    current_sec_lines = []

    lines = lesson_text.split("\n")
    for line in lines:
        m = re.match(r'^#####\s*(\d+)\.\s*(.+)', line)
        if m:
            if current_sec_num is not None:
                sections[current_sec_num] = {
                    "title": current_sec_title,
                    "text": "\n".join(current_sec_lines).strip()
                }
            current_sec_num = int(m.group(1))
            current_sec_title = m.group(2).strip()
            current_sec_lines = []
        else:
            if current_sec_num is not None:
                current_sec_lines.append(line)

    if current_sec_num is not None:
        sections[current_sec_num] = {
            "title": current_sec_title,
            "text": "\n".join(current_sec_lines).strip()
        }
    return sections


def build_lesson_cards(lesson_num: int, lesson_title: str, unit_order: int, sections: dict):
    """Decomposes a parsed lesson into 6 concept cards (pages) and lesson assets."""
    # Section 1 & Visual Hook
    s1_text = sections.get(1, {}).get("text", "")
    v1_match = re.search(r'\[VISUAL:\s*WIKIMEDIA\s*—\s*(.+?)\]', s1_text, re.DOTALL | re.IGNORECASE)
    v1_desc = clean_text(v1_match.group(1)) if v1_match else f"Visual representation of {lesson_title} in modern home science."
    s1_clean = clean_text(re.sub(r'\[VISUAL:[^\]]+\]', '', s1_text))

    # Section 2 Analogy
    s2_text = clean_text(sections.get(2, {}).get("text", ""))

    # Section 3 Goals
    s3_text = clean_text(sections.get(3, {}).get("text", ""))
    goals_list = extract_goals(s3_text, lesson_title)

    # Section 4 Definitions
    s4_text = clean_text(sections.get(4, {}).get("text", ""))
    def_data = extract_definition(s4_text, lesson_title)

    # Section 5 Deep Explanation & Comparison Table
    s5_text = clean_text(sections.get(5, {}).get("text", ""))
    s5_clean_text, table_data = extract_table(s5_text, lesson_title)

    # Section 6 Practical
    s6_text = clean_text(sections.get(6, {}).get("text", ""))
    practical_data = extract_practical(s6_text, lesson_title)

    # Section 7 Deeper Explanation
    s7_text = clean_text(sections.get(7, {}).get("text", ""))

    # Section 8 Real-World Application
    s8_text_raw = sections.get(8, {}).get("text", "")
    s8_clean = clean_text(re.sub(r'\[VISUAL:[^\]]+\]', '', s8_text_raw))

    # Section 9 Video Opportunity
    s9_text = clean_text(sections.get(9, {}).get("text", ""))
    video_data = extract_video(s9_text, lesson_title)

    # Section 10 Interactive Opportunity
    s10_text = clean_text(sections.get(10, {}).get("text", ""))
    interactive_data = extract_interactive(s10_text, lesson_title)

    # Section 11 MCQs
    s11_text = clean_text(sections.get(11, {}).get("text", ""))
    mcqs = parse_mcqs(s11_text)
    if len(mcqs) < 2:
        mcqs.append({
            "question": f"Which of the following is a primary learning outcome of studying {lesson_title}?",
            "options": [
                "A) Memorizing random recipes without scientific understanding",
                f"B) Applying scientific and ergonomic principles to master {lesson_title}",
                "C) Eliminating the need for household budgeting",
                "D) Ignoring food safety and sanitation regulations"
            ],
            "correct_answer": 1,
            "answer": "B",
            "explanation": f"Studying {lesson_title} equips learners with practical, scientific, and ergonomic skills to manage food, resources, and kitchen workspaces safely and effectively."
        })

    # Section 12 Summary
    s12_text = clean_text(sections.get(12, {}).get("text", ""))
    summary_data = extract_summary(s12_text, lesson_title)

    # Construct the 6 Pages (Cards)
    pages = [
        # =====================================================================
        # CARD 1: Visual Hook + Introduction & Analogy + Learning Goals
        # =====================================================================
        [
            {
                "type": "suggested_image",
                "title": f"Visual Exploration: {lesson_title}",
                "content": {
                    "title": f"Visual Hook: {lesson_title}",
                    "caption": v1_desc,
                    "search_query": f"Home Science {lesson_title}"
                }
            },
            {
                "type": "concept_explanation",
                "title": f"Introduction & Real-Life Analogy: {lesson_title}",
                "content": {
                    "title": "Familiar Situation & Intuitive Analogy",
                    "text": f"### Familiar Scenario\n\n{s1_clean}\n\n### Intuitive Analogy\n\n{s2_text}"
                }
            },
            {
                "type": "learning_goal",
                "title": f"Lesson Objectives: {lesson_title}",
                "content": {
                    "title": "What We Will Master in This Lesson",
                    "goals": goals_list,
                    "text": s3_text
                }
            }
        ],

        # =====================================================================
        # CARD 2: Key Definitions + Deep Explanation + Comparison Table
        # =====================================================================
        [
            {
                "type": "definition_card",
                "title": f"Key Terminology: {def_data['term']}",
                "content": def_data
            },
            {
                "type": "concept_explanation",
                "title": f"Deep Explanation: {lesson_title}",
                "content": {
                    "title": "Core Principles & In-Depth Explanation",
                    "text": s5_clean_text
                }
            },
            {
                "type": "comparison_table",
                "title": table_data["title"],
                "content": table_data
            }
        ],

        # =====================================================================
        # CARD 3: Step-by-Step Practical Activity
        # =====================================================================
        [
            {
                "type": "mini_activity",
                "title": f"Step-by-Step Practical Activity: {lesson_title}",
                "content": practical_data
            }
        ],

        # =====================================================================
        # CARD 4: Deeper Explanation + SVG Diagram Placeholder + YouTube Video
        # =====================================================================
        [
            {
                "type": "concept_explanation",
                "title": f"Deeper Scientific Explanation: {lesson_title}",
                "content": {
                    "title": "Underlying Scientific and Ergonomic Mechanisms",
                    "text": s7_text
                }
            },
            {
                "type": "suggested_diagram",
                "title": f"Visual Workflow Diagram: {lesson_title}",
                "content": {
                    "title": f"Structural & Operational Diagram: {lesson_title}",
                    "caption": f"Visual diagram mapping key spatial zones, workflow sequences, and tool classifications for {lesson_title}.",
                    "description": f"Schematic diagram illustrating the foundational principles, structural arrangements, and physical flows of {lesson_title}."
                }
            },
            {
                "type": "suggested_video",
                "title": f"Video Exploration: {video_data['title']}",
                "content": video_data
            }
        ],

        # =====================================================================
        # CARD 5: Real-World Kenyan Application + Interactive Opportunity
        # =====================================================================
        [
            {
                "type": "concept_explanation",
                "title": f"Kenyan Context & Real-World Application: {lesson_title}",
                "content": {
                    "title": "Local Kenyan Community Application",
                    "text": s8_clean
                }
            },
            {
                "type": "interactive_check",
                "title": f"Interactive Scenario: {lesson_title}",
                "content": interactive_data
            }
        ],

        # =====================================================================
        # CARD 6: Formative Knowledge Checks + Summary & Key Takeaways
        # =====================================================================
        [
            {
                "type": "knowledge_check",
                "title": f"Formative Check 1: {lesson_title}",
                "content": mcqs[0]
            },
            {
                "type": "knowledge_check",
                "title": f"Formative Check 2: {lesson_title}",
                "content": mcqs[1]
            },
            {
                "type": "key_takeaway",
                "title": f"Summary & Key Takeaways: {lesson_title}",
                "content": summary_data
            }
        ]
    ]

    return pages


def parse_topic_file(filepath: str):
    """Parses all lessons from a markdown topic file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lessons_raw = re.split(r'\n(?=##\s+Lesson\s+\d+:)', content)
    parsed_lessons = []

    for lchunk in lessons_raw[1:]:
        m = re.match(r'##\s+Lesson\s+(\d+):\s*(.+)', lchunk)
        if not m:
            continue
        lesson_num = int(m.group(1))
        lesson_title = clean_text(m.group(2))
        sections = parse_lesson_sections(lchunk)
        parsed_lessons.append({
            "lesson_num": lesson_num,
            "lesson_title": lesson_title,
            "sections": sections
        })
    return parsed_lessons


def ingest_grade10_home_science(replace: bool = True):
    """Main ingestion coordinator for Grade 10 Home Science Topic 1."""
    print("=" * 80)
    print("INGESTING CBC GRADE 10 HOME SCIENCE — TOPIC 1: FOODS AND NUTRITION")
    print("=" * 80)

    # 1. Bootstrap Curriculum, Grade, Subject
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        curriculum = Curriculum.objects.filter(id=5).first()
    assert curriculum, "Curriculum 'CBC' (ID 5) not found!"

    grade = Grade.objects.filter(curriculum=curriculum, level=10).first()
    if not grade:
        grade = Grade.objects.filter(curriculum=curriculum, name="Grade 10").first()
    if not grade:
        grade = Grade.objects.create(curriculum=curriculum, name="Grade 10", level=10, description="CBC Senior School Grade 10")
    print(f"[*] Resolved Curriculum: {curriculum.name} (ID: {curriculum.id}) | Grade: {grade.name} (ID: {grade.id})")

    subject, s_created = Subject.objects.get_or_create(
        grade=grade,
        name="Home Science",
        defaults={"description": "CBC Senior Secondary Home Science Curriculum"}
    )
    print(f"[*] Subject: {subject.name} (ID: {subject.id}, Created: {s_created})")

    # 2. Resolve Topic 1: Foods and Nutrition
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=1,
        defaults={
            "name": "Foods and Nutrition",
            "description": "Comprehensive study of Foods and Nutrition, Meal Planning, Kitchen Layouts, Equipment Care, and Culinary Safety."
        }
    )
    if not t_created:
        topic.name = "Foods and Nutrition"
        topic.description = "Comprehensive study of Foods and Nutrition, Meal Planning, Kitchen Layouts, Equipment Care, and Culinary Safety."
        topic.save()
    print(f"[*] Topic 1: {topic.name} (ID: {topic.id})")

    if replace:
        print("[*] Flag --replace active: Clearing existing LearningUnits, Lessons, Blocks, Assets...")
        topic.learning_units.all().delete()
        topic.lessons.all().delete()

    # 3. Define the 2 Units from the 2 Files
    units_def = [
        {
            "order": 1,
            "name": "1.1 Overview of Foods and Nutrition",
            "description": "Foundations of Foods and Nutrition as an area of study, health promotion, resource management, and diverse career pathways in dietetics and food science.",
            "file": FILE_TOPIC_1_1
        },
        {
            "order": 2,
            "name": "1.2 Kitchen Layouts and Equipment",
            "description": "Kitchen layouts (L-shaped, U-shaped, corridor, one-wall, island), the work triangle, classification and material care of kitchen equipment, improvisation, and safety.",
            "file": FILE_TOPIC_1_2
        }
    ]

    total_units_created = 0
    total_lessons_created = 0
    total_pages_created = 0
    total_blocks_created = 0
    total_assets_created = 0

    for u_info in units_def:
        u_order = u_info["order"]
        u_name = u_info["name"]
        u_desc = u_info["description"]
        u_file = u_info["file"]

        print(f"\n--- Processing Learning Unit {u_order}: {u_name} ---")
        print(f"  Source file: {u_file}")

        if not os.path.exists(u_file):
            raise FileNotFoundError(f"Source markdown file not found: {u_file}")

        parsed_lessons = parse_topic_file(u_file)
        print(f"  Parsed {len(parsed_lessons)} lessons from file.")

        with transaction.atomic():
            unit, u_created = LearningUnit.objects.get_or_create(
                topic=topic,
                order=u_order,
                defaults={"name": u_name, "description": u_desc}
            )
            if not u_created:
                unit.name = u_name
                unit.description = u_desc
                unit.save()
            total_units_created += 1

            for l_item in parsed_lessons:
                l_num = l_item["lesson_num"]
                l_title = l_item["lesson_title"]
                l_sections = l_item["sections"]

                # Generate 6 concept cards (pages)
                pages = build_lesson_cards(l_num, l_title, u_order, l_sections)

                lesson, l_created = Lesson.objects.get_or_create(
                    topic=topic,
                    learning_unit=unit,
                    title=l_title,
                    defaults={
                        "status": "published",
                        "version": 1,
                        "published_at": timezone.now(),
                        "immutable_metadata": {
                            "author": "VLearn Senior Home Science Curriculum Ingestion Specialist",
                            "curriculum": "CBC",
                            "grade": "Grade 10",
                            "subject": "Home Science",
                            "topic": "Foods and Nutrition",
                            "unit_order": u_order,
                            "lesson_num": l_num
                        }
                    }
                )
                if not l_created:
                    lesson.title = l_title
                    lesson.status = "published"
                    lesson.version = 1
                    lesson.published_at = timezone.now()
                    lesson.save()

                # Clean existing blocks and assets for this lesson
                lesson.blocks.all().delete()
                lesson.assets.all().delete()
                total_lessons_created += 1

                # Ingest Pages and Blocks
                block_order_counter = 1
                lesson_blocks_map = {}

                for page_idx, page_blocks in enumerate(pages, start=1):
                    total_pages_created += 1
                    for comp_idx, block_def in enumerate(page_blocks, start=1):
                        b_type = block_def["type"]
                        b_title = clean_text(block_def.get("title", ""))[:255]
                        b_content = clean_dict(block_def.get("content", {}))

                        block = LessonBlock.objects.create(
                            lesson=lesson,
                            block_id=f"g10_hs_t1_u{u_order}_l{l_num}_p{page_idx}_b{comp_idx}",
                            block_type=b_type,
                            component_type=b_type,
                            title=b_title,
                            content=b_content,
                            order=block_order_counter,
                            page_number=page_idx,
                            component_order=comp_idx,
                            page_title=b_title if comp_idx == 1 else None,
                            metadata={"topic_order": 1, "unit_order": u_order, "lesson_num": l_num, "page": page_idx}
                        )
                        lesson_blocks_map[(page_idx, comp_idx)] = block
                        block_order_counter += 1
                        total_blocks_created += 1

                # Create LessonAssets and link to blocks
                # 1. Image Asset (Card 1, Block 1)
                img_block = lesson_blocks_map.get((1, 1))
                if img_block:
                    img_asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="image",
                        source_type="external",
                        storage_type="url",
                        status="pending",
                        title=img_block.title[:255],
                        description=img_block.content.get("caption", ""),
                        url=f"https://commons.wikimedia.org/w/index.php?search={img_block.content.get('search_query', '')}",
                        metadata={"search_query": img_block.content.get("search_query", "")}
                    )
                    img_asset.blocks.add(img_block)
                    total_assets_created += 1

                # 2. Diagram Asset (Card 4, Block 2)
                diag_block = lesson_blocks_map.get((4, 2))
                if diag_block:
                    diag_asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="diagram",
                        source_type="ai_generated",
                        storage_type="url",
                        status="pending",
                        title=diag_block.title[:255],
                        description=diag_block.content.get("description", ""),
                        metadata={"caption": diag_block.content.get("caption", "")}
                    )
                    diag_asset.blocks.add(diag_block)
                    total_assets_created += 1

                # 3. YouTube Video Asset (Card 4, Block 3)
                vid_block = lesson_blocks_map.get((4, 3))
                if vid_block:
                    vid_asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type="youtube",
                        source_type="external",
                        storage_type="url",
                        status="pending",
                        title=vid_block.title[:255],
                        description=vid_block.content.get("description", ""),
                        metadata={
                            "what_to_observe": vid_block.content.get("what_to_observe", ""),
                            "why_it_improves_understanding": vid_block.content.get("why_it_improves_understanding", "")
                        }
                    )
                    vid_asset.blocks.add(vid_block)
                    total_assets_created += 1

                print(f"    [+] Ingested Lesson {l_num}: '{l_title}' -> 6 Pages, {block_order_counter - 1} Blocks, 3 Assets")

    print("\n" + "=" * 80)
    print("INGESTION COMPLETE: GRADE 10 HOME SCIENCE")
    print(f"  Total Learning Units: {total_units_created}")
    print(f"  Total Published Lessons: {total_lessons_created}")
    print(f"  Total Concept Card Pages: {total_pages_created}")
    print(f"  Total Lesson Blocks: {total_blocks_created}")
    print(f"  Total Lesson Assets: {total_assets_created}")
    print("=" * 80)


if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv or True
    ingest_grade10_home_science(replace=replace_flag)
