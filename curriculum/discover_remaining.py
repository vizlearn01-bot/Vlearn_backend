import os
import sys
import json
import urllib.request
import urllib.parse
import re

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
            video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
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

REMAINING_TOPICS = {
    (1, 2): "brene brown empathy rsa",
    (1, 8): "question tags intonation english pronunciation",
    (3, 1): "inclusive gender neutral pronouns english grammar"
}

if __name__ == '__main__':
    with open('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/curriculum/discovered_videos.json', 'r') as f:
        discovered = json.load(f)
        
    for (t, u), query in REMAINING_TOPICS.items():
        print(f"\nSearching for T{t}.L{u} ('{query}')...")
        vids = search_youtube_query(query)
        print(f"Found candidate IDs: {vids}")
        for vid in vids:
            ok, title, author = verify_video_id(vid)
            if ok:
                print(f"  --> MATCH: {vid} | '{title}' by {author}")
                discovered[f"{t}_{u}"] = {
                    "video_id": vid,
                    "title": title,
                    "author": author
                }
                break
                
    with open('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/curriculum/discovered_videos.json', 'w') as f:
        json.dump(discovered, f, indent=2)
    print(f"\nTotal discovered and verified in dictionary: {len(discovered)}/23")
