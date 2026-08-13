import importlib
import sys
import os

def check_topic(topic_name, module):
    report = []
    
    # Find all lesson variables
    lessons = []
    for key in dir(module):
        if key.startswith('LESSON_') and key.endswith('_DATA') and isinstance(getattr(module, key), dict):
            lessons.append(getattr(module, key))
            
    if not lessons:
        report.append(f"Could not find LESSON_X_DATA dictionaries in {topic_name}")
        return report
        
    for lesson in lessons:
        lesson_title = lesson.get('lesson_title', 'Unknown Lesson')
        
        for page in lesson.get('pages', []):
            page_title = page.get('page_title', 'Unknown Page')
            
            for block in page.get('blocks', []):
                block_type = block.get('block_type', '')
                content = block.get('content', {})
                title = block.get('title', 'Unknown')
                
                # Check concept cards / explanations
                if block_type in ['concept_explanation', 'definition_card']:
                    text = content.get('text', '') or content.get('definition', '')
                    # Heuristic for missing steps / low detail
                    if len(text.split()) < 30 and block_type == 'concept_explanation':
                        report.append(f"[{topic_name} - {lesson_title} - {page_title}] {block_type} '{title}' has a short explanation ({len(text.split())} words). Might lack detail.")
                        
                # Check worked examples
                elif block_type == 'worked_example':
                    solution = str(content.get('steps', '')) + str(content.get('text', ''))
                    
                    has_trace = any(op in solution for op in ['+', '-', '*', '/', '=', 'Add', 'Subtract', 'Balance'])
                    has_t_account = 'T-account' in solution or 'Dr' in solution or 'Cr' in solution or 'Account' in solution or '|' in solution
                    
                    if not has_trace:
                        report.append(f"[{topic_name} - {lesson_title} - {page_title}] Worked Example '{title}' missing explicit arithmetic trace (+, -, =).")
                    
                    if not has_t_account and any(kw in lesson_title.lower() for kw in ['account', 'ledger', 'cash book']):
                        report.append(f"[{topic_name} - {lesson_title} - {page_title}] Worked Example '{title}' in accounting topic missing T-account formatting ('Dr', 'Cr', or '|').")
                        
                # Check SVGs
                # Sometimes the block type is 'interactive_svg' or 'visual_element' or it's a visualization array.
                # In the updated structure, they are often blocks of type 'svg_diagram' or 'visual_element'
                if block_type in ['svg_diagram', 'interactive_svg', 'visual_element']:
                    is_svg = content.get('type') == 'svg' or block_type in ['svg_diagram', 'interactive_svg']
                    if is_svg:
                        if 'svg_markup' not in content or 'svg_content' not in content:
                            report.append(f"[{topic_name} - {lesson_title} - {page_title}] SVG '{title}' missing 'svg_markup' or 'svg_content'. Present: {list(content.keys())}")
                            
                # Also just in case they put SVGs in visualizations
                if 'visualizations' in content:
                    for vis in content['visualizations']:
                        if vis.get('type') == 'svg':
                            vis_content = vis.get('content', {})
                            if 'svg_markup' not in vis_content or 'svg_content' not in vis_content:
                                report.append(f"[{topic_name} - {lesson_title} - {page_title}] Nested SVG in '{title}' missing keys. Present: {list(vis_content.keys())}")
                                

    return report

def main():
    sys.path.insert(0, '/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/curriculum')
    sys.path.insert(0, '/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
    
    overall_report = []
    
    for i in range(1, 8):
        topic_name = f"topic{i}_data"
        try:
            module = importlib.import_module(f'curriculum.{topic_name}')
            topic_report = check_topic(topic_name, module)
            if topic_report:
                overall_report.extend(topic_report)
            else:
                overall_report.append(f"{topic_name}: All checks passed based on heuristics.")
        except Exception as e:
            overall_report.append(f"Error loading {topic_name}: {e}")
            
    with open('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/curriculum/audit_report_bs.txt', 'w') as f:
        f.write("\n".join(overall_report))
        
if __name__ == '__main__':
    main()
