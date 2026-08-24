"""
Live YouTube Video Finder and oEmbed Verifier for Grade 8 Home Science.
Runs live queries directly on YouTube, extracts candidate video IDs, and
verifies each via YouTube's official oEmbed endpoint.
"""

import urllib.request
import urllib.parse
import re
import json
import time

def search_and_verify(query, max_candidates=4):
    encoded = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={encoded}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    })
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8")
            video_ids = re.findall(r'\"videoId\":\"([a-zA-Z0-9_-]{11})\"', html)
            
            seen = set()
            unique_ids = []
            for vid in video_ids:
                if vid not in seen:
                    seen.add(vid)
                    unique_ids.append(vid)
            
            verified = []
            for vid in unique_ids:
                oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
                oreq = urllib.request.Request(oembed_url, headers={"User-Agent": "Mozilla/5.0"})
                try:
                    with urllib.request.urlopen(oreq, timeout=3) as oresp:
                        if oresp.status == 200:
                            data = json.loads(oresp.read().decode())
                            verified.append({
                                "id": vid,
                                "title": data.get("title"),
                                "author": data.get("author_name"),
                                "url": f"https://www.youtube.com/watch?v={vid}"
                            })
                            if len(verified) >= max_candidates:
                                break
                except:
                    continue
            return verified
    except Exception as e:
        print(f"Error for query '{query}': {e}")
        return []

GRADE8_LESSON_QUERIES = [
    # Topic 1: Foods and Nutrition
    (1, 715, "Kitchen Gardening & Household Food Security", "kitchen gardening container gardening for beginners food security"),
    (1, 716, "Scientific Cooking of Starchy Carbohydrate Foods", "gelatinization of starch cooking science chemistry of carbohydrates"),
    (1, 717, "Table Setting, Meal Presentation & Service Styles", "how to set a dining table properly table manners service styles"),
    (1, 718, "Nutritional Meal Planning for Special Groups", "meal planning for special nutritional needs elderly adolescents pregnant"),
    (1, 719, "Meals for Special Occasions & Kitchen Waste Management", "kitchen waste management composting food waste segregation"),
    
    # Topic 2: Consumer Education
    (2, 720, "Consumer Awareness & Household Buying Habits", "consumer awareness and rights financial literacy smart buying habits"),
    (2, 721, "Market Competition & Consumer Protection", "consumer protection fair trade market competition economics"),
    
    # Topic 3: Textile and Clothing
    (3, 722, "Artificial Textile Fibres", "synthetic fibres nylon polyester rayon acrylic textile science"),
    (3, 723, "Seams in Garment Construction", "how to sew a flat felled seam run and fell seam tutorial"),
    (3, 724, "Methods of Controlling Fullness", "how to sew gathers pleats and darts controlling fullness sewing basics"),
    
    # Topic 4: Caring for the Family
    (4, 725, "Childcare & Prenatal Development", "prenatal care and baby development maternal health education"),
    (4, 726, "Providing Family Shelter", "types of houses and shelter building materials home science"),
    (4, 727, "Room & Area Interrelationship", "house floor plan room layout functional zones interior design basics"),
    (4, 728, "The Kitchen & The Work Triangle", "kitchen work triangle layout ergonomic kitchen design"),
    (4, 729, "Cleaning the Kitchen & Surface Care", "kitchen deep cleaning routine surface care degreasing countertops"),
    (4, 730, "Colour in the Home & Interior Decoration", "colour theory in interior design colour wheel room decoration"),
    (4, 731, "Soft Furnishings & Home Crafts", "DIY soft furnishings cushion covers curtains home decor crafts"),
    
    # Topic 5: Community Service Learning (CSL) Class Activity
    (5, 732, "Spotting Community Problems & Pertinent Issues", "community problem solving identifying community needs youth action"),
    (5, 733, "Community Research & Data Collection Tools", "data collection methods interviews surveys research for students"),
    (5, 734, "Project Planning, Resource Management & Reflection", "project management planning and execution for students CSL reflection"),
]

if __name__ == "__main__":
    results = {}
    for topic_order, lesson_id, lesson_name, query in GRADE8_LESSON_QUERIES:
        print(f"\n[Searching] Topic {topic_order} (ID {lesson_id}): {lesson_name} -> Query: '{query}'")
        candidates = search_and_verify(query, max_candidates=3)
        results[lesson_name] = candidates
        for i, c in enumerate(candidates, 1):
            print(f"  {i}. [{c['id']}] \"{c['title']}\" by {c['author']}")
        time.sleep(0.5)

    with open("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/curriculum/grade8_verified_videos.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\n[SUCCESS] Verified video search complete for Grade 8. Saved to grade8_verified_videos.json")
