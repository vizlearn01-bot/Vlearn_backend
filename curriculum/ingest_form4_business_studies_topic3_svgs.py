"""
VLearn Form 4 Business Studies — Topic 3 SVG Vector Graphics
Authoritative dark-mode high-contrast educational diagrams for Money and Banking.
"""

SVG_BARTER_VS_MONEY_FLOW = """<svg viewBox="0 0 840 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="barterBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <linearGradient id="moneyBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#064e3b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <linearGradient id="goldCoin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24" />
      <stop offset="100%" stop-color="#d97706" />
    </linearGradient>
    <marker id="bArrowRed" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f43f5e" />
    </marker>
    <marker id="mArrowGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="420" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Barter Bottleneck vs. Monetary Exchange Efficiency</text>
  <text x="420" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">How Money Resolves the Double Coincidence of Wants</text>

  <!-- Panel 1: Barter Trade Friction (Left) -->
  <rect x="30" y="80" width="370" height="310" rx="16" fill="url(#barterBg)" stroke="#f43f5e" stroke-width="1.5" />
  <text x="215" y="110" fill="#f43f5e" font-size="16" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">BARTER SYSTEM (Deadlock)</text>
  <text x="215" y="130" fill="#fecdd3" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">Requires Double Coincidence of Wants</text>

  <!-- Trader A -->
  <rect x="50" y="150" width="100" height="60" rx="10" fill="#334155" stroke="#94a3b8" />
  <text x="100" y="174" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Trader A</text>
  <text x="100" y="194" fill="#93c5fd" font-size="10" text-anchor="middle">Has: Goat | Wants: Fish</text>

  <!-- Trader B -->
  <rect x="280" y="150" width="100" height="60" rx="10" fill="#334155" stroke="#94a3b8" />
  <text x="330" y="174" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Trader B</text>
  <text x="330" y="194" fill="#a7f3d0" font-size="10" text-anchor="middle">Has: Fish | Wants: Maize</text>

  <!-- Trader C -->
  <rect x="165" y="270" width="100" height="60" rx="10" fill="#334155" stroke="#94a3b8" />
  <text x="215" y="294" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Trader C</text>
  <text x="215" y="314" fill="#fde68a" font-size="10" text-anchor="middle">Has: Maize | Wants: Goat</text>

  <!-- Mismatched Red Arrows -->
  <path d="M 150 170 L 280 170" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#bArrowRed)" />
  <text x="215" y="162" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">No Direct Match ✖</text>

  <path d="M 330 210 L 240 270" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#bArrowRed)" />
  <path d="M 190 270 L 100 210" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#bArrowRed)" />

  <rect x="70" y="348" width="290" height="26" rx="6" fill="#1e1b4b" />
  <text x="215" y="365" fill="#f43f5e" font-size="11" font-weight="700" text-anchor="middle">Trade Blocked: Exhausting Search Costs</text>

  <!-- Panel 2: Monetary Exchange (Right) -->
  <rect x="440" y="80" width="370" height="310" rx="16" fill="url(#moneyBg)" stroke="#34d399" stroke-width="1.5" />
  <text x="625" y="110" fill="#34d399" font-size="16" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">MONEY SYSTEM (Frictionless)</text>
  <text x="625" y="130" fill="#a7f3d0" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">Universal Intermediary Token of Exchange</text>

  <!-- Center Coin -->
  <circle cx="625" cy="225" r="32" fill="url(#goldCoin)" stroke="#fef08a" stroke-width="2" />
  <text x="625" y="222" fill="#78350f" font-size="13" font-weight="800" text-anchor="middle">MONEY</text>
  <text x="625" y="238" fill="#78350f" font-size="10" font-weight="700" text-anchor="middle">(KES)</text>

  <!-- Trader A (Right) -->
  <rect x="460" y="150" width="90" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" />
  <text x="505" y="172" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Trader A</text>
  <text x="505" y="188" fill="#93c5fd" font-size="9" text-anchor="middle">Sells Goat for KES</text>

  <!-- Trader B (Right) -->
  <rect x="700" y="150" width="90" height="50" rx="8" fill="#1e293b" stroke="#34d399" />
  <text x="745" y="172" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Trader B</text>
  <text x="745" y="188" fill="#a7f3d0" font-size="9" text-anchor="middle">Sells Fish for KES</text>

  <!-- Trader C (Right) -->
  <rect x="580" y="295" width="90" height="50" rx="8" fill="#1e293b" stroke="#fbbf24" />
  <text x="625" y="317" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Trader C</text>
  <text x="625" y="333" fill="#fde68a" font-size="9" text-anchor="middle">Sells Maize for KES</text>

  <!-- Green Connecting Arrows -->
  <path d="M 550 175 L 595 210" fill="none" stroke="#34d399" stroke-width="2.5" marker-end="url(#mArrowGreen)" />
  <path d="M 700 175 L 655 210" fill="none" stroke="#34d399" stroke-width="2.5" marker-end="url(#mArrowGreen)" />
  <path d="M 625 257 L 625 295" fill="none" stroke="#34d399" stroke-width="2.5" marker-end="url(#mArrowGreen)" />

  <rect x="480" y="355" width="290" height="26" rx="6" fill="#064e3b" />
  <text x="625" y="372" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">All Trades Complete Smoothly in Seconds</text>
</svg>"""

SVG_MONEY_EVOLUTION_TIMELINE = """<svg viewBox="0 0 860 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="stg1" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#be123c"/><stop offset="100%" stop-color="#881337"/></linearGradient>
    <linearGradient id="stg2" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#d97706"/><stop offset="100%" stop-color="#b45309"/></linearGradient>
    <linearGradient id="stg3" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#0369a1"/></linearGradient>
    <linearGradient id="stg4" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#059669"/><stop offset="100%" stop-color="#047857"/></linearGradient>
    <linearGradient id="stg5" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#6d28d9"/></linearGradient>
    <marker id="tArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="430" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">The Five Stages of Monetary Evolution</text>
  <text x="430" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">From Direct Commodity Swaps to Instant Cashless Digital Transfers</text>

  <!-- Stage 1: Barter -->
  <rect x="20" y="90" width="150" height="170" rx="14" fill="url(#stg1)" stroke="#f43f5e" stroke-width="2" />
  <text x="95" y="120" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">STAGE 1</text>
  <text x="95" y="140" fill="#fecdd3" font-size="13" font-weight="700" text-anchor="middle">Barter Trade</text>
  <text x="95" y="170" fill="#ffe4e6" font-size="11" text-anchor="middle">• Goods for goods</text>
  <text x="95" y="190" fill="#ffe4e6" font-size="11" text-anchor="middle">• High friction</text>
  <text x="95" y="210" fill="#ffe4e6" font-size="11" text-anchor="middle">• Double coincidence</text>
  <rect x="30" y="225" width="130" height="22" rx="6" fill="#0f172a" />
  <text x="95" y="240" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">Early Societies</text>

  <!-- Arrow 1 -> 2 -->
  <line x1="170" y1="175" x2="185" y2="175" stroke="#38bdf8" stroke-width="3" marker-end="url(#tArrow)" />

  <!-- Stage 2: Commodity Money -->
  <rect x="190" y="90" width="150" height="170" rx="14" fill="url(#stg2)" stroke="#fbbf24" stroke-width="2" />
  <text x="265" y="120" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">STAGE 2</text>
  <text x="265" y="140" fill="#fef3c7" font-size="13" font-weight="700" text-anchor="middle">Commodities</text>
  <text x="265" y="170" fill="#fffbeb" font-size="11" text-anchor="middle">• Salt, shells, cattle</text>
  <text x="265" y="190" fill="#fffbeb" font-size="11" text-anchor="middle">• Universal value</text>
  <text x="265" y="210" fill="#fffbeb" font-size="11" text-anchor="middle">• Perishable / bulky</text>
  <rect x="200" y="225" width="130" height="22" rx="6" fill="#0f172a" />
  <text x="265" y="240" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">Standard Tokens</text>

  <!-- Arrow 2 -> 3 -->
  <line x1="340" y1="175" x2="355" y2="175" stroke="#38bdf8" stroke-width="3" marker-end="url(#tArrow)" />

  <!-- Stage 3: Metallic Money -->
  <rect x="360" y="90" width="150" height="170" rx="14" fill="url(#stg3)" stroke="#38bdf8" stroke-width="2" />
  <text x="435" y="120" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">STAGE 3</text>
  <text x="435" y="140" fill="#e0f2fe" font-size="13" font-weight="700" text-anchor="middle">Metallic Coins</text>
  <text x="435" y="170" fill="#f0f9ff" font-size="11" text-anchor="middle">• Gold, silver, bronze</text>
  <text x="435" y="190" fill="#f0f9ff" font-size="11" text-anchor="middle">• Durable &amp; divisible</text>
  <text x="435" y="210" fill="#f0f9ff" font-size="11" text-anchor="middle">• Heavy to transport</text>
  <rect x="370" y="225" width="130" height="22" rx="6" fill="#0f172a" />
  <text x="435" y="240" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Stamped Metals</text>

  <!-- Arrow 3 -> 4 -->
  <line x1="510" y1="175" x2="525" y2="175" stroke="#38bdf8" stroke-width="3" marker-end="url(#tArrow)" />

  <!-- Stage 4: Paper Money -->
  <rect x="530" y="90" width="150" height="170" rx="14" fill="url(#stg4)" stroke="#34d399" stroke-width="2" />
  <text x="605" y="120" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">STAGE 4</text>
  <text x="605" y="140" fill="#d1fae5" font-size="13" font-weight="700" text-anchor="middle">Paper Money</text>
  <text x="605" y="170" fill="#ecfdf5" font-size="11" text-anchor="middle">• Goldsmith receipts</text>
  <text x="605" y="190" fill="#ecfdf5" font-size="11" text-anchor="middle">• Central Bank notes</text>
  <text x="605" y="210" fill="#ecfdf5" font-size="11" text-anchor="middle">• Highly portable</text>
  <rect x="540" y="225" width="130" height="22" rx="6" fill="#0f172a" />
  <text x="605" y="240" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Legal Tender</text>

  <!-- Arrow 4 -> 5 -->
  <line x1="680" y1="175" x2="695" y2="175" stroke="#38bdf8" stroke-width="3" marker-end="url(#tArrow)" />

  <!-- Stage 5: Electronic / Mobile -->
  <rect x="700" y="90" width="140" height="170" rx="14" fill="url(#stg5)" stroke="#c084fc" stroke-width="2" />
  <text x="770" y="120" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">STAGE 5</text>
  <text x="770" y="140" fill="#f3e8ff" font-size="13" font-weight="700" text-anchor="middle">Digital Money</text>
  <text x="770" y="170" fill="#faf5ff" font-size="11" text-anchor="middle">• M-Pesa, EFT, Cards</text>
  <text x="770" y="190" fill="#faf5ff" font-size="11" text-anchor="middle">• Instant transfers</text>
  <text x="770" y="210" fill="#faf5ff" font-size="11" text-anchor="middle">• Completely cashless</text>
  <rect x="705" y="225" width="130" height="22" rx="6" fill="#0f172a" />
  <text x="770" y="240" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">Modern Era</text>

  <!-- Summary Banner -->
  <rect x="60" y="290" width="740" height="60" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
  <text x="430" y="318" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Evolutionary Driving Force: Minimizing Transaction Friction &amp; Maximizing Trust</text>
  <text x="430" y="338" fill="#cbd5e1" font-size="12" text-anchor="middle" font-family="system-ui, sans-serif">Each stage resolved physical limitations of durability, portability, and divisibility.</text>
</svg>"""

SVG_LIQUIDITY_PREFERENCE_TREE = """<svg viewBox="0 0 840 440" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="lpRoot" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <linearGradient id="txMotive" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#059669"/><stop offset="100%" stop-color="#064e3b"/></linearGradient>
    <linearGradient id="prMotive" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#d97706"/><stop offset="100%" stop-color="#78350f"/></linearGradient>
    <linearGradient id="spMotive" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#4c1d95"/></linearGradient>
    <marker id="lpArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="420" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Liquidity Preference: The Three Motives for Holding Cash</text>
  <text x="420" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">Why Rational Individuals and Firms Choose Liquid Cash Over Illiquid Assets</text>

  <!-- Root Node: LIQUIDITY PREFERENCE -->
  <rect x="280" y="80" width="280" height="60" rx="14" fill="url(#lpRoot)" stroke="#38bdf8" stroke-width="2" />
  <text x="420" y="106" fill="#ffffff" font-size="15" font-weight="800" text-anchor="middle">DEMAND FOR MONEY</text>
  <text x="420" y="126" fill="#38bdf8" font-size="12" font-weight="600" text-anchor="middle">(Liquidity Preference)</text>

  <!-- Branch Lines -->
  <path d="M 320 140 L 150 190" fill="none" stroke="#34d399" stroke-width="2.5" marker-end="url(#lpArrow)" />
  <path d="M 420 140 L 420 190" fill="none" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#lpArrow)" />
  <path d="M 520 140 L 690 190" fill="none" stroke="#c084fc" stroke-width="2.5" marker-end="url(#lpArrow)" />

  <!-- 1. Transaction Motive (Left) -->
  <rect x="40" y="195" width="220" height="135" rx="12" fill="url(#txMotive)" stroke="#34d399" stroke-width="1.5" />
  <text x="150" y="222" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">1. TRANSACTION</text>
  <text x="150" y="240" fill="#a7f3d0" font-size="11" text-anchor="middle">Daily regular expenses</text>
  <line x1="55" y1="248" x2="245" y2="248" stroke="#34d399" stroke-width="1" />
  <text x="150" y="268" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">• Income: Food, fare, rent</text>
  <text x="150" y="286" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">• Business: Wages, materials</text>
  <text x="150" y="310" fill="#d1fae5" font-size="10" text-anchor="middle">(Depends on Income Level)</text>

  <!-- 2. Precautionary Motive (Center) -->
  <rect x="310" y="195" width="220" height="135" rx="12" fill="url(#prMotive)" stroke="#fbbf24" stroke-width="1.5" />
  <text x="420" y="222" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">2. PRECAUTIONARY</text>
  <text x="420" y="240" fill="#fde68a" font-size="11" text-anchor="middle">Unforeseen emergencies</text>
  <line x1="325" y1="248" x2="515" y2="248" stroke="#fbbf24" stroke-width="1" />
  <text x="420" y="268" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">• Sudden illness / hospital</text>
  <text x="420" y="286" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">• Urgent vehicle repairs</text>
  <text x="420" y="310" fill="#fef3c7" font-size="10" text-anchor="middle">(Emergency Buffer Fund)</text>

  <!-- 3. Speculative Motive (Right) -->
  <rect x="580" y="195" width="220" height="135" rx="12" fill="url(#spMotive)" stroke="#c084fc" stroke-width="1.5" />
  <text x="690" y="222" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">3. SPECULATIVE</text>
  <text x="690" y="240" fill="#e9d5ff" font-size="11" text-anchor="middle">Investment opportunities</text>
  <line x1="595" y1="248" x2="785" y2="248" stroke="#c084fc" stroke-width="1" />
  <text x="690" y="268" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">• Buying cheap shares</text>
  <text x="690" y="286" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">• Land &amp; asset price dips</text>
  <text x="690" y="310" fill="#f3e8ff" font-size="10" text-anchor="middle">(Depends on Interest Rates)</text>

  <!-- Money Supply Bottom Banner -->
  <rect x="40" y="355" width="760" height="60" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
  <text x="420" y="380" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">MONEY SUPPLY = Currency in Circulation (Banknotes + Coins) + Demand Deposits (Current Accounts)</text>
  <text x="420" y="400" fill="#94a3b8" font-size="11" text-anchor="middle">Regulated by the Central Bank of Kenya to manage inflation and stabilize the shilling.</text>
</svg>"""

SVG_KENYAN_BANKING_PYRAMID = """<svg viewBox="0 0 840 440" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="cbkApex" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#0369a1"/></linearGradient>
    <linearGradient id="commTier" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#059669"/><stop offset="100%" stop-color="#047857"/></linearGradient>
    <linearGradient id="devTier" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#d97706"/><stop offset="100%" stop-color="#b45309"/></linearGradient>
    <linearGradient id="nbfiTier" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#6d28d9"/></linearGradient>
  </defs>

  <!-- Title -->
  <text x="420" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">The Kenyan Banking &amp; Financial System Hierarchy</text>
  <text x="420" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">Regulatory Structure and Institutional Classification</text>

  <!-- Tier 1: Apex - CBK -->
  <polygon points="420,80 300,150 540,150" fill="url(#cbkApex)" stroke="#38bdf8" stroke-width="2" />
  <text x="420" y="120" fill="#ffffff" font-size="14" font-weight="800" text-anchor="middle">CENTRAL BANK OF KENYA</text>
  <text x="420" y="138" fill="#e0f2fe" font-size="10" font-weight="600" text-anchor="middle">(Apex Monetary Regulator)</text>

  <!-- Tier 2: Commercial Banks -->
  <polygon points="300,155 210,230 630,230 540,155" fill="url(#commTier)" stroke="#34d399" stroke-width="2" />
  <text x="420" y="185" fill="#ffffff" font-size="15" font-weight="700" text-anchor="middle">COMMERCIAL BANKS</text>
  <text x="420" y="205" fill="#d1fae5" font-size="11" text-anchor="middle">KCB, Equity, Co-op, Absa, Stanbic</text>
  <text x="420" y="222" fill="#a7f3d0" font-size="10" text-anchor="middle">• Demand Deposits • Cheques • Overdrafts • Credit Creation</text>

  <!-- Tier 3: Specialized Development Banks -->
  <polygon points="210,235 130,310 710,310 630,235" fill="url(#devTier)" stroke="#fbbf24" stroke-width="2" />
  <text x="420" y="265" fill="#ffffff" font-size="15" font-weight="700" text-anchor="middle">SPECIALIZED DEVELOPMENT BANKS (DFIs)</text>
  <text x="420" y="285" fill="#fef3c7" font-size="11" text-anchor="middle">Industrial Development Bank (IDB), KIE, DFCK, Agricultural Finance Corp (AFC)</text>
  <text x="420" y="302" fill="#fde68a" font-size="10" text-anchor="middle">• Long-term Capital • Industrial &amp; Agricultural Infrastructure Financing</text>

  <!-- Tier 4: Non-Bank Financial Institutions (NBFIs) -->
  <polygon points="130,315 40,395 800,395 710,315" fill="url(#nbfiTier)" stroke="#c084fc" stroke-width="2" />
  <text x="420" y="345" fill="#ffffff" font-size="15" font-weight="700" text-anchor="middle">NON-BANK FINANCIAL INSTITUTIONS (NBFIs)</text>
  <text x="420" y="365" fill="#f3e8ff" font-size="11" text-anchor="middle">SACCOs (Mwalimu, Stima) • Insurance Companies • Building Societies (HFCK) • Pension Funds (NSSF)</text>
  <text x="420" y="382" fill="#e9d5ff" font-size="10" text-anchor="middle">• Mobilize Sectoral Savings • Long-term Mortgages • NO Cheque Accounts • NO Credit Creation</text>

  <!-- Bottom note -->
  <text x="420" y="420" fill="#94a3b8" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">Governed under Banking Act, CBK Prudential Guidelines, SACCO Societies Act, and Insurance Act.</text>
</svg>"""

SVG_MONETARY_POLICY_TRANSMISSION = """<svg viewBox="0 0 860 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="background:#090d16; border-radius:1.5rem;">
  <defs>
    <linearGradient id="cbkBox" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <linearGradient id="commBox" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#059669"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <linearGradient id="mktBox" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#d97706"/><stop offset="100%" stop-color="#0f172a"/></linearGradient>
    <marker id="polArrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
    </marker>
  </defs>

  <!-- Title -->
  <text x="430" y="36" fill="#f8fafc" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Central Bank Monetary Policy Transmission Mechanism</text>
  <text x="430" y="58" fill="#94a3b8" font-size="13" text-anchor="middle" font-family="system-ui, sans-serif">How CBK Credit Control Tools Regulate Money Supply &amp; Cool Inflation</text>

  <!-- Step 1: CBK Tools Box (Left) -->
  <rect x="30" y="90" width="240" height="230" rx="14" fill="url(#cbkBox)" stroke="#38bdf8" stroke-width="2" />
  <text x="150" y="120" fill="#38bdf8" font-size="15" font-weight="800" text-anchor="middle">1. CBK ACTION</text>
  <text x="150" y="140" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">(To Curb High Inflation)</text>
  <line x1="45" y1="150" x2="255" y2="150" stroke="#38bdf8" stroke-width="1" />
  <text x="50" y="175" fill="#e0f2fe" font-size="11" font-weight="600">▲ Raise Bank Rate (Discount)</text>
  <text x="50" y="205" fill="#e0f2fe" font-size="11" font-weight="600">▲ Sell Treasury Bills (OMO)</text>
  <text x="50" y="235" fill="#e0f2fe" font-size="11" font-weight="600">▲ Raise Cash Reserve Ratio</text>
  <text x="50" y="265" fill="#e0f2fe" font-size="11" font-weight="600">▲ Moral Suasion / Directives</text>
  <rect x="45" y="285" width="210" height="22" rx="6" fill="#0f172a" />
  <text x="150" y="300" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Tight Monetary Policy</text>

  <!-- Arrow 1 -> 2 -->
  <path d="M 270 205 L 305 205" fill="none" stroke="#38bdf8" stroke-width="3" marker-end="url(#polArrow)" />

  <!-- Step 2: Commercial Bank Response (Middle) -->
  <rect x="310" y="90" width="240" height="230" rx="14" fill="url(#commBox)" stroke="#34d399" stroke-width="2" />
  <text x="430" y="120" fill="#34d399" font-size="15" font-weight="800" text-anchor="middle">2. BANK RESPONSE</text>
  <text x="430" y="140" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">(Credit Constriction)</text>
  <line x1="325" y1="150" x2="535" y2="150" stroke="#34d399" stroke-width="1" />
  <text x="330" y="175" fill="#d1fae5" font-size="11" font-weight="600">▲ Borrowing from CBK costlier</text>
  <text x="330" y="205" fill="#d1fae5" font-size="11" font-weight="600">▼ Excess liquid cash drained</text>
  <text x="330" y="235" fill="#d1fae5" font-size="11" font-weight="600">▲ Banks raise loan interest rates</text>
  <text x="330" y="265" fill="#d1fae5" font-size="11" font-weight="600">▼ Lending criteria tightened</text>
  <rect x="325" y="285" width="210" height="22" rx="6" fill="#0f172a" />
  <text x="430" y="300" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Lending Capacity Drops</text>

  <!-- Arrow 2 -> 3 -->
  <path d="M 550 205 L 585 205" fill="none" stroke="#34d399" stroke-width="3" marker-end="url(#polArrow)" />

  <!-- Step 3: Real Economy Outcome (Right) -->
  <rect x="590" y="90" width="240" height="230" rx="14" fill="url(#mktBox)" stroke="#fbbf24" stroke-width="2" />
  <text x="710" y="120" fill="#fbbf24" font-size="15" font-weight="800" text-anchor="middle">3. MACRO OUTCOME</text>
  <text x="710" y="140" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">(Price Stabilization)</text>
  <line x1="605" y1="150" x2="815" y2="150" stroke="#fbbf24" stroke-width="1" />
  <text x="610" y="175" fill="#fef3c7" font-size="11" font-weight="600">▼ Public borrowing falls</text>
  <text x="610" y="205" fill="#fef3c7" font-size="11" font-weight="600">▼ Consumer spending slows</text>
  <text x="610" y="235" fill="#fef3c7" font-size="11" font-weight="600">▼ Money supply contracts</text>
  <text x="610" y="265" fill="#fef3c7" font-size="11" font-weight="600">▼ Inflation rate declines</text>
  <rect x="605" y="285" width="210" height="22" rx="6" fill="#0f172a" />
  <text x="710" y="300" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">Price Level Stabilized</text>

  <!-- Summary Footer -->
  <rect x="30" y="340" width="800" height="55" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
  <text x="430" y="365" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle">Expansionary Policy is the Exact Reverse: Lower Bank Rate, Buy Treasury Bills, Lower Cash Ratio</text>
  <text x="430" y="385" fill="#94a3b8" font-size="11" text-anchor="middle">Used during economic recessions to stimulate commercial lending and boost aggregate demand.</text>
</svg>"""
