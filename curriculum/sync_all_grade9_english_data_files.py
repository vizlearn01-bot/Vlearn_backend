"""
VLearn CBC Grade 9 English — Data Files Video Synchronization Script
Updates verified live YouTube video IDs in cbc_grade9_english_topic[1..4]_data.py files.
"""

import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from curriculum.update_all_grade9_english_videos import VERIFIED_VIDEOS

data_files = {
    1: BASE_DIR / "cbc_grade9_english_topic1_data.py",
    2: BASE_DIR / "cbc_grade9_english_topic2_data.py",
    3: BASE_DIR / "cbc_grade9_english_topic3_data.py",
    4: BASE_DIR / "cbc_grade9_english_topic4_data.py"
}

for (t_order, u_order), vdata in VERIFIED_VIDEOS.items():
    file_path = data_files.get(t_order)
    if not file_path or not file_path.exists():
        continue
    content = file_path.read_text(encoding="utf-8")
    
    # We will search for unit_order or lesson blocks to update youtube_id and url
    # Let's replace youtube_id patterns within the specific lesson definition
    new_id = vdata["id"]
    new_url = f"https://www.youtube.com/watch?v={new_id}"

print("[+] Synchronizing data files...")

# Let's do regex replacements per lesson section in data files
for t_order, fpath in data_files.items():
    if not fpath.exists():
        continue
    text = fpath.read_text(encoding="utf-8")
    
    for (top_num, unit_num), vdata in VERIFIED_VIDEOS.items():
        if top_num != t_order:
            continue
        new_id = vdata["id"]
        # Find unit section
        # Replace youtube_id: "..." and url: "https://www.youtube.com/watch?v=..."
        # We can regex substitute inside the matching unit block
        pattern = rf'("unit_order":\s*{unit_num},[\s\S]*?"type":\s*"suggested_video"[\s\S]*?"youtube_id":\s*")[^"]+("[\s\S]*?"url":\s*")https://www\.youtube\.com/watch\?v=[^"]+(")'
        replacement = rf'\g<1>{new_id}\g<2>https://www.youtube.com/watch?v={new_id}\g<3>'
        text = re.sub(pattern, replacement, text, count=1)
        
    fpath.write_text(text, encoding="utf-8")
    print(f"  [✔] Synchronized {fpath.name}")

print("Done!")
