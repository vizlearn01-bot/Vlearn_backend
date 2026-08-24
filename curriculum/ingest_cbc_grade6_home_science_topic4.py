"""
VLearn Curriculum Ingestion Script
CBC Grade 6 — Home Science
Topic 4: Clothing and Laundry (Order: 4)

Ingests:
- 6 Learning Units
- 6 Published Lessons (48 Pages total, 8 pages per lesson)
- 60 LessonBlocks (10 blocks per lesson)
- Fully aligned with CBC Grade 6 syllabus from Lessons.md
- Zero bracket citations, zero developer meta-words, strict markdown '- ' bullet formatting.
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

TOPIC4_DATA = {
    "topic_name": "Clothing and Laundry",
    "topic_order": 4,
    "topic_description": "Equipping Grade 6 learners with essential needlework, fabric-making crafts (weaving, knitting, crocheting), pocket repair, and specialized laundry care techniques.",
    "units": [
        {
            "order": 1,
            "title": "Sewing Tools & Equipment",
            "description": "Identifying, choosing, using, and safely caring for specialized sewing equipment at home and school.",
            "lessons": [
                {
                    "title": "Our Helpful Sewing Tools",
                    "description": "Discover five specialized sewing tools that make clothing repairs, garment pressing, and waistband maintenance fast, neat, and safe.",
                    "pages": [
                        {
                            "page_number": 1,
                            "blocks": [
                                {
                                    "block_type": "suggested_image",
                                    "title": "The Elastic Waistband Emergency!",
                                    "content": {
                                        "caption": "A tailor and seamstress using specialized sewing tools to mend garments neatly and safely.",
                                        "description": "A close-up view of essential sewing tools and hands mending fabric."
                                    }
                                },
                                {
                                    "block_type": "rich_text",
                                    "title": "The Vanished Waistband Cord",
                                    "content": {
                                        "text": "Imagine getting ready for physical education class when you pull on your sports shorts and hear a sharp snap! The elastic waistband has snapped and slipped deep inside the narrow fabric tunnel around your waist.\n\nYour fingers cannot reach inside because the tunnel is too long and tight. How can you pull the elastic all the way through without damaging your shorts? Today, we explore five specialized tools in our sewing box that help us handle clothing emergencies quickly and neatly."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 2,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "The 5 Specialized Home Sewing Tools Toolkit Blueprint",
                                    "content": {
                                        "caption": "The five essential home sewing tools: bodkin, iron box, ironing board, sprinkling can, and sleeve board.",
                                        "description": "A technical diagram illustrating the 5 key sewing maintenance tools and their functions."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 3,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Functions of Essential Sewing Tools",
                                    "content": {
                                        "text": "A sewing kit contains specialized tools designed for specific needlework and pressing tasks:\n\n- Bodkin: A blunt, flat, needle-like tool with a large eye. Because its tip is rounded and smooth, it easily slides elastic bands, ribbons, or cords through narrow fabric casings (such as pajama or shorts waistbands) without piercing or tearing the cloth.\n- Iron Box (Electric or Charcoal): A heavy tool that uses controlled heat and weight to press fabrics flat, remove wrinkles, and crease sharp seams neatly during garment construction and maintenance.\n- Ironing Board or Surface: A sturdy, padded, heat-resistant board that safely supports clothes during pressing, protecting table surfaces from heat damage.\n- Sprinkling Can or Spray Bottle: A container used to mist clean water lightly onto dry, stiff cotton or linen fabrics, allowing the hot iron to smooth out stubborn wrinkles effortlessly.\n- Sleeve Board: A small, narrow padded board that slides inside shirt sleeves, trouser legs, and small cuffs so they can be pressed smoothly without creating double creases on the opposite side."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 4,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "Sewing Tools Maintenance & Rust Prevention Matrix",
                                    "content": {
                                        "caption": "Daily maintenance rules and rust prevention steps for metal sewing equipment.",
                                        "description": "A matrix diagram showing safe storage, rust protection, and heat safety rules."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 5,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Care, Safety, and Rust Prevention",
                                    "content": {
                                        "text": "Proper maintenance ensures that sewing tools remain safe and last for many years:\n\n- Rust Prevention: Metal tools like bodkins, scissors, and iron plates rust quickly when exposed to moisture. Always wipe them dry with a clean cloth after use and store them in a dry sewing box. Light machine oil can be applied to metal pivot joints.\n- Heat & Electrical Safety: Always place hot irons on their heat-resistant metal stands. Never leave an iron facedown on fabric. Unplug electric irons immediately after pressing and allow them to cool completely before storing.\n- Charcoal Iron Care: Empty cold ashes from the charcoal iron's grate after every use to prevent soot accumulation and maintain good airflow.\n- Safe Storage: Keep all needles, pins, and bodkins in a secure pin-cushion or plastic container out of reach of young children."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 6,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Hands-On Practical: Replacing a Waistband Elastic",
                                    "content": {
                                        "text": "Follow these simple practical steps in your exercise book to thread a new elastic band into school shorts:\n\n- Step 1: Measure the student's waist circumference and cut a fresh strip of elastic band 5 cm shorter than the waist measurement.\n- Step 2: Thread one end of the elastic through the large eye of a steel bodkin and knot or pin it securely.\n- Step 3: Insert the blunt tip of the bodkin into the waistband casing opening.\n- Step 4: Bunched fabric forward with one hand while pushing the bodkin ahead with the other until the bodkin emerges from the opposite opening.\n- Step 5: Overlap the two elastic ends by 2 cm, stitch them together firmly with strong backstitches, and slip the joined elastic inside the casing."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 7,
                            "blocks": [
                                {
                                    "block_type": "scenario_check",
                                    "title": "Knowledge Check: Selecting Sewing Equipment",
                                    "content": {
                                        "question": "Why is a bodkin manufactured with a blunt, rounded tip rather than a sharp point like a regular sewing needle?",
                                        "options": [
                                            "To make the bodkin cheaper to manufacture in factories",
                                            "To slide smoothly through fabric casings without piercing or snagging the cloth",
                                            "Because it is only designed to pierce thick leather materials",
                                            "To allow it to pick up hot charcoal from the jiko"
                                        ],
                                        "correct_index": 1,
                                        "explanation": "A bodkin is specifically designed with a blunt, rounded tip so that it can easily glide through narrow fabric channels without puncturing or tearing the fabric fibers."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 8,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Lesson Summary & Home Science Reflection",
                                    "content": {
                                        "text": "Summary of Key Learnings:\n\n- Specialized sewing tools help us maintain clothing assets, save money, and keep our school uniforms neat and presentable.\n- The bodkin guides elastic bands through narrow fabric tunnels safely because of its blunt tip.\n- Iron boxes, padded boards, and sleeve boards smooth out fabric wrinkles and crease seams without creating unwanted double folds.\n- Sprinkling cans mist water to soften stiff dry cotton fibers for effortless pressing.\n- Keeping metal tools dry and wiping them after use prevents rust formation and extends tool life.\n\nTake action at home: Inspect your clothing at home and practice threading a cord or pressing a shirt sleeve using a sleeve board!"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "order": 2,
            "title": "Weaving Crafts",
            "description": "Exploring warp and weft principles, plain weave, basket weave, and building improvised cardboard looms.",
            "lessons": [
                {
                    "title": "Weaving Our First Mat",
                    "description": "Learn the ancient craft of fabric construction by crossing vertical warp and horizontal weft threads on an improvised cardboard loom.",
                    "pages": [
                        {
                            "page_number": 1,
                            "blocks": [
                                {
                                    "block_type": "suggested_image",
                                    "title": "Criss-Crossing Threads into Cloth!",
                                    "content": {
                                        "caption": "Traditional handloom weaving tools and colorful textile threads showing the crossing of warp and weft yarns.",
                                        "description": "A close-up photograph of weaving yarns on a handloom."
                                    }
                                },
                                {
                                    "block_type": "rich_text",
                                    "title": "From Individual Threads to Strong Fabric",
                                    "content": {
                                        "text": "Look closely at your school uniform shirt, a cotton bedsheet, or a woven sisal kiondo basket. Have you ever wondered how individual thin threads are turned into a solid, durable sheet of cloth?\n\nThey are not glued together; they are constructed through weaving! Weaving is one of humanity's oldest and most valuable fabric-making methods. Today, we discover the secrets of the loom and build our very own functional table mat using local materials."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 2,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "Plain Weave (1x1) vs. Basket Weave (2x2) Grid Pathways Blueprint",
                                    "content": {
                                        "caption": "A side-by-side comparison of 1x1 plain weave (over-one-under-one) and 2x2 basket weave (over-two-under-two) patterns.",
                                        "description": "A technical SVG diagram showing warp and weft thread movement."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 3,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Core Principles of Weaving",
                                    "content": {
                                        "text": "Weaving is the process of interlacing two sets of yarns at right angles to construct fabric:\n\n- Warp Threads: The vertical threads stretched tightly lengthwise across the loom frame. They form the stationary backbone of the woven article.\n- Weft (or Woof) Threads: The horizontal threads carried across the warp threads by a shuttle, weaving over and under them.\n- Plain Weave (1x1): The simplest and most common weave pattern. The weft thread passes over one warp thread and under the next, alternating across the entire row (over 1, under 1). It produces a firm, uniform, and durable fabric.\n- Basket Weave (2x2): A decorative variation where two parallel weft threads pass over two warp threads and under the next two (over 2, under 2). It creates a textured, checkered appearance resembling woven reed baskets."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 4,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "Cardboard Frame Loom & Cardboard Shuttle Construction Guide",
                                    "content": {
                                        "caption": "Step-by-step guide to constructing an improvised cardboard frame loom with notched edges and yarn shuttle.",
                                        "description": "An architectural diagram of an improvised cardboard loom."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 5,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Constructing an Improvised Cardboard Loom",
                                    "content": {
                                        "text": "You do not need expensive factory machines to weave beautiful articles. You can build a sturdy loom at home using recycled materials:\n\n- Required Materials: A rectangular piece of stiff cardboard (approx. 20 cm by 30 cm), a ruler, a pencil, scissors, a cardboard strip for the shuttle, and local yarns (sisal, acrylic wool, or banana fiber strips).\n- Step 1: Using your ruler, mark 1 cm notches along the top and bottom edges of the cardboard.\n- Step 2: Cut small 5 mm slits into each mark.\n- Step 3: Wind your warp yarn vertically through the notches, keeping the tension firm and even across the front of the board.\n- Step 4: Wind your weft yarn onto a notched cardboard shuttle and weave across the warp in your chosen pattern (plain or basket weave).\n- Step 5: Use a fork or a wooden ruler to press and compact each row of weft threads down firmly before starting the next row."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 6,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Finishing and Household Utility",
                                    "content": {
                                        "text": "Once your woven mat reaches the top of the cardboard frame, follow these steps to secure the edges:\n\n- Cutting the Warp: Carefully snip the warp loops at the back of the cardboard.\n- Tying Off: Tie adjacent pairs of warp threads together using neat double overhand knots to lock the weft threads in place and prevent unraveling.\n- Trimming: Trim the fringe evenly with scissors.\n- Household Uses: Your completed woven article can be used as a dining table coaster, a hot-pot mat, a colorful wall hanging, or a decorative doormat.\n- Economic Value: Weaving items using free local fibers like sisal, reeds, or fabric scraps provides practical craft skills and entrepreneurial income."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 7,
                            "blocks": [
                                {
                                    "block_type": "scenario_check",
                                    "title": "Knowledge Check: Weaving Patterns",
                                    "content": {
                                        "question": "A Grade 6 learner is weaving a doormat by passing two horizontal weft threads over two vertical warp threads and under the next two. Which weave pattern are they using?",
                                        "options": [
                                            "The plain weave method (1x1)",
                                            "The basket weave method (2x2)",
                                            "The crochet chain method",
                                            "The knit stitch method"
                                        ],
                                        "correct_index": 1,
                                        "explanation": "The basket weave method is constructed by grouping yarns in pairs, weaving two weft threads over and under two warp threads in a 2x2 pattern."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 8,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Lesson Summary & Weaving Reflection",
                                    "content": {
                                        "text": "Summary of Key Learnings:\n\n- Weaving creates solid fabric by interlacing vertical warp yarns and horizontal weft yarns at right angles.\n- Plain weave follows an alternating over-one-under-one (1x1) pattern.\n- Basket weave groups yarns into pairs with an over-two-under-two (2x2) pattern.\n- Improvised looms can easily be crafted from notched cardboard and scrap yarns.\n- Compacting weft rows with a comb or fork ensures a dense, durable, and neat finished article.\n\nTake action at home: Collect discarded cardboard boxes and practice making a 15-row plain weave coaster for your family drinking glasses!"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "order": 3,
            "title": "Knitting & Crocheting",
            "description": "Understanding loop fabric structures, knitting with two needles (knit & purl), and crocheting with a single hook.",
            "lessons": [
                {
                    "title": "The Knitting Needle and the Crochet Hook",
                    "description": "Explore the warmth and elasticity of interlocking loops through hand knitting and single-hook crocheting.",
                    "pages": [
                        {
                            "page_number": 1,
                            "blocks": [
                                {
                                    "block_type": "suggested_image",
                                    "title": "Loops of Warmth and Stretch!",
                                    "content": {
                                        "caption": "Skeins of knitting wool and long pointed knitting needles ready for fabric crafting.",
                                        "description": "A close-up photograph of knitting needles and colorful balls of yarn."
                                    }
                                },
                                {
                                    "block_type": "rich_text",
                                    "title": "The Magic of Interlocking Yarn Loops",
                                    "content": {
                                        "text": "Stretch the ribbed cuff of your school cardigan or a pair of woollen socks. Notice how it expands easily over your hand or foot and immediately springs back to fit snugly.\n\nUnlike woven cloth, which is made from crossed straight threads, knitted and crocheted fabrics are constructed from rows of interconnected loops. These loops behave like tiny springs, trapping warm air and giving sweaters their cozy elasticity. Today, we discover how to knit and crochet functional household items."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 2,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "Knit Stitch vs. Purl Stitch Needle Insertion Pathways",
                                    "content": {
                                        "caption": "The four movements of executing a knit stitch (front-to-back) versus a purl stitch (back-to-front).",
                                        "description": "A technical diagram illustrating the needle movements in knitting."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 3,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "The Art and Technique of Knitting",
                                    "content": {
                                        "text": "Knitting uses two pointed needles to interlock a continuous strand of yarn into rows of loops:\n\n- Holding the Needles: Hold the needle with the active stitches in your left hand and the working needle in your right hand, keeping a relaxed, even grip.\n- Knit Stitch (Garter Stitch): Insert the right needle into the front of the loop on the left needle from front to back. Wrap yarn around the right needle tip, pull a new loop through, and slip the old loop off the left needle.\n- Purl Stitch: Insert the right needle from back to front into the loop, wrap yarn around the needle, pull the loop through to the front, and slip the old stitch off.\n- Elasticity and Warmth: Alternating knit and purl stitches creates ribbed textures that stretch flexibly, making them ideal for neck scarves, beanies, and sweater cuffs."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 4,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "Single Crochet vs. Double Crochet Structural Loops Comparison",
                                    "content": {
                                        "caption": "An infographic showing the single active loop pathway of single crochet versus tall double crochet.",
                                        "description": "A vector comparison of single and double crochet stitches."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 5,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "The Technique of Crocheting",
                                    "content": {
                                        "text": "Crocheting uses a single hooked needle (crochet hook) to loop yarn:\n\n- The Single-Loop Advantage: Unlike knitting, where dozens of loops sit open on two needles, crocheting manages only one active loop at a time. If you drop the hook, your project will not easily unravel.\n- Slip Knot and Foundation Chain: Every crochet project starts with a slip knot on the hook, followed by pulling the yarn through the loop repeatedly to form a foundation chain resembling a braided rope.\n- Single Crochet (SC): A short, dense stitch worked by inserting the hook through a chain loop, wrapping yarn (yarn over), pulling up a loop (2 loops on hook), and pulling yarn through both loops. Ideal for sturdy hot-pads and hats.\n- Double Crochet (DC): A taller, airy stitch worked by wrapping yarn around the hook before inserting it into the chain (yarn over first). It creates open, lace-like patterns and finishes projects faster."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 6,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Improvising Tools & Practical Project: Winter Scarf",
                                    "content": {
                                        "text": "You can improvise your own crafting tools using local materials:\n\n- Improvised Knitting Needles: Smooth pieces of dry bamboo, thin wooden twigs, or sturdy plastic straw tubes can be carved and smoothed with sandpaper to create blunt, snag-free needles.\n- Improvised Crochet Hooks: Carve a small notch near the tip of a smooth wooden twig or rigid wire.\n- Practical Project: Knit or crochet a 1-metre neck scarf using soft acrylic wool. Maintain even yarn tension so the edges stay straight and uniform.\n- Safety Note: Always store pointed needles and hooks safely in a pencil pouch or case to avoid puncture injuries."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 7,
                            "blocks": [
                                {
                                    "block_type": "scenario_check",
                                    "title": "Knowledge Check: Knitting vs. Crocheting",
                                    "content": {
                                        "question": "Why is crocheting often considered easier to pause and manage for a beginner compared to knitting?",
                                        "options": [
                                            "Because crocheting does not use any yarn or wool",
                                            "Because crocheting maintains only one active loop on a single hook, preventing dropped stitches from unraveling whole rows",
                                            "Because crochet hooks are made of sharp iron that pierces the cloth automatically",
                                            "Because crocheting can only make straight ropes"
                                        ],
                                        "correct_index": 1,
                                        "explanation": "Crocheting holds only a single active loop at a time on one hook, meaning that if the tool is set down or dropped, the entire row will not unravel like open knitting loops."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 8,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Lesson Summary & Craft Reflection",
                                    "content": {
                                        "text": "Summary of Key Learnings:\n\n- Knitted and crocheted fabrics are stretchy and warm because of their springy interlocking loop structure.\n- Knitting uses two needles and two core stitches: the knit stitch (worked front-to-back) and the purl stitch (worked back-to-front).\n- Crocheting uses a single hooked needle working with one active loop at a time.\n- Single crochet creates dense, compact stitches, while double crochet creates tall, open patterns.\n- Both tools can be improvised safely using smoothed bamboo, wooden twigs, or rigid reeds.\n\nTake action at home: Practice making a 10-stitch foundation chain using a piece of yarn and an improvised wooden hook!"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "order": 4,
            "title": "Repairing Uniform Pockets",
            "description": "Identifying pocket types (patch vs. in-seam), diagnosing damage, matching thread colors, and executing strong backstitch repairs.",
            "lessons": [
                {
                    "title": "Mending Our Uniform Pockets",
                    "description": "Learn to inspect, diagnose, and neatly repair loose stitching and tears on school uniform pockets using strong, neat backstitches.",
                    "pages": [
                        {
                            "page_number": 1,
                            "blocks": [
                                {
                                    "block_type": "suggested_image",
                                    "title": "The Vanishing Pen Mystery!",
                                    "content": {
                                        "caption": "Hand-sewing with a needle and matching thread to repair fabric seams neatly and firmly.",
                                        "description": "A close-up photograph of needle and thread hand stitching."
                                    }
                                },
                                {
                                    "block_type": "rich_text",
                                    "title": "The Loose Pocket Leak",
                                    "content": {
                                        "text": "You slide your favorite red pen into your school shirt pocket before morning assembly. But when you sit at your desk, the pen is gone! You look closely at your shirt and discover that the top corner of your pocket has peeled away because the machine stitches have snapped and unraveled.\n\nPockets carry pencils, money, and handkerchiefs every day, making them prone to strain and tears. Learning how to repair loose pocket seams keeps your uniform neat and saves your family the expense of hiring a tailor."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 2,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "Patch Pocket vs. Pocket-in-Seam Anatomy Blueprint",
                                    "content": {
                                        "caption": "Anatomy and construction differences between an external patch pocket and a hidden pocket-in-seam.",
                                        "description": "A technical SVG blueprint illustrating the two primary pocket types."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 3,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Understanding Pocket Types and Damage",
                                    "content": {
                                        "text": "Pockets are constructed in two common styles:\n\n- Patch Pocket: A pocket pouch cut from a separate piece of cloth and stitched directly onto the outer surface of a garment (common on school shirts, blouses, and jackets).\n- Pocket-in-Seam: A concealed pocket bag sewn into the side seam of a garment, with only a narrow opening visible along the seam crease (common on school shorts, trousers, and skirts).\n\nCommon Types of Pocket Damage:\n- Loose Stitching: The sewing thread snaps or unravels, causing the pocket corner or edge to peel away from the main garment.\n- Torn Pocket: The fabric itself rips or splits, usually caused by carrying sharp items or catching the pocket edge on a desk corner."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 4,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "Patch Pocket Corner Repair with Overlapping Backstitches Storyboard",
                                    "content": {
                                        "caption": "Step-by-step repair sequence: starting 3 stitches before the tear, sewing backstitches, and triple corner locking.",
                                        "description": "A storyboard diagram showing proper pocket mending procedure."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 5,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "5 Factors Before Repairing & Mending Protocol",
                                    "content": {
                                        "text": "Always evaluate these 5 factors before starting your repair:\n\n- 1. Type of Damage: Determine whether the thread is loose or the cloth is torn.\n- 2. Size of Damage: Measure how far the seam has separated.\n- 3. Position of Damage: Notice whether the damage is at a high-strain corner or along the bottom edge.\n- 4. Fabric Color & Texture: Select a thread that matches the garment's color and weight exactly. If your uniform shirt is navy blue, use navy blue thread—never bright yellow or white!\n- 5. Choice of Stitches: Use small, tight backstitches. Backstitches interlock firmly, making them as strong as machine stitching.\n\nStep-by-Step Mending Procedure:\n- Step 1: Thread your needle with matching thread and knot the end.\n- Step 2: Insert the needle from the underside, starting 3 or 4 stitches before the loose area to overlap and lock the remaining factory thread.\n- Step 3: Sew along the original seam line using neat backstitches.\n- Step 4: Reinforce the top corner with 3 tight anchor stitches in the exact same spot.\n- Step 5: Fasten off securely on the inside of the garment with a double knot."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 6,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Grooming Standards and Economic Benefits",
                                    "content": {
                                        "text": "Maintaining your clothing has valuable personal and financial benefits:\n\n- Self-Reliance: Repairing your own school uniform builds independence and practical life skills.\n- Smart Grooming: Well-mended clothing with neat, invisible repairs keeps you looking clean, disciplined, and respectable at school.\n- Financial Savings: Fixing small tears promptly prevents them from growing larger, extending the garment's lifespan and saving family money.\n- Common Mending Mistake: Never use wide, loose tacking stitches or contrasting thread colors for permanent repairs, as they will quickly pull open under pressure."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 7,
                            "blocks": [
                                {
                                    "block_type": "scenario_check",
                                    "title": "Knowledge Check: Repairing Loose Seams",
                                    "content": {
                                        "question": "Why is it important to start your repair stitches 3 or 4 stitches before the loose section when mending a patch pocket?",
                                        "options": [
                                            "To make the pocket pouch smaller and tighter",
                                            "To overlap and lock the remaining intact machine stitches, preventing further unraveling",
                                            "To test whether the needle is sharp enough",
                                            "To use up excess sewing thread from the spool"
                                        ],
                                        "correct_index": 1,
                                        "explanation": "Overlapping the repair stitching with 3 or 4 intact factory stitches anchors the existing thread ends and prevents the rest of the pocket seam from continuing to unravel."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 8,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Lesson Summary & Mending Reflection",
                                    "content": {
                                        "text": "Summary of Key Learnings:\n\n- Pockets are either external patch pockets or concealed pocket-in-seams.\n- Before repairing, evaluate damage type, size, position, fabric color, and stitch choice.\n- Always match the sewing thread color exactly to the fabric for neat, discreet repairs.\n- Backstitches provide maximum strength for high-strain pocket corners.\n- Overlapping previous intact stitches locks unraveled threads and prevents seam breakdown.\n\nTake action at home: Check all the pockets on your school uniforms today and repair any loose corner stitching neatly with matching thread!"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "order": 5,
            "title": "Special Laundry Treatments",
            "description": "Understanding stain removal, chewing gum removal, disinfecting, bleaching, fabric conditioning, and chemical handling safety.",
            "lessons": [
                {
                    "title": "Defeating Tough Playground Stains",
                    "description": "Master the science of stain removal, disinfecting, bleaching, and fabric conditioning to restore stained and soiled garments safely.",
                    "pages": [
                        {
                            "page_number": 1,
                            "blocks": [
                                {
                                    "block_type": "suggested_image",
                                    "title": "Mud, Ink, and Grass!",
                                    "content": {
                                        "caption": "Washing laundry in basins with soap and water to clean and treat clothing.",
                                        "description": "A close-up photograph of a student washing laundry in basins."
                                    }
                                },
                                {
                                    "block_type": "rich_text",
                                    "title": "The Playground Stain Mystery",
                                    "content": {
                                        "text": "During an exciting soccer match at break time, you slide across the grass to score a winning goal. But when you look down, your bright white school uniform shorts are covered in green grass stains, pen ink marks, and a spot of blood from a scraped knee.\n\nNormal washing with regular bar soap and water cannot lift these stubborn marks; it merely leaves dull grey smudges. Today, we become laundry stain detectives and explore special chemical and natural treatments that lift tough stains safely without damaging our clothes."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 2,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "The 4-Quadrant Playground Stain Removal Reagent Matrix",
                                    "content": {
                                        "caption": "A 4-quadrant guide matching blood, ink, grass, and chewing gum stains to their specific cold/warm household reagents.",
                                        "description": "A comparative matrix SVG for laundry stain removal."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 3,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Targeted Stain Removal Chemistry",
                                    "content": {
                                        "text": "Different stains have different chemical structures and require targeted treatments:\n\n- Blood Stains (Protein-based): Always soak immediately in cold salt water. Cold water dissolves protein. Warning: Never use hot water, because heat coagulates (bakes) blood proteins permanently into the fabric fibers, turning it into an indelible brown stain.\n- Grass Stains (Chlorophyll-based): Rub the green stain with methylated spirit or lemon juice to dissolve the plant chlorophyll before washing with warm soapy water.\n- Ink Stains (Chemical dye-based): Treat promptly with fresh lemon juice and salt or soak in warm fresh milk to lift the ink pigment from the fibers.\n- Chewing Gum (Adhesive polymer): Rub the sticky gum with ice cubes until it freezes hard and becomes brittle. Once frozen, gently peel or scrape it off with a blunt butter knife without tearing the fabric threads."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 4,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "Chemical Laundry Reagents Safety & Handling Guide",
                                    "content": {
                                        "caption": "Safe handling procedures for laundry chemicals: rubber gloves, ventilation, dilution, and zero chemical mixing.",
                                        "description": "A safety SVG diagram outlining laundry chemical precautions."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 5,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Other Special Laundry Treatments",
                                    "content": {
                                        "text": "Special laundry treatments solve specific fabric and hygiene problems:\n\n- Disinfecting: Using boiling water or antiseptic liquids (like Dettol) to destroy disease-causing germs and fungi on underwear, handkerchiefs, and sickroom bedding.\n- Bleaching: Using mild chemical bleach (such as sodium hypochlorite) diluted in water to whiten discolored white cotton items and remove stubborn mildew spots. Caution: Never use chlorine bleach on colored clothes or silk/wool fibers!\n- Fabric Conditioning: Adding liquid fabric softener to the final rinse water to reduce static electricity, soften stiff fibers, and leave a pleasant fresh fragrance.\n- Laundry Blue: Adding a minute drop of blue tint powder or liquid to the final rinse of white clothes to counteract natural yellowing, making white shirts look bright and crisp."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 6,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Safety Precautions When Handling Laundry Chemicals",
                                    "content": {
                                        "text": "Laundry chemicals are powerful and require careful handling:\n\n- Wear Protective Gloves: Wear rubber gloves to protect sensitive skin from chemical irritation and burns.\n- Work in Well-Ventilated Areas: Open windows and doors so that chemical fumes disperse freely.\n- Dilute Properly: Always dissolve bleaches and disinfectants in water according to packet instructions before adding clothes.\n- NEVER Mix Chemicals: Never mix bleach with other cleaning agents (such as paraffin or toilet cleaners), as this produces toxic, suffocating chlorine gas.\n- Wash Hands Thoroughly: Always wash your hands with clean water and soap immediately after handling laundry chemicals."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 7,
                            "blocks": [
                                {
                                    "block_type": "scenario_check",
                                    "title": "Knowledge Check: Blood Stain Protocol",
                                    "content": {
                                        "question": "Why must you strictly use COLD water rather than HOT water when treating a fresh blood stain on a school shirt?",
                                        "options": [
                                            "Hot water makes the fabric fibers stretch out of shape",
                                            "Hot water coagulates (cooks) blood proteins, permanently binding them into the cloth as an indelible brown stain",
                                            "Cold water boils the bacteria away instantly",
                                            "Hot water dissolves laundry soap too quickly"
                                        ],
                                        "correct_index": 1,
                                        "explanation": "Blood is rich in protein (haemoglobin). Exposing blood to hot water causes the protein to coagulate and lock permanently into the fabric fibers, whereas cold water dissolves and flushes the protein out safely."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 8,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Lesson Summary & Stain Removal Reflection",
                                    "content": {
                                        "text": "Summary of Key Learnings:\n\n- Special treatments include stain removal, gum removal, disinfecting, bleaching, and fabric conditioning.\n- Blood stains must always be treated with cold salt water to prevent protein coagulation.\n- Grass stains dissolve with methylated spirit, ink lifts with lemon juice and salt, and chewing gum hardens with ice cubes.\n- Disinfectants kill harmful bacteria on handkerchiefs, bedding, and underwear.\n- Always wear protective gloves, work in airy rooms, and never mix household laundry chemicals.\n\nTake action at home: Practice safely removing a pencil or ink smudge from a scrap cloth using lemon juice and salt!"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "order": 6,
            "title": "Laundering Woollens & Loose Colours",
            "description": "Mastering the 7-step wool-care protocol (kneading, squeezing, flat shade-drying) and laundering loose-dyed clothes with salt color-fixing.",
            "lessons": [
                {
                    "title": "Caring for Sweaters and Loose Colours",
                    "description": "Learn the scientific techniques for washing delicate woollen sweaters without shrinkage and protecting loose colored clothes from dye bleeding.",
                    "pages": [
                        {
                            "page_number": 1,
                            "blocks": [
                                {
                                    "block_type": "suggested_image",
                                    "title": "The Shrunken Sweater Mystery!",
                                    "content": {
                                        "caption": "Clean laundry hanging to dry properly outdoors in the shade.",
                                        "description": "A photograph of washed clothes drying neatly."
                                    }
                                },
                                {
                                    "block_type": "rich_text",
                                    "title": "The Shrinkage and Bleeding Scare",
                                    "content": {
                                        "text": "Imagine washing your warm school sweater in boiling soapy water, scrubbing it roughly on a washing stone, and hanging it by the shoulders on a wire clothesline in blazing sunshine. When it dries, disaster strikes!\n\nYour cozy sweater has shrunk into a tiny, stiff doll's cardigan, while the sleeves have stretched all the way to your knees. Worse yet, a new red T-shirt washed in the same basin bled loose dye, turning your white school socks bright pink! Today, we discover the scientific protocols for caring for delicate woollens and loose colored garments safely."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 2,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "The 7-Step Wool-Care & Flat Shade Drying Protocol Storyboard",
                                    "content": {
                                        "caption": "The 7-step wool laundering sequence: tracing size map, lukewarm squeeze washing, towel rolling, and flat shade drying.",
                                        "description": "A storyboard diagram illustrating proper wool laundering steps."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 3,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "The Science of Wool Care",
                                    "content": {
                                        "text": "Wool is a natural animal fiber sheared from sheep, and acrylic is a synthetic wool substitute. Both require specialized laundry care due to unique physical properties:\n\n- Wet Weakness: Wool fibers lose up to 30% of their physical strength when wet, making them fragile and easily torn by harsh rubbing or scrubbing.\n- Interlocking Scales (Shrinkage): Under a microscope, wool fibers have overlapping scales. Hot water and friction cause these scales to hook together tightly (felting), permanently shrinking and hardening the garment.\n- Heavy Water Weight: Wet wool absorbs large quantities of water. Hanging a wet sweater on a hanger or clothesline causes gravity to pull the heavy loops downward, permanently stretching the sleeves and hem out of shape.\n\nThe 7-Step Wool Laundry Protocol:\n- 1. Mending: Check and repair any loose seams or buttons before washing.\n- 2. Tracing: Lay the dry sweater flat on brown paper and trace its outline with a pencil to create a size map.\n- 3. Squeeze Washing: Wash in lukewarm water using mild detergent by gently kneading and squeezing—never scrub or wring!\n- 4. Rinsing: Rinse thoroughly in lukewarm water until the water is completely clear.\n- 5. Towel Rolling: Roll the wet sweater in a dry cotton towel to gently absorb excess water.\n- 6. Flat Shade Drying: Lay the sweater flat in the shade, gently easing it back to fit your pencil size map.\n- 7. Storage: Fold neatly and store flat in a drawer—never hang on coat hangers."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 4,
                            "blocks": [
                                {
                                    "block_type": "diagram",
                                    "title": "Loose-Coloured Item 4-Step Wash & Salt Color-Fixing Basin Setup",
                                    "content": {
                                        "caption": "Basin setup for loose colored laundry: separate basin, colorfastness rub test, and salt mordant bath.",
                                        "description": "A technical diagram illustrating the loose color washing protocol."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 5,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Laundering Loose-Coloured Garments",
                                    "content": {
                                        "text": "Brightly dyed cotton clothes (such as tie-and-dye shirts or colorful kitenge fabrics) often contain unstable dyes that bleed into wash water:\n\n- Dangers of Loose Dyes: Bleeding dyes cause the garment to fade rapidly and transfer unwanted color onto light-colored clothes in the same wash basin.\n- The Colorfastness Rub Test: Dampen a hidden inside hem of the garment and press a clean white cloth against it. If color transfers to the white cloth, the dye is loose and unstable!\n- Separate Washing: Always wash bleeding garments in a separate basin—never mix them with white or pastel school uniforms.\n- The Salt-Water Color Shield: Add a handful of common kitchen salt (sodium chloride) or a splash of vinegar to the wash and rinse water. Salt acts as a mordant (color fixer) that chemically binds and locks loose dye molecules into the fabric fibers.\n- Shade Drying Inside Out: Turn the garment inside out and dry it in the shade. Direct sun breaks down unstable dyes, causing rapid color fading."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 6,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Practical Laundry Checklist for Home and School",
                                    "content": {
                                        "text": "Follow this practical checklist during your weekly laundry routine:\n\n- Step 1: Sort clothes into three separate piles: Whites, Colorfast colored clothes, and Loose-dye bleeding items.\n- Step 2: Perform spot stain removal (cold water for blood, methylated spirit for grass) before general washing.\n- Step 3: Use lukewarm water and gentle kneading for woollen sweaters; roll in towels and dry flat in the shade.\n- Step 4: Add kitchen salt to bleeding items, wash quickly without prolonged soaking, and hang inside out in the shade.\n- Step 5: Press woollen garments under a damp pressing cloth to prevent scorching the delicate fibers."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 7,
                            "blocks": [
                                {
                                    "block_type": "scenario_check",
                                    "title": "Knowledge Check: Wool Care & Dye Fixing",
                                    "content": {
                                        "question": "Why is a handful of kitchen salt added to the wash water when laundering a bleeding, brightly dyed cotton garment?",
                                        "options": [
                                            "Salt bleaches the fabric to turn it white",
                                            "Salt acts as a color fixer (mordant) that binds loose dye molecules to the fabric, reducing color bleeding",
                                            "Salt causes the fabric to dry faster in the dark",
                                            "Salt makes the water boil without using fire"
                                        ],
                                        "correct_index": 1,
                                        "explanation": "Kitchen salt contains sodium chloride, which acts as a mordant to chemically bind and lock loose dye molecules back into the fabric fibers, preventing excessive color bleeding and fading."
                                    }
                                }
                            ]
                        },
                        {
                            "page_number": 8,
                            "blocks": [
                                {
                                    "block_type": "rich_text",
                                    "title": "Lesson Summary & Laundry Mastery Reflection",
                                    "content": {
                                        "text": "Summary of Key Learnings:\n\n- Wool fibers weaken when wet and shrink when subjected to heat, friction, and harsh rubbing.\n- Tracing a sweater before washing provides a size map to guide gentle reshaping during flat shade-drying.\n- Rolling a wet sweater in a towel removes excess moisture without damaging fragile fibers.\n- Loose colored items must be tested for colorfastness, washed separately, and protected with a salt-water color-fixing bath.\n- Drying colored clothes inside out in the shade protects delicate dyes from sunlight fading.\n\nTake action at home: Assist your family on laundry day by sorting whites from colored clothes and practicing flat towel-rolling on a woollen cardigan!"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

def ingest_cbc_grade6_home_science_topic4():
    print("=" * 80)
    print("INGESTING CBC GRADE 6 HOME SCIENCE — TOPIC 4: CLOTHING AND LAUNDRY")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"

    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    assert grade, "Grade 6 not found!"

    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject 'Home Science' under Grade 6 not found!"

    print(f"[*] Hierarchy: {curriculum.name} -> {grade.name} -> {subject.name}")

    topic, _ = Topic.objects.update_or_create(
        subject=subject,
        order=TOPIC4_DATA["topic_order"],
        defaults={
            "name": TOPIC4_DATA["topic_name"],
            "description": TOPIC4_DATA["topic_description"]
        }
    )
    print(f"[+] Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    # Clear existing units under this topic for clean ingestion
    for old_unit in topic.learning_units.all():
        for old_lesson in old_unit.lessons.all():
            old_lesson.blocks.all().delete()
            old_lesson.assets.all().delete()
            old_lesson.delete()
        old_unit.delete()
    print("[*] Cleared existing learning units and lessons under Grade 6 Topic 4.")

    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    for unit_data in TOPIC4_DATA["units"]:
        unit, _ = LearningUnit.objects.get_or_create(
            topic=topic,
            name=unit_data["title"],
            defaults={
                "order": unit_data["order"],
                "description": unit_data["description"]
            }
        )
        unit.name = unit_data["title"]
        unit.order = unit_data["order"]
        unit.description = unit_data["description"]
        unit.save()

        for lesson_data in unit_data["lessons"]:
            lesson, _ = Lesson.objects.get_or_create(
                topic=topic,
                learning_unit=unit,
                defaults={
                    "title": lesson_data["title"],
                    "status": "published"
                }
            )
            lesson.title = lesson_data["title"]
            lesson.status = "published"
            lesson.save()
            lesson.blocks.all().delete()

            total_lessons += 1
            pages_count = len(lesson_data["pages"])
            total_pages += pages_count

            for page_dict in lesson_data["pages"]:
                p_num = page_dict["page_number"]
                for b_order, block_dict in enumerate(page_dict["blocks"], start=1):
                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=p_num,
                        block_type=block_dict["block_type"],
                        title=block_dict["title"],
                        order=b_order,
                        content=block_dict["content"]
                    )
                    total_blocks += 1

            print(f"  [+] Ingested Unit {unit.order}: '{unit.name}' -> Lesson: '{lesson.title}' ({pages_count} Pages, {lesson.blocks.count()} Blocks)")

    print("\n" + "=" * 80)
    print(f"[SUCCESS] CBC Grade 6 Home Science Topic 4 Ingestion Complete!")
    print(f"[*] Total Lessons: {total_lessons}, Total Pages across lessons: {total_pages}, Total Blocks: {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_cbc_grade6_home_science_topic4()
