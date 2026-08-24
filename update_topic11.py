import re

with open("curriculum/topic11_data.py", "r") as f:
    content = f.read()

# Fix bullets
content = content.replace("• ", "- ")

# Update Images
images_replacement = """# Verified Wikimedia photographic assets
IMG_LEDGER_BOOK = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/d/d0/Camp_Chesterfield_general_account_ledger%2C_1910-1916_-_DPLA_-_206e8c73ecb9419118717c75562a2497_%28page_1%29.jpg",
    "text": "A handwritten general account ledger — showing the traditional T-account format with debit and credit columns used in double-entry bookkeeping.",
    "author": "Public Domain (DPLA)",
    "licensing": "Public domain",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Camp_Chesterfield_general_account_ledger,_1910-1916_-_DPLA_-_206e8c73ecb9419118717c75562a2497_(page_1).jpg"
}

IMG_MILLINERY_LEDGER = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/4/40/Millinery_Book_Ledger_-_DPLA_-_4e890e62dfe17d454d28440b56c6c3e4.jpg",
    "text": "A historical business ledger book showing organised financial account entries — the foundation of all double-entry bookkeeping.",
    "author": "Clark, William Samuel (1846-1923)",
    "licensing": "Public domain",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Millinery_Book_Ledger_-_DPLA_-_4e890e62dfe17d454d28440b56c6c3e4.jpg"
}

IMG_ACCOUNTANT_DESK = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/b/bc/The_Accountants_desks_%283817577217%29.jpg",
    "text": "An accounting office with organised workstations — representing systematic bookkeeping and financial record management.",
    "author": "Kristin Dos Santos",
    "licensing": "CC BY-SA 2.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:The_Accountants_desks_(3817577217).jpg"
}

IMG_ANALYZING_FINANCIAL_DATA = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg",
    "text": "A person analysing financial data and spreadsheets — representing the process of preparing and reviewing financial accounts.",
    "author": "Dave Dugdale",
    "licensing": "CC BY-SA 2.0",
    "commons_page_url": "https://commons.wikimedia.org/wiki/File:Analyzing_Financial_Data_(5099605109).jpg"
}
"""

content = re.sub(r'# Verified Wikimedia photographic assets.*?# ==============================================================================', images_replacement + '\n# ==============================================================================', content, flags=re.DOTALL)

# Add photo to Lesson 1, Page 1
content = re.sub(
    r'("page_number": 1,\s*"page_title": "Introduction to Ledgers and Accounts",\s*"blocks": \[)',
    r'\1\n                {\n                    "block_type": "suggested_image",\n                    "component_type": "photo_view",\n                    "title": "General Account Ledger",\n                    "content": IMG_LEDGER_BOOK\n                },',
    content
)

# Add photo to Lesson 2, Page 1
content = re.sub(
    r'("page_number": 1,\s*"page_title": "Introduction to Posting Rules",\s*"blocks": \[)',
    r'\1\n                {\n                    "block_type": "suggested_image",\n                    "component_type": "photo_view",\n                    "title": "Organized Financial Entries",\n                    "content": IMG_MILLINERY_LEDGER\n                },',
    content
)

# Add photo to Lesson 3, Page 1
content = re.sub(
    r'("page_number": 1,\s*"page_title": "Introduction to Balancing Accounts",\s*"blocks": \[)',
    r'\1\n                {\n                    "block_type": "suggested_image",\n                    "component_type": "photo_view",\n                    "title": "Accountant Workspace",\n                    "content": IMG_ACCOUNTANT_DESK\n                },',
    content
)

# Add photo to Lesson 4, Page 1
content = re.sub(
    r'("page_number": 1,\s*"page_title": "Introduction to Ledger Classifications",\s*"blocks": \[)',
    r'\1\n                {\n                    "block_type": "suggested_image",\n                    "component_type": "photo_view",\n                    "title": "Analyzing Financial Classifications",\n                    "content": IMG_ANALYZING_FINANCIAL_DATA\n                },',
    content
)

content = content.replace("IMG_ACCOUNTING_DESK", "IMG_ACCOUNTANT_DESK")

# Fix Learning Goals
content = content.replace(
    '"text": "By the end of this lesson, you should be able to explain the meaning and purpose of a ledger and a ledger account, state the basic rules of double-entry bookkeeping, and describe the format and key columns of a standard T-account."',
    '"goals": [\n                            "Explain the meaning and purpose of a ledger and a ledger account",\n                            "State the basic rules of double-entry bookkeeping",\n                            "Describe the format and key columns of a standard T-account"\n                        ]'
)
content = content.replace(
    '"text": "By the end of this lesson, you should be able to state and apply the posting rules for assets, liabilities, capital, expenses, and revenues, execute the 5-step transaction analysis, and post stock movements in specialized accounts."',
    '"goals": [\n                            "State and apply the posting rules for assets, liabilities, capital, expenses, and revenues",\n                            "Execute the 5-step transaction analysis",\n                            "Post stock movements in specialized accounts"\n                        ]'
)
content = content.replace(
    '"text": "By the end of this lesson, you should be able to explain the meaning of balancing a ledger account, detail the 5 procedural balancing steps, distinguish between debit and credit balances, and balance off a full set of accounts."',
    '"goals": [\n                            "Explain the meaning of balancing a ledger account",\n                            "Detail the 5 procedural balancing steps",\n                            "Distinguish between debit and credit balances",\n                            "Balance off a full set of accounts"\n                        ]'
)
content = content.replace(
    '"text": "By the end of this lesson, you should be able to list and define the six primary classifications of ledgers, assign accounts to correct ledger books, execute multi-step postings, and master KCSE trial balance error essays."',
    '"goals": [\n                            "List and define the six primary classifications of ledgers",\n                            "Assign accounts to correct ledger books",\n                            "Execute multi-step postings",\n                            "Master KCSE trial balance error essays"\n                        ]'
)

# Convert Steps to Array in Worked Examples
# Lesson 2, Page 4: Mathai's Business 4-Transaction Worked Walkthrough
content = content.replace(
    '"text": "Transaction 1 [Feb 1]: Mathai started business with 70k cash ---> Dr Cash A/C 70,000; Cr Capital A/C 70,000.\\nTransaction 2 [Feb 4]: Bought office equipment for 20k cash ---> Dr Office Equipment A/C 20,000; Cr Cash A/C 20,000.\\nTransaction 3 [Feb 6]: Bought motor vehicle for 350k on credit from Chama Motors ---> Dr Motor Vehicle A/C 350,000; Cr Chama Motors A/C 350,000.\\nTransaction 4 [Feb 14]: Deposited 40k cash into bank ---> Dr Bank A/C 40,000; Cr Cash A/C 40,000."',
    '"intro": "Mathai\'s Transactions",\n                        "steps": [\n                            "Transaction 1 [Feb 1]: Mathai started business with 70k cash ---> Dr Cash A/C 70,000; Cr Capital A/C 70,000.",\n                            "Transaction 2 [Feb 4]: Bought office equipment for 20k cash ---> Dr Office Equipment A/C 20,000; Cr Cash A/C 20,000.",\n                            "Transaction 3 [Feb 6]: Bought motor vehicle for 350k on credit from Chama Motors ---> Dr Motor Vehicle A/C 350,000; Cr Chama Motors A/C 350,000.",\n                            "Transaction 4 [Feb 14]: Deposited 40k cash into bank ---> Dr Bank A/C 40,000; Cr Cash A/C 40,000."\n                        ]'
)

# Lesson 3, Page 5
content = content.replace(
    '"text": "1. Capital A/C: Cr Jan 1 Furniture 130k. Jan 10 Balance c/d Dr 130k. Jan 10 Balance b/d Cr 130k.\\n2. Furniture A/C: Dr Jan 1 Capital 130k. Jan 10 Balance c/d Cr 130k. Jan 10 Balance b/d Dr 130k.\\n3. Purchases A/C: Dr Jan 2 Nyamwea 50k. Jan 10 Balance c/d Cr 50k. Jan 10 Balance b/d Dr 50k.\\n4. Sales A/C: Cr Jan 4 Cash 40k. Jan 10 Balance c/d Dr 40k. Jan 10 Balance b/d Cr 40k."',
    '"intro": "Balances for Accounts 1-4:",\n                        "steps": [\n                            "1. Capital A/C: Cr Jan 1 Furniture 130k. Jan 10 Balance c/d Dr 130k. Jan 10 Balance b/d Cr 130k.",\n                            "2. Furniture A/C: Dr Jan 1 Capital 130k. Jan 10 Balance c/d Cr 130k. Jan 10 Balance b/d Dr 130k.",\n                            "3. Purchases A/C: Dr Jan 2 Nyamwea 50k. Jan 10 Balance c/d Cr 50k. Jan 10 Balance b/d Dr 50k.",\n                            "4. Sales A/C: Cr Jan 4 Cash 40k. Jan 10 Balance c/d Dr 40k. Jan 10 Balance b/d Cr 40k."\n                        ]'
)

# Lesson 3, Page 6
content = content.replace(
    '"text": "5. Bank A/C: Dr (20k + 30k = 50k); Cr (30k + 60k = 90k). Dr Balance c/d 40k. Cr Balance b/d 40k (Bank Overdraft!).\\n6. Cash A/C: Dr (40k + 60k = 100k); Cr (20k). Cr Balance c/d 80k. Dr Balance b/d 80k.\\n7. KIE Loan A/C: Cr Jan 6 Bank 30k. Dr Balance c/d 30k. Cr Balance b/d 30k. (Source typo 60k corrected to 30k!)\\n8. Nyamwea A/C: Dr Jan 7 Bank 30k; Cr Jan 2 Purchases 50k. Dr Balance c/d 20k. Cr Balance b/d 20k."',
    '"intro": "Balances for Accounts 5-8:",\n                        "steps": [\n                            "5. Bank A/C: Dr (20k + 30k = 50k); Cr (30k + 60k = 90k). Dr Balance c/d 40k. Cr Balance b/d 40k (Bank Overdraft!).",\n                            "6. Cash A/C: Dr (40k + 60k = 100k); Cr (20k). Cr Balance c/d 80k. Dr Balance b/d 80k.",\n                            "7. KIE Loan A/C: Cr Jan 6 Bank 30k. Dr Balance c/d 30k. Cr Balance b/d 30k. (Source typo 60k corrected to 30k!)",\n                            "8. Nyamwea A/C: Dr Jan 7 Bank 30k; Cr Jan 2 Purchases 50k. Dr Balance c/d 20k. Cr Balance b/d 20k."\n                        ]'
)

# Lesson 4, Page 4
content = content.replace(
    '"text": "Transactions:\\nNov 1: Started business with 80k cash till.\\nNov 3: Bought furniture 15k on credit from Woodworks Ltd.\\nNov 5: Bought goods 30k cash.\\nNov 12: Deposited 40k cash into bank.\\nNov 20: Paid Woodworks Ltd 10k by cheque.\\n\\nBalances as at Nov 30:\\nCapital b/d Cr 80k, Furniture b/d Dr 15k, Purchases b/d Dr 30k, Cash b/d Dr 10k, Bank b/d Dr 30k, Woodworks Ltd b/d Cr 5k."',
    '"intro": "Transactions and Balances:",\n                        "steps": [\n                            "Nov 1: Started business with 80k cash till.",\n                            "Nov 3: Bought furniture 15k on credit from Woodworks Ltd.",\n                            "Nov 5: Bought goods 30k cash.",\n                            "Nov 12: Deposited 40k cash into bank.",\n                            "Nov 20: Paid Woodworks Ltd 10k by cheque.",\n                            "Balances as at Nov 30:\\nCapital b/d Cr 80k, Furniture b/d Dr 15k, Purchases b/d Dr 30k, Cash b/d Dr 10k, Bank b/d Dr 30k, Woodworks Ltd b/d Cr 5k."\n                        ]'
)

# Semantic Upgrades
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Watch Out: Left vs Right Memory"',
    '"component_type": "memory_tip",\n                    "title": "Watch Out: Left vs Right Memory"'
)
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Source Typo Corrections"',
    '"component_type": "common_mistake",\n                    "title": "Source Typo Corrections"'
)
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Watch Out: Resale vs Asset Purchases"',
    '"component_type": "common_mistake",\n                    "title": "Watch Out: Resale vs Asset Purchases"'
)
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Watch Out: Balance b/d Side"',
    '"component_type": "common_mistake",\n                    "title": "Watch Out: Balance b/d Side"'
)
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "Watch Out: Error of Principle"',
    '"component_type": "common_mistake",\n                    "title": "Watch Out: Error of Principle"'
)
content = content.replace(
    '"component_type": "concept_card",\n                    "title": "KCSE Paper 1 Double-Entry Table"',
    '"component_type": "key_takeaway",\n                    "title": "KCSE Paper 1 Double-Entry Table"'
)

with open("curriculum/topic11_data.py", "w") as f:
    f.write(content)

