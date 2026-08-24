"""
VLearn CBC Grade 6 — Home Science
YouTube Video Enrichment Script (Reconciled & Verified)

All video URLs have been individually verified against their actual YouTube titles
and content before assignment. Each video is placed only in a lesson whose
topic it genuinely addresses.

Verified assignments:
  Topic 1 → Grooming & Personal Care  → AMAZE Org: Taking Care of Your Body During Puberty
  Topic 1 → Exercise & Safety         → Dr. Binocs: Spending Too Much Time On Your Phone? (screen vs. activity)
  Topic 2 → Needs, Wants & Budgets    → Learn Bright: Financial Literacy — Needs and Wants
  Topic 3 → Essential Minerals        → Dr. Binocs: Why Are Minerals Important? ✓ (already correct)
  Topic 3 → Food Preservation         → Learning Junction: Food Preservation Methods for Kids ✓
  Topic 3 → Practical Cookery Baking  → 1Room Kenya Lesson 42: Dry Heat Cooking — Roasting and Baking ✓
  Topic 4 → Weaving                   → Metropolitan Museum: Paper/Cardboard Loom Weaving ✓
  Topic 4 → Knitting & Crocheting     → Crochet for Beginners/Kids Classroom Edition ✓
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db.models import Max
from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


VIDEO_ENRICHMENTS = [

    # ── TOPIC 1 ────────────────────────────────────────────────────────────────
    # Lesson: Daily Grooming, Menstrual Hygiene & Personal Care
    # Video: AMAZE Org — "Taking Care of Your Body During Puberty"
    # Covers: managing body odour, acne, hair growth, and menstrual hygiene
    # during puberty — directly relevant to this lesson's content.
    {
        "topic_order": 1,
        "lesson_title_contains": "Grooming",
        "blocks": [
            {
                "block_type": "suggested_video",
                "title": "Watch: Taking Care of Your Body During Puberty",
                "content": {
                    "url": "https://www.youtube.com/watch?v=00BYyDr8Xdg",
                    "text": (
                        "AMAZE Org's short, friendly animation walks through the real "
                        "hygiene challenges that come with puberty — managing body odour "
                        "with deodorant, keeping skin clear, handling menstrual hygiene, "
                        "and building a daily grooming routine that helps you feel clean "
                        "and confident at school every day."
                    ),
                    "author": "AMAZE Org",
                    "licensing": "Standard YouTube License"
                }
            },
            {
                "block_type": "callout",
                "title": "🎬 Reflect on What You Watched",
                "content": {
                    "text": (
                        "After watching the video, think carefully:\n\n"
                        "**1.** Name TWO grooming habits the video recommends for "
                        "managing body odour during puberty.\n\n"
                        "**2.** Why is it important to wash your face regularly during "
                        "adolescence, and what skin condition can result from not doing so?\n\n"
                        "**3.** Which ONE grooming habit from this lesson will you "
                        "start doing consistently every morning — and why?"
                    )
                }
            }
        ]
    },

    # ── TOPIC 1 ────────────────────────────────────────────────────────────────
    # Lesson: Daily Exercise Fitness, Environmental Hazards & Digital Safety
    # Video: Dr. Binocs — "Spending Too Much Time On Your Phone?"
    # Covers: the health and mental consequences of screen inactivity vs. the
    # benefits of outdoor physical play — directly mirrors the lesson's contrast
    # between active living and digital hazards.
    {
        "topic_order": 1,
        "lesson_title_contains": "Exercise",
        "blocks": [
            {
                "block_type": "suggested_video",
                "title": "Watch: What Happens When You Spend Too Much Time On Your Phone?",
                "content": {
                    "url": "https://www.youtube.com/watch?v=v0uaBuM9TMQ",
                    "text": (
                        "Dr. Binocs explains the real physical and mental effects of "
                        "prolonged screen time — poor posture, strained eyesight, "
                        "disrupted sleep, and reduced physical activity — and makes a "
                        "strong case for why balancing digital time with outdoor exercise "
                        "is essential for a healthy, growing adolescent body and mind."
                    ),
                    "author": "Peekaboo Kidz (Dr. Binocs Show)",
                    "licensing": "Standard YouTube License"
                }
            },
            {
                "block_type": "callout",
                "title": "🎬 Reflect on What You Watched",
                "content": {
                    "text": (
                        "After watching the video, think carefully:\n\n"
                        "**1.** Name TWO physical health effects of spending too many "
                        "hours on a phone or tablet without taking a break.\n\n"
                        "**2.** Dr. Binocs recommends balancing screen time with outdoor "
                        "activity. What specific activities does the lesson suggest you "
                        "do daily to keep your body strong and active?\n\n"
                        "**3.** Design your ideal after-school timetable: how many "
                        "minutes of exercise and how many minutes of screen time would "
                        "you include — and why?"
                    )
                }
            }
        ]
    },

    # ── TOPIC 2 ────────────────────────────────────────────────────────────────
    # Lesson: Discovering Needs, Wants, and Budgets
    # Video: Learn Bright — "Financial Literacy — Needs and Wants"
    # Covers: distinguishing between needs and wants, opportunity costs,
    # and making wise spending decisions — exact match for this lesson.
    {
        "topic_order": 2,
        "lesson_title_contains": "Needs, Wants",
        "blocks": [
            {
                "block_type": "suggested_video",
                "title": "Watch: Financial Literacy — Understanding Needs vs. Wants",
                "content": {
                    "url": "https://www.youtube.com/watch?v=1F_4-pM-w5U",
                    "text": (
                        "Learn Bright's animated lesson on financial literacy explains "
                        "exactly what makes something a Need (essential for survival and "
                        "school) versus a Want (nice to have but not necessary), and "
                        "introduces the idea of opportunity cost — what you give up when "
                        "you choose to spend money on one thing instead of another."
                    ),
                    "author": "Learn Bright",
                    "licensing": "Standard YouTube License"
                }
            },
            {
                "block_type": "callout",
                "title": "🎬 Reflect on What You Watched",
                "content": {
                    "text": (
                        "After watching the video, think carefully:\n\n"
                        "**1.** Give ONE example of a Need and ONE example of a Want "
                        "from the video. Explain why each is classified the way it is.\n\n"
                        "**2.** What is 'opportunity cost'? Give a Kenyan example using "
                        "school pocket money — what do you give up when you buy a soda "
                        "instead of a pencil?\n\n"
                        "**3.** If you had 150 shillings for the school week, write "
                        "a simple plan showing how you would split it between Needs "
                        "and Wants."
                    )
                }
            }
        ]
    },

    # ── TOPIC 3 ────────────────────────────────────────────────────────────────
    # Lesson: Essential Minerals and Deficiency Disorders
    # Video: Dr. Binocs — "Why Are Minerals Important?" (VERIFIED CORRECT ✓)
    {
        "topic_order": 3,
        "lesson_title_contains": "Minerals",
        "blocks": [
            {
                "block_type": "suggested_video",
                "title": "Watch: Why Are Minerals Important? — Iron, Iodine and Your Body",
                "content": {
                    "url": "https://www.youtube.com/watch?v=uZousR_FfEE",
                    "text": (
                        "Dr. Binocs explains the essential roles of key dietary minerals — "
                        "how Iron builds oxygen-carrying red blood cells to prevent anaemia, "
                        "how Iodine supports the thyroid gland to prevent goitre, and which "
                        "everyday Kenyan foods supply these life-saving minerals."
                    ),
                    "author": "Peekaboo Kidz (Dr. Binocs Show)",
                    "licensing": "Standard YouTube License"
                }
            },
            {
                "block_type": "callout",
                "title": "🎬 Reflect on What You Watched",
                "content": {
                    "text": (
                        "After watching the video, think carefully:\n\n"
                        "**1.** What disease does a lack of Iron in the body cause, "
                        "and what are two symptoms you would notice?\n\n"
                        "**2.** Which organ is affected by Iodine deficiency, and what "
                        "visible condition does this produce on the neck?\n\n"
                        "**3.** Name TWO foods you eat at home that supply Iron or "
                        "Iodine to support your growing body."
                    )
                }
            }
        ]
    },

    # ── TOPIC 3 ────────────────────────────────────────────────────────────────
    # Lesson: Food Preservation in the Home
    # Video: Learning Junction — "Food Preservation Methods, Techniques & Types"
    # Covers: drying, salting, smoking, canning, and refrigeration — exact match.
    {
        "topic_order": 3,
        "lesson_title_contains": "Preservation",
        "blocks": [
            {
                "block_type": "suggested_video",
                "title": "Watch: Food Preservation Methods — Drying, Salting and Smoking Explained",
                "content": {
                    "url": "https://www.youtube.com/watch?v=gPz41u5_J7U",
                    "text": (
                        "Learning Junction's kid-friendly guide explains why food spoils "
                        "and how traditional preservation methods — salting, sun-drying, "
                        "and smoking — remove the moisture that bacteria need to survive, "
                        "keeping food safe to eat for weeks or months without a refrigerator."
                    ),
                    "author": "Learning Junction",
                    "licensing": "Standard YouTube License"
                }
            },
            {
                "block_type": "callout",
                "title": "🎬 Reflect on What You Watched",
                "content": {
                    "text": (
                        "After watching the video, think carefully:\n\n"
                        "**1.** In one sentence, explain WHY removing moisture from food "
                        "prevents it from going bad.\n\n"
                        "**2.** Which preservation method shown in the video do families "
                        "in your community use most often — and for which type of food?\n\n"
                        "**3.** How does traditional food preservation help a Kenyan "
                        "family manage their food supply during the dry season when fresh "
                        "food is scarce?"
                    )
                }
            }
        ]
    },

    # ── TOPIC 3 ────────────────────────────────────────────────────────────────
    # Lesson: Practical Cookery: Stewing and Baking
    # Video: 1Room Kenya Lesson 42 — "Dry Heat Cooking Method: Roasting and Baking"
    # Covers: baking technique, dry heat oven principle — correct match.
    {
        "topic_order": 3,
        "lesson_title_contains": "Cookery",
        "blocks": [
            {
                "block_type": "suggested_video",
                "title": "Watch: Dry Heat Cooking — Roasting and Baking Techniques",
                "content": {
                    "url": "https://www.youtube.com/watch?v=y6U36582528",
                    "text": (
                        "1Room Kenya's Home Science lesson demonstrates dry heat cooking "
                        "methods — how roasting and baking use hot, dry air to cook food "
                        "from the outside in, and how to assemble an improvised dual-sufuria "
                        "hot sand oven over a charcoal jiko to bake successfully without "
                        "an electric oven."
                    ),
                    "author": "1Room Kenya",
                    "licensing": "Standard YouTube License"
                }
            },
            {
                "block_type": "callout",
                "title": "🎬 Reflect on What You Watched",
                "content": {
                    "text": (
                        "After watching the video, think carefully:\n\n"
                        "**1.** What makes 'dry heat' cooking different from boiling "
                        "or stewing? What happens to the food's outer surface during baking?\n\n"
                        "**2.** How does the improvised sand oven work — what role does "
                        "the sand play in trapping and distributing heat evenly?\n\n"
                        "**3.** Name ONE advantage and ONE disadvantage of baking using "
                        "a charcoal jiko compared to an electric oven."
                    )
                }
            }
        ]
    },

    # ── TOPIC 4 ────────────────────────────────────────────────────────────────
    # Lesson: Weaving Our First Mat
    # Video: Metropolitan Museum — "Paper/Cardboard Loom Weaving" (VERIFIED ✓)
    {
        "topic_order": 4,
        "lesson_title_contains": "Weaving",
        "blocks": [
            {
                "block_type": "suggested_video",
                "title": "Watch: How to Weave on a Cardboard Loom",
                "content": {
                    "url": "https://www.youtube.com/watch?v=AWLIy-Um7_0",
                    "text": (
                        "A clear, hands-on demonstration of making a simple loom from "
                        "scrap cardboard, cutting slot notches for the warp threads, "
                        "and weaving horizontal weft yarn over and under in plain and "
                        "basket weave patterns — exactly the technique you practise in "
                        "this lesson."
                    ),
                    "author": "The Metropolitan Museum of Art",
                    "licensing": "Standard YouTube License"
                }
            },
            {
                "block_type": "callout",
                "title": "🎬 Reflect on What You Watched",
                "content": {
                    "text": (
                        "After watching the video, think carefully:\n\n"
                        "**1.** What materials were used to build the loom frame in the "
                        "video? What local materials could you substitute from your home?\n\n"
                        "**2.** Watch the weft thread carefully as it moves across the "
                        "warp. Describe in your own words the over-under pattern of plain weave.\n\n"
                        "**3.** What finished article would you most like to weave — "
                        "a coaster, floor mat, or wall hanging? What yarn or local fibre "
                        "would you collect?"
                    )
                }
            }
        ]
    },

    # ── TOPIC 4 ────────────────────────────────────────────────────────────────
    # Lesson: The Knitting Needle and the Crochet Hook
    # Video: Crochet for Beginners / Kids — Classroom Edition (VERIFIED ✓)
    {
        "topic_order": 4,
        "lesson_title_contains": "Knitting",
        "blocks": [
            {
                "block_type": "suggested_video",
                "title": "Watch: Crochet for Beginners — Slip Knot, Chain and Single Crochet",
                "content": {
                    "url": "https://www.youtube.com/watch?v=WRhJeCnTmEo",
                    "text": (
                        "A classroom-friendly crochet series designed specifically for "
                        "kids and teachers — learn how to hold the hook, form a slip knot, "
                        "build a foundation chain, and complete single and double crochet "
                        "stitches at a slow, easy-to-follow pace ideal for first-time learners."
                    ),
                    "author": "Crochet for Beginners / Classroom Edition",
                    "licensing": "Standard YouTube License"
                }
            },
            {
                "block_type": "callout",
                "title": "🎬 Reflect on What You Watched",
                "content": {
                    "text": (
                        "After watching the video, think carefully:\n\n"
                        "**1.** What is the very first step before starting any crochet "
                        "project, and how do you form it with the hook and yarn?\n\n"
                        "**2.** How does the presenter hold the crochet hook? Practice "
                        "holding your pencil in the same comfortable grip and describe it.\n\n"
                        "**3.** What is ONE practical item — like a hot-pad, scarf, or "
                        "dishcloth — you could crochet for your family using simple "
                        "single crochet stitches?"
                    )
                }
            }
        ]
    }
]


def run_enrichment():
    print("=" * 80)
    print("[START] CBC Grade 6 Home Science — YouTube Video Enrichment (Reconciled)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    assert grade, "Grade 6 not found!"
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject 'Home Science' under Grade 6 not found!"

    print(f"[*] Hierarchy: {curriculum.name} → {grade.name} → {subject.name}\n")

    total_videos = 0
    total_blocks = 0

    for enrichment in VIDEO_ENRICHMENTS:
        topic = Topic.objects.filter(subject=subject, order=enrichment["topic_order"]).first()
        if not topic:
            print(f"  [SKIP] Topic {enrichment['topic_order']} not found.")
            continue

        lesson = None
        for unit in topic.learning_units.all():
            candidate = unit.lessons.filter(
                title__icontains=enrichment["lesson_title_contains"]
            ).first()
            if candidate:
                lesson = candidate
                break

        if not lesson:
            print(f"  [SKIP] No lesson matching '{enrichment['lesson_title_contains']}' in Topic {enrichment['topic_order']}.")
            continue

        # Determine page and order to append after existing content
        max_page = lesson.blocks.aggregate(max_page=Max("page_number"))["max_page"] or 8
        new_page = max_page + 1
        max_order = lesson.blocks.aggregate(max_order=Max("order"))["max_order"] or 0

        print(f"  [+] Topic {enrichment['topic_order']} → '{lesson.title}' (page {new_page})")

        block_order = max_order + 1
        for block_dict in enrichment["blocks"]:
            b_type = block_dict["block_type"]
            LessonBlock.objects.create(
                lesson=lesson,
                page_number=new_page,
                block_type=b_type,
                component_type=b_type,
                title=block_dict["title"],
                order=block_order,
                content=block_dict["content"]
            )
            block_order += 1
            total_blocks += 1

            if b_type == "suggested_video":
                video_url = block_dict["content"].get("url", "")
                if video_url:
                    LessonAsset.objects.update_or_create(
                        lesson=lesson,
                        title=block_dict["title"],
                        defaults={
                            "asset_type": "video",
                            "source_type": "external",
                            "storage_type": "url",
                            "status": "attached",
                            "url": video_url,
                            "description": block_dict["content"].get("text", ""),
                            "metadata": {
                                "author": block_dict["content"].get("author", ""),
                                "licensing": block_dict["content"].get("licensing", "Standard YouTube License"),
                                "caption": block_dict["content"].get("text", "")
                            }
                        }
                    )
                    total_videos += 1
                    print(f"      → {video_url}")

    print("\n" + "=" * 80)
    print(f"[SUCCESS] Reconciled Video Enrichment Complete!")
    print(f"[*] Total Videos Added:   {total_videos}")
    print(f"[*] Total Blocks Created: {total_blocks}")
    print("=" * 80)


if __name__ == "__main__":
    run_enrichment()
