"""
VLearn Form 4 Business Studies — Topic 2: Population and Employment
Authoritative Pedagogical Data Structures for 6 Lessons (60 Pages).
"""

from curriculum.ingest_form4_business_studies_topic2_svgs import (
    SVG_DEMOGRAPHIC_BALANCE_FLOW,
    SVG_OPTIMUM_POPULATION_CURVE,
    SVG_POPULATION_PYRAMID_STRUCTURE,
    SVG_LABOR_FORCE_CLASSIFICATION_TREE,
    SVG_UNEMPLOYMENT_POLICY_MATRIX
)

# Verified Wikimedia photographic assets
IMG_WANGIGE_MARKET_DENSITY = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "text": "Wangige market in Kiambu, illustrating consumer demand, population density, and informal trade employment in Kenya.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
}

IMG_MWEA_RICE_LABOUR = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Mwea_Rice_Plantation.jpg",
    "text": "Mwea Rice Irrigation Scheme, demonstrating labor-intensive agricultural production and seasonal rural employment.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Mwea_Rice_Plantation.jpg"
}

IMG_JUA_KALI_INFORMAL = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
    "text": "Jua Kali artisans in Nairobi, illustrating vocational skills, self-employment, and micro-enterprise job creation.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_fabricator.jpg"
}

IMG_RUKURIRI_TEA_PROCESSING = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/2009.12-363-1125ap_tea%2Cprocessing%28withering%29%2Cstirring_Rukuriri_Tea_Factory%2Ctea-zone_N_of_Embu%28C_Highlands%29%2CKE_mon14dec2009-1242h.jpg",
    "text": "Rukuriri Tea Factory in Embu, showing agro-processing industrialization that converts seasonal tea harvesting into year-round manufacturing jobs.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:2009.12-363-1125ap_tea,processing(withering),stirring_Rukuriri_Tea_Factory,tea-zone_N_of_Embu(C_Highlands),KE_mon14dec2009-1242h.jpg"
}

IMG_SGR_INFRASTRUCTURE = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/New_SGR_train_Nairobi.jpg",
    "text": "Standard Gauge Railway logistics, illustrating large-scale public capital infrastructure and long-term labor mobility.",
    "author": "Wikimedia Commons Contributor",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:New_SGR_train_Nairobi.jpg"
}

# ==============================================================================
# LESSON 1: POPULATION GROWTH AND DEMOGRAPHIC CONCEPTS (10 Pages)
# ==============================================================================
LESSON_1_DATA = {
    "unit_order": 1,
    "unit_name": "Population Growth and Demographic Concepts",
    "lesson_title": "Demographic Measurements, Growth Determinants, and Census Planning",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Demography",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define population and population growth rate, explain birth rate, mortality rate, and migration, analyze factors driving high and declining birth rates, and state the purpose of a national population census."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Population Studies Matter",
                    "content": {
                        "text": "For any government or business to plan effectively, they must know how many people they are serving. Just as a school principal needs to know student enrollment to purchase desks and books, a government needs to know its population size and growth rate to plan for hospitals, housing, roads, food security, and job creation."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Meaning of Population & Demography",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Core Definitions",
                    "content": {
                        "term": "Population & Demography",
                        "definition": "Population is the total number of human beings living in a specific geographical territory at a particular point in time. Demography is the scientific and statistical study of human populations, their size, distribution, and changes over time."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Population Concentration in Kenya",
                    "content": IMG_WANGIGE_MARKET_DENSITY
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Basic Demographic Concepts",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Four Pillars of Population Change",
                    "content": {
                        "text": "1. Population Growth Rate: The percentage rate at which a population size increases or decreases over a given time period (usually one year).\n2. Crude Birth Rate (CBR): The number of live births per 1,000 individuals in a population in one year.\n3. Crude Death / Mortality Rate (CDR): The number of deaths per 1,000 individuals in a population in one year.\n4. Migration: The spatial movement of people from one region or country to another, comprising Immigration (incoming settlers) and Emigration (departing residents)."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "The Demographic Balance Equation",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "How Population Changes Mathematically",
                    "content": {
                        "text": "Population change is determined by the interaction between natural increase (Births - Deaths) and net migration (Immigration - Emigration). If inflows exceed outflows, the population expands."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "The Demographic Balance Equation",
                    "svg_content": SVG_DEMOGRAPHIC_BALANCE_FLOW,
                    "content": {
                        "text": "Vector flowchart showing inflows (births and immigration) versus outflows (deaths and emigration) driving total national population size."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Factors Promoting High Birth Rates",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Socio-Cultural & Economic Drivers of High Fertility",
                    "content": {
                        "text": "1. Cultural Beliefs & Prestige: High social status accorded to large families and polygamy in traditional communities.\n2. Early Marriages: Girls marrying at a young age, extending their total reproductive/childbearing years.\n3. Children as Cheap Farm Labor: In rural agrarian setups, children are viewed as economic assets who help on family farms.\n4. Search for a Male Child: Cultural preference for male heirs causing couples to keep conceiving until a son is born.\n5. Religious Beliefs: Religious doctrines prohibiting modern artificial contraceptive methods.\n6. Ignorance / Lack of Family Planning: Limited awareness or access to reproductive healthcare."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Factors Promoting Declining Birth Rates",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Modernization & Economic Drivers of Declining Fertility",
                    "content": {
                        "text": "1. Delayed Marriages: Individuals marrying later in life to pursue higher education and establish careers, shortening childbearing years.\n2. Desire for Higher Standard of Living: Couples preferring smaller families so household income can provide high-quality housing, nutrition, and lifestyle.\n3. Heavy Investment in Child Education: High costs of private schooling and university tuition leading parents to limit family size.\n4. Reduced Infant Mortality: Modern immunization and medical care assure parents that children will survive, removing the need for 'replacement births'.\n5. Viable Retirement Pension Schemes: Social security (e.g. NSSF, private pensions) removes dependence on children for old-age financial support."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Comparative Matrix of Birth Rate Determinants",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "High Birth Rate Drivers vs Declining Birth Rate Drivers",
                    "content": {
                        "headers": ["Dimension", "Factors Promoting High Birth Rates", "Factors Promoting Declining Birth Rates"],
                        "rows": [
                            ["Marriage Age", "Early marriages extending reproductive lifespan", "Delayed marriages due to higher education and career building"],
                            ["Economic Role of Children", "Children seen as cheap agricultural field labor", "Children viewed as expensive dependents requiring heavy tuition"],
                            ["Cultural Norms", "High prestige for large families and male heirs", "Preference for nuclear 1-to-2-child households"],
                            ["Old-Age Security", "Reliance on adult children for financial care in old age", "Establishment of formal pension schemes and social security"],
                            ["Healthcare Dynamics", "High infant mortality triggering replacement births", "Low infant mortality ensuring child survival confidence"],
                            ["Family Planning", "Ignorance or religious prohibition of contraception", "Widespread education, awareness, and contraceptive access"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "The Population Census",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition & Importance of Population Census",
                    "content": {
                        "term": "Population Census",
                        "definition": "The official, systematic counting and demographic enumeration of all persons residing in a country at a specific reference time, typically conducted every 10 years by the national statistical agency."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Four Uses of Census Data in Kenya",
                    "content": {
                        "text": "1. Resource Allocation: Helps the Commission on Revenue Allocation (CRA) distribute national revenue equitably across the 47 counties.\n2. Infrastructure Planning: Provides exact demographic data to build schools, hospitals, water supplies, and electricity grids.\n3. Boundary Delimitation: Guides the Independent Electoral and Boundaries Commission (IEBC) in creating fair parliamentary and ward constituencies.\n4. Labor Market Planning: Informs the government on the size of the future labor force and employment creation needs."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Worked Analysis: Interpreting Demographic Trends",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Scenario: Explaining Severe Population Decline",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Information", "description": "Country X had a population of 40 million in 2001. By 2004, its population plummeted to 9 million."},
                            {"title": "Step 2: Required Diagnostic", "description": "Explain the demographic factors that could cause such an extreme population drop over three years."},
                            {"title": "Step 3: Demographic Principles", "description": "Population drops only through mortality spikes, heavy emigration, or sudden fertility collapse."},
                            {"title": "Step 4: Substitution & Analysis", "description": "A drop of 31 million people in 3 years is too rapid for declining birth rates alone. It points to catastrophic outflows: severe civil war, famine, or massive emigration/refugee flight."},
                            {"title": "Step 5: Alternative Verification", "description": "Check equation: Net Population Change = (Births - Deaths) + (Immigration - Emigration). A massive negative net migration and mortality spike explains the collapse."},
                            {"title": "Step 6: Economic Conclusion", "description": "The decline is caused primarily by massive emigration (refugee outflows) combined with catastrophic mortality shocks."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Demographic Concepts",
                    "content": {
                        "question": "How does the establishment of viable national retirement pension schemes influence a country's birth rate?",
                        "options": [
                            {"id": "a", "text": "It increases birth rates because parents have extra pension cash for school fees"},
                            {"id": "b", "text": "It leads to a decline in birth rates because parents no longer rely on many children for financial support in old age", "correct": True, "feedback": "Correct! When formal pensions guarantee financial security in old age, the economic motive to have large families diminishes."},
                            {"id": "c", "text": "It increases the crude death rate across the youth population"},
                            {"id": "d", "text": "It forces citizens to emigrate to neighboring countries"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 1 Summary",
                    "content": {
                        "text": "Population changes through births, deaths, and migration. High birth rates are driven by cultural prestige and early marriage, while declining birth rates stem from education, small-family preferences, and pensions. Censuses guide national planning."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 2: OPTIMUM, UNDER-POPULATION & OVER-POPULATION (10 Pages)
# ==============================================================================
LESSON_2_DATA = {
    "unit_order": 2,
    "unit_name": "Optimum, Under-population, and Over-population",
    "lesson_title": "Optimum Theory, Resource Balance, and Per-Capita Welfare",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Optimum Population",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define optimum population, under-population, and over-population, analyze their causes and socio-economic effects, and compute per-capita resource indicators to identify the state of population."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Is a Large Population Good or Bad?",
                    "content": {
                        "text": "Neither a large nor a small population is inherently good or bad. It all depends on the country's available economic resources (land, minerals, capital, and technology). The optimum state occurs when population perfectly balances resource capacity to produce the highest living standards."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Meaning of Optimum Population",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Optimum Population",
                    "content": {
                        "term": "Optimum Population",
                        "definition": "The population size that is perfectly in balance with a country's available economic resources and technology, generating the highest possible standard of living (maximum output/income per capita)."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "The Optimum Population Curve",
                    "svg_content": SVG_OPTIMUM_POPULATION_CURVE,
                    "content": {
                        "text": "Inverted U-shape economic curve showing standard of living (per capita GDP) peaking at optimum population and falling under under-population and over-population."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Under-population: Meaning and Causes",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Under-population",
                    "content": {
                        "term": "Under-population",
                        "definition": "A situation where a country's population size is too small relative to its abundant economic resources and technology, leaving natural resources underutilized."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Causes of Under-population",
                    "content": {
                        "text": "1. Extremely low fertility / birth rates.\n2. High mortality rates resulting from epidemics, wars, or natural disasters.\n3. High rates of net emigration (brain drain and refugee flight).\n4. Rapid discovery of vast new natural resources (e.g. oil or mineral strikes in a sparsely populated territory)."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Effects of Under-population",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Positive & Negative Consequences of Under-population",
                    "content": {
                        "text": "- Positive Effects: Zero congestion in social amenities, abundant employment opportunities, high per-capita access to public infrastructure, and clean unpolluted environments.\n- Negative Effects: Underutilization of resources, acute labor/manpower shortages, small domestic market size (discouraging large-scale business investments), high cost of providing public infrastructure per person, and difficulty defending territorial borders."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Over-population: Meaning and Causes",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Over-population",
                    "content": {
                        "term": "Over-population",
                        "definition": "A situation where a country's population size exceeds its available economic resources and technology, overstretching amenities and dragging down per-capita income and living standards."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Causes of Over-population",
                    "content": {
                        "text": "1. Consistently high birth rates.\n2. Rapidly declining mortality rates due to advanced medical care without a corresponding drop in fertility.\n3. Massive influx of incoming immigrants or refugees.\n4. Depletion of natural resources or environmental degradation reducing carrying capacity."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Effects of Over-population",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Advantages & Disadvantages of Over-population",
                    "content": {
                        "text": "- Advantages: Wide domestic market for consumer goods, large pool of labor supply, stimulated entrepreneurial investment, and high labor mobility.\n- Disadvantages: Severe strain on social amenities (overcrowded hospitals, congested classrooms), falling living standards, high youth dependency, food insecurity, urban slums, rising crime rates, and environmental degradation."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Comparative Population States Matrix",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "Under-population vs Optimum vs Over-population",
                    "content": {
                        "headers": ["Dimension", "Under-population", "Optimum Population", "Over-population"],
                        "rows": [
                            ["Resource Balance", "Resources exceed population capacity", "Population perfectly matches resources", "Population exceeds resource capacity"],
                            ["Standard of Living", "Lower than potential due to idle resources", "Maximum possible output per capita", "Declining living standards and poverty"],
                            ["Domestic Market", "Small domestic demand; limits economies of scale", "Balanced and vibrant domestic market", "Large domestic market with high demand"],
                            ["Labor Supply", "Acute manpower shortages; idle land", "Sufficient labor matching all sectors", "Excess labor leading to mass unemployment"],
                            ["Social Amenities", "Underutilized schools and hospitals", "Equitably utilized infrastructure", "Severely congested and overstretched facilities"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "The Dynamic Nature of Optimum Population",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Optimum Population is Not a Fixed Number",
                    "content": {
                        "text": "Optimum population is dynamic. If a country discovers oil, adopts high-yield agricultural biotechnology, or expands solar energy, its productive resource capacity shifts upwards. As a result, its optimum population level increases, allowing it to support more citizens at even higher living standards."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "6-Step Calculation: Determining Population State",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Example: Comparative Per Capita GDP Calculation",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Information", "description": "Country A: GDP = Sh. 500,000M, Pop = 10M. Country B: GDP = Sh. 900,000M, Pop = 15M. Country C: GDP = Sh. 800,000M, Pop = 25M. (Identical resources & technology)."},
                            {"title": "Step 2: Identify What is Required", "description": "Compute Per Capita GDP for A, B, and C, and identify which country has achieved Optimum Population."},
                            {"title": "Step 3: State the Formula", "description": "Per Capita GDP = Total GDP ÷ Total Population."},
                            {"title": "Step 4: Substitute & Compute", "description": "Country A: 500,000M ÷ 10M = Sh. 50,000. Country B: 900,000M ÷ 15M = Sh. 60,000. Country C: 800,000M ÷ 25M = Sh. 32,000."},
                            {"title": "Step 5: Check Direction of Change", "description": "As population grows from 10M to 15M, per capita income rises from 50k to 60k (increasing returns). Beyond 15M, per capita income falls to 32k (diminishing returns)."},
                            {"title": "Step 6: Economic Interpretation", "description": "Country B has achieved the Optimum Population (highest living standard of Sh. 60,000). Country A is Under-populated; Country C is Over-populated."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Optimum Population",
                    "content": {
                        "question": "Which of the following conditions characterizes a country experiencing under-population?",
                        "options": [
                            {"id": "a", "text": "High congestion and overstretched healthcare clinics"},
                            {"id": "b", "text": "Abundant natural resources remaining idle due to inadequate labor supply", "correct": True, "feedback": "Correct! Under-population means the workforce is too small to exploit abundant resources fully."},
                            {"id": "c", "text": "Extremely high per-capita waste and slum formation"},
                            {"id": "d", "text": "A massive domestic consumer market that exhausts food supplies"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 2 Summary",
                    "content": {
                        "text": "Optimum population maximizes per-capita standard of living. Under-population leaves resources idle due to labor shortages, while over-population strains amenities and causes poverty. The optimum shifts with technological advancement."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 3: POPULATION STRUCTURE & DEPENDENCY (10 Pages)
# ==============================================================================
LESSON_3_DATA = {
    "unit_order": 3,
    "unit_name": "Population Structure, Age Distribution, and Dependency",
    "lesson_title": "Age/Gender/Geographic Structure and the Dependency Burden",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Population Structure",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define population structure, analyze the economic implications of young versus ageing populations, and calculate the national dependency ratio using the 6-step framework."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Why Composition Matters More Than Size",
                    "content": {
                        "text": "Two countries can have the exact same population of 50 million people, but if Country A is mostly school-going children and Country B is mostly working adults, Country B will possess a massive productive workforce while Country A will face heavy school and pediatric healthcare bills."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Meaning of Population Structure",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Population Structure",
                    "content": {
                        "term": "Population Structure",
                        "definition": "The internal composition and distribution of a country's population categorized by demographic characteristics such as age, gender, geographical location (rural vs urban), literacy levels, and dependency."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Age Structure & Age Brackets",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Three Standard Economic Age Cohorts",
                    "content": {
                        "text": "Economists divide population into three functional cohorts:\n1. Children & Adolescents (0–14 years): Dependent non-working population consuming educational and pediatric resources.\n2. Working-Age Population (15–64 years): Productive labor force generating national income, paying taxes, and supporting dependents.\n3. Elderly Population (65+ years): Dependent retired population requiring pensions and geriatric healthcare."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Comparative Population Pyramids",
                    "svg_content": SVG_POPULATION_PYRAMID_STRUCTURE,
                    "content": {
                        "text": "Comparative vector diagram contrasting the broad-based young population pyramid of developing countries with the narrow-based ageing population pyramid of developed countries."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Young Population: Characteristics & Implications",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Implications of a High Youth Proportion (e.g. Kenya)",
                    "content": {
                        "text": "- Causes: High fertility/birth rates combined with declining infant mortality.\n- Negative Implications:\n  1. High Dependency Burden: Few working adults must feed, house, and educate many children.\n  2. Diversion of Government Budget: State funds diverted to consumption amenities (free primary/secondary education, immunization) rather than capital infrastructure.\n  3. Low National Savings: Household income is spent on immediate basic needs, leaving little for bank savings and investments.\n  4. Future Unemployment Pressure: Large cohorts of youth entering the labor market annually.\n- Positive Implication: Guarantees an abundant energetic labor supply for the future."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Ageing Population: Characteristics & Implications",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Implications of a High Elderly Proportion",
                    "content": {
                        "text": "- Causes: Low birth rates combined with long life expectancy (common in developed nations like Japan and Western Europe).\n- Economic Problems:\n  1. Acute Manpower Shortages: A shrinking working-age cohort leads to labor scarcity and high wage costs.\n  2. Heavy Pension & Healthcare Burden: Heavy state expenditure on retirement benefits and elderly care homes.\n  3. Reduced Labor Mobility: Older workers are less willing to retrain, learn new technology, or relocate geographically.\n  4. Decreased Social Innovation: Lower entrepreneurial risk-taking and dynamism."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Gender Structure and Rural-Urban Distribution",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Gender & Spatial Demographics",
                    "content": {
                        "text": "1. Gender Structure: The ratio of males to females. A severe imbalance can affect marriage rates, fertility patterns, and sector-specific labor supply (e.g. mining vs nursing).\n2. Geographical Distribution: The proportion living in rural vs urban centers. Rapid rural-urban migration causes urban congestion, housing deficits, and slums in cities while leaving fertile agricultural land underutilized in rural areas."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Rural Agricultural Production",
                    "content": IMG_MWEA_RICE_LABOUR
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "The Dependency Ratio Concept",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Definition of Dependency Ratio",
                    "content": {
                        "term": "Dependency Ratio",
                        "definition": "The mathematical ratio of the dependent population (children aged 0–14 plus elderly persons aged 65+) to the productive working-age population (aged 15–64), expressed as a percentage."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Formula",
                    "content": {
                        "text": "$$\\text{Dependency Ratio} = \\left( \\frac{\\text{Number of Dependents } (0-14 + 65+)}{\\text{Working-Age Population } (15-64)} \\right) \\times 100$$"
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "6-Step Calculation: Dependency Ratio",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Example: Computing National Dependency Ratio",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Information", "description": "Country K census data: Total Population = 50M; Children (0–14) = 28M; Working-Age (15–64) = 20M; Elderly (65+) = 2M."},
                            {"title": "Step 2: Identify What is Required", "description": "Calculate the national Dependency Ratio and provide an economic interpretation."},
                            {"title": "Step 3: State the Formula", "description": "Dependency Ratio = ((Children 0-14 + Elderly 65+) ÷ Working-Age 15-64) × 100."},
                            {"title": "Step 4: Substitute & Compute", "description": "Total Dependents = 28M + 2M = 30M. Dependency Ratio = (30M ÷ 20M) × 100 = 1.5 × 100 = 150%."},
                            {"title": "Step 5: Alternative Verification", "description": "Ratio of Dependents to Workers = 30 : 20 = 3 : 2. For every 2 workers, there are 3 dependents (1.5 dependents per worker = 150%)."},
                            {"title": "Step 6: Economic Interpretation", "description": "Every 100 working-age citizens support 150 dependents. This is an extremely high dependency burden, severely constraining household savings and state investment."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Intermediate Dependency Problem",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Calculation: Determining Dependent Population from Ratio",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Data", "description": "County M has a dependency ratio of 80% and an active working-age population of 500,000 people."},
                            {"title": "Step 2: Required", "description": "Calculate the total number of dependent persons residing in County M."},
                            {"title": "Step 3: Formula", "description": "Dependents = (Dependency Ratio ÷ 100) × Working-Age Population."},
                            {"title": "Step 4: Substitute & Compute", "description": "Dependents = (80 ÷ 100) × 500,000 = 0.8 × 500,000 = 400,000 dependents."},
                            {"title": "Step 5: Verification", "description": "Check: (400,000 ÷ 500,000) × 100 = 0.8 × 100 = 80%. Perfect match."},
                            {"title": "Step 6: Conclusion", "description": "County M has exactly 400,000 dependent children and elderly residents."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Population Structure",
                    "content": {
                        "question": "A country has 10 million children (0–14), 20 million working adults (15–64), and 2 million retirees (65+). What is its dependency ratio?",
                        "options": [
                            {"id": "a", "text": "40%"},
                            {"id": "b", "text": "60%", "correct": True, "feedback": "Correct! Dependents = 10M + 2M = 12M. (12M ÷ 20M) × 100 = 60%."},
                            {"id": "c", "text": "120%"},
                            {"id": "d", "text": "50%"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 3 Summary",
                    "content": {
                        "text": "Population structure categorizes populations by age, gender, and geography. Young populations face high dependency and schooling costs, while ageing populations face labor shortages and pension burdens. Dependency ratios quantify this load."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 4: POPULATION DYNAMICS IN DEVELOPMENT (9 Pages)
# ==============================================================================
LESSON_4_DATA = {
    "unit_order": 4,
    "unit_name": "Population Dynamics in National Development",
    "lesson_title": "Population Growth and Socio-Economic Development Trade-offs",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Population and Development",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to analyze both the positive and negative implications of rapid population growth on economic development, and evaluate the economic impact of rural-urban migration."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Double-Edged Sword of Growth",
                    "content": {
                        "text": "Rapid population growth is a double-edged sword. On one hand, it creates a massive consumer market and provides an abundant labor supply. On the other hand, if growth outstrips capital accumulation, it leads to poverty, unemployment, and environmental degradation."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Positive Implications of Population Growth",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Four Economic Benefits of Population Growth",
                    "content": {
                        "text": "1. Wider Domestic Market: A growing population increases aggregate consumer demand for food, housing, clothing, and services, allowing firms to enjoy economies of scale.\n2. Abundant Labor Supply: Expands the national labor pool, preventing wage inflation and providing workers for manufacturing, agriculture, and services.\n3. Pressure for Innovation: Resource scarcity forces society to develop efficient new technologies, such as irrigation and solar power.\n4. Talent & Skill Diversity: A larger population yields greater intellectual diversity, entrepreneurship, and specialized expertise."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Large-Scale Public Capital Investment",
                    "content": IMG_SGR_INFRASTRUCTURE
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Negative Implications of Rapid Population Growth",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Five Macroeconomic Risks of Rapid Growth",
                    "content": {
                        "text": "1. Falling Per-Capita Income: When population grows faster than national output (GDP), average living standards decline.\n2. High Dependency Burden: High youth population forces families and government to spend heavily on consumption rather than savings and capital accumulation.\n3. Massive Unemployment: Labor supply outpaces job creation capacity.\n4. Overstretching of Social Amenities: Severe congestion in public hospitals, schools, water supply, and transport networks.\n5. Environmental Degradation: Deforestation, soil erosion, and pollution caused by pressure on land."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Comparative Trade-offs Matrix",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "Socio-Economic Impacts of Rapid Population Growth",
                    "content": {
                        "headers": ["Economic Sector", "Positive Potential", "Negative Risk if Unchecked"],
                        "rows": [
                            ["Domestic Market", "Expands sales volume and business profitability", "Demand outstrips supply, fueling inflation"],
                            ["Labor Market", "Provides abundant and affordable manpower", "Severe youth unemployment and underemployment"],
                            ["National Budget", "Expands future tax base as youth grow up", "Current funds diverted to schools and clinics"],
                            ["Savings & Investment", "Larger pool of future corporate investors", "Low household savings due to high daily consumption"],
                            ["Environment & Land", "Stimulates agricultural intensification and innovation", "Deforestation, land fragmentation, and urban slums"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Rural-Urban Migration Dynamics",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Push and Pull Factors of Urbanization",
                    "content": {
                        "text": "Rural-urban migration is the movement of people from countryside villages to cities (such as Nairobi, Mombasa, Kisumu, Nakuru):\n- Push Factors (Rural): Land fragmentation, lack of electricity/paved roads, seasonal drought, and lack of non-farm employment.\n- Pull Factors (Urban): Perception of abundant white-collar jobs, better educational institutions, modern entertainment, and superior healthcare facilities."
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Consequences of Rapid Urbanization",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Urban Congestion vs Rural Agricultural Decline",
                    "content": {
                        "text": "- Urban Consequences: Proliferation of informal settlements (slums), increased urban crime, traffic gridlock, overstretched sewage systems, and high open urban unemployment.\n- Rural Consequences: Loss of energetic, educated young labor in farming villages, leaving agricultural land underutilized and managed by the elderly."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Policy Case Study: Balanced Regional Planning",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Mitigating Spatial Imbalance in Kenya",
                    "content": {
                        "text": "To curb the negative effects of rural-urban migration, Kenya implements regional balance policies:\n1. Rural Electrification: Supplying power to trading centers to support welding, salons, and agro-processing.\n2. County Devolution: Channeling 15%+ of national revenue to the 47 county headquarters, creating administrative and commercial hubs outside Nairobi.\n3. Road Infrastructure: Tarmacking rural access roads so farmers can transport produce easily to markets."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Worked Analysis: Evaluating Growth Scenarios",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Scenario: Policy Response to Rapid Urban Growth",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Situation", "description": "City N experiences a 7% annual influx of rural school leavers, leading to 25% youth unemployment and mushrooming slums."},
                            {"title": "Step 2: Required Policy", "description": "Propose two targeted policy measures to resolve the urban crisis at its root."},
                            {"title": "Step 3: Root Cause Analysis", "description": "The crisis is driven by rural push factors (lack of rural jobs) and urban white-collar illusions."},
                            {"title": "Step 4: Policy Formulations", "description": "Policy 1: Establish rural agro-processing factories to absorb rural youth locally. Policy 2: Decentralize technical vocational institutes (TVETs) to provide localized employment skills."},
                            {"title": "Step 5: Verification", "description": "Targeting rural origins curbs the push factor, directly reducing city migration pressure."},
                            {"title": "Step 6: Economic Takeaway", "description": "Solving urban congestion requires investing in rural economic capacity."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Population and Development",
                    "content": {
                        "question": "Which of the following is a direct economic consequence of rapid rural-urban migration on the rural agrarian sector?",
                        "options": [
                            {"id": "a", "text": "Rapid expansion of modern rural tarmac highways"},
                            {"id": "b", "text": "Underutilization of fertile agricultural land due to the loss of energetic youth labor", "correct": True, "feedback": "Correct! When young, able-bodied workers migrate to cities, rural agriculture suffers from a severe labor deficit."},
                            {"id": "c", "text": "Immediate elimination of national youth unemployment"},
                            {"id": "d", "text": "Spike in rural household bank savings"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 4 Summary",
                    "content": {
                        "text": "Population growth expands market size and labor supply, but risks lowering per-capita income and overstretching amenities if uncontrolled. Rural-urban migration requires decentralized infrastructure and devolution to balance."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 5: EMPLOYMENT & TYPES/CAUSES OF UNEMPLOYMENT (11 Pages)
# ==============================================================================
LESSON_5_DATA = {
    "unit_order": 5,
    "unit_name": "Employment and Types & Causes of Unemployment",
    "lesson_title": "Labor Force Classification, 8 Types of Unemployment, and Root Causes",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Labor Economics",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to define employment, underemployment, unemployment, and the labor force, identify and distinguish the 8 types of unemployment, and analyze the root causes of unemployment in Kenya."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "The Economic Diagnostic of Unemployment",
                    "content": {
                        "text": "Unemployment is one of Kenya's most urgent economic challenges. Just as a doctor cannot prescribe treatment without diagnosing the exact disease, a government cannot solve unemployment without identifying its specific economic type and root cause."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Foundational Labor Definitions",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Core Labor Concepts",
                    "content": {
                        "term": "Employment vs Unemployment",
                        "definition": "Employment is engagement in any productive, income-generating economic activity. Unemployment is a state where working-age individuals who are physically fit, capable, and actively seeking work at the prevailing wage rate cannot secure jobs."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "definition_card",
                    "title": "Underemployment",
                    "content": {
                        "term": "Underemployment",
                        "definition": "A situation where a person is employed, but their labor capacity is underutilized, either in terms of working hours (time-based) or qualifications (skill-based, such as an engineering graduate working as a casual hand-cart puller)."
                    }
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "The Labor Force & Classification Tree",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Who Belongs in the Labor Force?",
                    "content": {
                        "text": "The Labor Force consists of all physically fit individuals within the productive age bracket (15–64 years) who are either currently employed or actively looking for work. It strictly excludes full-time students, retirees, the incapacitated, and discouraged workers who have stopped searching."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Classification of National Labor Resources",
                    "svg_content": SVG_LABOR_FORCE_CLASSIFICATION_TREE,
                    "content": {
                        "text": "Structural hierarchy diagram breaking down the total population into dependents and working-age cohorts, out-of-labor-force individuals, and active labor force."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Types of Unemployment: Seasonal & Frictional",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "1. Seasonal and 2. Frictional Unemployment",
                    "content": {
                        "text": "1. Seasonal Unemployment: Occurs when demand for labor fluctuates systematically according to climatic or holiday seasons (e.g. coffee/sugarcane cutters idle after harvesting, or beach resort tour guides in Mombasa idle during tourism low seasons).\n2. Frictional (Casual/Search) Unemployment: Temporary unemployment that arises when workers are in transition between leaving one job and securing a new one."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Types of Unemployment: Structural & Technological",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "3. Structural and 4. Technological Unemployment",
                    "content": {
                        "text": "3. Structural Unemployment: A severe, long-term mismatch between the skills job-seekers possess and the technical qualifications demanded by employers as the economy modernizes (e.g. manual typists unable to get programming jobs).\n4. Technological Unemployment: Occurs when workers are directly retrenched and replaced by automated machines, robotics, or computerized software."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Industrial Mechanization and Labor Demand",
                    "content": IMG_RUKURIRI_TEA_PROCESSING
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Types of Unemployment: Cyclical, Disguised & Others",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "5. Cyclical, 6. Disguised, 7. Residual & 8. Real-Wage",
                    "content": {
                        "text": "5. Cyclical (Demand-Deficient) Unemployment: Caused by general macroeconomic recessions when aggregate spending falls, forcing firms to lay off staff.\n6. Disguised (Hidden) Unemployment: Occurs when more workers are engaged than required; removing surplus workers leaves total output unchanged (e.g. 6 family members tilling a 1-acre plot that requires only 2).\n7. Residual Unemployment: Affects individuals with physical or mental disabilities that limit their employment.\n8. Real-Wage (Voluntary) Unemployment: Job-seekers refusing available work because market wages are lower than their personal wage expectations."
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "Master Unemployment Types Matrix",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "The Eight Types of Unemployment",
                    "content": {
                        "headers": ["Type of Unemployment", "Underlying Economic Cause", "Kenyan Real-World Example"],
                        "rows": [
                            ["Seasonal", "Periodic seasonal changes in production/climate", "Sugarcane harvesters idle during rainy off-season"],
                            ["Frictional", "Search time between job transitions", "A secondary school teacher who resigned to join another school"],
                            ["Structural", "Qualitative mismatch between worker skills and job vacancies", "Graduates with theoretical degrees unable to fill coding vacancies"],
                            ["Technological", "Workers replaced by automation and machinery", "Bank tellers retrenched after introduction of mobile apps and ATMs"],
                            ["Cyclical", "Macroeconomic depression and falling aggregate demand", "Hotel workers retrenched during an international economic recession"],
                            ["Disguised / Hidden", "Marginal productivity of extra workers is zero", "Excess family members working on a small subsistence farm"],
                            ["Residual", "Physical or mental disability constraints", "Persons with severe physical impairment lacking adapted workplaces"],
                            ["Real-Wage (Voluntary)", "Workers rejecting prevailing market wage rates", "A graduate refusing a Sh. 30,000 technician job holding out for 100k"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "Root Causes of Unemployment in Kenya",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Six Structural Drivers of Kenyan Unemployment",
                    "content": {
                        "text": "1. Rapid Population Growth: Annual growth of school-leavers exceeds the absorption capacity of the formal economy.\n2. Inappropriate Education Curriculum: Historical over-emphasis on theoretical white-collar credentials rather than practical vocational skills.\n3. Adoption of Capital-Intensive Methods: Use of imported heavy machinery in agriculture and manufacturing where manual labor could be hired.\n4. Seasonality of Key Sectors: Heavy dependence on rain-fed agriculture and tourism causing recurring off-season idleness.\n5. Rural-Urban Migration: Influx of job-seekers into major towns overwhelming urban industrial capacity.\n6. Shortage of Capital & Credit: High interest rates preventing small entrepreneurs from expanding and hiring others."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "Worked Analysis: Scenario-Based Unemployment Diagnostic",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Classification: Diagnosing Unemployment Cases",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Scenarios", "description": "Case A: A tea picker in Kericho has no work from January to March. Case B: An office clerk was retrenched after the firm installed computerized document management. Case C: A graduate holds an arts degree while firms only seek mechanical technicians."},
                            {"title": "Step 2: Required Diagnostic", "description": "Classify the exact type of unemployment in each case."},
                            {"title": "Step 3: Definitions", "description": "Climatic lull = Seasonal; Machine replacement = Technological; Skills mismatch = Structural."},
                            {"title": "Step 4: Classification", "description": "Case A: Seasonal Unemployment; Case B: Technological Unemployment; Case C: Structural Unemployment."},
                            {"title": "Step 5: Verification", "description": "Check: Case B is specifically direct machine replacement; Case C is broader qualitative skill misalignment."},
                            {"title": "Step 6: Economic Takeaway", "description": "Correct diagnosis enables targeted policy interventions."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Full Employment and the Natural Rate",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "What Does 'Full Employment' Really Mean?",
                    "content": {
                        "text": "In economics, full employment does NOT mean 0% unemployment. There will always be some frictional unemployment (people switching jobs) and seasonal fluctuations. Full employment is the state where all involuntarily unemployed people who desire to work at the prevailing wage have found jobs, with only unavoidable frictional search remaining."
                    }
                }
            ]
        },
        {
            "page_number": 11,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Types of Unemployment",
                    "content": {
                        "question": "Which type of unemployment occurs when manual packaging clerks are retrenched because the factory installed an automated robotic conveyor belt?",
                        "options": [
                            {"id": "a", "text": "Cyclical unemployment"},
                            {"id": "b", "text": "Technological unemployment", "correct": True, "feedback": "Correct! Technological unemployment occurs when workers are directly replaced by machines and automation."},
                            {"id": "c", "text": "Frictional unemployment"},
                            {"id": "d", "text": "Disguised unemployment"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 5 Summary",
                    "content": {
                        "text": "The labor force comprises employed and involuntarily unemployed working-age individuals. The 8 types of unemployment include seasonal, structural, technological, frictional, cyclical, disguised, residual, and real-wage, driven by rapid population growth and educational mismatches."
                    }
                }
            ]
        }
    ]
}

# ==============================================================================
# LESSON 6: SOLUTIONS TO UNEMPLOYMENT & KCSE MASTERY (10 Pages)
# ==============================================================================
LESSON_6_DATA = {
    "unit_order": 6,
    "unit_name": "Solutions to Unemployment & KCSE Mastery",
    "lesson_title": "Targeted Policy Interventions, Diversification, and KCSE Examination Mastery",
    "pages": [
        {
            "page_number": 1,
            "page_title": "Introduction to Policy Interventions",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "learning_goal",
                    "title": "Learning Goals",
                    "content": {
                        "text": "By the end of this lesson, you should be able to evaluate state policy measures to solve unemployment, map specific solutions to root causes, and master KCSE Paper 1 and Paper 2 compulsory examination questions."
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "A Multi-Pronged National Strategy",
                    "content": {
                        "text": "There is no single magic bullet for unemployment. A successful national policy must combine quantitative measures (attracting investment to build factories) with qualitative measures (reforming the education curriculum so citizens can work in those factories)."
                    }
                }
            ]
        },
        {
            "page_number": 2,
            "page_title": "Core Policy Solutions (Part 1)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Education Reform & Enterprise Credit",
                    "content": {
                        "text": "1. Reforming Education Curriculum (TVET & CBC): Shifting from pure theoretical academia to technical, vocational, and entrepreneurship training to eliminate structural unemployment.\n2. Promoting Self-Employment and SME Funding: Providing low-interest revolving credit through state funds (Youth Enterprise Development Fund - YEDF, Women Enterprise Fund - WEF, Uwezo Fund) to turn job-seekers into job-creators."
                    }
                },
                {
                    "block_type": "suggested_image",
                    "component_type": "photo_view",
                    "title": "Technical and Vocational Skills Training",
                    "content": IMG_JUA_KALI_INFORMAL
                }
            ]
        },
        {
            "page_number": 3,
            "page_title": "Core Policy Solutions (Part 2)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Rural Development, Labor Intensity & Diversification",
                    "content": {
                        "text": "3. Rural Delocalization & Electrification: Providing tarmac roads, clean water, and electricity to rural towns to decentralize industries and curb rural-urban migration.\n4. Encouraging Labor-Intensive Public Works: Prioritizing manual labor over imported machinery in road construction and dam building to absorb unskilled workers.\n5. Agro-Processing & Diversification: Establishing agricultural processing factories to convert raw crops into packaged goods, creating year-round manufacturing jobs that eliminate seasonal lulls."
                    }
                },
                {
                    "block_type": "suggested_diagram",
                    "component_type": "svg_viewer",
                    "title": "Cause-to-Solution Policy Alignment",
                    "svg_content": SVG_UNEMPLOYMENT_POLICY_MATRIX,
                    "content": {
                        "text": "Matrix mapping specific unemployment causes (skills mismatch, capital shortage, rural migration, seasonality) to targeted state policy responses."
                    }
                }
            ]
        },
        {
            "page_number": 4,
            "page_title": "Core Policy Solutions (Part 3)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Foreign Investment & Population Planning",
                    "content": {
                        "text": "6. Attracting Foreign Direct Investment (FDI): Creating Export Processing Zones (EPZs), offering tax holidays, and maintaining political stability to encourage multinational companies to establish manufacturing plants in Kenya.\n7. Population Growth Control: Encouraging family planning and small-family norms to bring population growth into balance with national economic expansion."
                    }
                }
            ]
        },
        {
            "page_number": 5,
            "page_title": "Cause-to-Solution Matching Matrix",
            "blocks": [
                {
                    "block_type": "comparison_table",
                    "component_type": "table_view",
                    "title": "Mapping Unemployment Causes to Targeted Interventions",
                    "content": {
                        "headers": ["Root Cause of Unemployment", "Targeted Policy Measure", "Operational Mechanism"],
                        "rows": [
                            ["White-collar syllabus bias", "Curriculum reform (TVET / CBC)", "Teaches practical carpentry, electrical, and programming trades"],
                            ["Lack of business capital", "Youth Enterprise Fund (YEDF)", "Disburses interest-free and concessionary startup loans"],
                            ["Rural-urban migration", "Rural electrification & infrastructure", "Creates attractive rural industrial hubs; reduces city slum drift"],
                            ["Seasonality of agriculture", "Agro-processing factories", "Processes tea/coffee into packaged products year-round"],
                            ["Capital-intensive mechanization", "Labor-intensive public procurement", "Government mandates manual labor for road desilting and trenching"],
                            ["Rapid population explosion", "Family planning and reproductive healthcare", "Aligns population growth rate with national GDP creation rate"]
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 6,
            "page_title": "Policy Simulation Case Study",
            "blocks": [
                {
                    "block_type": "worked_example",
                    "component_type": "step_process",
                    "title": "Worked Scenario: Resolving Seasonal Unemployment in a Tea Constituency",
                    "content": {
                        "steps": [
                            {"title": "Step 1: Given Scenario", "description": "In a tea-growing rural constituency, 5,000 youths are unemployed for 4 months annually during the dry agricultural lull. The MP proposes building an automated packaging factory."},
                            {"title": "Step 2: Required Evaluation", "description": "Evaluate the proposal's benefits and identify its major structural risk."},
                            {"title": "Step 3: Economic Principles", "description": "Agro-processing diversifies agriculture into year-round manufacturing, but heavy automation creates technological replacement."},
                            {"title": "Step 4: Evaluation", "description": "Benefit: Agro-processing provides year-round industrial employment. Risk: If the factory is fully automated, it will employ only 10 technicians, leaving the 5,000 youths jobless."},
                            {"title": "Step 5: Alternative Recommendation", "description": "The MP should mandate labor-intensive manual packaging and establish a local TVET center to train youth in factory maintenance."},
                            {"title": "Step 6: Economic Takeaway", "description": "Agro-processing must be paired with labor-intensive techniques to maximize employment absorption."}
                        ]
                    }
                }
            ]
        },
        {
            "page_number": 7,
            "page_title": "KCSE Paper 1 Short-Answer Practice",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "Compulsory Short-Answer Practice & Model Answers",
                    "content": {
                        "text": "Question 1: Distinguish between optimum population and under-population. (4 Marks)\n- Model Answer: Optimum population is the population size that generates the highest possible per-capita standard of living with available resources. Under-population is where the population is too small relative to resources, leaving resources underutilized.\n\nQuestion 2: State four factors that contribute to a declining birth rate in a country. (4 Marks)\n- Model Answer: (1) Delayed marriages due to career/education; (2) Desire for a higher standard of living; (3) Reduced infant mortality; (4) Access to modern family planning methods.\n\nQuestion 3: Calculate the dependency ratio for a village of 3,000 children (0–14), 5,000 working adults (15–64), and 1,000 elderly (65+). (4 Marks)\n- Model Answer: Total Dependents = 3,000 + 1,000 = 4,000. Dependency Ratio = (4,000 ÷ 5,000) × 100 = 80%."
                    }
                }
            ]
        },
        {
            "page_number": 8,
            "page_title": "KCSE Paper 2 Essay Mastery (Young Population)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "KCSE Essay Model Answer: Challenges of a Young Population",
                    "content": {
                        "text": "Essay Question: Explain five challenges that Country K might experience if its population has a very high proportion of young people aged 0–14 years. (10 Marks)\n\nModel Answer:\n1. High Dependency Burden: A large child cohort means few working adults must support many dependents, reducing household standard of living.\n2. Diversion of Public Resources: State expenditure is diverted to consumption amenities (schools, pediatric care) rather than capital investments (railways, energy grids).\n3. Low National Savings: Families spend almost all income on immediate needs (food, clothing, tuition), lowering bank savings and loanable funds.\n4. Future Unemployment Crisis: The large child cohort will soon flood the labor market, putting immense pressure on job creation.\n5. High Import Bill: Children are non-productive consumers, forcing the country to import medicines, food, and books, worsening balance-of-payments deficits."
                    }
                }
            ]
        },
        {
            "page_number": 9,
            "page_title": "KCSE Paper 2 Essay Mastery (Structural Unemployment)",
            "blocks": [
                {
                    "block_type": "text",
                    "component_type": "concept_card",
                    "title": "KCSE Essay Model Answer: Measures to Curb Structural Unemployment",
                    "content": {
                        "text": "Essay Question: Explain five practical measures that the Kenyan government can take to curb high structural unemployment. (10 Marks)\n\nModel Answer:\n1. Education Curriculum Reform (TVET / CBC): Reorienting the syllabus from pure theory to technical and vocational training, equipping graduates with hands-on skills matching employer vacancies.\n2. Funding Self-Employment: Providing affordable startup capital through the Youth Enterprise Development Fund to turn job-seekers into enterprise owners.\n3. Decentralization of Industries (Rural Electrification): Establishing rural infrastructure to encourage factories to locate in the countryside, creating jobs where youth reside.\n4. Labor-Market Information Centers: Creating digital national job databases to connect job-seekers with employers, minimizing informational mismatch.\n5. Attracting Foreign Direct Investment: Creating tax incentives and export zones to attract multinational manufacturing plants, expanding skilled technical jobs."
                    }
                }
            ]
        },
        {
            "page_number": 10,
            "page_title": "Knowledge Check & Unit Summary",
            "blocks": [
                {
                    "block_type": "knowledge_check",
                    "component_type": "mcq_interactive",
                    "title": "Check Your Understanding: Solutions to Unemployment",
                    "content": {
                        "question": "Which of the following policy measures is specifically designed to eliminate structural unemployment caused by a skills mismatch?",
                        "options": [
                            {"id": "a", "text": "Reforming the educational syllabus to emphasize technical, vocational (TVET), and competency-based training", "correct": True, "feedback": "Correct! Reforming education aligns graduates' practical skills with actual industrial requirements, eliminating structural mismatch."},
                            {"id": "b", "text": "Importing automated robotic conveyor belts for all factories"},
                            {"id": "c", "text": "Increasing personal income tax rates on all formal employees"},
                            {"id": "d", "text": "Raising the retirement age from 60 to 75 years"}
                        ]
                    }
                },
                {
                    "block_type": "text",
                    "component_type": "summary_card",
                    "title": "Lesson 6 Summary",
                    "content": {
                        "text": "Solving unemployment requires education reform (TVET/CBC), enterprise credit (YEDF), rural electrification, labor-intensive works, agro-processing, and foreign investment. Mastering these solutions is essential for KCSE Papers 1 and 2."
                    }
                }
            ]
        }
    ]
}
