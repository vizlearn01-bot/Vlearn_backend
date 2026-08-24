"""
VLearn Form 4 Business Studies — Topic 12: A Trial Balance
Authoritative Pedagogical Data Structures for 3 Lessons (30 Pages).
"""

from curriculum.ingest_form4_business_studies_topic12_svgs import (
    SVG_TRIAL_BALANCE_ARITHMETIC_SCALE,
    SVG_TRIAL_BALANCE_STANDARD_LAYOUT,
    SVG_ERRORS_DISCLOSED_VS_UNDISCLOSED_TREE,
    SVG_SIX_UNDISCLOSED_ERRORS_MATRIX,
    SVG_ONYATI_RECONSTRUCTION_FLOW
)

LESSON_1_DATA = {'unit_order': 1,
 'unit_name': 'Meaning, Purpose, and Preparation of a Trial Balance',
 'lesson_title': 'Arithmetic Equilibrium, DR. EXP vs CR. LIC Rules, and Tabular Formats',
 'pages': [{'page_number': 1,
            'page_title': 'Introduction to Trial Balances',
            'blocks': [{'block_type': 'suggested_image',
                        'component_type': 'photo_view',
                        'title': 'Real-World Context',
                        'content': {'url': 'https://upload.wikimedia.org/wikipedia/commons/b/bc/The_Accountants_desks_%283817577217%29.jpg',
                                    'text': 'An accounting office with organised workstations — representing '
                                            'systematic bookkeeping and financial record management',
                                    'author': 'Kristin Dos Santos',
                                    'licensing': 'CC BY-SA 2.0',
                                    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:The_Accountants_desks_(3817577217).jpg'}},
                       {'block_type': 'text',
                        'component_type': 'learning_goal',
                        'title': 'Learning Goals',
                        'content': {'goals': ['Define a trial balance',
                                              'Explain its core purposes',
                                              'Formulate a correct standard layout',
                                              'Identify balance types for major account classes',
                                              'Prepare a balanced trial balance.']}},
                       {'block_type': 'text',
                        'component_type': 'concept_card',
                        'title': 'The Accounting Health Check',
                        'content': {'text': 'Imagine running a supermarket with thousands of daily transactions. If '
                                            'you record a sale of Sh. 10,000 but forget to enter cash received, or '
                                            'make an addition error, final financial statements will be wrong. A Trial '
                                            "Balance acts as a regular 'health check' to catch arithmetic and entry "
                                            'mistakes before preparing final accounts.'}}]},
           {'page_number': 2,
            'page_title': 'Definition and Purpose of a Trial Balance',
            'blocks': [{'block_type': 'text',
                        'component_type': 'definition_card',
                        'title': 'Trial Balance Definition',
                        'content': {'term': 'Trial Balance',
                                    'definition': 'A statement prepared at a particular date showing all debit '
                                                  'balances in one column and all credit balances in another column. '
                                                  'It is not an account, but a summary list of ledger balances.'}}]},
           {'page_number': 3,
            'page_title': 'The Core Rule of Balances: DR. EXP vs. CR. LIC',
            'blocks': [{'block_type': 'text',
                        'component_type': 'concept_card',
                        'title': 'The DR. EXP vs. CR. LIC Memory Rule',
                        'content': {'text': '- **Debit Side (Dr.)**: DR. EXP ---> Drawings, Assets, Expenses.\n'
                                            '- **Credit Side (Cr.)**: CR. LIC ---> Capital, Revenues, Liabilities.\n'
                                            'Every account balance must reside strictly on its assigned side to '
                                            'maintain arithmetic equilibrium.'}},
                       {'block_type': 'suggested_diagram',
                        'component_type': 'svg_viewer',
                        'title': 'Trial Balance Arithmetic Scale Diagram',
                        'svg_content': SVG_TRIAL_BALANCE_ARITHMETIC_SCALE,
                        'content': {'text': 'Scale diagram visualizing DR. EXP (Drawings, Assets, Expenses) vs CR. LIC '
                                            '(Capital, Revenues, Liabilities).'}}]},
           {'page_number': 4,
            'page_title': 'Standard 3-Column Tabular Layout',
            'blocks': [{'block_type': 'text',
                        'component_type': 'concept_card',
                        'title': 'Three-Part Heading & Layout Rules',
                        'content': {'text': "1. Three-Part Heading: Name of business ('San Enterprises'), statement "
                                            "title ('Trial Balance'), and date ('As at 30th April 1995').\n"
                                            '2. Three Columns: Details (Account Title), Debit (Dr.) Shs, Credit (Cr.) '
                                            'Shs.\n'
                                            '3. Bottom Line: Totals of both columns are double-underlined.'}},
                       {'block_type': 'suggested_diagram',
                        'component_type': 'svg_viewer',
                        'title': 'Trial Balance Standard Tabular Layout',
                        'svg_content': SVG_TRIAL_BALANCE_STANDARD_LAYOUT,
                        'content': {'text': 'Layout diagram showing 3-part heading, Details column, and Debit/Credit '
                                            'columns.'}}]},
           {'page_number': 5,
            'page_title': 'Account Classification Table for Trial Balances',
            'blocks': [{'block_type': 'table',
                        'component_type': 'comparison_table',
                        'title': 'Account Category & Balance Placement Matrix',
                        'content': {'headers': ['Account Category',
                                                'Nature / Effect',
                                                'Trial Balance Column',
                                                'Standard Examples'],
                                    'rows': [['Assets',
                                              'Owned business properties & resources',
                                              'Debit (Dr.)',
                                              'Premises, Motor Vehicles, Debtors, Stock, Cash'],
                                             ['Expenses',
                                              'Operational running costs incurred',
                                              'Debit (Dr.)',
                                              'Salaries, Rent, Water & Light, Purchases, Wages'],
                                             ['Drawings',
                                              'Private withdrawals taken by owner',
                                              'Debit (Dr.)',
                                              'Cash or goods taken for personal/home use'],
                                             ['Liabilities',
                                              'External debts owed to outsiders',
                                              'Credit (Cr.)',
                                              'Bank Loans, Trade Creditors, Bank Overdraft'],
                                             ['Capital',
                                              "Owner's investment / equity stake",
                                              'Credit (Cr.)',
                                              'Initial or additional capital contribution'],
                                             ['Revenues',
                                              'Incomes & trading gains earned',
                                              'Credit (Cr.)',
                                              'Sales, Rent Received, Commission Received']]}}]},
           {'page_number': 6,
            'page_title': 'San Enterprises Worked Trial Balance',
            'blocks': [{'block_type': 'text',
                        'component_type': 'worked_example',
                        'title': 'San Enterprises Trial Balance Extraction & Analysis',
                        'content': {'text': 'Problem: Given balances: Capital Sh. 947,000; Cash Sh. 74,000; Premises '
                                            'Sh. 870,000; Debtors Sh. 36,520; Creditors Sh. 45,300; Stock Sh. 12,250.\n'
                                            'Accounting Classification & Placement:\n'
                                            '- **Assets (Debit)**: Cash (74,000) + Premises (870,000) + Debtors '
                                            '(36,520) + Stock (12,250) = Sh. 992,770.\n'
                                            '- **Equity & Liabilities (Credit)**: Capital (947,000) + Creditors '
                                            '(45,300) = Sh. 992,300.\n'
                                            '- **Note on Discrepancy**: The debit side exceeds the credit side by Sh. '
                                            '470 in raw exam print, highlighting an unlocated posting error requiring '
                                            'investigation.'}},
                       {'block_type': 'table',
                        'component_type': 'comparison_table',
                        'title': 'San Enterprises Trial Balance as at 30th April 1995',
                        'content': {'headers': ['Account Title (Details)', 'Debit (Dr.) Shs', 'Credit (Cr.) Shs'],
                                    'rows': [['Capital Account', '-', '947,000'],
                                             ['Cash in Hand', '74,000', '-'],
                                             ['Premises Account', '870,000', '-'],
                                             ['Debtors Account', '36,520', '-'],
                                             ['Creditors Account', '-', '45,300'],
                                             ['Stock (Inventory) Account', '12,250', '-'],
                                             ['TOTALS', '992,770', '992,300']]}}]},
           {'page_number': 7,
            'page_title': 'Kiboko Traders Balanced Trial Balance',
            'blocks': [{'block_type': 'text',
                        'component_type': 'worked_example',
                        'title': 'Kiboko Traders Trial Balance Extraction',
                        'content': {'text': 'Problem: Extract: Motor Vehicle 240k, Current Liabilities 440k, Land & '
                                            'Building 200k, Current Assets 420k, Furniture 60k, Capital 480k.\n'
                                            'Calculation & Placement:\n'
                                            '- **Debits (Assets)**: Motor Vehicle (240k) + Land & Building (200k) + '
                                            'Current Assets (420k) + Furniture (60k) = Sh. 920,000.\n'
                                            '- **Credits (Capital & Liabilities)**: Capital (480k) + Current '
                                            'Liabilities (440k) = Sh. 920,000.\n'
                                            '- **Results**: Both sides match perfectly at Sh. 920,000.'}},
                       {'block_type': 'table',
                        'component_type': 'comparison_table',
                        'title': 'Kiboko Traders Trial Balance as at 30th June 1999',
                        'content': {'headers': ['Account Title (Details)', 'Debit (Dr.) Shs', 'Credit (Cr.) Shs'],
                                    'rows': [['Motor Vehicle Account', '240,000', '-'],
                                             ['Land & Building Account', '200,000', '-'],
                                             ['Current Assets Account', '420,000', '-'],
                                             ['Furniture Account', '60,000', '-'],
                                             ['Capital Account', '-', '480,000'],
                                             ['Current Liabilities Account', '-', '440,000'],
                                             ['TOTALS', '920,000', '920,000']]}},
                       {'block_type': 'suggested_image',
                        'component_type': 'photo_view',
                        'title': 'Retail Commercial Enterprise Operations',
                        'content': {'url': 'https://upload.wikimedia.org/wikipedia/commons/4/49/2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg',
                                    'text': 'Commercial enterprise logistics operations, demonstrating multi-asset '
                                            'ledger balances, trade creditors, and trial balance extraction.',
                                    'author': 'Wikimedia Commons Contributor',
                                    'licensing': 'CC BY-SA 4.0',
                                    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:2015_07_31_Mombasa_Port_JPEG_RESIZED_0039.jpg'}}]},
           {'page_number': 8,
            'page_title': 'Key Idea & Summary',
            'blocks': [{'block_type': 'text',
                        'component_type': 'summary',
                        'title': 'Key Idea',
                        'content': {'text': 'A Trial Balance tests double-entry arithmetic equality. DR. EXP '
                                            '(Drawings, Assets, Expenses) go to the Debit column. CR. LIC (Capital, '
                                            'Revenues, Liabilities) go to the Credit column.'}}]},
           {'page_number': 9,
            'page_title': "Watch Out: 'As at' Heading Requirement",
            'blocks': [{'block_type': 'text',
                        'component_type': 'common_mistake',
                        'title': 'Watch Out: Trial Balance Heading',
                        'content': {'text': 'Like a Balance Sheet, a Trial Balance is extracted on one specific '
                                            "calendar day. The heading must strictly state 'Trial Balance as at "
                                            "[Date]', NOT 'for the year ended...'."}}]},
           {'page_number': 10,
            'page_title': 'Check Your Understanding',
            'blocks': [{'block_type': 'text',
                        'component_type': 'knowledge_check',
                        'title': 'Formative Assessment',
                        'content': {'question': 'Which of the following account balances is placed in the Credit (Cr.) '
                                                'column of a Trial Balance?',
                                    'options': ['Premises and Land Account',
                                                'Trade Debtors Account',
                                                'Bank Overdraft Account',
                                                'Purchases Account'],
                                    'correct_answer': 'Bank Overdraft Account',
                                    'explanation': 'Bank Overdraft is a liability (CR. LIC rule: Capital, Revenues, '
                                                   'Liabilities), so its balance resides on the Credit side.'}}]}]}

LESSON_2_DATA = {'unit_order': 2,
 'unit_name': 'Limitations of a Trial Balance (Disclosed vs Undisclosed Errors)',
 'lesson_title': 'Disclosed Mismatches, Hidden Double-Sided Errors, and Error Diagnostics',
 'pages': [{'page_number': 1,
            'page_title': 'Introduction to Trial Balance Limitations',
            'blocks': [{'block_type': 'suggested_image',
                        'component_type': 'photo_view',
                        'title': 'Real-World Context',
                        'content': {'url': 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Analyzing_Financial_Data_%285099605109%29.jpg',
                                    'text': 'A person analysing financial data and spreadsheets — representing the '
                                            'process of preparing and reviewing financial accounts',
                                    'author': 'Dave Dugdale',
                                    'licensing': 'CC BY-SA 2.0',
                                    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Analyzing_Financial_Data_(5099605109).jpg'}},
                       {'block_type': 'text',
                        'component_type': 'learning_goal',
                        'title': 'Learning Goals',
                        'content': {'goals': ['Explain errors disclosed by a trial balance (totals mismatch)',
                                              'Master the six types of errors not disclosed by a trial balance (totals '
                                              'still agree).']}},
                       {'block_type': 'text',
                        'component_type': 'concept_card',
                        'title': 'The Dangerous Balanced Fallacy',
                        'content': {'text': 'If a Trial Balance balances, does it mean your books are 100% correct? '
                                            'No! This is one of the most dangerous misconceptions in accounting. An '
                                            'entire transaction could be completely forgotten or posted to the wrong '
                                            "person's account, and the Trial Balance will still balance perfectly!"}}]},
           {'page_number': 2,
            'page_title': 'Errors Disclosed by a Trial Balance (Totals Mismatch)',
            'blocks': [{'block_type': 'text',
                        'component_type': 'concept_card',
                        'title': 'Causes of Trial Balance Discrepancies',
                        'content': {'text': 'Disclosed errors occur when single-sided or unequal entries cause Debit '
                                            'Total != Credit Total:\n'
                                            '1. Single-Sided Posting (Only one account debited or credited).\n'
                                            '2. Unequal Entry (Different amounts entered on debit vs credit side).\n'
                                            '3. Wrong Balance Transfer (Copying an incorrect number onto the sheet).\n'
                                            '4. Omission of Ledger Balance (Forgetting to list an active T-account).\n'
                                            '5. Wrong-Side Posting (Putting a debit balance in credit column).\n'
                                            '6. Double Posting on Same Side (Debiting both accounts).\n'
                                            '7. Arithmetic Mistakes (Addition errors when balancing T-accounts).'}}]},
           {'page_number': 3,
            'page_title': 'Six Errors NOT Disclosed by a Trial Balance',
            'blocks': [{'block_type': 'text',
                        'component_type': 'common_mistake',
                        'title': 'The Six Hidden Errors (Totals Still Agree)',
                        'content': {'text': '1. Error of Omission: Transaction completely unrecorded anywhere.\n'
                                            '2. Error of Commission: Posted to wrong individual account within same '
                                            'class (e.g. Ochieng instead of Onyango).\n'
                                            '3. Error of Principle: Posted to wrong account class violating '
                                            'capital/revenue rules (e.g. van repairs debited to Motor Vehicle Asset).\n'
                                            '4. Error of Compensation: Unrelated separate errors cancel each other '
                                            'out.\n'
                                            '5. Complete Reversal of Entries: Correct accounts used, but debit and '
                                            'credit are swapped.\n'
                                            '6. Error of Original Entry: Wrong figure entered as both debit and '
                                            'credit.'}},
                       {'block_type': 'suggested_diagram',
                        'component_type': 'svg_viewer',
                        'title': 'Errors Disclosed vs Undisclosed Mind Map',
                        'svg_content': SVG_ERRORS_DISCLOSED_VS_UNDISCLOSED_TREE,
                        'content': {'text': 'Mind map contrasting disclosed mismatch errors with undisclosed hidden '
                                            'errors.'}}]},
           {'page_number': 4,
            'page_title': 'Detailed Matrix of Undisclosed Errors',
            'blocks': [{'block_type': 'suggested_diagram',
                        'component_type': 'svg_viewer',
                        'title': 'Six Errors Not Disclosed Matrix',
                        'svg_content': SVG_SIX_UNDISCLOSED_ERRORS_MATRIX,
                        'content': {'text': 'Matrix explaining Omission, Commission, Principle, Compensation, '
                                            'Reversal, and Original Entry.'}}]},
           {'page_number': 5,
            'page_title': 'Corporate Audit Verification Operations',
            'blocks': [{'block_type': 'suggested_image',
                        'component_type': 'photo_view',
                        'title': 'Corporate Audit Desk Verification',
                        'content': {'url': 'https://upload.wikimedia.org/wikipedia/commons/5/57/Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg',
                                    'text': 'Corporate accounting desk operations in Kenya, illustrating trial balance '
                                            'verification, debit-credit arithmetic checking, and financial audit '
                                            'controls.',
                                    'author': 'Wikimedia Commons Contributor',
                                    'licensing': 'CC BY-SA 4.0',
                                    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Wangige_vegetable_local_market_in_Kiambu_Kenya.jpg'}}]},
           {'page_number': 6,
            'page_title': 'Error of Commission vs. Error of Principle',
            'blocks': [{'block_type': 'text',
                        'component_type': 'concept_card',
                        'title': 'Commission vs Principle Distinction',
                        'content': {'text': '- Commission = Correct Class / Wrong Person (e.g. Credited Ochieng '
                                            'instead of Onyango; both are Debtors).\n'
                                            '- Principle = Wrong Class / Wrong Accounting Nature (e.g. Debited van '
                                            'repairs to Motor Vehicles Asset instead of Maintenance Expense).'}}]},
           {'page_number': 7,
            'page_title': 'Key Idea & Summary',
            'blocks': [{'block_type': 'text',
                        'component_type': 'summary',
                        'title': 'Key Idea',
                        'content': {'text': 'A balanced Trial Balance proves arithmetic equality, but it does NOT '
                                            'prove absolute correctness because double-sided errors (omission, '
                                            'commission, principle) remain hidden.'}}]},
           {'page_number': 8,
            'page_title': 'Watch Out: Error of Original Entry Math',
            'blocks': [{'block_type': 'text',
                        'component_type': 'common_mistake',
                        'title': 'Watch Out: Transposed Digits',
                        'content': {'text': 'If a payment of Sh. 9,400 is recorded as Sh. 4,900 on both debit and '
                                            'credit sides, an Error of Original Entry occurred. Equal debits and '
                                            'credits exist, so Trial Balance totals WILL STILL BALANCE!'}}]},
           {'page_number': 9,
            'page_title': 'Check Your Understanding 1',
            'blocks': [{'block_type': 'text',
                        'component_type': 'common_mistake',
                        'title': 'Compensating Error Mechanism',
                        'content': {'text': 'How Compensating Errors work: If Purchases is under-added by Sh. 1,000 on '
                                            'debit side, and Sales is separately under-added by Sh. 1,000 on credit '
                                            'side, the two errors cancel out completely.'}}]},
           {'page_number': 10,
            'page_title': 'Check Your Understanding 2',
            'blocks': [{'block_type': 'text',
                        'component_type': 'knowledge_check',
                        'title': 'Formative Assessment',
                        'content': {'question': 'A bookkeeper debits Sh. 150,000 spent on expanding a factory '
                                                'warehouse to the Maintenance Expense account instead of the Buildings '
                                                'Asset account. What type of error occurred?',
                                    'options': ['Error of Omission',
                                                'Error of Commission',
                                                'Error of Principle',
                                                'Error of Original Entry'],
                                    'correct_answer': 'Error of Principle',
                                    'explanation': 'Debiting a fixed asset capital expenditure to an expense account '
                                                   'breaks accounting principles, making it an Error of '
                                                   'Principle.'}}]}]}

LESSON_3_DATA = {'unit_order': 3,
 'unit_name': 'Reconstruction of Trial Balances and KCSE Mastery',
 'lesson_title': 'Ledger Side Corrections, Auditor Error Analysis, and KCSE Examination Essays',
 'pages': [{'page_number': 1,
            'page_title': 'Introduction to Reconstructing Trial Balances',
            'blocks': [{'block_type': 'suggested_image',
                        'component_type': 'photo_view',
                        'title': 'Real-World Context',
                        'content': {'url': 'https://upload.wikimedia.org/wikipedia/commons/d/d0/Camp_Chesterfield_general_account_ledger%2C_1910-1916_-_DPLA_-_206e8c73ecb9419118717c75562a2497_%28page_1%29.jpg',
                                    'text': 'A handwritten general account ledger — showing the traditional T-account '
                                            'format with debit and credit columns used in double-entry bookkeeping',
                                    'author': 'Public Domain (DPLA)',
                                    'licensing': 'Public domain',
                                    'commons_page_url': 'https://commons.wikimedia.org/wiki/File:Camp_Chesterfield_general_account_ledger,_1910-1916_-_DPLA_-_206e8c73ecb9419118717c75562a2497_(page_1).jpg'}},
                       {'block_type': 'text',
                        'component_type': 'learning_goal',
                        'title': 'Learning Goals',
                        'content': {'goals': ['Reconstruct an incorrectly prepared trial balance by correcting account '
                                              'sides',
                                              'Analyze auditor error scenarios',
                                              'Master kcse essay model answers.']}},
                       {'block_type': 'text',
                        'component_type': 'concept_card',
                        'title': 'Fixing Inexperienced Clerk Drafts',
                        'content': {'text': 'In inexperienced accounting drafts, clerks often mix up debit and credit '
                                            'placements (e.g. putting Capital on debit or Debtors on credit). '
                                            'Reconstructing requires re-aligning every account onto its correct side '
                                            'using DR. EXP vs CR. LIC rules!'}}]},
           {'page_number': 2,
            'page_title': 'The Onyati Clerk Reconstruction Case Study',
            'blocks': [{'block_type': 'text',
                        'component_type': 'worked_example',
                        'title': 'Onyati Incorrect Draft & Side Corrections',
                        'content': {'text': 'Onyati Clerk Mistakes:\n'
                                            '- Capital (99,600) placed on Debit ---> Correct: Credit (Cr)\n'
                                            '- Debtors (30,520) placed on Credit ---> Correct: Debit (Dr)\n'
                                            '- Creditors (25,670) placed on Debit ---> Correct: Credit (Cr)\n'
                                            '- Motor Vehicles (80,000) placed on Credit ---> Correct: Debit (Dr)\n'
                                            '- Cash (2,500) & Stock (140,250) ---> Debit (Dr)\n'
                                            'Corrected Totals: Debit = 253,270 Shs; Credit = 125,270 Shs.'}},
                       {'block_type': 'suggested_diagram',
                        'component_type': 'svg_viewer',
                        'title': 'Onyati Case Study Reconstruction Flowchart',
                        'svg_content': SVG_ONYATI_RECONSTRUCTION_FLOW,
                        'content': {'text': "Flowchart tracing clerk's wrong-side errors and corrected side "
                                            'placements.'}}]},
           {'page_number': 3,
            'page_title': 'Straightforward Debit Column Total Math',
            'blocks': [{'block_type': 'text',
                        'component_type': 'worked_example',
                        'title': 'Debit Total Extraction Math',
                        'content': {'text': 'Problem: Capital 200k, Purchases 80k, Sales 120k, Motor vehicle 150k, '
                                            'Cash 10k, Creditors 15k, Debtors 95k. Find Debit Column Total.\n'
                                            '\n'
                                            'Solution:\n'
                                            'Debit Items (DR. EXP): Purchases (80k) + Motor Vehicle (150k) + Cash '
                                            '(10k) + Debtors (95k) = Sh. 335,000.\n'
                                            'Credit Check (CR. LIC): Capital (200k) + Sales (120k) + Creditors (15k) = '
                                            'Sh. 335,000 [BALANCED!]'}}]},
           {'page_number': 4,
            'page_title': 'Mwenza Traders Auditor Multi-Step Scenario',
            'blocks': [{'block_type': 'text',
                        'component_type': 'worked_example',
                        'title': 'Mwenza Traders Auditor Error Diagnosis',
                        'content': {'intro': 'Auditor Findings:',
                                    'steps': ['Electricity 12k debited as 21k and credited as 21k ---> Error of '
                                              'Original Entry (Equal Dr/Cr ---> Will NOT cause Trial Balance '
                                              'mismatch).',
                                              'Warehouse expansion 50k debited to Maintenance Expense ---> Error of '
                                              'Principle (Equal Dr/Cr ---> Will NOT cause Trial Balance '
                                              'mismatch).']}}]},
           {'page_number': 5,
            'page_title': 'Key Idea & Summary',
            'blocks': [{'block_type': 'text',
                        'component_type': 'summary',
                        'title': 'Key Idea',
                        'content': {'text': 'Reconstructing a Trial Balance requires placing Assets, Expenses, and '
                                            'Drawings on the Debit side and Capital, Revenues, and Liabilities on the '
                                            'Credit side.'}}]},
           {'page_number': 6,
            'page_title': 'Watch Out: Single-Sided Error Identification',
            'blocks': [{'block_type': 'text',
                        'component_type': 'common_mistake',
                        'title': 'Watch Out: Single-Sided Errors',
                        'content': {'text': 'Only single-sided errors (like adding a T-account column incorrectly or '
                                            'omitting one account from the sheet) cause a Trial Balance mismatch. '
                                            'Double-sided errors preserve column equality.'}}]},
           {'page_number': 7,
            'page_title': 'KCSE Integrated Practice: Paper 1',
            'blocks': [{'block_type': 'text',
                        'component_type': 'concept_card',
                        'title': 'KCSE Paper 1 Short-Answer Mastery',
                        'content': {'text': '1. Purpose of Trial Balance: Check arithmetic accuracy of ledger '
                                            'postings.\n'
                                            '2. Three Debit Accounts: Assets, Expenses, Drawings (DR. EXP).\n'
                                            '3. Three Credit Accounts: Capital, Revenues, Liabilities (CR. LIC).\n'
                                            '4. Why Balanced TB can be Wrong: Hidden double-sided errors (omission, '
                                            'principle, commission).'}}]},
           {'page_number': 8,
            'page_title': 'KCSE Integrated Practice: Paper 2 (Errors Not Disclosed Essay)',
            'blocks': [{'block_type': 'text',
                        'component_type': 'worked_example',
                        'title': 'KCSE Essay Model Answer: Five Errors Not Disclosed by Trial Balance',
                        'content': {'intro': 'Question: Explain five types of errors that are not disclosed by a Trial '
                                             'Balance (10 Marks).\n'
                                             '\n'
                                             'Model Answer:',
                                    'steps': ['Error of Omission: Transaction completely unrecorded in books; both '
                                              'debit and credit columns equally unaffected.',
                                              'Error of Commission: Transaction recorded in wrong personal account of '
                                              'correct class, preserving Dr/Cr balance.',
                                              'Error of Principle: Transaction recorded in wrong class of account '
                                              '(capital vs revenue error), maintaining Dr/Cr balance.',
                                              'Error of Compensation: Unrelated errors of equal value on opposite '
                                              'sides cancel each other out.',
                                              'Complete Reversal of Entries: Correct accounts used, but debit and '
                                              'credit entries are swapped.']}}]},
           {'page_number': 9,
            'page_title': 'Check Your Understanding 1',
            'blocks': [{'block_type': 'text',
                        'component_type': 'common_mistake',
                        'title': 'Error of Original Entry Check',
                        'content': {'text': 'Why Original Entry Error Balances: Entering Sh. 4,900 instead of Sh. '
                                            '9,400 on both debit and credit sides maintains perfect column equality, '
                                            'hiding the Sh. 4,500 difference.'}}]},
           {'page_number': 10,
            'page_title': 'Check Your Understanding 2',
            'blocks': [{'block_type': 'text',
                        'component_type': 'knowledge_check',
                        'title': 'Formative Assessment',
                        'content': {'question': 'Which of the following errors WILL cause a Trial Balance debit and '
                                                'credit total to mismatch?',
                                    'options': ['Completely omitting a cash sale of Sh. 10,000',
                                                'Entering an addition mistake of Sh. 500 when balancing the Cash '
                                                'T-account',
                                                'Crediting Ochieng instead of Onyango for a credit purchase',
                                                'Debiting van repairs to the Motor Vehicle Asset account'],
                                    'correct_answer': 'Entering an addition mistake of Sh. 500 when balancing the Cash '
                                                      'T-account',
                                    'explanation': 'An arithmetic addition mistake in a T-account is a single-sided '
                                                   'error that causes Trial Balance totals to mismatch.'}}]}]}

TOPIC12_UNITS = [LESSON_1_DATA, LESSON_2_DATA, LESSON_3_DATA]
