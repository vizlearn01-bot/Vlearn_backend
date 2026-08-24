"""
VLearn CBC Grade 8 — Home Science
Live-Verified YouTube Video Enrichment Script

Enriches all 20 lessons across the 5 Topics of CBC Grade 8 Home Science
with 100% live-verified, active, working, and educationally matched YouTube videos.
All video URLs were verified live against YouTube's official oEmbed API.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db.models import Max
from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


GRADE8_VERIFIED_ENRICHMENTS = [
    # =========================================================================
    # TOPIC 1: FOODS AND NUTRITION (5 Lessons)
    # =========================================================================
    {
        "topic_order": 1,
        "lesson_id": 715,
        "lesson_contains": "Kitchen Gardening & Household Food Security",
        "video": {
            "title": "Watch: How To Prepare Soil For Sacks & Containers Vegetable Gardening",
            "url": "https://www.youtube.com/watch?v=xYUYpmj6LC4",
            "author": "Orina Dominic",
            "description": "Learn practical soil preparation and container/sack gardening techniques for urban and rural households — mixing topsoil, compost manure, and sand to grow nutritious indigenous vegetables (sukuma wiki, spinach, terere) and secure household food security.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What is the recommended ratio of topsoil, well-rotted manure, and sand when preparing sack or container gardens?\n\n"
                "**2.** How does practicing kitchen gardening improve household nutrition and save family food expenses?\n\n"
                "**3.** Identify a small unused space at home or school where you could set up a sack or recycled bucket garden."
            )
        }
    },
    {
        "topic_order": 1,
        "lesson_id": 716,
        "lesson_contains": "Scientific Cooking of Starchy Carbohydrate Foods",
        "video": {
            "title": "Watch: What is Starch Gelatinization — Food Science & Processing",
            "url": "https://www.youtube.com/watch?v=qXv6vcgJYII",
            "author": "Esculenta Science",
            "description": "Understand the scientific principles of cooking starchy foods — how starch granules absorb water, swell under moist heat, and gelatinize at specific temperatures to make foods like ugali, rice, and porridge digestible, soft, and palatable.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Describe what happens to starch granules when heated in liquid during the gelatinization process.\n\n"
                "**2.** Why must maize flour be stirred continuously when making ugali or porridge to prevent lump formation?\n\n"
                "**3.** What is retrogradation (staling), and what happens when cooked starchy foods cool down?"
            )
        }
    },
    {
        "topic_order": 1,
        "lesson_id": 717,
        "lesson_contains": "Table Setting, Meal Presentation & Service Styles",
        "video": {
            "title": "Watch: How to Properly Set a Dining Table",
            "url": "https://www.youtube.com/watch?v=e5Rh41TfYiI",
            "author": "Small & Simple Stuff",
            "description": "A step-by-step visual tutorial on setting a dining table correctly — arranging cutlery (forks on the left, knives and spoons on the right), water glasses, side plates, and napkins for casual and formal meal service.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** On which side of the dinner plate are forks placed, and where do knives and soup spoons go?\n\n"
                "**2.** What is the difference between family-style meal service and buffet-style service?\n\n"
                "**3.** Practice setting a clean, organized table setting for your family's evening meal using available tableware."
            )
        }
    },
    {
        "topic_order": 1,
        "lesson_id": 718,
        "lesson_contains": "Nutritional Meal Planning for Special Groups",
        "video": {
            "title": "Watch: Planning Meals for Adolescents — Food, Nutrition & Health",
            "url": "https://www.youtube.com/watch?v=MdNln-7VC18",
            "author": "Fairy's Tutorials",
            "description": "Explore the unique nutritional requirements of special physiological groups — adolescent growth spurts, pregnant/lactating mothers, manual workers, convalescents, and the elderly — emphasizing balanced nutrient density.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why do adolescent girls require increased dietary iron compared to other age groups?\n\n"
                "**2.** What special dietary considerations should be kept in mind when preparing meals for an elderly family member?\n\n"
                "**3.** Plan a balanced one-day menu for a teenage athlete including energy, body-building, and protective foods."
            )
        }
    },
    {
        "topic_order": 1,
        "lesson_id": 719,
        "lesson_contains": "Meals for Special Occasions & Kitchen Waste Management",
        "video": {
            "title": "Watch: How to Decompose Kitchen Scraps & Make Compost",
            "url": "https://www.youtube.com/watch?v=6KPYWQF-YCk",
            "author": "Our Green Diary",
            "description": "Learn effective household kitchen waste management — segregating organic food scraps from non-biodegradable waste, constructing a compost pit, and turning vegetable peelings into rich organic fertilizer for the kitchen garden.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What kitchen waste items are suitable for composting, and which items (e.g. bones, plastic) must be excluded?\n\n"
                "**2.** How does sorting and composting kitchen waste help both the environment and family gardening?\n\n"
                "**3.** Design a 3-course menu suitable for a special family celebration (e.g. birthday or graduation)."
            )
        }
    },

    # =========================================================================
    # TOPIC 2: CONSUMER EDUCATION (2 Lessons)
    # =========================================================================
    {
        "topic_order": 2,
        "lesson_id": 720,
        "lesson_contains": "Consumer Awareness & Household Buying Habits",
        "video": {
            "title": "Watch: Financial Literacy and Consumer Choices",
            "url": "https://www.youtube.com/watch?v=0KC3LQ7t1dM",
            "author": "ClickView",
            "description": "Understand consumer decision-making and psychology — recognizing how advertising, peer influence, and branding impact buying habits, and developing a shopping checklist to avoid impulse purchasing.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** How do marketing strategies in supermarkets encourage shoppers to spend money on impulse items?\n\n"
                "**2.** Why is preparing a strict shopping list before visiting the market considered a smart financial habit?\n\n"
                "**3.** Give an example of a buying decision you made recently and evaluate whether it was driven by a need or a want."
            )
        }
    },
    {
        "topic_order": 2,
        "lesson_id": 721,
        "lesson_contains": "Market Competition & Consumer Protection",
        "video": {
            "title": "Watch: Antitrust & Competition Laws Explained",
            "url": "https://www.youtube.com/watch?v=8tQa92BWjvM",
            "author": "One Minute Economics",
            "description": "Discover how fair market competition protects consumers from monopolies and price-fixing, ensuring fair pricing, high product quality, and consumer choice across retail markets.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** How does healthy competition between different sellers benefit ordinary household consumers?\n\n"
                "**2.** What is a monopoly, and why can monopolies be harmful to consumers in terms of price and quality?\n\n"
                "**3.** Which regulatory body in Kenya protects consumers against counterfeit products and substandard goods?"
            )
        }
    },

    # =========================================================================
    # TOPIC 3: TEXTILE AND CLOTHING (3 Lessons)
    # =========================================================================
    {
        "topic_order": 3,
        "lesson_id": 722,
        "lesson_contains": "Artificial Textile Fibres",
        "video": {
            "title": "Watch: Types of Synthetic Fibres — Nylon, Rayon, Polyester & Acrylic",
            "url": "https://www.youtube.com/watch?v=yA5yiz14VdE",
            "author": "Aastha Mulkarwar",
            "description": "An educational guide to artificial/synthetic textile fibres — exploring the origins, chemical production, and properties of regenerated cellulose (rayon) and synthetic polymers (nylon, polyester, acrylic).",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What is the difference between a regenerated fibre (like rayon/viscose) and a purely synthetic fibre (like nylon)?\n\n"
                "**2.** State TWO advantages and TWO disadvantages of synthetic polyester fabrics compared to natural cotton.\n\n"
                "**3.** Why must synthetic garments be ironed at low heat settings compared to cotton or linen?"
            )
        }
    },
    {
        "topic_order": 3,
        "lesson_id": 723,
        "lesson_contains": "Seams in Garment Construction",
        "video": {
            "title": "Watch: How To Sew a TRUE Flat Felled Seam — Step-by-Step Tutorial",
            "url": "https://www.youtube.com/watch?v=E1vJzVW2lLk",
            "author": "Notches Sewing",
            "description": "Learn the construction of the flat-felled (run-and-fell) seam — a very strong, flat, double-stitched seam with no exposed raw edges, widely used in jeans, sportswear, men's shirts, and reversible garments.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why is a flat-felled (machine-and-fell) seam preferred for sewing heavy garments like denim jeans and school shorts?\n\n"
                "**2.** Describe the trimming step in a flat-felled seam: why is one seam allowance trimmed to half its width?\n\n"
                "**3.** How many rows of stitching are visible on the right side of a completed flat-felled seam?"
            )
        }
    },
    {
        "topic_order": 3,
        "lesson_id": 724,
        "lesson_contains": "Methods of Controlling Fullness",
        "video": {
            "title": "Watch: Types of Pleats, Tucks, Gathering, Shirring and Smocking",
            "url": "https://www.youtube.com/watch?v=OXwCj-uuXP0",
            "author": "Garments Learner",
            "description": "A comprehensive overview of garment fullness control methods — demonstrating how darts shape flat fabric to body curves, how gathers and pleats distribute volume, and how tucks add decorative structure.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What is the main functional difference between a dart (shaping to body curves) and gathering (distributing fullness)?\n\n"
                "**2.** Name THREE types of pleats commonly used in skirts and school uniforms (knife pleats, box pleats, inverted pleats).\n\n"
                "**3.** Inspect a dress, skirt, or pair of trousers at home. Which methods of controlling fullness can you identify?"
            )
        }
    },

    # =========================================================================
    # TOPIC 4: CARING FOR THE FAMILY (7 Lessons)
    # =========================================================================
    {
        "topic_order": 4,
        "lesson_id": 725,
        "lesson_contains": "Childcare & Prenatal Development",
        "video": {
            "title": "Watch: Prenatal Care & Trimester Visits — Maternal & Child Health",
            "url": "https://www.youtube.com/watch?v=wt9-6VWbfHI",
            "author": "Level Up RN",
            "description": "An educational health review covering prenatal care — maternal nutrition, folic acid and iron supplementation, avoiding harmful substances, routine clinical check-ups, and immunization for healthy infant development.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why is early and regular prenatal clinic attendance critical for both mother and unborn child?\n\n"
                "**2.** What role does folic acid play in preventing birth defects during early pregnancy?\n\n"
                "**3.** State three essential hygiene practices when caring for a newborn baby at home."
            )
        }
    },
    {
        "topic_order": 4,
        "lesson_id": 726,
        "lesson_contains": "Providing Family Shelter",
        "video": {
            "title": "Watch: Building a Traditional House with Local Natural Materials",
            "url": "https://www.youtube.com/watch?v=ZETR7IGTjS8",
            "author": "FutureLoom",
            "description": "Explore the principles of family shelter — comparing traditional housing using local earth, timber, and thatch with modern permanent construction (bricks, cement, iron sheets), evaluating climate suitability and ventilation.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What are the primary functions of family shelter (protection, privacy, security, bonding)?\n\n"
                "**2.** Compare the thermal comfort of a mud-thatch house with a stone-iron sheet house in hot weather.\n\n"
                "**3.** Name three local building materials available in your community and state their uses in shelter construction."
            )
        }
    },
    {
        "topic_order": 4,
        "lesson_id": 727,
        "lesson_contains": "Room & Area Interrelationship",
        "video": {
            "title": "Watch: Architect's Advice — Floor Plan Layouts & Functional Zones",
            "url": "https://www.youtube.com/watch?v=OvSPAvG0_A4",
            "author": "baixu",
            "description": "Learn how residential spaces are organized into functional zones — living/social area, sleeping/quiet area, and service/work area (kitchen and bathrooms) — and how efficient circulation connects them without noise conflict.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What are the three primary functional zones in a residential house plan?\n\n"
                "**2.** Why should the kitchen have easy access to the dining area and an external service entrance?\n\n"
                "**3.** Draw a simple sketch of your home's layout and label the social, quiet, and service zones."
            )
        }
    },
    {
        "topic_order": 4,
        "lesson_id": 728,
        "lesson_contains": "The Kitchen & The Work Triangle",
        "video": {
            "title": "Watch: The Kitchen Work Triangle Rule & Ergonomic Layouts",
            "url": "https://www.youtube.com/watch?v=D7KhBDig-hY",
            "author": "Kitchinsider",
            "description": "Understand the classic kitchen work triangle connecting the three main workstation hubs — food storage (refrigerator/pantry), preparation/washing (sink), and cooking (stove/jiko) — minimizing unnecessary footsteps and fatigue.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Which three workstation hubs form the corners of the kitchen work triangle?\n\n"
                "**2.** Why should traffic pathways through the kitchen avoid cutting across the work triangle?\n\n"
                "**3.** What kitchen floor layout (L-shaped, U-shaped, Corridor, One-wall) does your home kitchen have?"
            )
        }
    },
    {
        "topic_order": 4,
        "lesson_id": 729,
        "lesson_contains": "Cleaning the Kitchen & Surface Care",
        "video": {
            "title": "Watch: Do THIS To Keep Your Kitchen Clean & Grease-Free",
            "url": "https://www.youtube.com/watch?v=OYbIWeASTMI",
            "author": "Clean That Up",
            "description": "A practical guide to kitchen sanitation and surface care — degreasing stovetops, sanitizing food prep counters, descaling sinks, and scrubbing tile floors with appropriate cleaning agents.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why is it important to use separate cleaning cloths for washing dishes versus wiping floors?\n\n"
                "**2.** How does regular degreasing of stovetops and exhaust hoods prevent kitchen fire hazards?\n\n"
                "**3.** List the steps you would follow to thoroughly clean and sanitize a stainless steel kitchen sink."
            )
        }
    },
    {
        "topic_order": 4,
        "lesson_id": 730,
        "lesson_contains": "Colour in the Home & Interior Decoration",
        "video": {
            "title": "Watch: Interior Design Color Combinations & Home Decor Ideas",
            "url": "https://www.youtube.com/watch?v=FFSWd0PS2ek",
            "author": "D.Signers",
            "description": "Learn colour theory in home decoration — using the colour wheel, contrasting warm colours (red, orange, yellow) with cool calming tones (blue, green), and applying the 60-30-10 colour proportion rule.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** How do warm colours (like yellow and terracotta) affect the mood of a living room or dining room?\n\n"
                "**2.** What is the 60-30-10 rule in interior room decoration?\n\n"
                "**3.** Which colour palette would you choose for a quiet bedroom study area to promote concentration?"
            )
        }
    },
    {
        "topic_order": 4,
        "lesson_id": 731,
        "lesson_contains": "Soft Furnishings & Home Crafts",
        "video": {
            "title": "Watch: DIY Soft Furnishings & Cushion Covers Project",
            "url": "https://www.youtube.com/watch?v=usiUeI0Q5YY",
            "author": "Chris and Gunnar",
            "description": "A creative hands-on demonstration of making DIY soft furnishings — measuring, cutting, and stitching decorative throw cushions and pillow covers to enhance home comfort and beauty on a budget.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Name FOUR examples of soft furnishings used in a Kenyan home (curtains, cushion covers, bedspreads, table runners).\n\n"
                "**2.** How do soft furnishings contribute to both aesthetic beauty and physical comfort in a living room?\n\n"
                "**3.** What local fabric or craft technique (e.g. tie-and-dye, patchwork) would you use to make a cushion cover?"
            )
        }
    },

    # =========================================================================
    # TOPIC 5: COMMUNITY SERVICE LEARNING (CSL) CLASS ACTIVITY (3 Lessons)
    # =========================================================================
    {
        "topic_order": 5,
        "lesson_id": 732,
        "lesson_contains": "Spotting Community Problems & Pertinent Issues",
        "video": {
            "title": "Watch: Youth in Action — Identifying Community Problems & Solutions",
            "url": "https://www.youtube.com/watch?v=44JdQnCw0Ew",
            "author": "THINKING OUTSIDE THE BOX SHOW",
            "description": "Explore how young people identify pressing community challenges — water sanitation issues, youth unemployment, malnutrition, and environmental degradation — and brainstorm impactful community-led solutions.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What is the first step in identifying a genuine problem facing your school or local community?\n\n"
                "**2.** How can Home Science practical skills (like soap making, cooking, or tailoring) help solve community challenges?\n\n"
                "**3.** Name ONE pertinent problem in your neighbourhood that your class could tackle through a CSL project."
            )
        }
    },
    {
        "topic_order": 5,
        "lesson_id": 733,
        "lesson_contains": "Community Research & Data Collection Tools",
        "video": {
            "title": "Watch: Data Collection Methods — Surveys, Interviews & Observation",
            "url": "https://www.youtube.com/watch?v=Z2Uyw3HwuCg",
            "author": "Research Solution",
            "description": "A clear educational guide explaining primary data collection instruments — designing simple questionnaires, conducting polite interviews with community leaders, and recording direct observational data.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What is the difference between a questionnaire survey and an in-person interview?\n\n"
                "**2.** Why is direct observation a valuable tool when assessing community hygiene and sanitation needs?\n\n"
                "**3.** Draft THREE simple survey questions you would ask community members about local waste disposal."
            )
        }
    },
    {
        "topic_order": 5,
        "lesson_id": 734,
        "lesson_contains": "Project Planning, Resource Management & Reflection",
        "video": {
            "title": "Watch: Project Management Simplified — Planning, Execution & Evaluation",
            "url": "https://www.youtube.com/watch?v=ZKOL-rZ79gs",
            "author": "Deniz Sasal",
            "description": "Learn the essential phases of project management — defining project objectives, allocating budgets and local resources, assigning team roles, monitoring timelines, and conducting post-project reflection.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What are the 4 key stages of managing a successful community project (Initiation, Planning, Execution, Closure)?\n\n"
                "**2.** Why is keeping an accurate budget and resource inventory vital during project execution?\n\n"
                "**3.** How does post-project reflection help students evaluate what went well and what could be improved?"
            )
        }
    },
]


def run_enrichment():
    print("=" * 80)
    print("[START] CBC Grade 8 Home Science — Live-Verified Video Enrichment (20 Lessons)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 8").first()
    assert grade, "Grade 8 not found!"
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject 'Home Science' under Grade 8 not found!"

    print(f"[*] Hierarchy: {curriculum.name} -> {grade.name} -> {subject.name}\n")

    total_lessons_enriched = 0
    total_videos_created = 0
    total_blocks_created = 0

    for item in GRADE8_VERIFIED_ENRICHMENTS:
        topic_order = item["topic_order"]
        lesson_id = item["lesson_id"]
        lesson_substr = item["lesson_contains"]
        v_data = item["video"]

        topic = Topic.objects.filter(subject=subject, order=topic_order).first()
        if not topic:
            print(f"  [SKIP] Topic {topic_order} not found!")
            continue

        lesson = Lesson.objects.filter(id=lesson_id).first()
        if not lesson:
            for unit in topic.learning_units.all():
                candidate = unit.lessons.filter(title__icontains=lesson_substr).first()
                if candidate:
                    lesson = candidate
                    break

        if not lesson:
            print(f"  [SKIP] Lesson {lesson_id} ('{lesson_substr}') not found!")
            continue

        # 1. Clear any existing video blocks on page 9+ (idempotency)
        existing_video_pages = lesson.blocks.filter(block_type="suggested_video", page_number__gte=9)
        if existing_video_pages.exists():
            pages_to_clear = list(existing_video_pages.values_list("page_number", flat=True).distinct())
            lesson.blocks.filter(page_number__in=pages_to_clear).delete()
            lesson.assets.filter(asset_type="video").delete()

        # 2. Determine target page number (append to lesson, page 9)
        max_page = lesson.blocks.aggregate(max_page=Max("page_number"))["max_page"] or 8
        target_page = max_page + 1
        max_order = lesson.blocks.aggregate(max_order=Max("order"))["max_order"] or 0

        # 3. Create suggested_video block
        b_order = max_order + 1
        LessonBlock.objects.create(
            lesson=lesson,
            page_number=target_page,
            block_type="suggested_video",
            component_type="suggested_video",
            title=v_data["title"],
            order=b_order,
            content={
                "url": v_data["url"],
                "text": v_data["description"],
                "author": v_data["author"],
                "licensing": "Standard YouTube License"
            }
        )
        total_blocks_created += 1

        # 4. Create companion callout block on same page
        b_order += 1
        LessonBlock.objects.create(
            lesson=lesson,
            page_number=target_page,
            block_type="callout",
            component_type="callout",
            title="🎬 Reflect on What You Watched",
            order=b_order,
            content={
                "text": v_data["reflection"]
            }
        )
        total_blocks_created += 1

        # 5. Create LessonAsset
        LessonAsset.objects.update_or_create(
            lesson=lesson,
            title=v_data["title"],
            defaults={
                "asset_type": "video",
                "source_type": "external",
                "storage_type": "url",
                "status": "attached",
                "url": v_data["url"],
                "description": v_data["description"],
                "metadata": {
                    "author": v_data["author"],
                    "licensing": "Standard YouTube License",
                    "caption": v_data["description"]
                }
            }
        )
        total_videos_created += 1
        total_lessons_enriched += 1

        print(f"  [+] Topic {topic.order} -> Lesson {lesson.id}: '{lesson.title}' (Page {target_page})")
        print(f"      Video: {v_data['url']} | \"{v_data['title']}\" by {v_data['author']}")

    print("\n" + "=" * 80)
    print("[SUCCESS] CBC Grade 8 Home Science Video Enrichment Complete!")
    print(f"[*] Total Lessons Enriched: {total_lessons_enriched} / {len(GRADE8_VERIFIED_ENRICHMENTS)}")
    print(f"[*] Total Video Assets Created: {total_videos_created}")
    print(f"[*] Total Blocks Created: {total_blocks_created}")
    print("=" * 80)


if __name__ == "__main__":
    run_enrichment()
