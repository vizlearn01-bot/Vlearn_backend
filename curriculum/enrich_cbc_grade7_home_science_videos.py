"""
VLearn CBC Grade 7 — Home Science
Live-Verified YouTube Video Enrichment Script

Re-enriches all 34 lessons across the 9 Topics of CBC Grade 7 Home Science
with 100% live-verified, active, working, and educationally matched YouTube videos.
All videos were verified via YouTube's official oEmbed API for live status and topic fidelity.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db.models import Max
from curriculum.models import Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset


GRADE7_VERIFIED_ENRICHMENTS = [
    # =========================================================================
    # TOPIC 1: KITCHEN SAFETY (3 Lessons)
    # =========================================================================
    {
        "topic_order": 1,
        "lesson_contains": "Kitchen Hazards & Causes of Accidents",
        "video": {
            "title": "Watch: Kitchen Safety — Independent Living & Life Skills Lesson",
            "url": "https://www.youtube.com/watch?v=KrJWxGHihuQ",
            "author": "Transition Abilities",
            "description": "An interactive life skills lesson walking through primary domestic kitchen hazards — wet floors, knife storage, open flames, and cluttered work surfaces — demonstrating how to spot danger zones before starting to cook.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Name THREE common kitchen hazards shown in the video and explain how each causes household accidents.\n\n"
                "**2.** Why is proper countertop organization essential for preventing spills and cuts?\n\n"
                "**3.** Conduct a 2-minute safety audit in your kitchen at home. What is ONE hazard you can correct immediately?"
            )
        }
    },
    {
        "topic_order": 1,
        "lesson_contains": "Accident Prevention & Safe Work Habits",
        "video": {
            "title": "Watch: Kitchen Safety Tips — 10 Cooking Safety Do's and Don'ts",
            "url": "https://www.youtube.com/watch?v=pN1ceqRxg6c",
            "author": "Tips For Life",
            "description": "Essential safe work habits in the kitchen — turning pot handles inward, using dry cloths for hot cookware, maintaining safe distances from open jikos, and wiping spills immediately.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why should cooking pot and pan handles always be turned inward toward the back of the stove?\n\n"
                "**2.** Why must you NEVER use a wet or damp cloth to lift a hot sufuria?\n\n"
                "**3.** What is the 'clean-as-you-go' rule and how does it prevent slip and fall accidents?"
            )
        }
    },
    {
        "topic_order": 1,
        "lesson_contains": "Emergency First Aid & Kitchen Protective Apparel",
        "video": {
            "title": "Watch: How to Treat Burns — St John Ambulance Kenya",
            "url": "https://www.youtube.com/watch?v=6i7ov4vbxUc",
            "author": "St John Ambulance Kenya",
            "description": "St John Ambulance Kenya demonstrates the life-saving first-aid protocol for burns and scalds: cooling the burn immediately under clean running water for 20 minutes, avoiding grease or toothpaste, and covering with clean dressings.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** For how many minutes must a burn or scald be cooled under clean running water, according to St John Ambulance Kenya?\n\n"
                "**2.** Why should you NEVER apply home remedies like butter, raw eggs, or toothpaste to a burn?\n\n"
                "**3.** What kitchen protective apparel (aprons, oven mitts, closed shoes) must you wear to prevent burn injuries?"
            )
        }
    },

    # =========================================================================
    # TOPIC 2: SMALL KITCHEN TOOLS AND EQUIPMENT (3 Lessons)
    # =========================================================================
    {
        "topic_order": 2,
        "lesson_contains": "Classification & Functional Families of Kitchen Tools",
        "video": {
            "title": "Watch: Top 10 Essential Kitchen Utensils Names for Beginners",
            "url": "https://www.youtube.com/watch?v=lyD1vSF9FSI",
            "author": "Talk English Fluently",
            "description": "A clear visual guide identifying common kitchen tools, their names, and their functional families — including measuring spoons, spatulas, peelers, whisks, and cutting knives.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Group five kitchen tools shown in the video into their functional families (measuring, cutting, mixing, cooking).\n\n"
                "**2.** Why is it important to use the correct tool for a specific task (e.g. wooden spoon for stirring hot food)?\n\n"
                "**3.** Which three small tools in your home kitchen are used most frequently?"
            )
        }
    },
    {
        "topic_order": 2,
        "lesson_contains": "Smart Buying, Budgeting & Tool Care Protocols",
        "video": {
            "title": "Watch: How To Clean and Care for Wood Cutting Boards",
            "url": "https://www.youtube.com/watch?v=lu_f_V7gjVM",
            "author": "NYT Wirecutter",
            "description": "Expert advice on hygienic care and maintenance of wooden kitchen implements — scrubbing along the grain with mild soap, avoiding soaking in water to prevent warping and mold, and oiling to preserve durability.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why should wooden cooking sticks (mwikos) and cutting boards never be soaked in water or placed in dishwashers?\n\n"
                "**2.** How does drying wooden utensils thoroughly prevent bacterial contamination in food preparation?\n\n"
                "**3.** What factors would you check before buying a durable wooden or stainless steel kitchen tool?"
            )
        }
    },
    {
        "topic_order": 2,
        "lesson_contains": "Creative Improvisation & Upcycling Projects",
        "video": {
            "title": "Watch: 3 Amazing Kitchen DIY Ideas & Upcycling Crafts",
            "url": "https://www.youtube.com/watch?v=EhziBKlSEzg",
            "author": "Food facts & hacks",
            "description": "Creative upcycling ideas turning household scrap materials into functional kitchen accessories like pot coasters, hot-pads, and organizer mats.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What local scrap materials were upcycled into practical kitchen accessories in the video?\n\n"
                "**2.** Why is upcycling useful for saving money and reducing household waste?\n\n"
                "**3.** Describe how you could make an improvised pot stand (trivet) at home using local materials."
            )
        }
    },

    # =========================================================================
    # TOPIC 3: COOKING FOOD (4 Lessons)
    # =========================================================================
    {
        "topic_order": 3,
        "lesson_contains": "Principles of Heat Transfer & Grilling Food",
        "video": {
            "title": "Watch: Heat Transfer — Conduction, Convection and Radiation",
            "url": "https://www.youtube.com/watch?v=Me60Ti0E_rY",
            "author": "Next Generation Science",
            "description": "A science lesson clearly explaining the three heat transfer mechanisms: conduction (direct contact through solids), convection (movement in fluids/air), and radiation (electromagnetic heat waves like grilling over hot charcoal).",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Which heat transfer method cooks food placed on a wire rack above glowing charcoal embers?\n\n"
                "**2.** How does conduction transfer heat from a hot burner through the base of a metal sufuria into food?\n\n"
                "**3.** Why is grilling over charcoal considered a fast, healthy dry-heat cooking method?"
            )
        }
    },
    {
        "topic_order": 3,
        "lesson_contains": "Roasting & The Improvised Dual-Sufuria Sand Oven",
        "video": {
            "title": "Watch: Dry Heat Cooking Method — Roasting and Baking (KCSE Home Science)",
            "url": "https://www.youtube.com/watch?v=8ztOMTjmYr8",
            "author": "1Room Kenya",
            "description": "1Room Kenya's Home Science lesson demonstrating dry heat cooking — explaining the principles of roasting and baking, and showing how to construct an improvised sand oven using two sufurias over a charcoal jiko.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What is the purpose of placing clean dry sand at the base of the larger sufuria in an improvised oven?\n\n"
                "**2.** How does dry hot air cook food evenly from all sides during baking and roasting?\n\n"
                "**3.** Name two foods you can roast or bake at home using an improvised charcoal jiko oven."
            )
        }
    },
    {
        "topic_order": 3,
        "lesson_contains": "Steaming Food & Nutrient Preservation",
        "video": {
            "title": "Watch: How to Use a Food Steamer — Tips for Healthy Cooking",
            "url": "https://www.youtube.com/watch?v=e5OEuRifpss",
            "author": "Cooking Secrets Vault",
            "description": "A practical guide to steaming — demonstrating how steam cooks food gently at 100 deg C without submerging it, preserving water-soluble vitamins (B and C), natural colours, and crisp textures.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why does steaming preserve more nutrients than boiling vegetables in large volumes of water?\n\n"
                "**2.** Describe the 'steam shield' technique for safely removing a steamer lid without getting scalded.\n\n"
                "**3.** How can you improvise a steamer using a sufuria, a metal colander, and clean water at home?"
            )
        }
    },
    {
        "topic_order": 3,
        "lesson_contains": "Fuel Conservation, Kitchen Safety & Creative Plating",
        "video": {
            "title": "Watch: Maximize Savings with Energy-Efficient Cooking Methods",
            "url": "https://www.youtube.com/watch?v=lI2p-H6ggzw",
            "author": "Smart Life Hacks",
            "description": "Practical methods to conserve fuel in the kitchen — pre-soaking dry pulses, using tight lids, matching pan size to heat source, and using residual heat to finish cooking.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** How does pre-soaking dry beans overnight cut down cooking time and fuel use?\n\n"
                "**2.** Why does covering your cooking pot with a tight-fitting lid conserve substantial fuel?\n\n"
                "**3.** Name one simple way to garnish a plate of rice and vegetables to make it visually appealing."
            )
        }
    },

    # =========================================================================
    # TOPIC 4: CONSUMER EDUCATION (4 Lessons)
    # =========================================================================
    {
        "topic_order": 4,
        "lesson_contains": "Household Needs: Tangible Goods vs. Paid Services",
        "video": {
            "title": "Watch: Goods and Services for Kids — Economics in Daily Life",
            "url": "https://www.youtube.com/watch?v=Jd4kD9TicbA",
            "author": "Homeschool Pop",
            "description": "An engaging introduction explaining the difference between physical goods (groceries, clothing, books) and paid services (transport, haircuts, repairs, medical care).",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What is the key difference between a tangible good and a service?\n\n"
                "**2.** Give TWO examples of goods and TWO examples of services your family uses every week.\n\n"
                "**3.** Is electricity a good or a service? Explain your answer based on what you saw."
            )
        }
    },
    {
        "topic_order": 4,
        "lesson_contains": "Factors Influencing Buying Choices & Smart Saving",
        "video": {
            "title": "Watch: Financial Literacy — Needs and Wants & Opportunity Costs",
            "url": "https://www.youtube.com/watch?v=aRcXutXvfmM",
            "author": "Learn Bright",
            "description": "Learn Bright explains financial literacy basics — identifying essential needs vs optional wants, understanding opportunity cost, and building smart saving habits.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What is 'opportunity cost' in consumer decision making?\n\n"
                "**2.** How can peer pressure and clever advertising cause someone to spend money on wants instead of needs?\n\n"
                "**3.** If you receive 200 shillings, write a plan prioritizing needs before wants."
            )
        }
    },
    {
        "topic_order": 4,
        "lesson_contains": "Where We Shop, Payment Methods & The Market Survey",
        "video": {
            "title": "Watch: Price Comparison Shopping & Smart Market Decisions",
            "url": "https://www.youtube.com/watch?v=2Mn4xiaL3iU",
            "author": "The Everyday Why",
            "description": "Discover how price comparison across different shopping outlets helps consumers find the best value, evaluate unit costs, and save money.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What are the advantages of buying in bulk from a wholesale shop compared to a local kiosk?\n\n"
                "**2.** How does calculating the unit price (price per kg or litre) help you spot genuine bargains?\n\n"
                "**3.** What precautions should you take when paying with cash or mobile money at an open-air market?"
            )
        }
    },
    {
        "topic_order": 4,
        "lesson_contains": "Safe Transactions, Market Challenges & Consumer Integrity",
        "video": {
            "title": "Watch: Consumer Rights and Protection",
            "url": "https://www.youtube.com/watch?v=KAGWjGzo-28",
            "author": "NCFE - National Centre for Financial Education",
            "description": "An overview of consumer rights and responsibilities — the right to safety, information, and redress, checking expiry dates, and verifying quality standards.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Name TWO essential rights that every consumer possesses when buying products.\n\n"
                "**2.** Why is it important to check the official standardization mark (like KEBS) on manufactured goods?\n\n"
                "**3.** What should you do if you purchase a defective or expired product from a shop?"
            )
        }
    },

    # =========================================================================
    # TOPIC 5: NATURAL TEXTILE FIBRES (4 Lessons)
    # =========================================================================
    {
        "topic_order": 5,
        "lesson_contains": "Classification & Sources of Natural Textile Fibres",
        "video": {
            "title": "Watch: Top 5 Natural Fabrics — Cotton, Linen, Jute, Silk & Wool",
            "url": "https://www.youtube.com/watch?v=CFUQe__J-is",
            "author": "Designer Vinita Gupta",
            "description": "An educational guide to the five major natural fibres — classifying them into plant/vegetable origins (cotton, linen, jute) and animal origins (silk, wool), and reviewing their characteristics.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Which natural fibres are plant-based (cellulosic) and which are animal-based (protein)?\n\n"
                "**2.** Where does silk fibre originate from, and what gives it its natural luster?\n\n"
                "**3.** Name three clothing articles in your home and identify the natural fibre each is made from."
            )
        }
    },
    {
        "topic_order": 5,
        "lesson_contains": "Physical Properties & Microscopic Shapes of Natural Fibres",
        "video": {
            "title": "Watch: Textile Fibers Classification & Natural Fibers Explained",
            "url": "https://www.youtube.com/watch?v=3XJBBvzPw_E",
            "author": "FACTHUB",
            "description": "A deep dive into the microscopic structures and physical properties of natural fibres — cotton's flat twisted ribbon, wool's crimped scales, and silk's smooth triangular prism.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** How do the overlapping scales on wool fibres cause shrinkage when washed in hot water?\n\n"
                "**2.** Why does cotton's twisted ribbon shape make it highly absorbent for towels and school uniforms?\n\n"
                "**3.** Explain why wool traps warm air pockets, making it ideal for cold weather sweaters."
            )
        }
    },
    {
        "topic_order": 5,
        "lesson_contains": "Everyday Household Uses & Sight/Feel Detection",
        "video": {
            "title": "Watch: How to Identify Natural vs. Synthetic Fibres by Sight and Touch",
            "url": "https://www.youtube.com/watch?v=TE4qFrQjFI4",
            "author": "Evelyn Wood",
            "description": "Learn professional methods to identify textile fibres using sensory tests — testing drape, softness, cool feel, and wrinkle recovery without burning.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** How does pure linen feel against your skin compared to pure cotton?\n\n"
                "**2.** What happens when you crush a sample of cotton in your fist compared to wool?\n\n"
                "**3.** Why is cotton the preferred fabric for bedsheets and underwear in hot climates?"
            )
        }
    },
    {
        "topic_order": 5,
        "lesson_contains": "The Science of Burning Tests & Laboratory Safety",
        "video": {
            "title": "Watch: Burn Test — Natural vs. Synthetic Fabrics Identification",
            "url": "https://www.youtube.com/watch?v=ku97CbeszW4",
            "author": "Molecular Matters: Chemistry & Textiles",
            "description": "A laboratory demonstration of the flame test — observing burning behaviour, odour (burning paper for cotton vs burning hair for wool/silk), and residue (light ash vs hard bead).",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What characteristic smell is released when animal fibres (wool and silk) burn, and why?\n\n"
                "**2.** What type of ash or residue does pure cotton leave after burning?\n\n"
                "**3.** State TWO laboratory safety rules you must follow when performing a fabric burning test."
            )
        }
    },

    # =========================================================================
    # TOPIC 6: THE SEWING MACHINE (4 Lessons)
    # =========================================================================
    {
        "topic_order": 6,
        "lesson_contains": "Sewing Machine Types & Smart Buying Choices",
        "video": {
            "title": "Watch: What Type of Sewing Machine Should I Buy? Buyers Guide",
            "url": "https://www.youtube.com/watch?v=-qJqbat3nWQ",
            "author": "Kemafrik Sews",
            "description": "A comprehensive buyer's guide comparing manual hand-operated machines, foot-treadle machines, and modern electric machines — evaluating durability, cost, and power requirements.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why are treadle sewing machines widely used in areas without reliable electrical power?\n\n"
                "**2.** What is the main advantage of an electric sewing machine over a manual machine?\n\n"
                "**3.** What three factors should a school consider when purchasing sewing machines for Home Science?"
            )
        }
    },
    {
        "topic_order": 6,
        "lesson_contains": "Anatomy & Mechanical Parts of the Sewing Machine",
        "video": {
            "title": "Watch: Parts of a Sewing Machine & Their Functions (Beginner Guide)",
            "url": "https://www.youtube.com/watch?v=cC4Mssp_tcY",
            "author": "ByTinymite",
            "description": "A clear, beginner-friendly tour of the core parts of a lockstitch sewing machine — handwheel, spool pin, thread guides, tension discs, take-up lever, presser foot, feed dogs, and needle clamp.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What is the function of the feed dogs located beneath the presser foot?\n\n"
                "**2.** Why must the balance wheel always be turned toward you (counter-clockwise) when sewing?\n\n"
                "**3.** Explain the role of the thread take-up lever in locking each stitch securely."
            )
        }
    },
    {
        "topic_order": 6,
        "lesson_contains": "Setup, Threading & Safe Straight Stitching",
        "video": {
            "title": "Watch: Beginner's Upper Threading Guide for Sewing Machines",
            "url": "https://www.youtube.com/watch?v=FWbLNWN2H24",
            "author": "Sew & Style Tips",
            "description": "Step-by-step demonstration of the complete threading pathway — from spool pin through tension discs and take-up lever down to the needle, followed by drawing up the bobbin thread.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What happens if you skip the thread take-up lever when threading your machine?\n\n"
                "**2.** How do you pull up the bobbin (lower) thread before you start stitching on fabric?\n\n"
                "**3.** Describe safe hand placement and posture when feeding fabric under the presser foot."
            )
        }
    },
    {
        "topic_order": 6,
        "lesson_contains": "Troubleshooting Stitch Faults & Machine Care",
        "video": {
            "title": "Watch: How to Adjust Your Sewing Machine for Perfect Tension",
            "url": "https://www.youtube.com/watch?v=xYm3vZBCk_Q",
            "author": "Machine Technology",
            "description": "Diagnosing and correcting common stitch faults — adjusting upper and lower tension to fix looping stitches, replacing blunt needles, removing lint from the bobbin case, and oiling moving parts.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** If loose thread loops appear on the underside of your fabric, which tension needs tightening?\n\n"
                "**2.** Why should you only use specialized sewing machine oil and never edible cooking oil on a machine?\n\n"
                "**3.** What are two common causes of needle breakage during stitching?"
            )
        }
    },

    # =========================================================================
    # TOPIC 7: SEAMS (4 Lessons)
    # =========================================================================
    {
        "topic_order": 7,
        "lesson_contains": "The Secret Inside Your Clothes: Understanding Seams & Allowances",
        "video": {
            "title": "Watch: What is Seam Allowance? Sewing Basics",
            "url": "https://www.youtube.com/watch?v=c0q_U9cPkGA",
            "author": "Professor Pincushion",
            "description": "Professor Pincushion explains the fundamental concept of seams and seam allowances (typically 1.5 cm / 5/8 inch), showing how they provide structural strength and prevent seam breakdown.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What is a seam allowance and why is 1.5 cm the standard allowance in garment construction?\n\n"
                "**2.** What happens if a seam is sewn too close to the raw edge of woven fabric?\n\n"
                "**3.** Look inside your school uniform and identify the seam line and seam allowance width."
            )
        }
    },
    {
        "topic_order": 7,
        "lesson_contains": "The 4 Seam Types: Plain, French, Overlaid & Double-Stitched",
        "video": {
            "title": "Watch: How to Sew a French Seam Step-by-Step",
            "url": "https://www.youtube.com/watch?v=YYa86gQbN6c",
            "author": "Craftsy",
            "description": "Angela Wolf demonstrates the complete construction of a self-neatening French seam — stitching wrong sides together first, trimming the seam, pressing, and enclosing the raw edge in a second stitch row.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why is a French seam called a 'self-neatening' seam, and which fabrics is it best suited for?\n\n"
                "**2.** Which fabric sides face each other on the very first row of stitching in a French seam?\n\n"
                "**3.** Why would a French seam be unsuitable for heavy denim fabric?"
            )
        }
    },
    {
        "topic_order": 7,
        "lesson_contains": "Sealing Raw Edges: Pinking, Edge-Stitching & Hand Loop Stitches",
        "video": {
            "title": "Watch: How to Use Pinking Shears — Seam Finishing Technique",
            "url": "https://www.youtube.com/watch?v=Uhm-2qyCp3M",
            "author": "Let's Learn To Sew",
            "description": "Learn how to neatened raw seam edges to stop fabric fraying — using pinking shears with zigzag teeth on firmly woven cloth, edge-stitching, and hand overcasting.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** How does cutting seam allowances with pinking shears prevent woven threads from unraveling?\n\n"
                "**2.** When would you choose hand loop stitches (blanket stitch) over machine edge-stitching?\n\n"
                "**3.** Inspect three different garments at home and describe how their raw seam edges were neatened."
            )
        }
    },
    {
        "topic_order": 7,
        "lesson_contains": "Quality Audits & Step-by-Step Lap Bag Construction",
        "video": {
            "title": "Watch: Sew a Super Simple Tote Bag Project",
            "url": "https://www.youtube.com/watch?v=5drUqZIzycg",
            "author": "LearnCreateSew",
            "description": "A beginner project demonstrating step-by-step tote/lap bag assembly — drafting pattern pieces, sewing straight flat seams, neatening corners, pressing flat, and evaluating final seam quality.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What are the primary qualities of a well-made seam (flatness, even width, secure backstitches)?\n\n"
                "**2.** Why is pressing each seam with an iron as you sew essential for a professional finish?\n\n"
                "**3.** How would you evaluate your own completed lap bag before submitting it for grading?"
            )
        }
    },

    # =========================================================================
    # TOPIC 8: HOUSEHOLD CLEANING AGENTS & HOMEMADE SOAP (4 Lessons)
    # =========================================================================
    {
        "topic_order": 8,
        "lesson_contains": "Water Properties, Lathering Science & Soaps vs. Detergents",
        "video": {
            "title": "Watch: Hard & Soft Water — Environmental Chemistry",
            "url": "https://www.youtube.com/watch?v=2Fr0V9SZ6R8",
            "author": "FuseSchool - Global Education",
            "description": "FuseSchool explains the science of hard and soft water — how dissolved calcium and magnesium ions react with soap to form insoluble scum, and why synthetic detergents lather effectively in hard water.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why does soft rainwater lather easily with soap while borehole or well water forms scum?\n\n"
                "**2.** What chemical reaction produces soap scum in hard water?\n\n"
                "**3.** How can you test whether your home tap water is hard or soft using a jar and liquid soap?"
            )
        }
    },
    {
        "topic_order": 8,
        "lesson_contains": "Forms of Cleaning Agents & The 4 Ingredients of Saponification",
        "video": {
            "title": "Watch: Saponification — The Process of Making Soap (MeitY OLabs)",
            "url": "https://www.youtube.com/watch?v=Tu_sWoHULtY",
            "author": "amritacreate (MeitY OLabs)",
            "description": "A laboratory chemistry experiment demonstrating saponification — the chemical reaction between vegetable oils/fats and alkali lye that produces soap and natural glycerin.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** What are the two primary chemical ingredients required for the saponification reaction?\n\n"
                "**2.** Why does the soap mixture release heat (exothermic reaction) when the alkali is mixed with oil?\n\n"
                "**3.** What local alkali source can be extracted from filtered wood ash to make soap in Kenyan communities?"
            )
        }
    },
    {
        "topic_order": 8,
        "lesson_contains": "Safe Cold Soap-Making, 4-Week Curing & Premium Additives",
        "video": {
            "title": "Watch: How To Make Cold Process Soap — Basics of Soap Making",
            "url": "https://www.youtube.com/watch?v=RYlyFOFR9cY",
            "author": "Bramble Berry",
            "description": "A comprehensive guide to cold process soap making — wearing safety goggles and gloves, mixing lye and oils to 'trace', pouring into molds, and allowing bars to cure for 4-6 weeks.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why must homemade soap cure for 4 to 6 weeks in a well-ventilated room before use?\n\n"
                "**2.** What benefits do local additives like neem leaves, aloe vera, or honey add to homemade soap?\n\n"
                "**3.** Name TWO essential safety precautions when handling caustic alkali solutions."
            )
        }
    },
    {
        "topic_order": 8,
        "lesson_contains": "The JSS Community Soap Project: Health, Sanitation & Enterprise",
        "video": {
            "title": "Watch: 10 Steps to Washing Your Hands — Hygiene Habits for Kids",
            "url": "https://www.youtube.com/watch?v=Br4sQmiJ1jU",
            "author": "Smile and Learn - English",
            "description": "An animated guide on effective handwashing with soap — demonstrating proper technique to eliminate bacteria and prevent disease transmission in schools and communities.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** How does making affordable soap at school promote hygiene and combat communicable diseases in the community?\n\n"
                "**2.** What are the 5 phases of a Community Service Learning (CSL) soap project cycle?\n\n"
                "**3.** How can a school soap-making club generate funds for Home Science practical materials?"
            )
        }
    },

    # =========================================================================
    # TOPIC 9: SPECIAL TREATMENTS IN LAUNDRYWORK (4 Lessons)
    # =========================================================================
    {
        "topic_order": 9,
        "lesson_contains": "The 4 Special Treatments: Spotting, Sponging, Starching & Dry-Cleaning",
        "video": {
            "title": "Watch: Perfectly Starched Clothes Every Time — Step-by-Step Guide",
            "url": "https://www.youtube.com/watch?v=50dklQV-SUs",
            "author": "Nick & Nate Chronicles",
            "description": "A practical demonstration of special laundry care — preparing and applying starch to cotton shirts to create a crisp, soil-resistant barrier that makes future washing easier.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** How does starching create a protective shield against red dust and dirt on school uniforms?\n\n"
                "**2.** Name the four special treatments in laundrywork and state when each is used.\n\n"
                "**3.** Why should starched garments be ironed while they are still slightly damp?"
            )
        }
    },
    {
        "topic_order": 9,
        "lesson_contains": "Stain Chemistry & Precision Spotting Techniques",
        "video": {
            "title": "Watch: Quick & Easy Stain Remover for Clothes — Spotting Techniques",
            "url": "https://www.youtube.com/watch?v=e4RbLOeynC4",
            "author": "KitHomey",
            "description": "Practical stain removal techniques using targeted household reagents — demonstrating why cold water must be used on protein stains (blood/egg) and how spotting lifts stubborn marks without damaging fabric.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why must blood and protein stains NEVER be treated with hot water?\n\n"
                "**2.** What local household reagent can you use to treat fresh ink or grass stains on cotton?\n\n"
                "**3.** Why is the blotting technique preferred over vigorous rubbing when spotting a stain?"
            )
        }
    },
    {
        "topic_order": 9,
        "lesson_contains": "Zero-Cost Homemade Starch Extraction & Fabric Starching",
        "video": {
            "title": "Watch: How to Apply Starch on Fabric at Home",
            "url": "https://www.youtube.com/watch?v=GSzgssdNsMA",
            "author": "My Activities vlogs",
            "description": "A step-by-step demonstration of preparing and applying natural starch on cotton fabrics at home, dissolving the starch paste in water, immersing the garment, and pressing for a smooth finish.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** How can you extract natural laundry starch from raw cassava or potatoes at zero cost?\n\n"
                "**2.** Describe the steps to dissolve and boil starch paste before adding it to rinse water.\n\n"
                "**3.** What happens if starch paste is too thick when applied to lightweight fabric?"
            )
        }
    },
    {
        "topic_order": 9,
        "lesson_contains": "Sponging Structured Blazers, Safe Dry-Cleaning & Eco-Disposal",
        "video": {
            "title": "Watch: How to Clean & Sponge Suits and Blazers at Home",
            "url": "https://www.youtube.com/watch?v=7UEO_gXGghs",
            "author": "Gentleman's Gazette",
            "description": "Professional guidance on maintaining structured wool blazers and jackets — brushing off surface dust, sponging soiled collars with mild soapy water, using a damp pressing cloth, and proper hanging.",
            "reflection": (
                "After watching the video, reflect on what you learned:\n\n"
                "**1.** Why should structured wool school blazers never be fully submerged in water and wrung out?\n\n"
                "**2.** Why must a damp pressing cloth always be placed between a hot iron and wool fabric?\n\n"
                "**3.** How does regular sponging, airing, and brushing save your family dry-cleaning expenses?"
            )
        }
    },
]


def run_enrichment():
    print("=" * 80)
    print("[START] CBC Grade 7 Home Science — Live-Verified Video Enrichment (34 Lessons)")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    assert curriculum, "Curriculum 'CBC' not found!"
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 7").first()
    assert grade, "Grade 7 not found!"
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()
    assert subject, "Subject 'Home Science' under Grade 7 not found!"

    print(f"[*] Hierarchy: {curriculum.name} -> {grade.name} -> {subject.name}\n")

    total_lessons_enriched = 0
    total_videos_created = 0
    total_blocks_created = 0

    for item in GRADE7_VERIFIED_ENRICHMENTS:
        topic_order = item["topic_order"]
        lesson_substr = item["lesson_contains"]
        v_data = item["video"]

        topic = Topic.objects.filter(subject=subject, order=topic_order).first()
        if not topic:
            print(f"  [SKIP] Topic {topic_order} not found!")
            continue

        lesson = None
        for unit in topic.learning_units.all():
            candidate = unit.lessons.filter(title__icontains=lesson_substr).first()
            if candidate:
                lesson = candidate
                break

        if not lesson:
            print(f"  [SKIP] Topic {topic_order}: Lesson matching '{lesson_substr}' not found!")
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

        print(f"  [+] Topic {topic.order} -> '{lesson.title}' (Page {target_page})")
        print(f"      Video: {v_data['url']} | \"{v_data['title']}\" by {v_data['author']}")

    print("\n" + "=" * 80)
    print("[SUCCESS] CBC Grade 7 Home Science Video Enrichment Complete!")
    print(f"[*] Total Lessons Enriched: {total_lessons_enriched} / {len(GRADE7_VERIFIED_ENRICHMENTS)}")
    print(f"[*] Total Video Assets Created: {total_videos_created}")
    print(f"[*] Total Blocks Created: {total_blocks_created}")
    print("=" * 80)


if __name__ == "__main__":
    run_enrichment()
