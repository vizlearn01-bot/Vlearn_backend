import os
import re

for topic_num in [7, 8, 9, 10]:
    md_path = f"/home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 10 Business Studies/Grade10_Business_Studies_Topic_{topic_num}.md"
    print(f"==================== TOPIC {topic_num} ====================")
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_lesson = None
    for line in lines:
        if line.startswith("## Lesson"):
            current_lesson = line.strip()
            print("\n" + current_lesson)
        elif line.startswith("### ") and current_lesson:
            print("  ", line.strip())
