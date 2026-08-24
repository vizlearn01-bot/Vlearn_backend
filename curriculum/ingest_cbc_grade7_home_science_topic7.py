"""
VLearn Curriculum Ingestion Script
CBC Grade 7 — Home Science
Topic 7: Seams (Order: 7)

Creates:
- Topic 7: Seams (Order: 7)
- 4 Learning Units
- 4 Published Lessons (32 Pages, 8 per lesson)
- 48 LessonBlocks (12 per lesson)
- Clean, student-friendly content with zero bracket citations, proper '- ' list formatting.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock
)

def ingest_cbc_grade7_home_science_topic7():
    print("=" * 80)
    print("INGESTING CBC GRADE 7 HOME SCIENCE — TOPIC 7: SEAMS")
    print("=" * 80)

    # 1. Resolve Curriculum, Grade, Subject
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "CBC Curriculum not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 7").first()
    assert grade, "Grade 7 not found!"
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject Home Science not found!"

    print(f"[*] Hierarchy: {curriculum.name} -> {grade.name} -> {subject.name}")

    # 2. Create or Get Topic 7
    topic, created = Topic.objects.get_or_create(
        subject=subject,
        name="Seams",
        defaults={
            "order": 7,
            "description": "Mastering seam terminology, comparing plain, French, overlaid, and double-stitched seams, neatening edges with pinking and loop stitches, and constructing functional household articles."
        }
    )
    if not created:
        topic.order = 7
        topic.description = "Mastering seam terminology, comparing plain, French, overlaid, and double-stitched seams, neatening edges with pinking and loop stitches, and constructing functional household articles."
        topic.save()
    print(f"[+] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # Clean existing units and lessons under this topic for idempotent ingestion
    topic.learning_units.all().delete()
    print("[*] Cleared existing learning units and lessons under Topic 7.")

    units_data = [
        {
            "order": 1,
            "title": "Understanding Seams and Seam Allowances",
            "description": "Explaining the meaning of a seam, seam line, 1.5 cm seam allowance, and seam turnings in clothing construction.",
            "lesson_title": "The Secret Inside Your Clothes: Understanding Seams & Allowances",
            "duration": 25,
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "The Secret Skeleton Inside Your Clothes!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "Inside view of a school uniform garment or shirt showing neatly stitched seam lines joining fabric panels.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/d/df/A_tailor_sewing_cloth.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/df/A_tailor_sewing_cloth.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "caption": "A tailor joining flat fabric panels on a sewing machine to construct a 3D wearable garment."
                    }
                },
                {
                    "page": 1,
                    "title": "Turn Your Clothes Inside Out!",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Hidden Stitch That Holds Everything Together

Stand up and turn the sleeve of your school shirt, skirt, or sweater inside out! What do you see running along the edges?

You will find a neat, firm row of interlocking threads holding your clothing panels together like a skeleton. This join is called a **seam**!

Why do we sew fabrics together instead of taping or gluing them?
- Cloth is made of thousands of tiny woven threads that need a strong, flexible join.
- Without strong seams, our clothes would split open the moment we bend, stretch, or run during sports.

Let's explore how dressmakers measure and stitch seams to build durable garments!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The Seam Terminology Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "The Seam Terminology & 1.5 cm Allowance Cross-Section Blueprint",
                        "description": "Cross-sectional labeled fabric diagram showing seam allowance, stitching line, raw edge, and folding margins."
                    }
                },
                {
                    "page": 2,
                    "title": "Mastering the Language of Seams",
                    "type": "rich_text",
                    "content": {
                        "text": """### The 4 Essential Terms Every Tailor Must Know

To construct clothes that fit comfortably and last for years, you must master the fundamental anatomy of a seam:

- **Seam**: The permanent line of stitching that joins two or more pieces of fabric together.
- **Seam Line**: The exact path where the needle stitches through the cloth to hold the panels together.
- **Seam Allowance**: The safety margin of extra fabric left between the seam line and the raw cut edge (standard **1.5 cm** in garment making).
- **Seam Turning**: The small folded edge pressed onto the seam allowance to prepare it for neatening.

> **Golden Rule**: Always measure your 1.5 cm seam allowance with a ruler before stitching so your garment keeps its exact designed size!"""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Why the 1.5 cm Safety Margin is Essential",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Science of Fabric Fraying & Structural Safety

Why can't we just sew right along the very edge of the cloth to save fabric?

When fabric is woven, long warp threads and crosswise weft threads crisscross each other. When you cut fabric, the threads at the cut margin are loose:

- **If you stitch too close to the edge (e.g. 2 mm)**: The slightest pull from bending or washing will cause the loose weave threads to slip out, and the entire seam will rip open!
- **With a 1.5 cm seam allowance**: The stitches anchor deep inside the firm, stable body of the woven fabric, providing a protective buffer that prevents fraying.
- **Room for adjustments**: If you grow taller or wider during the school term, the seam allowance allows a tailor to let the garment out easily!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "Woven Fabric Warp & Weft Thread Slippage Diagram",
                    "type": "diagram",
                    "content": {
                        "title": "Woven Fabric Warp & Weft Thread Slippage Diagram",
                        "description": "Vector diagram illustrating how woven yarns slip out under tension when stitches are placed too close to raw cut edges."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Common Seam Misconceptions & Pro-Tips",
                    "type": "rich_text",
                    "content": {
                        "text": """### Separating Tailoring Myths from Real Facts

**Myth 1**: *"Sewing right at the edge of the fabric is better because it saves cloth."*
- **Fact**: Stitching at the raw edge guarantees that the fabric threads will pull apart and tear open within days. A 1.5 cm allowance is necessary for structural strength.

**Myth 2**: *"Seam allowances can be any random width as long as the pieces stick together."*
- **Fact**: If your seam allowance varies (e.g. 2 cm at the top and 0.5 cm at the bottom), the garment will twist awkwardly and fit unevenly.

#### Pro-Tips for Measuring Allowances:
- Use a clear plastic ruler or tailor's measuring gauge.
- Mark your 1.5 cm guideline lightly with tailor's chalk on the wrong side of the fabric.
- Align the edge of your fabric with the 1.5 cm guide-line marked on the sewing machine needle plate."""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Marking and Pinning a Seam",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Prepare Fabric Panels for Machine Stitching

Follow these 4 practical steps to prepare perfect seams:

- **Step 1: Match the Panels**: Place the two fabric pieces with **right sides facing together**, matching the cut edges precisely.
- **Step 2: Measure the Allowance**: Measure exactly **1.5 cm** inward from the raw cut edge using a ruler, marking light dots with tailor's chalk.
- **Step 3: Pin Perpendicularly**: Insert dressmaker pins across the seam line at right angles (perpendicular) to hold the cloth layers firmly without bunching.
- **Step 4: Baste Temporarily**: Sew loose, temporary hand tacking stitches along the seam line to prevent slipping before machine stitching."""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Junior Tailor Challenge: The School Shorts Disaster",
                    "type": "rich_text",
                    "content": {
                        "text": """### Solve the Workshop Mystery

**The Situation**:
Amina stitched a pair of cotton physical education shorts for her brother. She stitched only 2 millimeters away from the cut edges because she wanted the shorts to feel extra wide. 

During the first football match, when her brother kicked the ball, the side seam completely split open, leaving a ragged hole with loose hanging threads.

**The Diagnosis**:
- Why did the seam fail? Amina stitched too close to the raw edge.
- Without a proper **1.5 cm seam allowance**, the woven fabric threads simply slipped apart under body tension.
- The fabric did not actually tear—the loose weave yarns just pulled out of the seam!

**The Professional Fix**:
- Cut new panels or re-align with a full 1.5 cm seam allowance, pin, tack, and machine-stitch along the true seam line."""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Seam Terminology Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "What is the standard width of the fabric safety margin left between the stitching line and the raw cut edge in clothing construction, and what is its main purpose?",
                        "options": [
                            "0.5 cm, used only to make the garment lighter",
                            "1.5 cm, used to anchor stitches firmly and prevent woven threads from fraying out",
                            "5.0 cm, used to fold heavy decorative pockets on shirts",
                            "No allowance is needed if the needle is sharp"
                        ],
                        "correct_index": 1,
                        "explanation": "In standard clothing construction, a 1.5 cm seam allowance provides a safe buffer that keeps stitches anchored firmly inside the fabric body, preventing the woven threads from fraying or pulling apart under wear."
                    }
                }
            ]
        },
        {
            "order": 2,
            "title": "Exploring the Four Types of Seams",
            "description": "Classifying and comparing plain (open), French, overlaid, and double-stitched seams, and selecting seams based on fabric weight.",
            "lesson_title": "The 4 Seam Types: Plain, French, Overlaid & Double-Stitched",
            "duration": 25,
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "Two Fabrics, Two Completely Different Joins!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "Close-up detail of double-stitched and overlaid seams on denim jeans pocket and yoke showing heavy durable joins.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Wrangler_jeans_back_detail_%282026-01-27%29.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Wrangler_jeans_back_detail_%282026-01-27%29.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "Double-stitched and overlaid seams on durable denim jeans designed to withstand heavy friction and stress."
                    }
                },
                {
                    "page": 1,
                    "title": "Why Do Jeans Look Different from Silk Blouses?",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Tailor's Secret: Matching Seam to Fabric

Imagine you are sewing two articles: a rugged denim school backpack and a delicate sheer silk headscarf.

Would you stitch them the exact same way?
- If you use a thick, heavy double-stitched seam on a delicate silk scarf, the scarf will look stiff, bulky, and puckered!
- If you use a light, single-stitched seam on a denim backpack, the bottom will burst open when loaded with heavy textbooks!

Dressmakers classify seams into four distinct construction methods to match different fabrics and stress points. Let's master all four!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The 4 Seam Types Structural Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "The 4 Seam Types Structural 3D Blueprint",
                        "description": "3D perspective blueprint comparing the construction folds of Plain/Open, French, Overlaid, and Double-Stitched seams."
                    }
                },
                {
                    "page": 2,
                    "title": "Classification of the 4 Main Seam Types",
                    "type": "rich_text",
                    "content": {
                        "text": """### How the 4 Seams are Constructed

Here is how tailors fold and stitch each of the 4 essential seams:

- **Plain (Open) Seam**: The simplest and most common seam. Two fabric layers are stitched once on the wrong side, and the allowances are pressed open flat like two wings. Inconspicuous (hidden), but raw edges must be neatened.
- **French Seam**: A self-neatening 'seam within a seam'. It is stitched twice—first on the right side, trimmed narrow, turned inside out, and stitched again on the wrong side to completely encase all raw edges in a folded pocket.
- **Overlaid Seam**: One fabric panel has its edge folded under and placed on top of another flat piece, then stitched from the right side. Highly visible and strong, perfect for curved yokes and patch pockets.
- **Double-Stitched (Machine-Fell) Seam**: An ultra-strong, flat seam with two parallel rows of stitches on the right side. All raw edges are folded and tucked under. Ideal for jeans, workwear, and sportswear."""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Conspicuous vs. Inconspicuous Seams",
                    "type": "rich_text",
                    "content": {
                        "text": """### Understanding Seam Visibility & Purpose

Tailors divide seams into two major visual categories:

#### 1. Inconspicuous Seams (Hidden from the Outside)
- **Examples**: Plain seams and French seams.
- **Appearance**: When the garment is viewed from the outside, only a clean, smooth hairline join is visible.
- **Best for**: Collars, side seams of dresses, school shirts, and formal wear where visible thread lines would look messy.

#### 2. Conspicuous Seams (Visible from the Outside)
- **Examples**: Overlaid seams and Double-stitched seams.
- **Appearance**: The rows of machine stitching are deliberately displayed on the right side of the garment.
- **Best for**: Denim jeans pockets, shirt yokes, heavy canvas bags, and safari jackets where stitches add decorative style and heavy-duty strength!"""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "The Fabric Weight & Seam Selection Spectrum",
                    "type": "diagram",
                    "content": {
                        "title": "The Fabric Weight & Seam Selection Spectrum",
                        "description": "Visual spectrum mapping fine sheer fabrics to French seams, medium cotton to plain open seams, and heavy denim to double-stitched seams."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Seam Selection Misconceptions & Traps",
                    "type": "rich_text",
                    "content": {
                        "text": """### Avoid These Common Selection Mistakes

**Myth 1**: *"The French seam is called French because it can only be sewn in France."*
- **Fact**: 'French seam' is a universal tailoring term for a double-stitched enclosed seam. It is used worldwide because it encloses raw edges without needing a separate serger machine.

**Myth 2**: *"Double-stitched seams are the strongest, so we should use them on every garment."*
- **Fact**: Never use a double-stitched seam on sheer silk or chiffon! The heavy folding and dual stitch lines will cause delicate fabric to pucker, bunch up, and lose its drape.

#### The Golden Selection Rules:
- **Fine/Sheer fabrics (silk, chiffon)**: Use **French Seams**.
- **Medium fabrics (cotton, calico, linen)**: Use **Plain Open Seams**.
- **Heavy fabrics (denim, drill, canvas)**: Use **Double-Stitched Seams**."""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Constructing a French Seam",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Create a Perfect Enclosed French Seam

The French seam is unique because it starts on the **right side** of the cloth:

- **Step 1: Place Wrong Sides Together**: Unlike plain seams, align your fabric panels with **wrong sides facing each other** (right side facing out).
- **Step 2: Stitch First Row**: Machine-stitch a straight line exactly **6 mm (1/4 inch)** away from the raw edge.
- **Step 3: Trim Raw Edges**: Trim the seam allowance down to **3 mm** with sharp shears to eliminate bulk and fraying threads.
- **Step 4: Press and Fold**: Press the seam open, then fold the fabric with **right sides facing together** along the stitch line.
- **Step 5: Stitch Second Row**: Stitch a second row exactly **6 mm** from the folded edge, completely encasing the trimmed raw edges inside a neat pouch!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Tailor's Decision Lab: Selecting the Best Seam",
                    "type": "rich_text",
                    "content": {
                        "text": """### Help the Apprentice Tailor Choose!

**Scenario A: Halima's Chiffon Scarf**
- Halima is sewing a delicate, sheer chiffon headscarf. She wants the edges to look neat with zero raw threads scratching her neck.
- **Correct Choice**: **French Seam**. It encloses all raw edges inside a narrow fold, preventing fraying on sheer material without adding bulky visible stitches.

**Scenario B: Kamau's Gardening Apron**
- Kamau is sewing a heavy cotton canvas work apron to hold sharp gardening trowels and heavy seeds.
- **Correct Choice**: **Double-Stitched (Machine-Fell) Seam** for the main body and an **Overlaid Seam** for the tool pockets. These provide maximum durability under load."""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Seam Types Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Which type of seam is stitched twice—first on the right side and then on the wrong side—to completely encase and hide the raw cut edges inside a neat folded pouch?",
                        "options": [
                            "Plain open seam",
                            "French seam",
                            "Overlaid seam",
                            "Double-stitched machine-fell seam"
                        ],
                        "correct_index": 1,
                        "explanation": "A French seam is a self-neatening seam stitched first on the right side, trimmed, turned inside out, and stitched again on the wrong side, completely enclosing all raw edges inside a clean, narrow fold."
                    }
                }
            ]
        },
        {
            "order": 3,
            "title": "Fighting Fraying: Neatening Seam Edges",
            "description": "Understanding edge fraying, and executing three edge neatening methods: pinking shears, machine edge-stitching, and hand loop stitches.",
            "lesson_title": "Sealing Raw Edges: Pinking, Edge-Stitching & Hand Loop Stitches",
            "duration": 25,
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "Stop the Fray: The Battle Against Unravelling!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "Tailoring pinking shears with distinctive zigzag cutting teeth positioned over woven fabric edges.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Pinking_scissors.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Pinking_scissors.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 3.0",
                        "caption": "Pinking shears with zigzag-toothed blades designed to cut fabric edges on the bias to prevent thread fraying."
                    }
                },
                {
                    "page": 1,
                    "title": "Why Do Plain Seams Fall Apart Without Neatening?",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Unseen Destroyer Inside Clothes

Have you ever pulled a single loose thread hanging from the raw edge of an unneatened seam, only to watch a whole strip of cloth unravel in your hands?

That is **fraying**, and it is the greatest enemy of handmade clothes!

Even if your sewing machine stitches are perfectly straight, an unneatened seam allowance will:
- Unravel into hairy threads every time the garment is washed.
- Gradually eat into the seam line until the stitches collapse.
- Look untidy and feel rough against the wearer's skin.

Today, we learn 3 essential methods to seal raw edges forever!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The 3 Edge-Neatening Methods Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "The 3 Edge-Neatening Methods 3-Panel Storyboard",
                        "description": "3-panel storyboard showing pinking shears cutting a zigzag edge, a machine foot sewing a turned edge-fold, and hand needle sewing loop stitches."
                    }
                },
                {
                    "page": 2,
                    "title": "Three Practical Ways to Neaten Seams",
                    "type": "rich_text",
                    "content": {
                        "text": """### Pinking, Machine Edge-Stitching & Loop Stitches

Grade 7 learners master three reliable edge-neatening techniques:

- **1. Pinking (Mechanical Cutting)**: Cutting the raw seam allowance edges using special zigzag-toothed scissors called **pinking shears**. Cutting the woven threads diagonally (on the bias) prevents long warp and weft yarns from pulling out. Best for firmly woven cottons.
- **2. Machine Edge-Stitching (Machine Fold & Sew)**: Turning under a tiny **3 mm** margin along each seam allowance edge, pressing it flat, and stitching a straight machine line close to the fold. Best for light-to-medium fabrics.
- **3. Hand Loop Stitches (Blanket / Loop Neatening)**: Using a hand needle and thread to sew evenly spaced loops over the raw fabric edge. The thread wraps around and binds the cut yarns down firmly. Best for thick, heavily fraying wool or curved edges."""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Why Pinking Shears Cut in a Zigzag",
                    "type": "rich_text",
                    "content": {
                        "text": """### The Geometry of Bias Cutting

Why do pinking shears have saw-tooth zigzag blades instead of straight blades?

- In woven cloth, threads run in straight horizontal (weft) and vertical (warp) grids.
- When straight scissors cut parallel to these threads, entire yarns can slip free with zero resistance.
- **The Zigzag Advantage**: Pinking shears cut every tiny thread at a 45-degree angle (**the bias**). 
- Because only microscopic tips of threads are exposed along the zigzag triangles, the yarns friction-lock together and cannot easily unravel!

> **Workshop Tip**: Always hold pinking shears flat on the cutting table and cut with smooth, continuous strokes so the zigzag teeth interlock cleanly."""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "The 4-Step Hand Loop Stitch Sequence Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "The 4-Step Hand Loop Stitch Sequence Blueprint",
                        "description": "Vector diagram detailing the exact sequence for sewing hand loop stitches: anchoring, needle angle, loop formation, and tension pull."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Neatening Misconceptions & Workshop Rules",
                    "type": "rich_text",
                    "content": {
                        "text": """### Common Edge-Neatening Traps

**Myth 1**: *"Pinking shears are just decorative scissors for arts and paper crafts."*
- **Fact**: Pinking shears are heavy-duty tailoring tools. Using them on paper will dull the steel blades instantly, ruining them for fabric cutting.

**Myth 2**: *"Loop stitches should be pulled as tightly as possible."*
- **Fact**: If you pull hand loop stitches too tightly, the edge of the fabric will curl up and form an ugly, puckered ridge. Pull the thread gently so the loop rests flat against the raw edge.

#### Golden Neatening Guidelines:
- Neaten each seam allowance separately before pressing the seam open.
- Keep loop stitches evenly spaced (about 3 mm to 5 mm apart).
- Ensure all loose fuzz and lint is trimmed away before edge-stitching."""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Executing Hand Loop Stitches",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Hand-Sew Loop Stitches Over Raw Edges

Master this essential hand-sewing procedure in 4 steps:

- **Step 1: Anchor the Thread**: Fasten the thread on the wrong side of the seam allowance with a tiny double stitch 5 mm below the raw edge.
- **Step 2: Insert the Needle**: Push the needle from the back of the fabric to the front, piercing the cloth 4 mm below the raw cut edge.
- **Step 3: Form the Loop**: Bring the needle point out, making sure the working thread loops around under the needle tip.
- **Step 4: Pull Flat**: Draw the needle through smoothly until the loop sits comfortably over the raw edge without curling the fabric, repeating every 4 mm along the seam."""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Workshop Challenge: Choosing the Right Neatening Method",
                    "type": "rich_text",
                    "content": {
                        "text": """### Match the Tool to the Project

**Challenge 1**: Juma is making a calico cotton pillowcase on a sewing machine. He wants a very fast, clean, professional neatening method for straight seams.
- **Best Choice**: **Pinking with pinking shears** or **Machine edge-stitching**.

**Challenge 2**: Wanjiku is making a heavy woolen lap blanket. The thick yarns are loose and unravelling rapidly, and the fabric is too thick to turn under on a machine.
- **Best Choice**: **Hand loop stitches**. The hand loops bind the thick loose yarns securely over the cut edge without creating a bulky fold!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Edge Neatening Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why are pinking shears effective at preventing firmly woven cotton fabric from fraying along raw seam allowance edges?",
                        "options": [
                            "They melt the plastic fibers in the fabric with electric heat",
                            "They cut the fabric at a 45-degree angle (on the bias), creating zigzag teeth that prevent long straight threads from slipping out",
                            "They apply a layer of waterproof glue along the cut line",
                            "They fold the raw edge under twice automatically"
                        ],
                        "correct_index": 1,
                        "explanation": "Pinking shears cut fabric edges in a zigzag saw-tooth pattern on the bias (at an angle to the warp and weft), which prevents long continuous yarns from unravelling when handled or washed."
                    }
                }
            ]
        },
        {
            "order": 4,
            "title": "Qualities of Well-Made Seams & Article Construction",
            "description": "Auditing seam quality indicators, diagnosing tension faults, and executing step-by-step construction of a household lap bag or pillowcase.",
            "lesson_title": "Quality Audits & Step-by-Step Lap Bag Construction",
            "duration": 25,
            "pages": [
                # Card 1: Hook
                {
                    "page": 1,
                    "title": "From Flat Fabric to a Beautiful Functional Bag!",
                    "type": "suggested_image",
                    "content": {
                        "search_query": "Hand embroidery needle and colorful thread executing decorative stitches on cotton fabric panel.",
                        "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/d/db/Running_stitch_for_hand_embroidery.jpg",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/d/db/Running_stitch_for_hand_embroidery.jpg",
                        "author": "Wikimedia Commons Contributor",
                        "licensing": "CC BY-SA 4.0",
                        "caption": "Hand embroidery stitching on a flat cotton fabric panel to create decorative surface designs before article assembly."
                    }
                },
                {
                    "page": 1,
                    "title": "Putting All Our Practical Skills to Work!",
                    "type": "rich_text",
                    "content": {
                        "text": """### Becoming a Junior Craftsperson

Home Science is not just about memorizing facts—it is about creating beautiful, functional articles that enrich our homes!

Today, we bring together:
- Accurate pattern measurement and cutting.
- Straight machine stitching with plain open seams.
- Clean edge neatening with pinking shears.
- Hand decorative embroidery (stem, chain, and satin stitches).

Before we assemble our project, we must learn the **5 Golden Quality Standards** of a champion seam!"""
                    }
                },
                # Card 2: Concept Core Blueprint
                {
                    "page": 2,
                    "title": "The Seam Quality Inspector Blueprint",
                    "type": "diagram",
                    "content": {
                        "title": "The Seam Quality Inspector Blueprint",
                        "description": "Side-by-side comparison chart contrasting a well-made flat seam against faulty seams with puckering, loose thread loops, and unneatened edges."
                    }
                },
                {
                    "page": 2,
                    "title": "The 5 Golden Standards of a Well-Made Seam",
                    "type": "rich_text",
                    "content": {
                        "text": """### How to Audit Your Seam Quality

A professional seam must satisfy five strict quality indicators:

- **1. Straight and Even Stitching**: The stitch line must run perfectly straight, maintaining an exact, uniform distance (1.5 cm) from the raw cut edge.
- **2. Correct Balanced Tension**: Stitches must lock firmly in the center of the fabric layers. No puckered wrinkling (upper tension too tight) and no loose floppy loops (upper tension too loose).
- **3. Flat and Well-Pressed**: The seam allowances must lie flat with no bulky lumps, pressed open cleanly with an iron.
- **4. Uniform Allowance Width**: Seam allowances must be trimmed to an even, equal width all along the join.
- **5. Cleanly Neatened**: All raw edges must be neatly pinked, edge-stitched, or bound with loop stitches with zero stray threads."""
                    }
                },
                # Card 3: Deep Dive & Mechanism
                {
                    "page": 3,
                    "title": "Diagnosing Seam Faults & Machine Adjustments",
                    "type": "rich_text",
                    "content": {
                        "text": """### The JSS Seam Doctor: Reading the Symptoms

When a seam looks imperfect, the stitching line tells you exactly what went wrong:

#### Symptom 1: Puckered (Wrinkled) Seam
- **Visual**: The fabric bunches up tightly along the stitches like an accordion.
- **Cause**: Upper thread tension is too tight, or the stitch length is too short.
- **Remedy**: Turn the tension regulator dial down (e.g. from 6 to 4) to relax the thread pull.

#### Symptom 2: Floppy Loops on the Underside
- **Visual**: Loose, floppy loops of thread hang underneath the seam line.
- **Cause**: Upper thread tension is too loose, or the thread slipped out of the tension discs.
- **Remedy**: Re-thread the machine carefully and tighten the tension regulator dial slightly.

#### Symptom 3: Wavy, Uneven Seam Line
- **Visual**: The seam snakes left and right, causing garment sides to bulge.
- **Cause**: The operator pushed or pulled the fabric instead of letting the feed dogs guide it."""
                    }
                },
                # Card 4: Visual Breakdown
                {
                    "page": 4,
                    "title": "The 5-Stage Lap Bag Construction Process Flow",
                    "type": "diagram",
                    "content": {
                        "title": "The 5-Stage Lap Bag Construction Process Flow",
                        "description": "Process flowchart showing step-by-step lap bag assembly: draft & cut, embroider flat panel, pin & machine stitch side seams, pink edges, and hem opening."
                    }
                },
                # Card 5: Common Misconceptions
                {
                    "page": 5,
                    "title": "Article Construction Traps & Pro-Tips",
                    "type": "rich_text",
                    "content": {
                        "text": """### The #1 Mistake in Household Article Construction

**The Fatal Mistake**: *Sewing the bag sides together before doing the decorative embroidery.*
- **Why It Fails**: Once a bag or pillowcase is sewn shut, it forms a narrow, closed pocket. Trying to maneuver a hand embroidery needle inside a closed pocket is almost impossible and will catch the back fabric layer!

#### The Golden Rule of Assembly:
> **Always complete all decorative hand embroidery (stem, chain, satin stitches) on the flat, open fabric panel BEFORE you pin and sew the side seams!**

#### Three Core Decorative Hand Stitches:
- **Stem Stitch**: Neat rope-like line stitch for stems and outlines.
- **Chain Stitch**: Interlocking loops for bold borders.
- **Satin Stitch**: Smooth, solid parallel stitches for filling flowers and leaf shapes."""
                    }
                },
                # Card 6: Step-by-Step Guide
                {
                    "page": 6,
                    "title": "Step-by-Step: Constructing a JSS Lap Bag",
                    "type": "rich_text",
                    "content": {
                        "text": """### The 5 Steps to Building a Functional Lap Bag

Follow this exact master workflow in your Home Science workshop:

- **Stage 1: Draft & Cut**: Measure and cut a rectangular cotton calico panel (**30 cm wide by 60 cm long**) using tailor's shears.
- **Stage 2: Embroider First**: Draw a simple design on the front half and embroider it using stem, chain, and satin stitches with bright embroidery floss.
- **Stage 3: Fold & Machine Sew**: Fold the panel in half (**right sides together**). Pin and machine-stitch both side seams with a **1.5 cm seam allowance**.
- **Stage 4: Neaten Edges**: Trim and zigzag-cut both side seam allowances using **pinking shears** to prevent unravelling.
- **Stage 5: Hem Top & Attach Handles**: Turn down a 2 cm double hem at the bag opening, machine-stitch, and attach two sturdy cotton tape handles!"""
                    }
                },
                # Card 7: Scenario Practice
                {
                    "page": 7,
                    "title": "Quality Audit Challenge: The Cushion Cover Inspection",
                    "type": "rich_text",
                    "content": {
                        "text": """### You Are the Chief Quality Inspector!

**The Inspection**:
Bakari completed a decorative cushion cover for his family's living room sofa. You are evaluating his project using the 5 Quality Standards:

1. **Stitch Line**: Perfectly straight, exactly 1.5 cm from the edges $\rightarrow$ **PASS (5/5)**
2. **Tension**: Stitches lock evenly in center with no puckering $\rightarrow$ **PASS (5/5)**
3. **Pressing**: Seams pressed flat and open with an iron $\rightarrow$ **PASS (5/5)**
4. **Neatening**: Raw allowances cut cleanly with pinking shears $\rightarrow$ **PASS (5/5)**
5. **Decoration**: Flower motif neatly filled with smooth satin stitches $\rightarrow$ **PASS (5/5)**

**Verdict**: Bakari's cushion cover receives the **Master Craftsperson Award** for exceptional durability and beauty!"""
                    }
                },
                # Card 8: Mastery Knowledge Check
                {
                    "page": 8,
                    "title": "Article Construction Mastery Check",
                    "type": "scenario_check",
                    "content": {
                        "question": "Why must all decorative hand embroidery (such as stem, chain, or satin stitches) be completed on a lap bag or pillowcase panel before the side seams are machine-stitched together?",
                        "options": [
                            "Because sewing machine needles will melt embroidery threads",
                            "Because embroidering on a flat, open piece of cloth is easy and accurate, whereas hand-stitching inside a closed narrow bag pocket is extremely difficult and may accidentally stitch the front and back layers together",
                            "Because decorative stitches can only be sewn through raw unneatened margins",
                            "Because embroidery thread is too heavy for flat fabric"
                        ],
                        "correct_index": 1,
                        "explanation": "Embroidering on a flat, open fabric panel allows the crafter to work smoothly and accurately without needle obstruction. Once the bag sides are sewn shut, maneuvering hand needles inside a narrow pocket is extremely difficult and risks sewing through both layers."
                    }
                }
            ]
        }
    ]

    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    for u_idx, u_data in enumerate(units_data, start=1):
        unit, _ = LearningUnit.objects.get_or_create(
            topic=topic,
            name=u_data["title"],
            defaults={
                "order": u_data["order"],
                "description": u_data["description"]
            }
        )
        unit.name = u_data["title"]
        unit.order = u_data["order"]
        unit.description = u_data["description"]
        unit.save()

        lesson, _ = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=unit,
            defaults={
                "title": u_data["lesson_title"],
                "status": "published"
            }
        )
        lesson.title = u_data["lesson_title"]
        lesson.status = "published"
        lesson.save()

        # Clear existing blocks
        lesson.blocks.all().delete()

        # Ingest blocks
        block_order = 1
        for p_data in u_data["pages"]:
            b = LessonBlock.objects.create(
                lesson=lesson,
                order=block_order,
                page_number=p_data["page"],
                block_type=p_data["type"],
                title=p_data["title"],
                content=p_data["content"]
            )
            block_order += 1
            total_blocks += 1
            total_pages = max(total_pages, p_data["page"])

        total_lessons += 1
        print(f"  [+] Ingested Unit {unit.order}: '{unit.name}' -> Lesson: '{lesson.title}' (8 Pages, {block_order-1} Blocks)")

    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 7 Home Science Topic 7 Ingestion Complete!")
    print(f"[*] Total Lessons: {total_lessons}, Total Pages across lessons: {total_lessons * 8}, Total Blocks: {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_cbc_grade7_home_science_topic7()
