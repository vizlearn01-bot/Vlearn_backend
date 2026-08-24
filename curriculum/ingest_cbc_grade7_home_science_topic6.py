"""
VLearn CBC Grade 7 Home Science — Topic 6: The Sewing Machine
Curriculum Ingestion Engine (Phase 1: Content, Pages & Blocks)

Curriculum: CBC (ID: 5)
Grade: Grade 7 (ID: 16, Level: 7)
Subject: Home Science (ID: 29)
Topic: The Sewing Machine (Order: 6)

Generates 4 Learning Units & 4 Published Lessons (32 Total Structured Pages, 47 Blocks):
  - Unit 1: Sewing Machine Types & Smart Buying Choices (8 Pages)
  - Unit 2: Anatomy & Mechanical Parts of the Sewing Machine (8 Pages)
  - Unit 3: Setup, Threading & Safe Straight Stitching (8 Pages)
  - Unit 4: Troubleshooting Stitch Faults & Machine Care (8 Pages)

Formatting Standards Applied:
  - Standard markdown bullet lists (- ) with blank line prefixes
  - Prominent bold terms and key concepts
  - Step processes, comparison matrices, and worked examples
  - Zero bracket citations ([95], [97]) and zero prompt meta-language

Usage:
  ./venv/bin/python curriculum/ingest_cbc_grade7_home_science_topic6.py [--replace]
"""

import os
import sys
import argparse
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock
)

def create_block(lesson, page_number, order, block_type, title, content):
    """Helper to create LessonBlock instances cleanly."""
    return LessonBlock.objects.create(
        lesson=lesson,
        page_number=page_number,
        order=order,
        block_type=block_type,
        title=title,
        content=content
    )

def ingest_cbc_grade7_home_science_topic6(replace=True):
    print("=" * 80)
    print("STARTING INGESTION: CBC GRADE 7 HOME SCIENCE — TOPIC 6: THE SEWING MACHINE")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"
    print(f"[*] Found Curriculum: {curriculum.name} (ID: {curriculum.id})")

    grade, _ = Grade.objects.get_or_create(
        curriculum=curriculum,
        name="Grade 7",
        defaults={"level": 7, "description": "Grade 7 Junior Secondary School"}
    )
    print(f"[*] Grade 7: ID {grade.id} (Level {grade.level})")

    subject, _ = Subject.objects.get_or_create(
        grade=grade,
        name="Home Science",
        defaults={"description": "CBC Grade 7 Home Science"}
    )
    print(f"[*] Subject: {subject.name} (ID: {subject.id})")

    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="The Sewing Machine",
        defaults={
            "order": 6,
            "description": "Classification of hand-driven, treadle, and electric sewing machines, 5 purchasing factors, anatomy of machine parts, needle and bobbin preparation, upper/lower threading pathways, safe straight stitching, troubleshooting stitch faults, and 4-step care maintenance."
        }
    )
    if not created and replace:
        print(f"[*] Replacing existing content for Topic: '{topic.name}' (ID: {topic.id})")
        topic.lessons.all().delete()
        topic.learning_units.all().delete()
    elif created:
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # =========================================================================
    # LESSON 1: SEWING MACHINE TYPES & BUYING CHOICES (8 Pages)
    # =========================================================================
    u1, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Sewing Machine Types & Smart Buying Choices",
        defaults={
            "order": 1,
            "description": "Classifying hand-driven, treadle, and electric sewing machines, and evaluating the 5 key household purchasing factors."
        }
    )
    l1 = Lesson.objects.create(
        topic=topic,
        learning_unit=u1,
        title="Sewing Machine Types & Smart Buying Choices",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 1: '{l1.title}' (Lesson ID: {l1.id})")

    # Page 1: Hook & Introduction
    create_block(l1, 1, 1, "suggested_image", "The Secret of the Tailor's Workshop", {
        "caption": "A sewing machine is a precision mechanical device that turns raw fabric into sturdy, durable clothing and home articles.",
        "search_query": "african tailor sewing machine market kiosk"
    })
    create_block(l1, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Classify sewing machines into **Hand-driven, Treadle, and Electric-driven** types.\n- Compare the operational advantages and limits of each machine type.\n- Evaluate the **5 key factors** considered when purchasing a sewing machine.\n- Match real-world tailoring scenarios to the most practical machine choice."
    })
    create_block(l1, 1, 3, "concept_explanation", "The Precision Stitching Helper", {
        "text": "A **sewing machine** is a mechanical device engineered to join fabrics together using a two-thread lockstitch system far faster and stronger than hand sewing!\n\n- **1. Hand-driven Sewing Machine**: Powered by turning a handwheel crank with one hand. Highly portable, lightweight, and works off-grid, but restricts the operator to guiding fabric with only one hand.\n- **2. Treadle Sewing Machine**: Powered by rocking a heavy iron foot-pedal back and forth. Leaves **both hands free to guide the fabric** and operates without electricity, but is bulky and stationary.\n- **3. Electric-driven Sewing Machine**: Powered by an electric motor regulated by a foot pedal. Extremely fast, efficient, and versatile, but requires stable grid electricity and careful speed control for beginners."
    })

    # Page 2: Machine Types Blueprint
    create_block(l1, 2, 1, "suggested_diagram", "Hand, Treadle & Electric Sewing Machines Blueprint", {
        "caption": "Comparative grid illustrating hand crank, treadle rocking foot-plate, and electric motor mechanisms.",
        "diagram_type": "comparative_grid"
    })
    create_block(l1, 2, 2, "concept_explanation", "The 5 Key Purchasing Factors", {
        "text": "A sewing machine is a significant financial asset. Before buying, families must evaluate 5 critical factors:\n\n- **1. Price and Budget**: What total amount can the household or business realistically invest?\n- **2. Power Source Available**: Is there steady grid electricity, or does the area require an off-grid mechanical solution?\n- **3. Purpose and Intended Use**: Is the machine for light domestic repairs or high-speed commercial tailoring?\n- **4. Spare Parts & Brand Reliability**: Are replacement needles, bobbins, and skilled local technicians easily available?\n- **5. Portability and Space**: Does the machine need to travel between markets, or is there a dedicated room for a cabinet?"
    })

    # Page 3: Comparison Table
    create_block(l1, 3, 1, "comparison_table", "Comparative Guide to the 3 Machine Types", {
        "headers": ["Machine Type", "Power Source", "Operator Hand Freedom", "Portability & Space", "Ideal User Profile"],
        "rows": [
            ["Hand-driven", "Manual hand crank on handwheel", "One hand turns crank; only one hand guides fabric", "Highly portable; compact desktop wooden base", "Mobile repair tailors, traveling artisans, light home mending"],
            ["Treadle", "Physical foot-rocking pedal with leather belt", "Both hands completely free to guide fabric accurately", "Heavy, stationary iron stand with wooden table", "Rural dressmakers, off-grid market kiosks, school workshops"],
            ["Electric-driven", "Electric motor with foot pressure control", "Both hands free to steer and control fabric", "Compact to medium; requires power outlet", "Urban tailors, garment factories, high-volume production"]
        ]
    })

    # Page 4: Detailed Buying Analysis
    create_block(l1, 4, 1, "concept_explanation", "Evaluating Off-Grid vs. On-Grid Choices", {
        "text": "Why is speed not always the deciding factor?\n\n- If you buy an expensive electric machine in a rural shopping center with frequent blackouts, your business grinds to a halt during power cuts!\n- A **treadle machine** continues sewing uninterrupted through blackouts, while keeping both of the tailor's hands free to manipulate intricate necklines and zippers."
    })

    # Page 5: Worked Example
    create_block(l1, 5, 1, "step_process", "Worked Example: Matching a Tailor's Needs to the Right Machine", {
        "steps": [
            {"number": 1, "title": "Analyze Buyer Profile", "description": "Aisha operates a dressmaking stall in an off-grid village market and needs to sew intricate school uniforms."},
            {"number": 2, "title": "Assess Power Constraint", "description": "No grid electricity is available, ruling out standard electric motor machines."},
            {"number": 3, "title": "Assess Technical Need", "description": "Guiding collar seams and pleated skirts requires having BOTH hands free on the fabric (ruling out hand-driven machines)."},
            {"number": 4, "title": "Optimal Decision", "description": "Aisha chooses a heavy-duty Treadle Sewing Machine—it runs reliably on foot power and leaves both hands free!"}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l1, 6, 1, "mini_activity", "Hands-On Task: The Sewing Machine Matchmaker", {
        "instructions": "In your notebook, match these 3 local entrepreneurs to their ideal machine:\n\n- **1. Juma**: A mobile tailor traveling on a bicycle between neighboring homesteads.\n- **2. Mary**: A factory owner in Nairobi producing 100 school shirts daily with grid power.\n- **3. Grace**: A rural dressmaker sewing wedding gowns in an off-grid shopping center.\n- State one clear reason for each choice."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l1, 7, 1, "key_takeaway", "Key Takeaways: Machine Types & Buying", {
        "text": "Remember these purchasing rules:\n\n- **Hand-driven**: Portable, off-grid, but uses one hand for cranking.\n- **Treadle**: Off-grid, foot-powered, and leaves **both hands free**.\n- **Electric**: High-speed and efficient, but requires steady electricity.\n- Weigh **Budget, Power, Purpose, Spare Parts, and Portability** before buying!"
    })

    # Page 8: Knowledge Check
    create_block(l1, 8, 1, "knowledge_check", "Scenario Knowledge Check: Machine Types & Buying Factors", {
        "question": "Why is a hand-driven sewing machine the most practical choice for a traveling tailor who visits different rural market centers on bicycle?",
        "options": [
            "It is the heaviest and largest machine available",
            "It is compact, lightweight, easy to transport, and operates anywhere without electricity",
            "It sews 5 times faster than industrial electric motors",
            "It has an iron foot pedal that locks to the bicycle frame"
        ],
        "correct_index": 1,
        "explanation": "Correct! Hand-driven machines are compact, lightweight, easily packed into carrying cases, and operate manually without needing electric power, making them ideal for mobile tailors."
    })

    # =========================================================================
    # LESSON 2: ANATOMY & MECHANICAL PARTS OF THE MACHINE (8 Pages)
    # =========================================================================
    u2, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Anatomy & Mechanical Parts of the Sewing Machine",
        defaults={
            "order": 2,
            "description": "Identifying the 12 key functional parts of a lockstitch sewing machine and understanding lower bobbin and feed dog mechanics."
        }
    )
    l2 = Lesson.objects.create(
        topic=topic,
        learning_unit=u2,
        title="Anatomy & Mechanical Parts of the Sewing Machine",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 2: '{l2.title}' (Lesson ID: {l2.id})")

    # Page 1: Hook & Introduction
    create_block(l2, 1, 1, "suggested_image", "A Team of Tiny Metal Helpers: Inside the Machine", {
        "caption": "A domestic lockstitch sewing machine is a coordinated team of metal gears, levers, and discs that form strong stitches.",
        "search_query": "sewing machine needle presser foot parts"
    })
    create_block(l2, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Identify the **12 primary functional parts** of a lockstitch sewing machine.\n- Explain the specific role of the **tension regulator, take-up lever, and presser foot**.\n- Explain how the **feed dog teeth** pull fabric smoothly without manual tugging.\n- Adjust the **stitch regulator dial** for seams versus temporary basting."
    })
    create_block(l2, 1, 3, "concept_explanation", "The 12 Core Mechanical Components", {
        "text": "Every lockstitch sewing machine relies on 12 essential parts:\n\n- **1. Spool Pin**: Vertical/horizontal pin holding the spool of upper thread.\n- **2. Thread Guides**: Metal loops directing thread smoothly along the machine arm.\n- **3. Tension Regulator**: Metal discs that squeeze the upper thread to control stitch tightness.\n- **4. Thread Take-up Lever**: Moves up and down, supplying slack and pulling up thread to complete the lockstitch.\n- **5. Needle Bar & Clamp**: Vertical shaft holding the needle firmly with a tightening screw.\n- **6. Presser Foot**: Metal shoe holding fabric flat against the throat plate.\n- **7. Presser Foot Lifter**: Back lever used to raise and lower the presser foot.\n- **8. Feed Dog**: Toothed metal ridges under the plate that slide fabric forward after each stitch.\n- **9. Balance Wheel (Handwheel)**: Large wheel rotated toward you to raise/lower the needle manually.\n- **10. Bobbin Winder**: Spindle used to wind thread evenly onto empty bobbins.\n- **11. Bobbin & Bobbin Case**: Metal spool and snug case holding the lower thread.\n- **12. Stitch Regulator Dial**: Dial adjusting stitch length from tight seams (1.5mm) to long basting (4mm)."
    })

    # Page 2: Anatomy Diagram Blueprint
    create_block(l2, 2, 1, "suggested_diagram", "Anatomy of a Lockstitch Sewing Machine Blueprint", {
        "caption": "Comprehensive annotated blueprint identifying the 12 core functional parts of a domestic sewing machine.",
        "diagram_type": "annotated_machine_schematic"
    })
    create_block(l2, 2, 2, "concept_explanation", "The Role of the Feed Dog and Presser Foot", {
        "text": "How do stitches stay evenly spaced?\n\n- The **presser foot** clamps the fabric flat against the throat plate.\n- The **feed dog's toothed metal ridges** rise up through the throat plate, grip the bottom of the fabric, and slide backward exactly one stitch length between needle strikes.\n- **Rule of Operation**: NEVER push or pull fabric with your hands! Let the feed dog pull the cloth at its own calibrated speed."
    })

    # Page 3: Comparison Table
    create_block(l2, 3, 1, "comparison_table", "Comprehensive Machine Parts & Functions Directory", {
        "headers": ["Machine Component", "Physical Location", "Mechanical Function in Stitching"],
        "rows": [
            ["Spool Pin", "Top of machine arm", "Holds upper thread spool securely during rapid feeding"],
            ["Tension Regulator", "Front face of machine arm", "Metal discs that squeeze thread to ensure balanced stitch tension"],
            ["Thread Take-up Lever", "Upper front left slot", "Rises to pull thread from spool; dips to allow needle loop formation"],
            ["Presser Foot", "Directly below needle bar", "Presses fabric flat against throat plate to prevent slipping"],
            ["Feed Dog", "Under needle / throat plate", "Toothed ridges that move up and back to feed fabric automatically"],
            ["Balance Wheel", "Right side of machine head", "Rotated toward operator by hand to raise or lower needle precisely"],
            ["Bobbin & Case", "Shuttle race beneath plate", "Holds and tensions the lower thread for lockstitch interlocking"],
            ["Stitch Regulator", "Lower right front panel", "Controls feed dog travel distance to adjust stitch length (mm)"]
        ]
    })

    # Page 4: The Underworld Blueprint
    create_block(l2, 4, 1, "suggested_diagram", "The Secret Underworld: Bobbin, Case & Feed Dog Teeth", {
        "caption": "Zoomed schematic illustrating the lower thread bobbin shuttle race and feed dog movement.",
        "diagram_type": "underworld_bobbin_feed"
    })
    create_block(l2, 4, 2, "concept_explanation", "How Upper & Lower Threads Interlock", {
        "text": "The magic of the lockstitch:\n\n- The needle carries the upper thread down through the fabric.\n- Beneath the plate, the revolving shuttle hook catches the needle thread loop and wraps it around the **bobbin case**.\n- The take-up lever rises, pulling the two threads tight so they knot together right in the center of the fabric layers!"
    })

    # Page 5: Worked Example
    create_block(l2, 5, 1, "step_process", "Worked Example: Adjusting the Stitch Regulator for Seams vs. Basting", {
        "steps": [
            {"number": 1, "title": "Identify Sewing Task", "description": "Decide whether you are sewing a permanent garment seam or temporary basting stitches to hold fabric together."},
            {"number": 2, "title": "Set for Permanent Seams", "description": "Rotate the stitch regulator dial to 2.0mm. The feed dog takes small steps, creating tight, durable stitches."},
            {"number": 3, "title": "Set for Temporary Basting", "description": "Rotate the dial to 4.0mm or 5.0mm. The feed dog takes large steps, creating long stitches that pull out easily."},
            {"number": 4, "title": "Test on Fabric Scrap", "description": "Always stitch a 5cm test line on a waste fabric strip to verify stitch length before sewing your main garment."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l2, 6, 1, "mini_activity", "Hands-On Task: Machine Part Identification Sketch", {
        "instructions": "In your Home Science notebook:\n\n- Draw an outline sketch of a sewing machine frame.\n- Label the **Spool Pin**, **Tension Discs**, **Take-up Lever**, **Presser Foot**, **Feed Dog**, and **Balance Wheel**.\n- Write a one-sentence functional summary next to each labeled part."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l2, 7, 1, "key_takeaway", "Key Takeaways: Anatomy & Parts", {
        "text": "Remember these part functions:\n\n- **Tension Regulator**: Controls upper thread tightness.\n- **Take-up Lever**: Supplies slack and pulls up the stitch.\n- **Presser Foot**: Holds fabric flat against the plate.\n- **Feed Dog**: Toothed ridges that **pull fabric automatically**.\n- **Balance Wheel**: Always turned **toward you** to control the needle."
    })

    # Page 8: Knowledge Check
    create_block(l2, 8, 1, "knowledge_check", "Scenario Knowledge Check: Parts & Mechanical Functions", {
        "question": "Which specific part of the sewing machine is responsible for holding the fabric flat against the throat plate to prevent it from bunching or shifting as the needle stitches?",
        "options": [
            "The stitch regulator lever",
            "The presser foot",
            "The balance handwheel",
            "The spool pin"
        ],
        "correct_index": 1,
        "explanation": "Correct! The presser foot is the metal shoe lowered by the presser lifter to press fabric firmly against the throat plate, ensuring smooth, accurate stitching."
    })

    # =========================================================================
    # LESSON 3: SETUP, THREADING & SAFE STRAIGHT STITCHING (8 Pages)
    # =========================================================================
    u3, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Setup, Threading & Safe Straight Stitching",
        defaults={
            "order": 3,
            "description": "Mastering the 5 preparation steps, upper and lower threading paths, posture ergonomics, and safe straight stitching on fabric swatches."
        }
    )
    l3 = Lesson.objects.create(
        topic=topic,
        learning_unit=u3,
        title="Setup, Threading & Safe Straight Stitching",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 3: '{l3.title}' (Lesson ID: {l3.id})")

    # Page 1: Hook & Introduction
    create_block(l3, 1, 1, "suggested_image", "Getting Ready to Stitch: Precision Setup", {
        "caption": "Threading a sewing machine follows an exact, unbroken sequence that ensures flawless stitch formation without thread snaps.",
        "search_query": "threading sewing machine needle eye spool"
    })
    create_block(l3, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Execute the **5 preparation setup steps** (needle insertion, bobbin winding, snap-in case).\n- Trace the complete **upper threading pathway** (Spool $\\rightarrow$ Discs $\\rightarrow$ Lever $\\rightarrow$ Needle).\n- Draw up the **lower bobbin thread loop** safely before sewing.\n- Practice **straight stitching** with upright posture and finger safety zones."
    })
    create_block(l3, 1, 3, "concept_explanation", "The 5 Machine Preparation Steps", {
        "text": "Before you can stitch, follow these 5 mandatory setup steps in exact order:\n\n- **1. Needle Placement**: Insert needle into clamp with the flat side of the shank facing the correct direction; push all the way up and tighten screw firmly.\n- **2. Winding the Bobbin**: Disengage handwheel clutch, guide thread to bobbin winder spindle, and wind thread smoothly and evenly.\n- **3. Lower Threading (Bobbin Case)**: Place wound bobbin in case, slide thread through tension slit under the spring, and snap case into the shuttle race.\n- **4. Upper Threading Pathway**: Spool Pin $\\rightarrow$ Thread Guides $\\rightarrow$ Tension Discs $\\rightarrow$ Take-up Lever Eye $\\rightarrow$ Lower Guides $\\rightarrow$ Needle Eye.\n- **5. Drawing Up the Lower Thread**: Hold upper thread tail, rotate balance wheel toward you once to dip needle down, pull upper thread to bring up bobbin loop, and pull both thread tails backward under the presser foot!"
    })

    # Page 2: Sequential Threading Blueprint
    create_block(l3, 2, 1, "suggested_diagram", "The Sequential Threading Pathway Blueprint", {
        "caption": "Numbered step-by-step schematic tracing upper threading path 1 to 6 and bobbin case insertion.",
        "diagram_type": "threading_pathway"
    })
    create_block(l3, 2, 2, "concept_explanation", "The Golden Rule of Upper Threading", {
        "text": "Always raise the presser foot before threading the upper path!\n\n- When the presser foot is raised, the **tension discs open up**, allowing the thread to sink deeply between the discs.\n- If you thread with the presser foot down, the thread sits outside the discs, resulting in zero tension and huge tangled loops under the fabric!"
    })

    # Page 3: Comparison Table
    create_block(l3, 3, 1, "comparison_table", "Step-by-Step Threading & Needle Setup Guide", {
        "headers": ["Setup Step", "Action to Perform", "Key Safety / Quality Rule"],
        "rows": [
            ["1. Needle Insertion", "Insert needle into bar with flat shank side facing right/back", "Push needle fully to top stop; tighten clamp screw firmly"],
            ["2. Bobbin Winding", "Place empty bobbin on spindle; disengage handwheel clutch", "Wind thread smoothly; do not overfill the bobbin spool"],
            ["3. Lower Case Setup", "Insert bobbin in case; pull thread through slot under leaf spring", "Listen for audible 'click' when snapping case into shuttle race"],
            ["4. Upper Threading", "Guide thread through tension discs, take-up lever, down to needle", "Raise presser foot first so thread sits deep inside tension discs"],
            ["5. Drawing Up Loop", "Rotate handwheel toward you once; pull upper thread to catch loop", "Pull both thread tails 10cm backward under the presser foot"]
        ]
    })

    # Page 4: Posture & Safety Zone Blueprint
    create_block(l3, 4, 1, "suggested_diagram", "Sewing Posture & The Finger Safety Zone Blueprint", {
        "caption": "Comparative ergonomic diagram showing correct upright posture, relaxed arms, and finger safety zones around the needle.",
        "diagram_type": "safety_posture"
    })
    create_block(l3, 4, 2, "concept_explanation", "Ergonomics & The Finger Safety Ring", {
        "text": "Sewing safety rules for junior secondary learners:\n\n- **1. Upright Ergonomic Posture**: Sit straight directly in front of the needle with feet flat and elbows level with the table to prevent back strain.\n- **2. The 2-Inch Safety Ring**: Keep fingers at least 2 inches away from the moving needle. Guide fabric gently from the sides.\n- **3. Power Safety**: Switch off electric power and remove feet from pedals whenever threading or changing needles to prevent accidental needle strikes."
    })

    # Page 5: Worked Example
    create_block(l3, 5, 1, "step_process", "Worked Example: Drawing Up the Lower Bobbin Thread Loop", {
        "steps": [
            {"number": 1, "title": "Hold Upper Needle Thread", "description": "Gently hold the loose end of the needle thread in your left hand with light tension."},
            {"number": 2, "title": "Rotate Handwheel Toward You", "description": "With your right hand, turn the balance wheel toward you one full revolution until the needle dips down and rises fully."},
            {"number": 3, "title": "Catch the Emerging Loop", "description": "Gently pull the upper thread. A loop of the lower bobbin thread will hop up through the needle plate hole."},
            {"number": 4, "title": "Sweep Both Tails Backward", "description": "Use a pair of scissors or tweezers to pull the loop free, then pull both thread tails backward under the presser foot."}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l3, 6, 1, "mini_activity", "Hands-On Task: Safe Straight Stitching Practice Strip", {
        "instructions": "Practice your straight stitching coordination:\n\n- Take a 15cm x 5cm strip of cotton fabric and draw 3 straight parallel lines with tailor's chalk.\n- Position fabric under presser foot, turn handwheel to lower needle into start of line, and lower presser foot.\n- Stitch slowly along each line, guiding fabric gently from the sides without pushing or pulling!"
    })

    # Page 7: Key Takeaways & Recall
    create_block(l3, 7, 1, "key_takeaway", "Key Takeaways: Setup & Safety", {
        "text": "Remember these setup essentials:\n\n- Thread with the **presser foot raised** so thread enters tension discs.\n- Always turn the **balance wheel toward you** to draw up the bobbin loop.\n- Pull **both thread tails backward** under the foot before starting.\n- Keep fingers **outside the 2-inch safety zone** around the needle!"
    })

    # Page 8: Knowledge Check
    create_block(l3, 8, 1, "knowledge_check", "Scenario Knowledge Check: Setup, Threading & Safety", {
        "question": "What is the mandatory final step an operator must complete after threading the machine and before inserting fabric to start sewing?",
        "options": [
            "Draw up the lower bobbin thread loop and pull both thread tails backward under the presser foot",
            "Set the stitch length regulator to maximum speed",
            "Oil the feed dog teeth with salad cooking oil",
            "Turn off the power and remove the needle"
        ],
        "correct_index": 0,
        "explanation": "Correct! Drawing up the lower bobbin thread loop and pulling both thread tails backward under the presser foot prevents threads from tangling or bunching in a bird's nest when stitching starts."
    })

    # =========================================================================
    # LESSON 4: TROUBLESHOOTING STITCH FAULTS & MACHINE CARE (8 Pages)
    # =========================================================================
    u4, _ = LearningUnit.objects.get_or_create(
        topic=topic,
        name="Troubleshooting Stitch Faults & Machine Care",
        defaults={
            "order": 4,
            "description": "Diagnosing common stitch faults (broken threads, puckered seams, skipped stitches) and executing the 4-step care maintenance protocol."
        }
    )
    l4 = Lesson.objects.create(
        topic=topic,
        learning_unit=u4,
        title="Troubleshooting Stitch Faults & Machine Care",
        status="published"
    )
    print(f"\n  [+] Ingesting Lesson 4: '{l4.title}' (Lesson ID: {l4.id})")

    # Page 1: Hook & Introduction
    create_block(l4, 1, 1, "suggested_image", "The JSS Machine Doctor: Reading the Stitch Symptoms", {
        "caption": "A skilled young tailor reads stitch symptoms systematically to diagnose tension faults, bent needles, and lint jams.",
        "search_query": "sewing machine maintenance cleaning oiling tools"
    })
    create_block(l4, 1, 2, "learning_goal", "What You Will Learn", {
        "text": "By the end of this lesson, you will be able to:\n\n- Diagnose the causes and remedies of **upper/lower thread breakage**.\n- Fix **skipped stitches, puckered seams, and bent/broken needles**.\n- Solve the classic misconception of **loose thread bunching underneath fabric**.\n- Execute the **4-step care protocol** (dusting, mineral oiling, wiping, covering)."
    })
    create_block(l4, 1, 3, "concept_explanation", "The Diagnostic Art of Sewing Troubleshooting", {
        "text": "When a sewing machine acts up, do not panic—read the stitch symptoms!\n\n- **1. Upper Thread Breaks**: Upper tension too tight, incorrect threading, needle inserted backwards, or rough eye on needle.\n- **2. Lower Thread Breaks**: Bobbin case threaded incorrectly, bobbin wound unevenly, or bobbin tension screw too tight.\n- **3. Skipped Stitches**: Needle is blunt, bent, inserted too low, or incorrect size for the fabric.\n- **4. Puckered Seams**: Thread tension is too tight for delicate fabric, or needle is blunt and snagging threads.\n- **5. Needle Breaks**: Operator is manually pulling/pushing fabric (bending needle against plate) or needle clamp is loose."
    })

    # Page 2: Troubleshooting Diagnostics Blueprint
    create_block(l4, 2, 1, "suggested_diagram", "Common Stitch Faults & Diagnostics Blueprint", {
        "caption": "Visual diagnostic guide comparing skipped stitches, puckered seams, thread loops, and a balanced lockstitch.",
        "diagram_type": "stitch_diagnostics"
    })
    create_block(l4, 2, 2, "concept_explanation", "The Classic Thread Bunching Misconception", {
        "text": "Beware this common mechanical error:\n\n- When messy loops of loose thread bunch up underneath your fabric (a 'bird's nest'), **the fault is almost always in the UPPER thread tension**, not the bobbin!\n- Because the top thread has zero tension (slipped out of tension discs or presser foot was down during threading), the bobbin mechanism pulls massive loops of top thread down through the plate.\n- **The Fix**: Raise presser foot, re-thread the top path completely, ensure thread sits between tension discs, and tighten discs slightly!"
    })

    # Page 3: Comparison Table
    create_block(l4, 3, 1, "comparison_table", "Comprehensive Troubleshooting Diagnostic Matrix", {
        "headers": ["Fault / Symptom", "Probable Mechanical Cause", "Corrective Action / Remedy"],
        "rows": [
            ["Upper Thread Snaps", "Tension discs too tight; needle inserted backwards; burred needle", "Loosen tension regulator; insert fresh needle with flat shank facing correctly"],
            ["Lower Thread Snaps", "Bobbin case slot threaded wrong; bobbin wound unevenly or too full", "Remove bobbin, wind evenly, and re-thread case tension spring properly"],
            ["Skipped Stitches", "Needle is blunt, bent, or not pushed fully up into clamp", "Replace with sharp new needle; push fully to top stop before clamping"],
            ["Puckered Seams", "Thread tension too tight; needle blunt; stitch length too long", "Loosen upper tension discs slightly; insert sharp new fine needle"],
            ["Needle Snaps Loudly", "Operator pulling fabric; needle too thin for heavy denim; loose screw", "Let feed dogs feed naturally; use heavy size needle; tighten clamp screw"]
        ]
    })

    # Page 4: 4-Step Maintenance Blueprint
    create_block(l4, 4, 1, "suggested_diagram", "The 4-Step Care & Maintenance Protocol Blueprint", {
        "caption": "Process storyboard demonstrating dry brush lint cleaning, mineral oil application, wiping, and dust covering.",
        "diagram_type": "care_maintenance_storyboard"
    })
    create_block(l4, 4, 2, "concept_explanation", "The 4 Golden Rules of Machine Maintenance", {
        "text": "Proper maintenance preserves your sewing machine for decades:\n\n- **1. Dusting & Lint Removal**: Use a small dry lint brush to sweep away fluff from around the feed dog and bobbin race. **CAUTION: Never blow with your mouth!** Breath moisture causes internal steel parts to rust.\n- **2. Oiling with Mineral Oil**: Apply 1 drop of clear sewing machine oil into marked oil holes. **NEVER use vegetable cooking/salad oil!** Cooking oil turns into sticky gummy glue that permanently freezes gears.\n- **3. Wiping**: Wipe excess oil from the machine arm with a clean, dry cotton cloth.\n- **4. Proper Storage**: Lower needle and presser foot down onto a scrap of fabric to absorb dripping oil, and slide the protective dust cover over the frame."
    })

    # Page 5: Worked Example
    create_block(l4, 5, 1, "step_process", "Worked Example: Fixing Loose Thread Bunching Underneath Fabric", {
        "steps": [
            {"number": 1, "title": "Observe the Symptom", "description": "You stitch a cotton strip and notice big tangles of loose looped thread bunching under the fabric."},
            {"number": 2, "title": "Resist Touching Bobbin Screw", "description": "Do not adjust the small bobbin case screw. The problem is 99% likely in the upper tension assembly."},
            {"number": 3, "title": "Raise Foot & Re-thread Path", "description": "Raise the presser foot lever to open tension discs, unthread the upper path, and re-thread from spool pin to needle."},
            {"number": 4, "title": "Test & Verify", "description": "Lower presser foot and stitch a test strip. The stitches are now perfectly balanced and flat on both sides!"}
        ]
    })

    # Page 6: Hands-On Activity
    create_block(l4, 6, 1, "mini_activity", "Hands-On Task: Machine Care Do's & Don'ts Sorting", {
        "instructions": "In your notebook, organize these 6 practices into **Smart Care** or **Damage Risk**:\n\n- 1. Brushing feed dog lint with a dry stiff brush.\n- 2. Blowing into the bobbin race with your mouth.\n- 3. Lubricating machine joints with kitchen cooking oil.\n- 4. Lowering the presser foot onto a scrap of cloth during storage.\n- 5. Using refined, clear sewing machine mineral oil.\n- 6. Pulling fabric tightly from behind the needle while stitching."
    })

    # Page 7: Key Takeaways & Recall
    create_block(l4, 7, 1, "key_takeaway", "Key Takeaways: Troubleshooting & Care", {
        "text": "Remember these maintenance essentials:\n\n- **Loops underneath** mean **upper tension is too loose**.\n- **Never pull fabric**—let the feed dog do the feeding.\n- **Never blow mouth breath** into the shuttle race (causes rust).\n- **Only use clear mineral machine oil**, never organic cooking oil.\n- Store with a **fabric scrap under the foot** and a **dust cover on top**."
    })

    # Page 8: Knowledge Check
    create_block(l4, 8, 1, "knowledge_check", "Scenario Knowledge Check: Troubleshooting & Maintenance", {
        "question": "A student sewing a cotton seam hears a loud snap and the needle breaks. They realize they were pulling the fabric tightly with their hands to make it sew faster. What was the cause of the breakage?",
        "options": [
            "The upper spool pin was bent",
            "Manually pulling the fabric bent the needle out of alignment, forcing it to strike the metal throat plate and snap",
            "The bobbin thread was wound with too much oil",
            "The stitch regulator was set to a tight 2mm length"
        ],
        "correct_index": 1,
        "explanation": "Correct! Pulling or pushing fabric manually bends the needle shank, causing it to strike the metal throat plate or presser foot and break with a snap. Operators must allow the feed dogs to feed fabric naturally."
    })

    total_lessons = topic.lessons.count()
    total_pages = sum(len(set(l.blocks.values_list("page_number", flat=True))) for l in topic.lessons.all())
    total_blocks = LessonBlock.objects.filter(lesson__topic=topic).count()

    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 6 Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CBC Grade 7 Home Science Topic 6: The Sewing Machine")
    parser.add_argument("--replace", action="store_true", default=True, help="Replace existing topic content")
    args = parser.parse_args()
    ingest_cbc_grade7_home_science_topic6(replace=args.replace)
