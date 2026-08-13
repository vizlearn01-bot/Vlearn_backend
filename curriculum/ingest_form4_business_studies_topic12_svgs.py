"""
VLearn Form 4 Business Studies — Topic 12: A Trial Balance
Educational Dark-Mode SVG Vector Graphics
"""

SVG_TRIAL_BALANCE_ARITHMETIC_SCALE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">THE TRIAL BALANCE EQUILIBRIUM SCALE: DR. EXP VS. CR. LIC</text>

  <!-- Physical Balance Scale Base -->
  <path d="M 450 110 L 450 310 M 350 310 L 550 310 M 450 310 L 420 360 L 480 360 Z" stroke="#64748b" stroke-width="4" fill="#334155"/>
  <line x1="200" y1="130" x2="700" y2="130" stroke="#38bdf8" stroke-width="6"/>

  <!-- Left Pan: DR. EXP (Debit Side) -->
  <line x1="200" y1="130" x2="200" y2="220" stroke="#cbd5e1" stroke-width="2"/>
  <path d="M 100 220 Q 200 260 300 220 Z" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
  <rect x="120" y="150" width="160" height="70" rx="8" fill="#0369a1"/>
  <text x="200" y="175" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">DEBIT SIDE (Dr.)</text>
  <text x="200" y="198" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">DR. EXP</text>
  <text x="200" y="214" fill="#e0f2fe" font-family="sans-serif" font-size="11" text-anchor="middle">(Drawings, Assets, Expenses)</text>

  <!-- Right Pan: CR. LIC (Credit Side) -->
  <line x1="700" y1="130" x2="700" y2="220" stroke="#cbd5e1" stroke-width="2"/>
  <path d="M 600 220 Q 700 260 800 220 Z" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
  <rect x="620" y="150" width="160" height="70" rx="8" fill="#b45309"/>
  <text x="700" y="175" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">CREDIT SIDE (Cr.)</text>
  <text x="700" y="198" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">CR. LIC</text>
  <text x="700" y="214" fill="#fef3c7" font-family="sans-serif" font-size="11" text-anchor="middle">(Capital, Revenues, Liabilities)</text>

  <!-- Formula Summary Box -->
  <g transform="translate(150, 365)">
    <rect x="0" y="0" width="600" height="70" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="300" y="25" fill="#fbbf24" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">CORE BALANCE PLACEMENT RULE</text>
    <text x="150" y="52" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Debit Column: Assets + Expenses + Drawings</text>
    <text x="450" y="52" fill="#f87171" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Credit Column: Capital + Liabilities + Revenues</text>
  </g>
</svg>"""

SVG_TRIAL_BALANCE_STANDARD_LAYOUT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%">
  <rect width="900" height="480" fill="#0f172a" rx="16"/>
  
  <!-- 3-Part Heading Box -->
  <rect x="200" y="20" width="500" height="75" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="450" y="42" fill="#f8fafc" font-family="sans-serif" font-size="16" font-weight="bold" text-anchor="middle">San Enterprises</text>
  <text x="450" y="62" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">Trial Balance</text>
  <text x="450" y="80" fill="#fbbf24" font-family="sans-serif" font-size="12" text-anchor="middle">As at 30th April 1995</text>

  <!-- Tabular Layout Container -->
  <g transform="translate(40, 110)">
    <rect x="0" y="0" width="820" height="340" rx="12" fill="#1e293b" stroke="#64748b" stroke-width="2"/>

    <!-- Header Row -->
    <rect x="0" y="0" width="820" height="40" rx="12" fill="#0284c7"/>
    <text x="180" y="25" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold">Details (Account Title)</text>
    <text x="520" y="25" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold">Debit (Dr.) Shs.</text>
    <text x="700" y="25" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold">Credit (Cr.) Shs.</text>

    <!-- Vertical Column Dividers -->
    <line x1="440" y1="0" x2="440" y2="340" stroke="#64748b" stroke-width="1.5"/>
    <line x1="630" y1="0" x2="630" y2="340" stroke="#64748b" stroke-width="1.5"/>

    <!-- Rows -->
    <text x="30" y="70" fill="#cbd5e1" font-family="sans-serif" font-size="13">Capital (Owner's Equity)</text>
    <text x="700" y="70" fill="#fbbf24" font-family="sans-serif" font-size="13">947,000</text>

    <text x="30" y="105" fill="#cbd5e1" font-family="sans-serif" font-size="13">Cash (Current Asset)</text>
    <text x="520" y="105" fill="#34d399" font-family="sans-serif" font-size="13">74,000</text>

    <text x="30" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="13">Premises (Fixed Asset)</text>
    <text x="520" y="140" fill="#34d399" font-family="sans-serif" font-size="13">870,000</text>

    <text x="30" y="175" fill="#cbd5e1" font-family="sans-serif" font-size="13">Debtors (Current Asset)</text>
    <text x="520" y="175" fill="#34d399" font-family="sans-serif" font-size="13">36,520</text>

    <text x="30" y="210" fill="#cbd5e1" font-family="sans-serif" font-size="13">Creditors (Current Liability)</text>
    <text x="700" y="210" fill="#fbbf24" font-family="sans-serif" font-size="13">45,300</text>

    <text x="30" y="245" fill="#cbd5e1" font-family="sans-serif" font-size="13">Stock (Current Asset)</text>
    <text x="520" y="245" fill="#34d399" font-family="sans-serif" font-size="13">12,250</text>

    <!-- Totals Line -->
    <line x1="20" y1="280" x2="800" y2="280" stroke="#cbd5e1" stroke-width="1"/>
    <text x="30" y="305" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold">TOTALS</text>
    <text x="520" y="305" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="bold">992,770</text>
    <text x="700" y="305" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">992,300</text>
    <line x1="20" y1="315" x2="800" y2="315" stroke="#38bdf8" stroke-width="3"/>
  </g>
</svg>"""

SVG_ERRORS_DISCLOSED_VS_UNDISCLOSED_TREE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">LIMITATIONS OF A TRIAL BALANCE: DISCLOSED VS. UNDISCLOSED ERRORS</text>

  <!-- Left Side: ERRORS DISCLOSED (Totals Mismatch) -->
  <g transform="translate(40, 65)">
    <rect x="0" y="0" width="390" height="360" rx="14" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <rect x="0" y="0" width="390" height="45" rx="14" fill="#be123c"/>
    <text x="195" y="28" fill="#ffffff" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">ERRORS DISCLOSED (Totals Mismatch)</text>

    <text x="20" y="75" fill="#f87171" font-family="sans-serif" font-size="12" font-weight="bold">• Single-Sided Posting (Only one account posted)</text>
    <text x="20" y="105" fill="#f87171" font-family="sans-serif" font-size="12">• Unequal Debit &amp; Credit Entry Amounts</text>
    <text x="20" y="135" fill="#f87171" font-family="sans-serif" font-size="12">• Posting Balance onto Wrong Side of Trial Balance</text>
    <text x="20" y="165" fill="#f87171" font-family="sans-serif" font-size="12">• Omission of a Ledger Balance from Trial Balance</text>
    <text x="20" y="195" fill="#f87171" font-family="sans-serif" font-size="12">• Double Posting on the Same Side of Accounts</text>
    <text x="20" y="225" fill="#f87171" font-family="sans-serif" font-size="12">• Arithmetic Summing Mistakes in T-Accounts</text>

    <rect x="20" y="270" width="350" height="65" rx="8" fill="#be123c" fill-opacity="0.25"/>
    <text x="195" y="295" fill="#fca5a5" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Result: Debit Total != Credit Total</text>
    <text x="195" y="315" fill="#fca5a5" font-family="sans-serif" font-size="11" text-anchor="middle">Immediately alerts bookkeeper to arithmetic error!</text>
  </g>

  <!-- Right Side: ERRORS NOT DISCLOSED (Totals Still Agree) -->
  <g transform="translate(470, 65)">
    <rect x="0" y="0" width="390" height="360" rx="14" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <rect x="0" y="0" width="390" height="45" rx="14" fill="#d97706"/>
    <text x="195" y="28" fill="#ffffff" font-family="sans-serif" font-size="15" font-weight="bold" text-anchor="middle">ERRORS NOT DISCLOSED (Totals Agree)</text>

    <text x="20" y="75" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold">1. Error of Omission (Completely unrecorded)</text>
    <text x="20" y="105" fill="#fbbf24" font-family="sans-serif" font-size="12">2. Error of Commission (Wrong person, same class)</text>
    <text x="20" y="135" fill="#fbbf24" font-family="sans-serif" font-size="12">3. Error of Principle (Wrong account class)</text>
    <text x="20" y="165" fill="#fbbf24" font-family="sans-serif" font-size="12">4. Error of Compensation (Errors cancel out)</text>
    <text x="20" y="195" fill="#fbbf24" font-family="sans-serif" font-size="12">5. Complete Reversal of Entries (Dr/Cr swapped)</text>
    <text x="20" y="225" fill="#fbbf24" font-family="sans-serif" font-size="12">6. Error of Original Entry (Wrong figure Dr &amp; Cr)</text>

    <rect x="20" y="270" width="350" height="65" rx="8" fill="#d97706" fill-opacity="0.25"/>
    <text x="195" y="295" fill="#fef3c7" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Result: Debit Total == Credit Total (Hidden!)</text>
    <text x="195" y="315" fill="#fef3c7" font-family="sans-serif" font-size="11" text-anchor="middle">Dangerous! Balanced totals hide serious errors.</text>
  </g>
</svg>"""

SVG_SIX_UNDISCLOSED_ERRORS_MATRIX = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">DETAILED ANALYSIS: SIX ERRORS NOT DISCLOSED BY TRIAL BALANCE</text>

  <g transform="translate(40, 65)">
    <!-- Header -->
    <rect x="0" y="0" width="820" height="35" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <text x="140" y="23" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Error Type</text>
    <text x="430" y="23" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Mechanism / Cause</text>
    <text x="710" y="23" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">Worked Example</text>

    <!-- Row 1: Omission -->
    <rect x="0" y="45" width="820" height="45" rx="6" fill="#1e293b"/>
    <text x="140" y="72" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">1. Omission</text>
    <text x="430" y="72" fill="#cbd5e1" font-family="sans-serif" font-size="11" text-anchor="middle">Transaction completely unrecorded in books</text>
    <text x="710" y="72" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">Sh. 5k cash stationery unrecorded</text>

    <!-- Row 2: Commission -->
    <rect x="0" y="95" width="820" height="45" rx="6" fill="#1e293b"/>
    <text x="140" y="122" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">2. Commission</text>
    <text x="430" y="122" fill="#cbd5e1" font-family="sans-serif" font-size="11">Wrong person's account within same class</text>
    <text x="710" y="122" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">Credited Ochieng instead of Onyango</text>

    <!-- Row 3: Principle -->
    <rect x="0" y="145" width="820" height="45" rx="6" fill="#1e293b"/>
    <text x="140" y="172" fill="#f87171" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">3. Principle</text>
    <text x="430" y="172" fill="#cbd5e1" font-family="sans-serif" font-size="11">Violates capital vs. revenue guidelines (wrong class)</text>
    <text x="710" y="172" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">Van repairs debited to Motor Vehicle Asset</text>

    <!-- Row 4: Compensation -->
    <rect x="0" y="195" width="820" height="45" rx="6" fill="#1e293b"/>
    <text x="140" y="222" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">4. Compensation</text>
    <text x="430" y="222" fill="#cbd5e1" font-family="sans-serif" font-size="11">Separate errors on Dr &amp; Cr cancel each other out</text>
    <text x="710" y="222" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">Purchases -1k &amp; Sales -1k offset</text>

    <!-- Row 5: Reversal -->
    <rect x="0" y="245" width="820" height="45" rx="6" fill="#1e293b"/>
    <text x="140" y="272" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">5. Complete Reversal</text>
    <text x="430" y="272" fill="#cbd5e1" font-family="sans-serif" font-size="11">Correct accounts used, but Dr and Cr swapped</text>
    <text x="710" y="272" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">Rent paid debited to Cash &amp; credited to Rent</text>

    <!-- Row 6: Original Entry -->
    <rect x="0" y="295" width="820" height="45" rx="6" fill="#1e293b"/>
    <text x="140" y="322" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">6. Original Entry</text>
    <text x="430" y="322" fill="#cbd5e1" font-family="sans-serif" font-size="11">Wrong figure entered on both Dr and Cr sides</text>
    <text x="710" y="322" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">Sh. 9,400 recorded as Sh. 4,900 Dr &amp; Cr</text>
  </g>
</svg>"""

SVG_ONYATI_RECONSTRUCTION_FLOW = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <rect width="900" height="460" fill="#0f172a" rx="16"/>
  <text x="450" y="35" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold" text-anchor="middle">ONYATI CLERK TRIAL BALANCE RECONSTRUCTION CASE STUDY</text>

  <!-- Left: Incorrect Clerk Placement -->
  <g transform="translate(40, 65)">
    <rect x="0" y="0" width="390" height="360" rx="14" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
    <rect x="0" y="0" width="390" height="45" rx="14" fill="#be123c"/>
    <text x="195" y="28" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">CLERK'S INCORRECT DRAFT (268,020 vs 110,520)</text>

    <text x="20" y="75" fill="#f87171" font-family="sans-serif" font-size="12">• Capital 99,600 (Placed on DEBIT side ---> ERROR!)</text>
    <text x="20" y="105" fill="#f87171" font-family="sans-serif" font-size="12">• Debtors 30,520 (Placed on CREDIT side ---> ERROR!)</text>
    <text x="20" y="135" fill="#f87171" font-family="sans-serif" font-size="12">• Creditors 25,670 (Placed on DEBIT side ---> ERROR!)</text>
    <text x="20" y="165" fill="#f87171" font-family="sans-serif" font-size="12">• Motor Vehicles 80,000 (Placed on CREDIT side ---> ERROR!)</text>
    <text x="20" y="195" fill="#cbd5e1" font-family="sans-serif" font-size="12">• Cash 2,500 (Debit - Correct)</text>
    <text x="20" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="12">• Stock 140,250 (Debit - Correct)</text>

    <rect x="20" y="270" width="350" height="65" rx="8" fill="#be123c" fill-opacity="0.25"/>
    <text x="195" y="295" fill="#fca5a5" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Result: Massive Mismatch of Sh. 157,500!</text>
  </g>

  <!-- Right: Corrected Placement -->
  <g transform="translate(470, 65)">
    <rect x="0" y="0" width="390" height="360" rx="14" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <rect x="0" y="0" width="390" height="45" rx="14" fill="#059669"/>
    <text x="195" y="28" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">RECONSTRUCTED CORRECT PLACEMENT</text>

    <text x="20" y="75" fill="#34d399" font-family="sans-serif" font-size="12">• Capital 99,600 ---> Shifted to CREDIT side</text>
    <text x="20" y="105" fill="#34d399" font-family="sans-serif" font-size="12">• Debtors 30,520 ---> Shifted to DEBIT side</text>
    <text x="20" y="135" fill="#34d399" font-family="sans-serif" font-size="12">• Creditors 25,670 ---> Shifted to CREDIT side</text>
    <text x="20" y="165" fill="#34d399" font-family="sans-serif" font-size="12">• Motor Vehicles 80,000 ---> Shifted to DEBIT side</text>
    <text x="20" y="195" fill="#34d399" font-family="sans-serif" font-size="12">• Cash 2,500 ---> DEBIT side</text>
    <text x="20" y="225" fill="#34d399" font-family="sans-serif" font-size="12">• Stock 140,250 ---> DEBIT side</text>

    <rect x="20" y="270" width="350" height="65" rx="8" fill="#059669" fill-opacity="0.25"/>
    <text x="195" y="295" fill="#d1fae5" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">Result: Re-aligned Column Totals</text>
    <text x="195" y="315" fill="#d1fae5" font-family="sans-serif" font-size="11" text-anchor="middle">Dr: 253,270 | Cr: 125,270 (Exposes 128k omission)</text>
  </g>
</svg>"""
