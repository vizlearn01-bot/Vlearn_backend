import re
import json
from curriculum.models import Subject, Topic, Lesson, LessonBlock, Simulation
from Resources.models import ExperimentVideo

subjects_to_scan = [
    ("Mathematics", 14),
    ("Physics", 11),
    ("Chemistry (Form 3)", 27),
    ("Chemistry (Form 4)", 4),
    ("Biology", 13),
    ("Geography", 18),
]

# Patterns for detecting unescaped / leaking LaTeX commands outside of $...$ or $$...$$
LATEX_COMMANDS = [
    r'\\text\{', r'\\frac\{', r'\\sqrt\{', r'\\begin\{', r'\\end\{',
    r'\\pmatrix', r'\\bmatrix', r'\\times', r'\\rightarrow', r'\\leftarrow',
    r'\\Delta', r'\\theta', r'\\lambda', r'\\alpha', r'\\beta', r'\\gamma',
    r'\\mu', r'\\pi', r'\\Omega', r'\\omega', r'\\sigma', r'\\rho',
    r'\\approx', r'\\neq', r'\\leq', r'\\geq', r'\\pm', r'\\circ',
    r'\\sum', r'\\int', r'\\partial', r'\\infty', r'\\cdot'
]

def check_latex_leak(text):
    """
    Checks if LaTeX commands appear OUTSIDE math delimiters ($...$ or $$...$$).
    Also checks for unclosed math delimiters or double escape issues.
    """
    if not isinstance(text, str) or not text.strip():
        return []
    
    issues = []
    
    # 1. Check unbalanced single or double dollar signs
    # Replace escaped dollars first
    clean_text = text.replace(r'\$', '')
    
    # Count $$
    double_dollars = clean_text.count('$$')
    if double_dollars % 2 != 0:
        issues.append(f"Unbalanced double dollar signs '$$' (count={double_dollars})")
    
    # Remove all $$...$$ blocks to check single $
    stripped_display_math = re.sub(r'\$\$.*?\$\$', '', clean_text, flags=re.DOTALL)
    single_dollars = stripped_display_math.count('$')
    if single_dollars % 2 != 0:
        issues.append(f"Unbalanced inline dollar signs '$' (count={single_dollars})")
        
    # 2. Check for LaTeX commands appearing outside $...$ and $$...$$
    # Remove all math blocks: $$...$$ and $...$
    no_math = re.sub(r'\$\$.*?\$\$', '', clean_text, flags=re.DOTALL)
    no_math = re.sub(r'\$.*?\$', '', no_math, flags=re.DOTALL)
    
    # Also check if there are raw LaTeX commands remaining
    for cmd in LATEX_COMMANDS:
        matches = list(re.finditer(cmd, no_math))
        if matches:
            for m in matches:
                start = max(0, m.start() - 25)
                end = min(len(no_math), m.end() + 25)
                snippet = no_math[start:end].replace('\n', ' ')
                issues.append(f"Raw LaTeX command outside math delimiter: '{m.group(0)}' in snippet: \"...{snippet}...\"")
                
    # 3. Check for specific corrupted tokens (like 'eq \text' from old unescape bug)
    if 'eq \\text' in text or 'eq \\' in text:
        issues.append("Detected corrupted 'eq \\text' (potential broken '\\neq' unescape)")
        
    # 4. Check for quadruple backslashes in JSON (e.g. \\\\frac)
    if '\\\\\\\\' in text:
        issues.append("Detected excessive backslashes ('\\\\\\\\') which may cause KaTeX parse failures")
        
    return issues

def scan_all():
    results = {}
    total_leaks_found = 0
    
    for subject_label, subj_id in subjects_to_scan:
        try:
            subject = Subject.objects.get(id=subj_id)
        except Subject.DoesNotExist:
            print(f"Subject {subject_label} (ID {subj_id}) not found!")
            continue
            
        topics = subject.topics.all().order_by('order', 'id')
        
        # Simulations count for this subject
        subj_name_lower = subject.name.lower()
        sim_subject_str = "CHEMISTRY" if "chem" in subj_name_lower else ("PHYSICS" if "phys" in subj_name_lower else "")
        simulations_count = Simulation.objects.filter(subject__iexact=sim_subject_str).count() if sim_subject_str else 0
        experiments_count = ExperimentVideo.objects.count() if "chem" in subj_name_lower else 0
        
        subject_data = {
            "id": subject.id,
            "name": subject.name,
            "grade": getattr(subject.grade, "name", "N/A"),
            "topic_count": topics.count(),
            "lesson_count": 0,
            "block_count": 0,
            "block_types_distribution": {},
            "simulations_count": simulations_count,
            "experiments_count": experiments_count,
            "topics_detail": [],
            "latex_issues": []
        }
        
        for topic in topics:
            lessons = topic.lessons.all().order_by('id')
            topic_sims = Simulation.objects.filter(subject__iexact=sim_subject_str, topic__icontains=topic.name.replace('Topic ', '').split(':')[0]).count() if sim_subject_str else 0
            
            topic_info = {
                "id": topic.id,
                "name": topic.name,
                "lesson_count": lessons.count(),
                "block_count": 0,
                "lessons": []
            }
            
            for lesson in lessons:
                blocks = lesson.blocks.all().order_by('order', 'id')
                block_count = blocks.count()
                topic_info["block_count"] += block_count
                subject_data["block_count"] += block_count
                subject_data["lesson_count"] += 1
                
                lesson_info = {
                    "id": lesson.id,
                    "title": lesson.title,
                    "status": lesson.status,
                    "block_count": block_count,
                    "block_types": [b.block_type for b in blocks]
                }
                topic_info["lessons"].append(lesson_info)
                
                # Check each block for LaTeX leaks and content richness
                for b in blocks:
                    b_type = b.block_type
                    subject_data["block_types_distribution"][b_type] = subject_data["block_types_distribution"].get(b_type, 0) + 1
                    
                    # Inspect block content string fields
                    content_str = json.dumps(b.content) if isinstance(b.content, (dict, list)) else str(b.content)
                    
                    # Also check title
                    title_issues = check_latex_leak(b.title or "")
                    if title_issues:
                        for iss in title_issues:
                            subject_data["latex_issues"].append({
                                "lesson_id": lesson.id,
                                "lesson_title": lesson.title,
                                "topic_name": topic.name,
                                "block_id": b.id,
                                "block_type": b.block_type,
                                "location": "title",
                                "issue": iss
                            })
                            total_leaks_found += 1
                            
                    # Check body/content
                    content_issues = check_latex_leak(content_str)
                    if content_issues:
                        for iss in content_issues:
                            subject_data["latex_issues"].append({
                                "lesson_id": lesson.id,
                                "lesson_title": lesson.title,
                                "topic_name": topic.name,
                                "block_id": b.id,
                                "block_type": b.block_type,
                                "location": "content",
                                "issue": iss
                            })
                            total_leaks_found += 1
                            
            subject_data["topics_detail"].append(topic_info)
            
        results[subject_label] = subject_data
        
    return results, total_leaks_found

results, total_leaks = scan_all()

# Print executive summary
print("=" * 80)
print(f"CURRICULUM SCAN COMPLETE: {len(results)} SUBJECTS AUDITED")
print(f"TOTAL POTENTIAL LATEX / KATEX ISSUES DETECTED: {total_leaks}")
print("=" * 80)

for subj_label, s_data in results.items():
    print(f"\n[{subj_label}] (Grade: {s_data['grade']}, ID: {s_data['id']})")
    print(f"  - Topics: {s_data['topic_count']}")
    print(f"  - Lessons: {s_data['lesson_count']}")
    print(f"  - Total Content Blocks: {s_data['block_count']} (avg {round(s_data['block_count']/(s_data['lesson_count'] or 1), 1)} blocks/lesson)")
    print(f"  - Simulations Available: {s_data['simulations_count']}")
    print(f"  - Experiments Available: {s_data['experiments_count']}")
    print(f"  - Block Types: {s_data['block_types_distribution']}")
    print(f"  - LaTeX/KaTeX Leaks Found: {len(s_data['latex_issues'])}")
    if s_data['latex_issues']:
        for issue in s_data['latex_issues'][:10]:  # preview first 10
            print(f"    * [Lesson {issue['lesson_id']} - {issue['block_type']}] ({issue['location']}): {issue['issue']}")
        if len(s_data['latex_issues']) > 10:
            print(f"    * ... and {len(s_data['latex_issues']) - 10} more issues.")

# Save full results as JSON for deeper analysis
with open("curriculum_scan_report.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nFull scan report saved to curriculum_scan_report.json")
