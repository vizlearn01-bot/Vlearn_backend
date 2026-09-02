import os
import re

for topic_num in [7, 8, 9, 10]:
    md_path = f"/home/jason-bitega/Desktop/VL/vlearn_repositories/Grade 10 Business Studies/Grade10_Business_Studies_Topic_{topic_num}.md"
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"=== TOPIC {topic_num} ===")
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        print("Title:", title_match.group(1) if title_match else "N/A")
        lessons = re.findall(r'^##\s+(Lesson\s+\d+:\s*.+)$', content, re.MULTILINE)
        print(f"Total Lessons ({len(lessons)}):")
        for l in lessons:
            print(" -", l)
    else:
        print(f"Topic {topic_num} markdown NOT found at {md_path}")
