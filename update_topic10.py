import re

with open("curriculum/topic10_data.py", "r") as f:
    content = f.read()

# Fix bullets
content = content.replace("• ", "- ")

# Update Images
images_replacement = """# Verified Wikimedia photographic assets
IMG_WANGIGE_MARKET = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg",
    "text": "Wangige local market in Kiambu County — a typical Kenyan retail market where cash and credit transactions take place daily.",
    "author": "Kristinabudiati",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg"
}

IMG_ANALYZING_FINANCIAL_DATA = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
    "text": "A person analysing financial data and tracking the effects of business transactions on the balance sheet equations.",
    "author": "Dave Dugdale",
    "licensing": "CC BY-SA 2.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Analyzing_Financial_Data_(5099605109).jpg"
}

IMG_JUA_KALI_POTS = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/b/be/Jua_Kali_cooking_pots.jpg",
    "text": "Jua Kali-made aluminium cooking pots ready for sale — representing business inventory and owner's capital investment.",
    "author": "Leonard Kisuu",
    "licensing": "CC BY-SA 4.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Jua_Kali_cooking_pots.jpg"
}
"""

content = re.sub(r'# Verified Wikimedia photographic assets.*?# ==============================================================================', images_replacement + '\n# ==============================================================================', content, flags=re.DOTALL)

# Add photo to Lesson 1, Page 1
content = re.sub(
    r'("page_number": 1,\s*"page_title": "Introduction to Business Transactions",\s*"blocks": \[)',
    r'\1\n                {\n                    "block_type": "suggested_image",\n                    "component_type": "photo_view",\n                    "title": "Cash Transactions at the Market",\n                    "content": IMG_WANGIGE_MARKET\n                },',
    content
)

# Add photo to Lesson 2, Page 1
content = re.sub(
    r'("page_number": 1,\s*"page_title": "Introduction to Balance Sheet Adjustments",\s*"blocks": \[)',
    r'\1\n                {\n                    "block_type": "suggested_image",\n                    "component_type": "photo_view",\n                    "title": "Tracking Balance Sheet Adjustments",\n                    "content": IMG_ANALYZING_FINANCIAL_DATA\n                },',
    content
)

# Add photo to Lesson 3, Page 1
content = re.sub(
    r'("page_number": 1,\s*"page_title": "Introduction to Capital Changes",\s*"blocks": \[)',
    r'\1\n                {\n                    "block_type": "suggested_image",\n                    "component_type": "photo_view",\n                    "title": "Capital and Inventory",\n                    "content": IMG_JUA_KALI_POTS\n                },',
    content
)

# Replace remaining IMG references inside
content = content.replace("IMG_MOBILE_PAYMENT", "IMG_WANGIGE_MARKET")
content = content.replace("IMG_RETAIL_CHECKOUT", "IMG_WANGIGE_MARKET") # Unlikely used but just in case
content = content.replace("IMG_JUA_KALI_INVESTMENT", "IMG_JUA_KALI_POTS")

# Fix Learning Goals
content = content.replace(
    '"text": "By the end of this lesson, you should be able to define what a business transaction is, distinguish clearly between cash and credit transactions, identify accepted payment mediums, and spot textbook typographical duplication."',
    '"goals": [\n                            "Define what a business transaction is",\n                            "Distinguish clearly between cash and credit transactions",\n                            "Identify accepted payment mediums",\n                            "Spot textbook typographical duplication"\n                        ]'
)
content = content.replace(
    '"text": "By the end of this lesson, you should be able to explain how transactions alter balance sheet items, describe the 3 rules governing balance sheet adjustments, and trace transactions step-by-step to construct a final balanced Balance Sheet."',
    '"goals": [\n                            "Explain how transactions alter balance sheet items",\n                            "Describe the 3 rules governing balance sheet adjustments",\n                            "Trace transactions step-by-step to construct a final balanced Balance Sheet"\n                        ]'
)
content = content.replace(
    '"text": "By the end of this lesson, you should be able to explain the four causes of capital changes, state and manipulate the capital tracking equation, calculate initial capital, final capital, drawings, investments, or profits, and master KCSE essay answers."',
    '"goals": [\n                            "Explain the four causes of capital changes",\n                            "State and manipulate the capital tracking equation",\n                            "Calculate initial capital, final capital, drawings, investments, or profits",\n                            "Master KCSE essay answers"\n                        ]'
)

# Semantic Component Upgrades
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Watch Out: Cheque Misconception"',
    '"component_type": "common_mistake",\n                    "title": "Watch Out: Cheque Misconception"'
)
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Watch Out: Dual Expansion"',
    '"component_type": "common_mistake",\n                    "title": "Watch Out: Dual Expansion"'
)
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Watch Out: Non-Cash Investments"',
    '"component_type": "common_mistake",\n                    "title": "Watch Out: Non-Cash Investments"'
)
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "KCSE Paper 1 Ledger Effects Table"',
    '"component_type": "key_takeaway",\n                    "title": "KCSE Paper 1 Ledger Effects Table"'
)

with open("curriculum/topic10_data.py", "w") as f:
    f.write(content)
