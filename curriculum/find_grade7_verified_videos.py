"""
Live YouTube Video Finder and oEmbed Verifier for Grade 7 Home Science.
Runs live queries directly on YouTube, extracts candidate video IDs, and
verifies each via YouTube's official oEmbed endpoint.
"""

import urllib.request
import urllib.parse
import re
import json
import time

def search_and_verify(query, max_candidates=5):
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

LESSON_QUERIES = [
    # Topic 1
    (1, "Kitchen Hazards & Causes of Accidents", "kitchen safety hazards for kids animation"),
    (1, "Accident Prevention & Safe Work Habits", "kitchen cooking safety rules for kids do and don'ts"),
    (1, "Emergency First Aid & Kitchen Protective Apparel", "first aid for burns British Red Cross St John Ambulance"),
    # Topic 2
    (2, "Classification & Functional Families of Kitchen Tools", "kitchen tools and equipment and their uses culinary"),
    (2, "Smart Buying, Budgeting & Tool Care Protocols", "kitchen knife safety cutting board care maintenance"),
    (2, "Creative Improvisation & Upcycling Projects", "upcycling DIY kitchen utensils crafts"),
    # Topic 3
    (3, "Principles of Heat Transfer & Grilling Food", "heat transfer conduction convection radiation science for kids"),
    (3, "Roasting & The Improvised Dual-Sufuria Sand Oven", "dry heat cooking methods roasting and baking"),
    (3, "Steaming Food & Nutrient Preservation", "steaming food cooking method nutrients"),
    (3, "Fuel Conservation, Kitchen Safety & Creative Plating", "energy efficient cooking tips save fuel kitchen"),
    # Topic 4
    (4, "Household Needs: Tangible Goods vs. Paid Services", "goods and services for kids social studies economics"),
    (4, "Factors Influencing Buying Choices & Smart Saving", "financial literacy for kids needs and wants saving money"),
    (4, "Where We Shop, Payment Methods & The Market Survey", "smart shopping comparison shopping price comparison"),
    (4, "Safe Transactions, Market Challenges & Consumer Integrity", "consumer rights and responsibilities consumer awareness"),
    # Topic 5
    (5, "Classification & Sources of Natural Textile Fibres", "natural fibres cotton wool silk linen textiles"),
    (5, "Physical Properties & Microscopic Shapes of Natural Fibres", "properties of natural fibres cotton wool silk"),
    (5, "Everyday Household Uses & Sight/Feel Detection", "fabric identification touch and sight textiles"),
    (5, "The Science of Burning Tests & Laboratory Safety", "fabric burn test fiber identification textile science"),
    # Topic 6
    (6, "Sewing Machine Types & Smart Buying Choices", "types of sewing machines for beginners"),
    (6, "Anatomy & Mechanical Parts of the Sewing Machine", "parts of a sewing machine for beginners"),
    (6, "Setup, Threading & Safe Straight Stitching", "how to thread a sewing machine step by step beginner"),
    (6, "Troubleshooting Stitch Faults & Machine Care", "sewing machine tension troubleshooting stitch faults"),
    # Topic 7
    (7, "The Secret Inside Your Clothes: Understanding Seams & Allowances", "what is a seam and seam allowance beginner sewing"),
    (7, "The 4 Seam Types: Plain, French, Overlaid & Double-Stitched", "how to sew a french seam step by step"),
    (7, "Sealing Raw Edges: Pinking, Edge-Stitching & Hand Loop Stitches", "how to finish raw seam edges pinking shears overcast"),
    (7, "Quality Audits & Step-by-Step Lap Bag Construction", "how to sew a simple tote bag beginner sewing"),
    # Topic 8
    (8, "Water Properties, Lathering Science & Soaps vs. Detergents", "hard water vs soft water science fuse school"),
    (8, "Forms of Cleaning Agents & The 4 Ingredients of Saponification", "saponification chemistry of soap making OLabs"),
    (8, "Safe Cold Soap-Making, 4-Week Curing & Premium Additives", "cold process soap making tutorial beginner chemistry"),
    (8, "The JSS Community Soap Project: Health, Sanitation & Enterprise", "handwashing with soap hygiene sanitation animation"),
    # Topic 9
    (9, "The 4 Special Treatments: Spotting, Sponging, Starching & Dry-Cleaning", "special laundry care clothing care spotting starching"),
    (9, "Stain Chemistry & Precision Spotting Techniques", "science of stain removal how to remove stains"),
    (9, "Zero-Cost Homemade Starch Extraction & Fabric Starching", "how to starch clothes at home DIY starch"),
    (9, "Sponging Structured Blazers, Safe Dry-Cleaning & Eco-Disposal", "how to clean suit jacket blazer at home"),
]

if __name__ == "__main__":
    results = {}
    for topic_order, lesson_name, query in LESSON_QUERIES:
        print(f"\n[Searching] Topic {topic_order}: {lesson_name} -> Query: '{query}'")
        candidates = search_and_verify(query, max_candidates=3)
        results[lesson_name] = candidates
        for i, c in enumerate(candidates, 1):
            print(f"  {i}. [{c['id']}] \"{c['title']}\" by {c['author']}")
        time.sleep(0.5)

    with open("/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend/curriculum/grade7_verified_videos.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\n[SUCCESS] Verified video search complete. Saved to grade7_verified_videos.json")
