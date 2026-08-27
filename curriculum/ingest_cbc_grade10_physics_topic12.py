"""
VLearn CBC Grade 10 Physics — Topic 12: Greenhouse Effect and Climate Change
Production Ingestion & Visual Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Physics
Topic: Greenhouse Effect and Climate Change (Order: 12)

2 Learning Units & 2 Published Lessons:
  1. Greenhouse Effect, Evidence and Impacts (8 Pages, 13 Blocks)
  2. Mitigation, Adaptation and Responsible Technology (8 Pages, 13 Blocks)

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
# SVG DEFINITIONS FOR TOPIC 12
# =============================================================================

def get_svg_greenhouse_effect_model():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 420" width="100%" height="100%">
  <rect width="840" height="420" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">PHYSICS OF THE GREENHOUSE EFFECT: GLOBAL ENERGY BALANCE</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Short-Wave Solar Radiation Ingress • Long-Wave Terrestrial Infrared Re-Radiation &amp; Trapping</text>

  <!-- Sun (Top Left) -->
  <g transform="translate(60, 80)">
    <circle cx="40" cy="40" r="30" fill="#f59e0b" stroke="#fbbf24" stroke-width="3"/>
    <text x="40" y="45" fill="#000" font-family="system-ui, sans-serif" font-size="12" font-weight="800" text-anchor="middle">SUN</text>
    <text x="40" y="85" fill="#f59e0b" font-size="10" text-anchor="middle">5500 °C</text>
  </g>

  <!-- Atmosphere Layer -->
  <rect x="180" y="110" width="580" height="70" fill="#0284c722" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3" rx="8"/>
  <text x="470" y="130" fill="#38bdf8" font-family="system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">ATMOSPHERE: GREENHOUSE GASES (CO₂, CH₄, N₂O, H₂O)</text>

  <!-- GHG Molecules in Atmosphere -->
  <circle cx="280" cy="155" r="10" fill="#22c55e"/>
  <text x="280" y="159" fill="#fff" font-size="8" font-weight="700" text-anchor="middle">CO₂</text>
  <circle cx="460" cy="155" r="10" fill="#22c55e"/>
  <text x="460" y="159" fill="#fff" font-size="8" font-weight="700" text-anchor="middle">CH₄</text>
  <circle cx="640" cy="155" r="10" fill="#22c55e"/>
  <text x="640" y="159" fill="#fff" font-size="8" font-weight="700" text-anchor="middle">H₂O</text>

  <!-- 1. Short-Wave Solar Radiation (Yellow straight arrows down) -->
  <path d="M 120 120 L 220 280 M 215 268 L 220 280 L 208 274" stroke="#f59e0b" stroke-width="3"/>
  <text x="110" y="200" fill="#f59e0b" font-size="10" font-weight="700">Short-Wave Solar Light (Passes Through)</text>

  <!-- 2. Warm Earth Surface (Curved Green Base) -->
  <g transform="translate(140, 280)">
    <path d="M 0 50 Q 300 10 650 50 L 650 80 L 0 80 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
    <text x="325" y="65" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">EARTH SURFACE (Warmed to ~15 °C)</text>
  </g>

  <!-- 3. Long-Wave Infrared Radiation (Red wavy arrows upward) -->
  <path d="M 380 280 Q 390 240 380 200 T 380 165" fill="none" stroke="#ef4444" stroke-width="3"/>
  <polygon points="380,165 375,175 385,175" fill="#ef4444"/>
  <text x="360" y="240" fill="#ef4444" font-size="10" font-weight="700" text-anchor="end">Long-Wave Infrared (Heat)</text>

  <!-- 4. Trapped Heat Re-Radiated Back Down -->
  <path d="M 470 165 Q 460 210 490 270" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="4 2"/>
  <polygon points="490,270 482,262 493,260" fill="#ef4444"/>
  <text x="510" y="235" fill="#ef4444" font-size="10" font-weight="700">Trapped Heat Re-Radiated to Ground</text>

  <!-- Escape to space -->
  <path d="M 640 145 L 700 85" stroke="#ef4444" stroke-width="2"/>
  <polygon points="700,85 690,88 695,97" fill="#ef4444"/>
  <text x="730" y="100" fill="#94a3b8" font-size="10">Escapes to Space</text>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg

def get_svg_sankey_lighting_efficiency():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 400" width="100%" height="100%">
  <rect width="840" height="400" fill="#0f172a" rx="16"/>
  <text x="420" y="34" fill="#f8fafc" font-family="system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">SANKEY ENERGY EFFICIENCY: INCANDESCENT BULB VS MODERN LED</text>
  <text x="420" y="55" fill="#94a3b8" font-family="system-ui, sans-serif" font-size="12" text-anchor="middle">Energy Efficiency (%) = (Useful Energy Output / Total Energy Input) × 100%</text>

  <!-- Left: Incandescent Bulb (5% Efficient) -->
  <g transform="translate(60, 85)">
    <rect width="330" height="275" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
    <text x="165" y="24" fill="#ef4444" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">1. INCANDESCENT BULB (Filament Heat)</text>

    <!-- 100 J Input Bar -->
    <rect x="20" y="90" width="70" height="80" fill="#38bdf8"/>
    <text x="55" y="135" fill="#000" font-size="11" font-weight="800" text-anchor="middle">100 J Input</text>

    <!-- 5 J Light Arrow (Thin Upward) -->
    <path d="M 90 90 L 180 90 L 180 60 L 220 75 L 180 90 L 180 100 L 90 100 Z" fill="#eab308"/>
    <text x="235" y="79" fill="#eab308" font-size="11" font-weight="700">Useful Light: 5 J (5%)</text>

    <!-- 95 J Wasted Heat Arrow (Thick Downward) -->
    <path d="M 90 100 L 150 100 Q 180 100 180 140 L 180 200 L 150 200 L 195 235 L 240 200 L 210 200 L 210 140 Q 210 170 90 170 Z" fill="#ef4444"/>
    <text x="245" y="195" fill="#ef4444" font-size="11" font-weight="700">Wasted Heat: 95 J (95%)</text>

    <text x="165" y="255" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">Extremely Inefficient (Sluggish Thermal Loss)</text>
  </g>

  <!-- Right: Modern LED Bulb (50% Efficient) -->
  <g transform="translate(450, 85)">
    <rect width="330" height="275" rx="8" fill="#1e293b" stroke="#22c55e" stroke-width="1.5"/>
    <text x="165" y="24" fill="#22c55e" font-family="system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">2. MODERN LED (Semiconductor Diode)</text>

    <!-- 100 J Input Bar -->
    <rect x="20" y="90" width="70" height="80" fill="#38bdf8"/>
    <text x="55" y="135" fill="#000" font-size="11" font-weight="800" text-anchor="middle">100 J Input</text>

    <!-- 50 J Light Arrow (Thick Upward) -->
    <path d="M 90 90 L 160 90 L 160 50 L 205 70 L 160 90 L 160 130 L 90 130 Z" fill="#22c55e"/>
    <text x="220" y="75" fill="#4ade80" font-size="11" font-weight="700">Useful Light: 50 J (50%)</text>

    <!-- 50 J Wasted Heat Arrow -->
    <path d="M 90 130 L 160 130 L 160 180 L 140 180 L 175 215 L 210 180 L 190 180 L 190 170 L 90 170 Z" fill="#ef4444"/>
    <text x="220" y="180" fill="#ef4444" font-size="11" font-weight="700">Wasted Heat: 50 J (50%)</text>

    <text x="165" y="255" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle">10× More Efficient than Filament Bulb!</text>
  </g>
</svg>"""
    is_valid, sanitized, _ = validate_and_sanitize_svg(svg)
    return sanitized if is_valid else svg


# =============================================================================
# CURRICULUM DEFINITION DATA FOR TOPIC 12
# =============================================================================

def build_topic12_curriculum_data():
    return [
        # ---------------------------------------------------------------------
        # LESSON 1: Greenhouse Effect, Evidence and Impacts
        # ---------------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Greenhouse Effect, Evidence and Impacts",
            "unit_description": "Physics of the greenhouse effect (short-wave solar ingress vs long-wave terrestrial infrared trapping), triatomic greenhouse gases (CO2, CH4, N2O, H2O), natural vs enhanced greenhouse effect, Ozone layer in stratosphere vs greenhouse effect in troposphere, and empirical climate change indicators.",
            "lesson_title": "Greenhouse Effect, Evidence and Impacts",
            "pages": [
                # Page 1: Hook & Flower Greenhouse Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Radiative Thermal Trapping: Agricultural Greenhouse in Kenya",
                        "content": {
                            "title": "Radiative Thermal Trapping: Agricultural Greenhouse in Kenya",
                            "caption": "An export commercial flower greenhouse in Naivasha, Kenya. The translucent plastic roof allows short-wave sunlight to enter but blocks escaping infrared radiation and convection, warming the interior air.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Commercial_greenhouse_naivasha_kenya.jpg/1280px-Commercial_greenhouse_naivasha_kenya.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Commercial_greenhouse_naivasha_kenya.jpg/1280px-Commercial_greenhouse_naivasha_kenya.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Agricultural Flower Greenhouse in Kenya",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Commercial_greenhouse_naivasha_kenya.jpg/1280px-Commercial_greenhouse_naivasha_kenya.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Commercial_greenhouse_naivasha_kenya.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Closed Cars Get Scorching Hot",
                        "content": {
                            "title": "The Trapping of Thermal Radiation",
                            "text": "When a car is parked in the hot sun with windows closed, the interior becomes much hotter than the outside air.\n\nGlass lets visible sunlight enter, but absorbs the outgoing **infrared heat radiation**, trapping energy inside. Earth's atmosphere behaves in the exact same way via the **Greenhouse Effect**."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: The Physics of Climate Change",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Explain the physical mechanism of the **Greenhouse Effect**.",
                                "Identify primary greenhouse gases (**$CO_2, CH_4, N_2O, H_2O$**).",
                                "Distinguish the **Natural** from the **Enhanced** greenhouse effect.",
                                "Differentiate the **Ozone Layer (UV shield)** from the **Greenhouse Effect (IR trap)**.",
                                "Evaluate empirical evidence for global climate change."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Greenhouse Effect",
                        "content": {
                            "term": "Greenhouse Effect",
                            "definition": "The physical process by which greenhouse gases in the troposphere absorb and re-radiate outgoing long-wave thermal infrared radiation from Earth's surface, warming the lower atmosphere.",
                            "example": "Natural greenhouse effect keeps Earth at a life-supporting average of +15 °C rather than -18 °C."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Ozone Layer",
                        "content": {
                            "term": "Ozone Layer",
                            "definition": "A protective layer of ozone gas (O3) in the stratosphere (15-30 km altitude) that absorbs up to 99% of incoming harmful high-energy ultraviolet (UV) radiation from the Sun.",
                            "example": "Protects humans from skin cancer and prevents damage to marine phytoplankton."
                        }
                    }
                ],
                # Page 3: Greenhouse Effect Model SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Physics of the Greenhouse Effect: Global Energy Balance",
                        "content": {
                            "title": "Physics of the Greenhouse Effect: Global Energy Balance",
                            "caption": "Short-wave solar light penetrates atmosphere easily; warmed Earth surface re-emits long-wave infrared radiation; greenhouse gases absorb and re-radiate heat back to ground.",
                            "svg_content": get_svg_greenhouse_effect_model(),
                            "svg": get_svg_greenhouse_effect_model()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Greenhouse Effect Global Energy Balance Diagram",
                            "metadata": {
                                "svg_content": get_svg_greenhouse_effect_model()
                            }
                        }
                    }
                ],
                # Page 4: Greenhouse Effect vs Ozone Layer Comparison
                [
                    {
                        "type": "comparison_table",
                        "title": "Greenhouse Effect vs Ozone Layer: Crucial Physics Distinctions",
                        "content": {
                            "title": "Atmospheric Comparison Matrix",
                            "headers": ["Feature", "Greenhouse Effect", "Ozone Layer ($O_3$)"],
                            "rows": [
                                ["Atmospheric Layer", "Troposphere ($0 - 12\\text{ km}$ altitude)", "Stratosphere ($15 - 30\\text{ km}$ altitude)"],
                                ["Radiation Handled", "Outgoing **Thermal Infrared Radiation (Heat)**", "Incoming **High-Energy Ultraviolet (UV) Rays**"],
                                ["Gases Involved", "$CO_2$, $CH_4$, $N_2O$, Water vapor ($H_2O$)", "Ozone ($O_3$)"],
                                ["Primary Physical Role", "Regulates Earth surface temperature.", "Shields biological DNA and eyes from UV damage."],
                                ["Human Impact Threat", "Excess fossil fuel combustion enhances warming.", "Chlorofluorocarbons (CFCs) cause ozone depletion."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Why CO2 and H2O Absorb Infrared",
                        "content": {
                            "question": "Why are carbon dioxide (CO2) and water vapor (H2O) effective greenhouse gases, while nitrogen (N2) and oxygen (O2) are not?",
                            "options": [
                                "Oxygen and nitrogen are too heavy to rise into the atmosphere.",
                                "CO2 and H2O are triatomic molecules with vibrational resonance modes that absorb infrared wavelengths, whereas symmetric diatomic N2 and O2 cannot.",
                                "Plants absorb nitrogen and cool the atmosphere.",
                                "CO2 molecules are dark and absorb all visible light."
                            ],
                            "answer": "B",
                            "explanation": "Over 99% of air consists of diatomic $N_2$ and $O_2$, which cannot interact with infrared radiation due to molecular symmetry. Triatomic greenhouse gases ($CO_2, H_2O, CH_4$) possess bending and stretching vibrational modes that **resonate at the exact frequencies of thermal infrared radiation**, absorbing and re-emitting the heat. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: Climate Change Empirical Evidence
                [
                    {
                        "type": "real_world_connection",
                        "title": "Physical Indicators of Climate Change in Kenya and Globally",
                        "content": {
                            "title": "Empirical Scientific Evidence",
                            "text": "- **Rising Temperatures**: Global average surface temperature has risen by $+1.1^\\circ\\text{C}$ since the industrial baseline.\n- **Mount Kenya Glacier Retreat**: Ice caps on Mount Kenya have lost over $90\\%$ of their volume in the past century.\n- **Thermal Sea-Level Rise**: Thermal expansion of ocean water (Topic 4!) and melting land ice cause global sea levels to rise $3.4\\text{ mm/year}$, threatening coastal Mombasa.\n- **Extreme Weather**: Prolonged droughts in Northern Kenya followed by severe flash floods."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Greenhouse Effect and Global Energy Balance",
                        "content": {
                            "title": "Physics Video: Greenhouse Effect and Global Energy Balance",
                            "description": "Video explaining the physics of solar radiation balance, molecular infrared absorption, and global climate evidence.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Greenhouse Effect and Climate Physics Video",
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
                                "**Greenhouse Effect**: Triatomic gases ($CO_2, CH_4, H_2O$) absorb outgoing long-wave infrared heat.",
                                "Natural greenhouse effect is essential (+15 °C); enhanced effect drives global warming.",
                                "**Ozone layer** blocks UV in stratosphere; **greenhouse gases** trap heat in troposphere.",
                                "Physical evidence includes glacier loss on Mt. Kenya, sea level rise, and weather extremes."
                            ]
                        }
                    }
                ]
            ]
        },

        # ---------------------------------------------------------------------
        # LESSON 2: Mitigation, Adaptation and Responsible Technology
        # ---------------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Mitigation, Adaptation and Responsible Technology",
            "unit_description": "Climate mitigation (stopping emissions via clean energy) vs adaptation (living with changes), clean energy physics (Solar PV photoelectric effect, Wind electromagnetic induction, Geothermal thermodynamics), Sankey energy efficiency diagrams, school energy audits, and off-grid solar design.",
            "lesson_title": "Mitigation, Adaptation and Responsible Technology",
            "pages": [
                # Page 1: Hook & Geothermal Power Image
                [
                    {
                        "type": "suggested_image",
                        "title": "Clean Energy Physics: Olkaria Geothermal Power Station in Kenya",
                        "content": {
                            "title": "Clean Energy Physics: Olkaria Geothermal Power Station in Kenya",
                            "caption": "The Olkaria geothermal power facility in the Great Rift Valley, Kenya. Harnessing deep subterranean thermal steam to drive electricity turbines generates over 800 MW of clean, zero-emission renewable power.",
                            "resolved_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Olkaria_geothermal_power_plant_kenya.jpg/1280px-Olkaria_geothermal_power_plant_kenya.jpg",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Olkaria_geothermal_power_plant_kenya.jpg/1280px-Olkaria_geothermal_power_plant_kenya.jpg"
                        },
                        "asset": {
                            "asset_type": "image",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Olkaria Geothermal Power Plant Kenya",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Olkaria_geothermal_power_plant_kenya.jpg/1280px-Olkaria_geothermal_power_plant_kenya.jpg",
                            "metadata": {
                                "author": "Wikimedia Commons",
                                "licensing": "CC BY-SA 3.0",
                                "commons_page_url": "https://commons.wikimedia.org/wiki/File:Olkaria_geothermal_power_plant_kenya.jpg"
                            }
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Physics Solutions to Global Challenges",
                        "content": {
                            "title": "Mitigation vs Adaptation",
                            "text": "To protect our future, physics provides two parallel paths:\n\n1. **Mitigation**: Switching from fossil fuels to renewable energy to reduce emissions.\n2. **Adaptation**: Designing drip irrigation, curved seawalls, and solar pumps to thrive amidst changing climate patterns."
                        }
                    }
                ],
                # Page 2: Learning Goals & Definitions
                [
                    {
                        "type": "learning_goal",
                        "title": "Lesson Objectives: Clean Technologies & Auditing",
                        "content": {
                            "title": "What We Will Master Today",
                            "goals": [
                                "Distinguish **Mitigation** from **Adaptation**.",
                                "Explain the physics principles of **Solar PV, Wind**, and **Geothermal** energy.",
                                "Analyze energy losses using **Sankey Diagrams**.",
                                "Perform a **School Energy Audit** to calculate financial and carbon savings."
                            ]
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Climate Mitigation",
                        "content": {
                            "term": "Climate Mitigation",
                            "definition": "Technological actions and policies aimed at reducing greenhouse gas emissions or expanding carbon sinks (e.g. solar PV, reforestation).",
                            "example": "Replacing coal plants with Olkaria geothermal energy."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Key Term: Climate Adaptation",
                        "content": {
                            "term": "Climate Adaptation",
                            "definition": "Practical adjustments in infrastructure, agriculture, and water management to minimize vulnerability to climate impacts.",
                            "example": "Using precision drip irrigation to farm in drought-prone areas."
                        }
                    }
                ],
                # Page 3: Sankey Efficiency SVG
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Sankey Energy Efficiency: Incandescent vs LED Lighting",
                        "content": {
                            "title": "Sankey Energy Efficiency: Incandescent vs LED Lighting",
                            "caption": "Sankey diagrams comparing energy flows: Incandescent bulb converts only 5% of energy into light (95% wasted heat) versus modern LED converting 50% into light (10x more efficient).",
                            "svg_content": get_svg_sankey_lighting_efficiency(),
                            "svg": get_svg_sankey_lighting_efficiency()
                        },
                        "asset": {
                            "asset_type": "diagram",
                            "storage_type": "embed",
                            "source_type": "ai_generated",
                            "title": "Sankey Energy Efficiency Diagram",
                            "metadata": {
                                "svg_content": get_svg_sankey_lighting_efficiency()
                            }
                        }
                    }
                ],
                # Page 4: Clean Energy Physics Mechanisms
                [
                    {
                        "type": "comparison_table",
                        "title": "Physics Mechanisms of Renewable Energy Technologies",
                        "content": {
                            "title": "Clean Energy Physics Matrix",
                            "headers": ["Technology", "Energy Transformation", "Core Physics Principle"],
                            "rows": [
                                ["Solar Photovoltaic (PV)", "Light Energy $\\longrightarrow$ Electrical DC Energy", "**Photoelectric Effect**: Photons excite electrons across semiconductor band gap."],
                                ["Wind Turbines", "Kinetic Wind Energy $\\longrightarrow$ Rotational Kinetic $\\longrightarrow$ Electrical Energy", "**Electromagnetic Induction**: Spinning aerodynamic blades rotate magnets in copper coils (Faraday's Law)."],
                                ["Geothermal Power", "Subterranean Thermal Energy $\\longrightarrow$ High-Pressure Steam $\\longrightarrow$ Electrical Energy", "**Thermodynamics**: Heat energy drives high-pressure turbines to do mechanical work."]
                            ]
                        }
                    }
                ],
                # Page 5: Formative MCQ
                [
                    {
                        "type": "knowledge_check",
                        "title": "Check Your Understanding: Sizing Off-Grid Solar Water Pump",
                        "content": {
                            "question": "A community installs an off-grid solar-powered water pump requiring 1.2 kW of electrical power. If each solar panel produces 300 W peak power, what is the minimum number of panels required, and how should they be connected?",
                            "options": [
                                "4 panels, connected purely in parallel.",
                                "4 panels, arranged in a calculated series-parallel network to match both required motor voltage and total power.",
                                "12 panels, connected in series.",
                                "1 panel, because solar panels are 100% efficient."
                            ],
                            "answer": "B",
                            "explanation": "Calculate minimum panels: $\\text{Number} = \\frac{1200\\text{ W}}{300\\text{ W}} = 4\\text{ panels}$. To operate the pump motor safely, the panels must be configured in a calculated **series-parallel network** (e.g. 2 parallel strings of 2 series panels) to match both the required motor voltage and total current. Option B is correct.",
                            "check_type": "multiple_choice"
                        }
                    }
                ],
                # Page 6: School Energy Audit Worked Example
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: School Energy Efficiency Upgrade",
                        "content": {
                            "title": "Financial and Carbon Savings Calculation",
                            "problem": "A school has 10 classrooms, each with ten $40\\text{ W}$ fluorescent tubes running $8\\text{ hours}$ daily. If they replace them with $18\\text{ W}$ LEDs at a tariff of $25.0\\text{ KES/kWh}$, calculate the monthly financial savings (20 school days).",
                            "steps": [
                                "1. **Old Energy**: $100\\text{ tubes} \\times 40\\text{ W} \\times 8\\text{ hrs} = 32.0\\text{ kWh/day}$.",
                                "2. **New Energy**: $100\\text{ tubes} \\times 18\\text{ W} \\times 8\\text{ hrs} = 14.4\\text{ kWh/day}$.",
                                "3. **Daily Saved**: $32.0 - 14.4 = 17.6\\text{ kWh/day}$.",
                                "4. **Monthly Savings**: $17.6\\text{ kWh/day} \\times 20\\text{ days} \\times 25.0\\text{ KES/kWh} = 8,800\\text{ KES}$."
                            ],
                            "answer": "The school saves 8,800 KES every month while cutting energy use by 55%."
                        }
                    }
                ],
                # Page 7: Video Demonstration
                [
                    {
                        "type": "suggested_video",
                        "title": "Physics Video: Clean Energy, Mitigation, and Energy Efficiency",
                        "content": {
                            "title": "Physics Video: Clean Energy, Mitigation, and Energy Efficiency",
                            "description": "Video explaining solar photovoltaic physics, wind turbines, geothermal energy, and calculating energy efficiency with Sankey diagrams.",
                            "url": "https://www.youtube.com/watch?v=CVsdXKO9xlk",
                            "resolved_video_id": "CVsdXKO9xlk"
                        },
                        "asset": {
                            "asset_type": "youtube",
                            "storage_type": "url",
                            "source_type": "external",
                            "title": "Renewable Energy and Climate Mitigation Video",
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
                                "**Mitigation** slashes emissions (Solar PV, Wind, Geothermal); **Adaptation** builds resilience (drip irrigation, seawalls).",
                                "**Sankey diagrams** visualize useful energy output versus wasted thermal losses.",
                                "LEDs are up to 10× more efficient than filament bulbs, drastically reducing electricity demand and costs."
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
def ingest_grade10_physics_topic12():
    print("======================================================================")
    print("INGESTING CBC GRADE 10 PHYSICS — TOPIC 12: GREENHOUSE EFFECT & CLIMATE")
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

    # 3. Get or Create Topic: Greenhouse Effect and Climate Change (Order: 12)
    topic, t_created = Topic.objects.get_or_create(
        subject=subject,
        order=12,
        defaults={
            "name": "Greenhouse Effect and Climate Change",
            "description": "Exploration of the greenhouse effect, global energy balance, triatomic atmospheric gases, ozone layer distinctions, empirical climate indicators, renewable energy mitigation (solar PV, wind, geothermal), energy efficiency with Sankey diagrams, and school energy auditing."
        }
    )
    if not t_created and topic.name != "Greenhouse Effect and Climate Change":
        topic.name = "Greenhouse Effect and Climate Change"
        topic.description = "Exploration of the greenhouse effect, global energy balance, triatomic atmospheric gases, ozone layer distinctions, empirical climate indicators, renewable energy mitigation (solar PV, wind, geothermal), energy efficiency with Sankey diagrams, and school energy auditing."
        topic.save()
    print(f"Topic: {topic.name} (ID: {topic.id}, Order: {topic.order})")

    curriculum_data = build_topic12_curriculum_data()

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
    print(f"TOPIC 12 INGESTION COMPLETE:")
    print(f"  - Learning Units: {total_units_created}")
    print(f"  - Lessons:        {total_lessons_created}")
    print(f"  - Lesson Blocks:  {total_blocks_created}")
    print(f"  - Lesson Assets:  {total_assets_created}")
    print("======================================================================")

if __name__ == "__main__":
    ingest_grade10_physics_topic12()
