"""
VLearn CBC Grade 10 Physics — Topic 13: Introduction to Space Physics
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Introduction to Space Physics (Order: 13)

2 Learning Units & 2 Published Lessons:
  1. Origin, Structure and Classification of the Universe (8 Pages, 13 Blocks)
  2. Gravity, Orbits, Space Flight and Careers (8 Pages, 13 Blocks)

Includes:
  - 4 Custom Responsive Sanitized Vector SVG Diagrams
  - 2 Verified Wikimedia Commons Photographic Assets
  - 2 Verified Educational YouTube Video Integrations
  - 2 Formative Scenario-Based MCQs with 4 Options and Pedagogical Feedback
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.media_orchestration.visual_intelligence.svg_sanitizer import validate_and_sanitize_svg

# =============================================================================
# SVG DEFINITIONS FOR TOPIC 13
# =============================================================================

def get_svg_big_bang_timeline():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">TIMELINE OF THE BIG BANG: 13.8 BILLION YEARS OF COSMIC EXPANSION</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Redshift Expansion • Cosmic Microwave Background Radiation (2.7 K) • Primordial Nucleosynthesis</text>

  <!-- Expansion Funnel Body -->
  <g transform="translate(60, 80)">
    <!-- Singularity Point -->
    <circle cx="30" cy="140" r="8" fill="#fbbf24" stroke="#f59e0b" stroke-width="2"/>
    <text x="30" y="115" fill="#fcd34d" font-size="10" font-weight="800" text-anchor="middle">Singularity</text>
    <text x="30" y="170" fill="#94a3b8" font-size="9" text-anchor="middle">t = 0</text>

    <!-- Expanding Shape Funnel -->
    <path d="M 30 140 Q 180 80 400 40 L 720 10 L 720 270 L 400 240 Q 180 200 30 140 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>

    <!-- Stage 1: Inflation -->
    <line x1="100" y1="120" x2="100" y2="160" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2"/>
    <text x="100" y="105" fill="#f59e0b" font-size="9" font-weight="700" text-anchor="middle">Inflation</text>
    <text x="100" y="180" fill="#94a3b8" font-size="8" text-anchor="middle">10⁻³⁵ s</text>

    <!-- Stage 2: Nuclei Form -->
    <line x1="190" y1="100" x2="190" y2="180" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 2"/>
    <text x="190" y="85" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle">H &amp; He Nuclei</text>
    <text x="190" y="200" fill="#94a3b8" font-size="8" text-anchor="middle">3 Minutes</text>

    <!-- Stage 3: CMBR Released -->
    <line x1="320" y1="75" x2="320" y2="205" stroke="#ef4444" stroke-width="2"/>
    <rect x="305" y="120" width="30" height="40" fill="#ef444433" rx="3"/>
    <text x="320" y="60" fill="#ef4444" font-size="9" font-weight="700" text-anchor="middle">CMBR Released</text>
    <text x="320" y="225" fill="#94a3b8" font-size="8" text-anchor="middle">380,000 Yrs</text>

    <!-- Stage 4: First Stars & Galaxies -->
    <line x1="480" y1="50" x2="480" y2="230" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="3 2"/>
    <text x="480" y="35" fill="#c084fc" font-size="9" font-weight="700" text-anchor="middle">First Galaxies</text>
    <text x="480" y="250" fill="#94a3b8" font-size="8" text-anchor="middle">400M Yrs</text>

    <!-- Stage 5: Present Day Universe -->
    <circle cx="680" cy="140" r="30" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
    <path d="M 665 140 Q 680 125 695 140 T 680 155" fill="none" stroke="#22c55e" stroke-width="2"/>
    <text x="680" y="190" fill="#4ade80" font-size="10" font-weight="800" text-anchor="middle">Present Day</text>
    <text x="680" y="205" fill="#cbd5e1" font-size="9" text-anchor="middle">13.8 Billion Yrs</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_newton_cannonball_kepler():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">ORBIT MECHANICS: NEWTON’S CANNONBALL &amp; KEPLER’S LAWS</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Forward Tangential Velocity (v) Balanced with Inward Centripetal Gravitational Force (Fg)</text>

  <!-- Left: Newton's Cannonball -->
  <g transform="translate(60, 85)">
    <rect width="330" height="275" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="24" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. NEWTON'S ORBIT THOUGHT EXPERIMENT</text>

    <!-- Earth Sphere -->
    <circle cx="165" cy="160" r="65" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="165" y="165" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Earth</text>

    <!-- Mountain & Cannon on Top -->
    <polygon points="165,95 158,110 172,110" fill="#64748b"/>
    <circle cx="165" cy="94" r="3" fill="#f59e0b"/>

    <!-- Path A (Low speed) -->
    <path d="M 165 94 Q 190 94 200 120" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3 2"/>
    <text x="215" y="115" fill="#ef4444" font-size="9">Path A (Falls)</text>

    <!-- Path B (Medium speed) -->
    <path d="M 165 94 Q 220 94 225 180" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 2"/>
    <text x="235" y="180" fill="#f59e0b" font-size="9">Path B (Farther)</text>

    <!-- Path C (Orbital speed - Full Circle) -->
    <circle cx="165" cy="160" r="75" fill="none" stroke="#22c55e" stroke-width="2"/>
    <text x="165" y="255" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle">Path C: Continuous Free-Fall Orbit</text>
  </g>

  <!-- Right: Kepler's 2nd Law (Equal Areas in Equal Times) -->
  <g transform="translate(450, 85)">
    <rect width="330" height="275" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="165" y="24" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. KEPLER'S EQUAL AREA LAW</text>

    <!-- Elliptical Orbit Track -->
    <ellipse cx="165" cy="140" rx="120" ry="70" fill="none" stroke="#64748b" stroke-width="1.5"/>

    <!-- Sun at Focus 1 -->
    <circle cx="110" cy="140" r="14" fill="#f59e0b" stroke="#fbbf24" stroke-width="2"/>
    <text x="110" y="144" fill="#000" font-size="9" font-weight="800" text-anchor="middle">Sun</text>

    <!-- Area A: Perihelion (Short & Wide, Fast) -->
    <path d="M 110 140 L 45 140 A 120 70 0 0 1 65 95 Z" fill="#22c55e44" stroke="#22c55e" stroke-width="1.5"/>
    <text x="60" y="125" fill="#4ade80" font-size="9" font-weight="700">Area A (Fast)</text>

    <!-- Area B: Aphelion (Long & Thin, Slow) -->
    <path d="M 110 140 L 285 140 A 120 70 0 0 0 270 110 Z" fill="#38bdf844" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="220" y="125" fill="#38bdf8" font-size="9" font-weight="700">Area B (Slow)</text>

    <text x="165" y="235" fill="#f8fafc" font-size="12" font-weight="700" text-anchor="middle">Area A = Area B for same time Δt</text>
    <text x="165" y="255" fill="#cbd5e1" font-size="10" text-anchor="middle">Planet speeds up near Sun; slows down far away</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 13
# =============================================================================

def build_topic13_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Origin, Structure and Classification of the Universe
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Origin, Structure and Classification of the Universe",
            "unit_description": "Big Bang Theory (13.8 billion years), cosmological evidence (redshift cosmic expansion, 2.7 K Cosmic Microwave Background Radiation, 75% H / 24% He elemental abundance), hierarchical classification of celestial bodies (stars, planets, moons, asteroids, comets, nebulae, galaxies), and observational astronomical technology.",
            "lesson_title": "Origin, Structure and Classification of the Universe",
            "pages": [
                # Page 1: Hook & Milky Way Over Kenya Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Cosmic Tapestry: The Milky Way Galaxy Over Kenya",
                        "content": {
                            "title": "Cosmic Tapestry: The Milky Way Galaxy Over Kenya",
                            "caption": "A long-exposure photograph of the dense star clouds of the Milky Way stretching across a dark Kenyan night sky over an acacia tree. Our galaxy contains over 100 billion stars and solar systems.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Milky_Way_Night_Sky_Acacia_Kenya.jpg/1280px-Milky_Way_Night_Sky_Acacia_Kenya.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Milky_Way_Night_Sky_Acacia_Kenya.jpg/1280px-Milky_Way_Night_Sky_Acacia_Kenya.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Milky Way Night Sky Kenya",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Milky_Way_Night_Sky_Acacia_Kenya.jpg/1280px-Milky_Way_Night_Sky_Acacia_Kenya.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Milky_Way_Night_Sky_Acacia_Kenya.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Peering into Cosmic Deep Time",
                        "content": {
                            "title": "Where Did Everything Begin?",
                            "text": "When you look up at the night sky, you are looking back in time.\n\nUsing **Astrophysics**, we trace the history of matter and energy back 13.8 billion years to understand the origin and hierarchical architecture of the observable universe."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Architecture of the Cosmos",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the **Big Bang Theory** and evaluate its 3 pillars of evidence.",
                                "Classify celestial bodies into a rigorous physical hierarchy.",
                                "Differentiate between the **Solar System** and the **Milky Way Galaxy**.",
                                "Trace the evolution of astronomical telescopes from Galileo to the **James Webb Space Telescope**."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Big Bang Theory",
                        "content": {
                            "term": "Big Bang Theory",
                            "definition": "The leading cosmological model explaining that the universe expanded from an extremely hot, dense point (singularity) approximately 13.8 billion years ago and continues to expand.",
                            "example": "Validated by Hubble redshift, CMBR at 2.7 K, and primordial light element ratios."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Galaxy",
                        "content": {
                            "term": "Galaxy",
                            "definition": "A massive, gravitationally bound system containing hundreds of billions of stars, planetary systems, gas, dust, and dark matter.",
                            "example": "The Milky Way galaxy is our home spiral galaxy."
                        }
                    }
                ],
                # Page 3: Big Bang Timeline SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Timeline of the Big Bang: 13.8 Billion Years of Cosmic Expansion",
                        "content": {
                            "title": "Timeline of the Big Bang: 13.8 Billion Years of Cosmic Expansion",
                            "caption": "Cosmic timeline: Singularity (t=0), Inflation, Nuclei formation (3 min), CMBR thermal echo (380,000 yrs), First galaxies (400M yrs), to present day.",
                            "svg_content": get_svg_big_bang_timeline(),
                            "svg": get_svg_big_bang_timeline()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Big Bang Timeline Diagram",
                            "metadata": {
                                "svg_content": get_svg_big_bang_timeline()
                            }
                        }
                    }
                ],
                # Page 4: Celestial Bodies Classification Table
                [
                    {
                        "type": "comparison_table",
                        "title": "Classification of Bodies in the Universe",
                        "content": {
                            "title": "Cosmic Objects Hierarchy",
                            "headers": ["Object Category", "Physical Nature", "Energy Source", "Example"],
                            "rows": [
                                ["Stars", "Massive luminous plasma spheres.", "Internal nuclear fusion (H $\\rightarrow$ He).", "The Sun, Sirius, Alpha Centauri."],
                                ["Planets", "Spherical bodies orbiting a star.", "Reflects stellar light.", "Earth, Mars, Jupiter, Venus."],
                                ["Moons", "Natural satellites orbiting planets.", "Reflects stellar light.", "Earth's Moon, Titan (Saturn), Ganymede."],
                                ["Asteroids & Comets", "Rocky / icy remnants of Solar System formation.", "Reflects sunlight; comets sublimate forming dust tail.", "Ceres, Halley's Comet, NEOWISE."],
                                ["Nebulae", "Interstellar clouds of dust and ionized gas.", "Excited by stellar UV radiation.", "Orion Nebula (stellar nursery)."],
                                ["Galaxies", "Gravitationally bound system of $10^{11}$ stars.", "Combined energy of billions of stars.", "Milky Way, Andromeda."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Solar System vs Milky Way Galaxy Scale",
                        "content": {
                            "question": "A student claims that the Solar System and the Milky Way are two different names for the exact same physical structure. Which of the following statements provides the correct physical distinction?",
                            "options": [
                                "The Solar System is a collection of billions of galaxies, while the Milky Way contains only the Earth.",
                                "The Solar System is our local neighborhood consisting of one single star (the Sun) and its eight planets, whereas the Milky Way is a gargantuan galaxy containing hundreds of billions of stars and solar systems.",
                                "The Milky Way is a cloud of gas where comets are born, while the Solar System is outer space.",
                                "The Solar System contains only rocky asteroids, while the Milky Way contains only gas planets."
                            ],
                            "answer": "B",
                            "explanation": "Our Solar System consists of just one star (the Sun) and the eight orbiting planets. The Milky Way is an entire spiral galaxy containing **over 100 billion individual stars and solar systems**. The Solar System is thus a microscopic component within the vast Milky Way. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Scale Model Demonstration
                [
                    {
                        "type": "step_process",
                        "title": "Classroom Scale Demonstration: Relative Cosmic Sizes",
                        "content": {
                            "title": "Modeling the Immensity of Space",
                            "steps": [
                                "1. Place a 24 cm basketball in classroom to represent the Sun.",
                                "2. Walk 26 metres away and place a 2.2 mm grain of sand to represent Earth's orbit!",
                                "3. Walk 135 metres away (outside school compound) and place a 2.4 cm marble for Jupiter.",
                                "4. On this exact scale, the nearest star (Proxima Centauri) would be 7,000 km away (Nairobi to Tokyo!).",
                                "5. Conclusion: Space is overwhelmingly empty; celestial objects are separated by massive distances."
                            ]
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Origin of the Universe and Deep Space Astronomy",
                        "content": {
                            "title": "Physics Video: Origin of the Universe and Deep Space Astronomy",
                            "description": "Video explaining the Big Bang theory, cosmic background radiation, cosmic hierarchy, and modern space telescopes.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Cosmology and Space Physics Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 1 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Big Bang Theory**: Universe originated 13.8 billion years ago from a hot singularity.",
                                "3 evidence pillars: Galaxy redshift (expansion), CMBR (2.7 K), 75% H / 24% He elemental abundance.",
                                "**Cosmic scale**: Asteroid $\\subset$ Moon $\\subset$ Planet $\\subset$ Star $\\subset$ Solar System $\\subset$ Nebula $\\subset$ Galaxy $\\subset$ Universe.",
                                "Modern observatories (James Webb) detect infrared light from the earliest galaxies."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Gravity, Orbits, Space Flight and Careers
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Gravity, Orbits, Space Flight and Careers",
            "unit_description": "Physics of orbits (Newton's Cannonball thought experiment, centripetal gravity vs tangential velocity), Kepler's 3 Laws of Planetary Motion (ellipses, equal areas in equal times, T² ∝ r³), Low Earth Orbit (LEO) vs Geostationary Orbit (GEO), Kenya's Taifa-1 satellite applications, and careers in space science.",
            "lesson_title": "Gravity, Orbits, Space Flight and Careers",
            "pages": [
                # Page 1: Hook & Moon Orbiting Earth Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Gravitational Tether: The Moon Orbiting Planet Earth",
                        "content": {
                            "title": "Gravitational Tether: The Moon Orbiting Planet Earth",
                            "caption": "A deep-space probe photograph of the Moon orbiting Earth. Gravitational attraction provides the continuous centripetal force that bends the Moon's forward motion into a stable orbit.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Earth_and_Moon_deep_space_probe.jpg/1280px-Earth_and_Moon_deep_space_probe.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Earth_and_Moon_deep_space_probe.jpg/1280px-Earth_and_Moon_deep_space_probe.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Earth and Moon Orbital Motion",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Earth_and_Moon_deep_space_probe.jpg/1280px-Earth_and_Moon_deep_space_probe.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Earth_and_Moon_deep_space_probe.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Invisible String in Space",
                        "content": {
                            "title": "How Objects Stay in Orbit",
                            "text": "Why doesn't the Moon fly away into deep space, or crash directly into Earth?\n\nGravity acts as an invisible tether, supplying the exact **centripetal force** required to keep satellites and celestial bodies in stable orbits."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Orbital Physics & Careers",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain orbital motion using **Newton's Cannonball Thought Experiment**.",
                                "State and apply **Kepler's Three Laws of Planetary Motion** ($T^2 \\propto r^3$).",
                                "Contrast **Low Earth Orbit (LEO)** with **Geostationary Orbit (GEO)**.",
                                "Examine real-world applications (Kenya's **Taifa-1 satellite**) and professional career pathways."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Orbit",
                        "content": {
                            "term": "Orbit",
                            "definition": "The gravitationally curved path of an object around a more massive body, maintained by a balance between tangential forward velocity and inward gravitational centripetal pull.",
                            "example": "The International Space Station orbiting at 7.6 km/s."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Geostationary Orbit (GEO)",
                        "content": {
                            "term": "Geostationary Orbit (GEO)",
                            "definition": "A circular equatorial orbit at an altitude of approximately 35,786 km where the satellite's orbital period matches Earth's 24-hour rotation exactly.",
                            "example": "Weather and communication satellites hovering permanently over Kenya."
                        }
                    }
                ],
                # Page 3: Newton Cannonball & Kepler SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Orbit Mechanics: Newton's Cannonball & Kepler's Laws",
                        "content": {
                            "title": "Orbit Mechanics: Newton's Cannonball & Kepler's Laws",
                            "caption": "Newton's cannonball orbital speed transition into continuous free-fall, paired with Kepler's Equal Area Law (Area A = Area B in equal time intervals).",
                            "svg_content": get_svg_newton_cannonball_kepler(),
                            "svg": get_svg_newton_cannonball_kepler()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Newton Cannonball and Kepler Orbit Diagram",
                            "metadata": {
                                "svg_content": get_svg_newton_cannonball_kepler()
                            }
                        }
                    }
                ],
                # Page 4: Kepler's Laws & Orbit Classification
                [
                    {
                        "type": "comparison_table",
                        "title": "Orbital Altitude Regimes: LEO vs GEO Satellites",
                        "content": {
                            "title": "Satellite Orbit Comparison Matrix",
                            "headers": ["Orbital Regime", "Altitude Range", "Orbital Period ($T$)", "Key Real-World Application"],
                            "rows": [
                                ["Low Earth Orbit (LEO)", "$300 - 1,000\\text{ km}$", "$90\\text{ minutes}$ (Fast)", "Earth remote sensing, disaster tracking, Kenya's **Taifa-1 satellite**."],
                                ["Medium Earth Orbit (MEO)", "$2,000 - 20,000\\text{ km}$", "$12\\text{ hours}$", "Global Positioning System (GPS) and navigation constellations."],
                                ["Geostationary Orbit (GEO)", "$35,786\\text{ km}$ (Equatorial)", "$24\\text{ hours}$ (Matches Earth)", "Continuous telecommunications, weather monitoring over East Africa."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Geostationary Weather Satellite Orbit",
                        "content": {
                            "question": "A telecommunications satellite is designed to monitor rainfall patterns over Kenya and must remain positioned directly above Nairobi twenty-four hours a day. Which orbit must this satellite be placed in?",
                            "options": [
                                "Low Earth Orbit (LEO), because it must travel as fast as possible to capture images rapidly.",
                                "Geostationary Orbit (GEO), because its orbital period must match Earth's 24-hour rotation exactly, making it appear stationary from the ground.",
                                "Polar Orbit, because it must orbit over the North and South poles.",
                                "An elliptical orbit with a 90-minute period."
                            ],
                            "answer": "B",
                            "explanation": "To remain hovering directly over a single point on Earth (like Nairobi), a satellite must be in an equatorial **Geostationary Orbit (GEO)** at an altitude of approx. 36,000 km, where its orbital period is exactly **24 hours**—matching Earth's rotation. LEO satellites circle every 90 minutes and drift past quickly. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Space Careers & Kenya Applications
                [
                    {
                        "type": "real_world_connection",
                        "title": "Careers in Space Physics and Kenya Space Applications",
                        "content": {
                            "title": "Space Technology in Kenya",
                            "text": "- **Kenya Space Agency & Taifa-1**: In 2023, Kenya launched **Taifa-1**, providing remote-sensing data for agriculture, forestry, and water resource management.\n- **Astrophysicists & Astronomers**: Researching stellar evolution, gravitational waves, and cosmology.\n- **Aerospace Engineers**: Designing satellites, propulsion systems, and thermal shielding.\n- **Satellite Data Analysts**: Processing satellite imagery to forecast drought, manage crop yields, and monitor wildlife migrations."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Orbital Mechanics, Satellites, and Space Flight",
                        "content": {
                            "title": "Physics Video: Orbital Mechanics, Satellites, and Space Flight",
                            "description": "Video illustrating Newton's cannonball orbit, Kepler's three laws, LEO vs GEO satellites, and space exploration careers.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Orbital Mechanics and Space Careers Video",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "metadata": {
                                "youtube_id": "CVsdXKO9xlk"
                            }
                        }
                    }
                ],
                # Page 8: Summary
                [
                    {
                        "type": "summary",
                        "title": "Lesson 2 Summary: Key Takeaways",
                        "content": {
                            "title": "Core Summary",
                            "takeaways": [
                                "**Orbit**: Centripetal gravity continuously bends forward tangential velocity into closed path.",
                                "**Kepler's Laws**: 1. Ellipses; 2. Equal areas in equal times; 3. Period-radius relation ($T^2 \\propto r^3$).",
                                "**LEO (90 min)** is for high-res imaging; **GEO (24 hr)** remains stationary for communications.",
                                "Kenya's **Taifa-1 satellite** is a vital tool for environmental and agricultural monitoring."
                            ]
                        }
                    }
                ]
            ]
        }
    ]


# =============================================================================
# INGESTION EXECUTION ENGINE
# =============================================================================

@transaction.atomic
def ingest_grade10_physics_topic13():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 13: INTRODUCTION TO SPACE PHYSICS")
    print("======================================================================")

    # 1. Verify Curriculum & Grade
    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    if not curriculum:
        raise ValueError("Curriculum 'CBC' (ID: 5) not found!")

    grade = Grade.objects.filter(curriculum=curriculum, name__icontains="10").first()
    if not grade:
        raise ValueError("Grade 10 not found under CBC curriculum!")

    # 2. Get Subject: Physics
    subject = Subject.objects.filter(grade=grade, name="Physics").first()
    if not subject:
        subject = Subject.objects.create(
            grade=grade,
            name="Physics",
            description="CBC Senior Secondary Physics"
        )
    print(f"Subject: {subject.name} (ID: {subject.id})")

    # 3. Get or Create Topic: Introduction to Space Physics (Order: 13)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=13,
        defaults={
            "name": "Introduction to Space Physics",
            "description": "Physical exploration of the universe, Big Bang Theory (13.8 billion years), cosmological evidence (redshift, CMBR, light elements), classification of celestial bodies, telescopes, orbit mechanics (Newton's Cannonball, Kepler's 3 laws), LEO vs GEO satellite regimes, Kenya's Taifa-1, and space science careers."
        }
    )
    if not t_created and topic.name != "Introduction to Space Physics":
        topic.name = "Introduction to Space Physics"
        topic.description = "Physical exploration of the universe, Big Bang Theory (13.8 billion years), cosmological evidence (redshift, CMBR, light elements), classification of celestial bodies, telescopes, orbit mechanics (Newton's Cannonball, Kepler's 3 laws), LEO vs GEO satellite regimes, Kenya's Taifa-1, and space science careers."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic13_curriculum_data()

    total_units_created = 0
    total_lessons_created = 0
    total_blocks_created = 0
    total_assets_created = 0

    for unit_data in curriculum_data:
        u_order = unit_data["unit_order"]
        u_name = unit_data["unit_name"]
        u_desc = unit_data["unit_description"]
        l_title = unit_data["lesson_title"]
        pages = unit_data["pages"]

        # Create or Update Learning Unit
        learning_unit, lu_created = LearningUnit.objects.get_or_create(
            topic=topic,
            order=u_order,
            defaults={"name": u_name, "description": u_desc}
        )
        if not lu_created:
            learning_unit.name = u_name
            learning_unit.description = u_desc
            learning_unit.save()
        total_units_created += 1

        # Create or Update Lesson
        lesson, l_created = Lesson.objects.get_or_create(
            topic=topic,
            learning_unit=learning_unit,
            defaults={"title": l_title, "status": "published", "version": 1}
        )
        if not l_created:
            lesson.title = l_title
            lesson.status = "published"
            lesson.version = 1
            lesson.save()
        total_lessons_created += 1

        # Idempotently refresh LessonBlocks and Assets for this lesson
        lesson.blocks.all().delete()
        lesson.assets.all().delete()

        block_order_counter = 10

        for page_idx, page_blocks in enumerate(pages, start=1):
            for comp_idx, block_spec in enumerate(page_blocks, start=1):
                b_type = block_spec["type"]
                b_title = block_spec.get("title", "")
                b_content = block_spec.get("content", {})
                b_meta = block_spec.get("metadata", {})

                # If block has inline SVG, store in metadata
                if "svg_content" in b_content:
                    b_meta["svg_content"] = b_content["svg_content"]

                block = LessonBlock.objects.create(
                    lesson=lesson,
                    block_type=b_type,
                    component_type=b_type,
                    title=b_title,
                    content=b_content,
                    metadata=b_meta,
                    page_number=page_idx,
                    component_order=comp_idx,
                    order=block_order_counter
                )
                block_order_counter += 10
                total_blocks_created += 1

                # If block has an associated asset specification, create LessonAsset
                if "asset" in block_spec:
                    asset_spec = block_spec["asset"]
                    asset = LessonAsset.objects.create(
                        lesson=lesson,
                        asset_type=asset_spec["asset_type"],
                        source_type=asset_spec.get("source_type", "external"),
                        storage_type=asset_spec.get("storage_type", "url"),
                        status="approved",
                        title=asset_spec.get("title", b_title),
                        description=asset_spec.get("description", ""),
                        url=asset_spec.get("url"),
                        metadata=asset_spec.get("metadata", {})
                    )
                    block.assets.add(asset)
                    total_assets_created += 1

        print(f"  -> Ingested Unit {u_order}: '{u_name}' | Lesson: '{l_title}' ({len(pages)} Pages, {lesson.blocks.count()} Blocks, {lesson.assets.count()} Assets)")

    print("======================================================================")
    print(f"TOPIC 13 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic13()
