import os, sys, django, json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

print("Starting deep math leak audit across all blocks and fields...")

issues = []

def check_text_for_leaks(text_val, block_info, field_name):
    if not isinstance(text_val, str) or not text_val.strip():
        return
    
    # 1. Check for unbalanced dollar signs
    # Exclude escaped dollars \$
    clean = re.sub(r'\\\$', '', text_val)
    # Exclude $$...$$ blocks
    clean_no_display = re.sub(r'\$\$[\s\S]*?\$\$', '', clean)
    # Count remaining single dollars
    dollar_count = clean_no_display.count('$')
    if dollar_count % 2 != 0:
        issues.append({
            'type': 'UNBALANCED_DOLLARS',
            'block_info': block_info,
            'field': field_name,
            'count': dollar_count,
            'snippet': clean_no_display[:120]
        })
    
    # 2. Check for naked subscripts like P_1, V_2, T_1, P_2V_2, R_A outside $...$ and $$...$$
    # Strip all valid math blocks ($$...$$ and $...$)
    outside_math = re.sub(r'\$\$[\s\S]*?\$\$', '', text_val)
    outside_math = re.sub(r'\$[^\$\n]+?\$', '', outside_math)
    
    # Search for naked subscripts (e.g. P_1, V_2, P_1V_1, R_A, M_r, etc.)
    # Exclude markdown formatting, URLs, code blocks, html tags
    naked_subscripts = re.findall(r'(?<![a-zA-Z0-9_\$])([A-Za-z]_[0-9A-Za-z]+)(?![a-zA-Z0-9_\$])', outside_math)
    if naked_subscripts:
        issues.append({
            'type': 'NAKED_SUBSCRIPTS',
            'block_info': block_info,
            'field': field_name,
            'items': list(set(naked_subscripts)),
            'snippet': outside_math[:120].strip()
        })
        
    # 3. Check for naked LaTeX commands
    naked_commands = re.findall(r'\\(?:frac|sqrt|implies|propto|times|approx|circ|rightarrow|rightleftharpoons|rho|Delta|text|mathrm|mathbf)\b', outside_math)
    if naked_commands:
        issues.append({
            'type': 'NAKED_COMMANDS',
            'block_info': block_info,
            'field': field_name,
            'commands': list(set(naked_commands)),
            'snippet': outside_math[:120].strip()
        })

for b in LessonBlock.objects.all().select_related('lesson'):
    les = b.lesson
    les_title = les.title if les else 'No Lesson'
    b_info = f"Lesson {b.lesson_id} ({les_title}) | Page {b.page_number} | Block {b.id} ({b.block_type})"
    
    if isinstance(b.content, dict):
        for k, v in b.content.items():
            if isinstance(v, str):
                check_text_for_leaks(v, b_info, k)
            elif isinstance(v, list):
                for idx, item in enumerate(v):
                    if isinstance(item, str):
                        check_text_for_leaks(item, b_info, f"{k}[{idx}]")
                    elif isinstance(item, dict):
                        for sub_k, sub_v in item.items():
                            if isinstance(sub_v, str):
                                check_text_for_leaks(sub_v, b_info, f"{k}[{idx}].{sub_k}")
            elif isinstance(v, dict):
                for sub_k, sub_v in v.items():
                    if isinstance(sub_v, str):
                        check_text_for_leaks(sub_v, b_info, f"{k}.{sub_k}")
    elif isinstance(b.content, str):
        check_text_for_leaks(b.content, b_info, 'content')

print(f"Total potential issues found: {len(issues)}")
for i, iss in enumerate(issues[:40]):
    print(f"[{i+1}] {iss['type']} in {iss['block_info']} -> Field: {iss['field']}")
    if 'items' in iss:
        print(f"     Items: {iss['items']}")
    if 'commands' in iss:
        print(f"     Commands: {iss['commands']}")
    print(f"     Snippet: {repr(iss['snippet'])}")
    print()
