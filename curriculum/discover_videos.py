import os
import sys
import json
import urllib.request
import urllib.parse
import re

# Search YouTube HTML pages for valid video IDs and check with oEmbed
def search_youtube_query(query):
    encoded = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={encoded}"
    req = urllib.request.Request(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            # Extract videoIds
            video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
            # unique while preserving order
            seen = set()
            unique_ids = []
            for v in video_ids:
                if v not in seen:
                    seen.add(v)
                    unique_ids.append(v)
            return unique_ids[:10]
    except Exception as e:
        print(f"Error scraping YT search for '{query}': {e}")
        return []

def verify_video_id(vid):
    oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
    req = urllib.request.Request(oembed_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return True, data.get('title'), data.get('author_name')
    except Exception:
        pass
    return False, None, None

LESSON_TOPICS = {
    (1, 1): "polite language euphemisms english lesson",
    (1, 2): "empathy active listening communication skills",
    (1, 4): "job interview skills tips english",
    (1, 6): "listening for details note taking english",
    (1, 7): "diphthongs english pronunciation phonetics",
    (1, 8): "question tags intonation sentence stress english",
    
    (2, 2): "sq3r reading method note taking summarising",
    (2, 3): "oral literature proverbs riddles tongue twisters",
    (2, 4): "how to analyze a poem rhythm rhyme structure",
    (2, 6): "characterization and conflict in literature",
    (2, 7): "literary themes style and lessons",
    
    (3, 1): "gender neutral language english grammar",
    (3, 2): "noun formation suffixes and quantifiers english",
    (3, 3): "relative pronouns who whom whose which that grammar",
    (3, 4): "order of adjectives english grammar lesson",
    (3, 5): "correlative conjunctions and prepositions grammar",
    (3, 6): "modal verbs modal auxiliaries english grammar",
    (3, 7): "present perfect vs past perfect tense english",
    (3, 8): "reported speech indirect speech rules grammar",
    
    (4, 3): "formal letter writing format and job application",
    (4, 4): "professional email writing etiquette format",
    (4, 6): "narrative writing plot structure story elements",
    (4, 7): "idioms in creative writing english figurative language"
}

if __name__ == '__main__':
    selected_videos = {}
    for (t, u), query in LESSON_TOPICS.items():
        print(f"\nSearching for T{t}.L{u} ('{query}')...")
        vids = search_youtube_query(query)
        print(f"Found candidate IDs: {vids}")
        found = False
        for vid in vids:
            ok, title, author = verify_video_id(vid)
            if ok:
                print(f"  --> MATCH: {vid} | '{title}' by {author}")
                selected_videos[(t, u)] = {
                    "video_id": vid,
                    "title": title,
                    "author": author
                }
                found = True
                break
        if not found:
            print(f"  --> NO VALID VIDEO FOUND for T{t}.L{u}")
            
    with open('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/curriculum/discovered_videos.json', 'w') as f:
        # Convert tuple keys to string
        json.dump({f"{k[0]}_{k[1]}": v for k, v in selected_videos.items()}, f, indent=2)
    print(f"\nDiscovered {len(selected_videos)}/{len(LESSON_TOPICS)} verified replacement videos.")
