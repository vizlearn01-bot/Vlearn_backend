import re

with open("curriculum/topic9_data.py", "r") as f:
    content = f.read()

# Fix bullets
content = content.replace("• ", "- ")

# 1. Update Images at the top
images_replacement = """# Verified Wikimedia photographic assets
IMG_JUA_KALI_FABRICATOR = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Jua_Kali_fabricator.jpg",
    "text": "A Jua Kali artisan fabricating metalwork in Nairobi's informal manufacturing sector, illustrating owner capital investment and machinery fixed assets.",
    "author": "Harold Odhiambo Otieno",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_fabricator.jpg"
}

IMG_ANALYZING_FINANCIAL_DATA = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
    "text": "A person analysing financial data and spreadsheets, working through balance sheet calculations and balance equations.",
    "author": "Dave Dugdale",
    "licensing": "CC BY-SA 2.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Analyzing_Financial_Data_(5099605109).jpg"
}

IMG_ACCOUNTANT_DESK = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/b/bc/The_Accountants_desks_%283817577217%29.jpg",
    "text": "An accounting office with organised workstations, showing the formal environment for balance sheet preparation and solvency assessment.",
    "author": "Kristin Dos Santos",
    "licensing": "CC BY-SA 2.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:The_Accountants_desks_(3817577217).jpg"
}
"""
content = re.sub(r'# Verified Wikimedia photographic assets.*?# ==============================================================================', images_replacement + '\n# ==============================================================================', content, flags=re.DOTALL)

# Add photo to Lesson 1, Page 1
content = re.sub(
    r'("page_number": 1,\s*"page_title": "Introduction to Bookkeeping and Accounting",\s*"blocks": \[)',
    r'\1\n                {\n                    "block_type": "suggested_image",\n                    "component_type": "photo_view",\n                    "title": "Jua Kali Business Assets",\n                    "content": IMG_JUA_KALI_FABRICATOR\n                },',
    content
)

# Add photo to Lesson 2, Page 1
content = re.sub(
    r'("page_number": 1,\s*"page_title": "Introduction to the Bookkeeping Equation",\s*"blocks": \[)',
    r'\1\n                {\n                    "block_type": "suggested_image",\n                    "component_type": "photo_view",\n                    "title": "Analyzing Balance Equations",\n                    "content": IMG_ANALYZING_FINANCIAL_DATA\n                },',
    content
)

# Add photo to Lesson 3, Page 1
content = re.sub(
    r'("page_number": 1,\s*"page_title": "Introduction to the Balance Sheet",\s*"blocks": \[)',
    r'\1\n                {\n                    "block_type": "suggested_image",\n                    "component_type": "photo_view",\n                    "title": "Formal Balance Sheet Preparation",\n                    "content": IMG_ACCOUNTANT_DESK\n                },',
    content
)

# Fix mismatched images inside the file (e.g., IMG_COMMERCIAL_BANKING, IMG_LOCAL_MARKET_RETAIL, etc.)
# If they are removed, we must remove them from block references or replace them.
# The user said: fix these existing mismatched image assignments.
# In topic 9, page 3 has: IMG_LOCAL_MARKET_RETAIL -> let's change it to IMG_JUA_KALI_FABRICATOR (since it shows assets)
content = content.replace("IMG_LOCAL_MARKET_RETAIL", "IMG_JUA_KALI_FABRICATOR")
content = content.replace("IMG_COMMERCIAL_BANKING", "IMG_ACCOUNTANT_DESK")

# Fix Learning Goals
content = content.replace(
    '"text": "By the end of this lesson, you should be able to explain the meaning of bookkeeping and transactions, define and classify debtors, creditors, and goods, classify assets into fixed and current, classify liabilities into long-term and current, and define capital."',
    '"goals": [\n                            "Explain the meaning of bookkeeping and transactions",\n                            "Define and classify debtors, creditors, and goods",\n                            "Classify assets into fixed and current",\n                            "Classify liabilities into long-term and current",\n                            "Define capital"\n                        ]'
)
content = content.replace(
    '"text": "By the end of this lesson, you should be able to state and derive the Bookkeeping Equation (Accounting Equation), manipulate it algebraically to solve for Assets (A), Capital (C), or Liabilities (L), and address source typographical inconsistencies."',
    '"goals": [\n                            "State and derive the Bookkeeping Equation (Accounting Equation)",\n                            "Manipulate it algebraically to solve for Assets (A), Capital (C), or Liabilities (L)",\n                            "Address source typographical inconsistencies"\n                        ]'
)
content = content.replace(
    '"text": "By the end of this lesson, you should be able to define a Balance Sheet and its heading rules, prepare a structured Balance Sheet, distinguish between solvency and insolvency, define Net Worth, and list uses for five stakeholders."',
    '"goals": [\n                            "Define a Balance Sheet and its heading rules",\n                            "Prepare a structured Balance Sheet",\n                            "Distinguish between solvency and insolvency",\n                            "Define Net Worth",\n                            "List uses for five stakeholders"\n                        ]'
)

# Fix Worked Examples (Steps format)
# "text": "Problem: Find missing variables W, X, and Y:\nBusiness A: Assets = 620,000; Liabilities = 230,000. Find Capital (W).\nBusiness B: Capital = 400,000; Liabilities = 120,000. Find Assets (X).\nBusiness C: Assets = 800,000; Capital = 500,000. Find Liabilities (Y).\n\nSolution:\nStep 1 (Business A): W = A - L = 620,000 - 230,000 = Sh. 390,000.\nStep 2 (Business B): X = C + L = 400,000 + 120,000 = Sh. 520,000.\nStep 3 (Business C): Y = A - C = 800,000 - 500,000 = Sh. 300,000.\nStep 4: Check balance: Business A: 390k + 230k = 620k [OK]; Business B: 520k - 120k = 400k [OK]; Business C: 500k + 300k = 800k [OK]."
content = content.replace(
    '"text": "Problem: Find missing variables W, X, and Y:\\nBusiness A: Assets = 620,000; Liabilities = 230,000. Find Capital (W).\\nBusiness B: Capital = 400,000; Liabilities = 120,000. Find Assets (X).\\nBusiness C: Assets = 800,000; Capital = 500,000. Find Liabilities (Y).\\n\\nSolution:\\nStep 1 (Business A): W = A - L = 620,000 - 230,000 = Sh. 390,000.\\nStep 2 (Business B): X = C + L = 400,000 + 120,000 = Sh. 520,000.\\nStep 3 (Business C): Y = A - C = 800,000 - 500,000 = Sh. 300,000.\\nStep 4: Check balance: Business A: 390k + 230k = 620k [OK]; Business B: 520k - 120k = 400k [OK]; Business C: 500k + 300k = 800k [OK]."',
    '"intro": "Problem: Find missing variables W, X, and Y:\\nBusiness A: Assets = 620,000; Liabilities = 230,000. Find Capital (W).\\nBusiness B: Capital = 400,000; Liabilities = 120,000. Find Assets (X).\\nBusiness C: Assets = 800,000; Capital = 500,000. Find Liabilities (Y).",\n                        "steps": [\n                            "Step 1 (Business A): W = A - L = 620,000 - 230,000 = Sh. 390,000.",\n                            "Step 2 (Business B): X = C + L = 400,000 + 120,000 = Sh. 520,000.",\n                            "Step 3 (Business C): Y = A - C = 800,000 - 500,000 = Sh. 300,000.",\n                            "Step 4: Check balance: Business A: 390k + 230k = 620k [OK]; Business B: 520k - 120k = 400k [OK]; Business C: 500k + 300k = 800k [OK]."\n                        ]'
)

# Gichuru Traders
content = content.replace(
    '"text": "Problem: Gichuru Traders has Fixed Assets of Sh. 450,000, Current Assets of Sh. 120,000, and owes Creditors Sh. 80,000. Calculate Capital.\\n\\nSolution:\\nStep 1: Total Assets = Fixed Assets + Current Assets = 450,000 + 120,000 = Sh. 570,000.\\nStep 2: Capital = Total Assets - Liabilities = 570,000 - 80,000 = Sh. 490,000."',
    '"intro": "Problem: Gichuru Traders has Fixed Assets of Sh. 450,000, Current Assets of Sh. 120,000, and owes Creditors Sh. 80,000. Calculate Capital.",\n                        "steps": [\n                            "Step 1: Total Assets = Fixed Assets + Current Assets = 450,000 + 120,000 = Sh. 570,000.",\n                            "Step 2: Capital = Total Assets - Liabilities = 570,000 - 80,000 = Sh. 490,000."\n                        ]'
)

# 9-Item Retail Shop
content = content.replace(
    '"text": "Problem: Extracted items: Premises 1.2M, Vehicles 800k, Stock 150k, Debtors 90k, Bank 210k, Cash 40k, 5-Yr Loan 600k, Creditors 120k, Accrued Electricity 10k.\\nCalculate: a) Fixed Assets b) Current Assets c) Long-Term Liabilities d) Short-Term Liabilities e) Capital\\n\\nSolution:\\na) Fixed Assets = 1.2M + 800k = Sh. 2,000,000\\nb) Current Assets = 150k + 90k + 210k + 40k = Sh. 490,000\\n   Total Assets = 2M + 490k = Sh. 2,490,000\\nc) Long-Term Liabilities = 5-Yr Loan = Sh. 600,000\\nd) Short-Term Liabilities = 120k + 10k = Sh. 130,000\\n   Total Liabilities = 600k + 130k = Sh. 730,000\\ne) Capital = Total Assets - Total Liabilities = 2,490,000 - 730,000 = Sh. 1,760,000."',
    '"intro": "Problem: Extracted items: Premises 1.2M, Vehicles 800k, Stock 150k, Debtors 90k, Bank 210k, Cash 40k, 5-Yr Loan 600k, Creditors 120k, Accrued Electricity 10k.\\nCalculate: a) Fixed Assets b) Current Assets c) Long-Term Liabilities d) Short-Term Liabilities e) Capital",\n                        "steps": [\n                            "a) Fixed Assets = 1.2M + 800k = Sh. 2,000,000",\n                            "b) Current Assets = 150k + 90k + 210k + 40k = Sh. 490,000\\n   Total Assets = 2M + 490k = Sh. 2,490,000",\n                            "c) Long-Term Liabilities = 5-Yr Loan = Sh. 600,000",\n                            "d) Short-Term Liabilities = 120k + 10k = Sh. 130,000\\n   Total Liabilities = 600k + 130k = Sh. 730,000",\n                            "e) Capital = Total Assets - Total Liabilities = 2,490,000 - 730,000 = Sh. 1,760,000."\n                        ]'
)

# Wasco Traders Balance Sheet as at 30th Oct 1995
content = content.replace(
    '"text": "Problem: Extract: Cash 20,520; Bank 160,230; Premises 800,000; Debtors 40,000; Creditors 62,500; 2-Yr Loan 40,000; Stock 2,500.\\n\\nSolution:\\nLeft Side (Assets):\\nFixed: Premises = 800,000\\nCurrent: Stock (2,500) + Debtors (40,000) + Bank (160,230) + Cash (20,520) = 223,250\\nTotal Assets = Sh. 1,023,250\\n\\nRight Side (Capital & Liabilities):\\nTotal Liabilities = 40,000 + 62,500 = 102,500\\nCapital (Net Worth) = 1,023,250 - 102,500 = Sh. 920,750\\nTotal Capital & Liabilities = 920,750 + 40,000 + 62,500 = Sh. 1,023,250 [BALANCED!]"',
    '"intro": "Problem: Extract: Cash 20,520; Bank 160,230; Premises 800,000; Debtors 40,000; Creditors 62,500; 2-Yr Loan 40,000; Stock 2,500.",\n                        "steps": [\n                            "Left Side (Assets):\\nFixed: Premises = 800,000\\nCurrent: Stock (2,500) + Debtors (40,000) + Bank (160,230) + Cash (20,520) = 223,250\\nTotal Assets = Sh. 1,023,250",\n                            "Right Side (Capital & Liabilities):\\nTotal Liabilities = 40,000 + 62,500 = 102,500\\nCapital (Net Worth) = 1,023,250 - 102,500 = Sh. 920,750\\nTotal Capital & Liabilities = 920,750 + 40,000 + 62,500 = Sh. 1,023,250 [BALANCED!]"\n                        ]'
)

# Mile Traders Balance Sheet (Net Profit Included)
content = content.replace(
    '"text": "Problem: Stock 100k, Capital 800k, Debtors 50k, Creditors 80k, Cash 10k, Net Profit 10k, Overdraft 70k, Machines 600k, Furniture 200k.\\n\\nSolution:\\nLeft Side (Assets): Machines (600k) + Furniture (200k) + Stock (100k) + Debtors (50k) + Cash (10k) = Sh. 960,000.\\nRight Side (Capital & Liabilities): Adjusted Capital = Capital (800k) + Net Profit (10k) = 810k. Liabilities = Creditors (80k) + Overdraft (70k) = 150k. Total = 810k + 150k = Sh. 960,000 [BALANCED!]"',
    '"intro": "Problem: Stock 100k, Capital 800k, Debtors 50k, Creditors 80k, Cash 10k, Net Profit 10k, Overdraft 70k, Machines 600k, Furniture 200k.",\n                        "steps": [\n                            "Left Side (Assets): Machines (600k) + Furniture (200k) + Stock (100k) + Debtors (50k) + Cash (10k) = Sh. 960,000.",\n                            "Right Side (Capital & Liabilities): Adjusted Capital = Capital (800k) + Net Profit (10k) = 810k. Liabilities = Creditors (80k) + Overdraft (70k) = 150k. Total = 810k + 150k = Sh. 960,000 [BALANCED!]"\n                        ]'
)

# Semantic Component Upgrades
# Lesson 1, Page 8: Watch Out: Debtors vs Creditors Memory Trick (memory_tip or common_mistake? "memory_tip" and "common_mistake" were mentioned)
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Watch Out: Debtors vs Creditors"',
    '"component_type": "memory_tip",\n                    "title": "Watch Out: Debtors vs Creditors"'
)

# Lesson 2, Page 3: Source Typo Corrections -> common_mistake
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Source Typo Warnings"',
    '"component_type": "common_mistake",\n                    "title": "Source Typo Warnings"'
)

# Lesson 2, Page 8: Watch Out: Dual Transaction Impact -> common_mistake
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Watch Out: Dual Transaction Impact"',
    '"component_type": "common_mistake",\n                    "title": "Watch Out: Dual Transaction Impact"'
)

# Lesson 3, Page 8: Watch Out: Heading Terminology -> common_mistake
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Watch Out: Heading Terminology"',
    '"component_type": "common_mistake",\n                    "title": "Watch Out: Heading Terminology"'
)

# KCSE paper blocks -> key_takeaway
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "KCSE Paper 1 Short-Answer Mastery"',
    '"component_type": "key_takeaway",\n                    "title": "KCSE Paper 1 Short-Answer Mastery"'
)

with open("curriculum/topic9_data.py", "w") as f:
    f.write(content)

