"""
VLearn CBC Grade 10 Business Studies — Topic 13: Business Transactions
Vector SVG Diagram Definitions (Lessons 1 to 5)
Dark theme optimized (viewBox='0 0 960 520')
"""

# =============================================================================
# LESSON 1: Meaning and Nature of Business Transactions
# =============================================================================
SVG_TRANSACTION_ANATOMY_AND_TAXONOMY = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="t13_bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="t13_blue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284C7" />
      <stop offset="100%" stop-color="#0369A1" />
    </linearGradient>
    <linearGradient id="t13_emerald" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <linearGradient id="t13_purple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7C3AED" />
      <stop offset="100%" stop-color="#6D28D9" />
    </linearGradient>
    <linearGradient id="t13_amber" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D97706" />
      <stop offset="100%" stop-color="#B45309" />
    </linearGradient>
    <filter id="t13_glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#38BDF8" flood-opacity="0.25" />
    </filter>
    <filter id="t13_card_shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="960" height="520" fill="url(#t13_bg)" rx="16" />

  <!-- Header Section -->
  <g transform="translate(40, 24)">
    <rect x="0" y="0" width="880" height="60" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1.5" />
    <text x="440" y="28" font-family="system-ui, -apple-system, sans-serif" font-size="18" font-weight="700" fill="#F8FAFC" text-anchor="middle">Anatomy &amp; Taxonomy of Business Transactions</text>
    <text x="440" y="48" font-family="system-ui, -apple-system, sans-serif" font-size="12" fill="#94A3B8" text-anchor="middle">Four Pillars of Validity, Internal vs. External Exchanges, and Accounting Impact</text>
  </g>

  <!-- 4 Pillars of a Valid Transaction (Top Cards) -->
  <g transform="translate(40, 96)">
    <!-- Pillar 1: Two Parties -->
    <g transform="translate(0, 0)" filter="url(#t13_card_shadow)">
      <rect width="208" height="96" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5" />
      <circle cx="28" cy="28" r="14" fill="#0284C7" />
      <text x="28" y="33" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1</text>
      <text x="50" y="32" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#38BDF8">Two Parties</text>
      <text x="14" y="56" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">Requires a buyer &amp; seller,</text>
      <text x="14" y="72" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8">or payer and payee entity.</text>
    </g>

    <!-- Pillar 2: Exchange of Value -->
    <g transform="translate(224, 0)" filter="url(#t13_card_shadow)">
      <rect width="208" height="96" rx="8" fill="#1E293B" stroke="#34D399" stroke-width="1.5" />
      <circle cx="28" cy="28" r="14" fill="#059669" />
      <text x="28" y="33" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2</text>
      <text x="50" y="32" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#34D399">Exchange of Value</text>
      <text x="14" y="56" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">Transfer of cash, goods,</text>
      <text x="14" y="72" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8">services, or legal rights.</text>
    </g>

    <!-- Pillar 3: Monetary Measure -->
    <g transform="translate(448, 0)" filter="url(#t13_card_shadow)">
      <rect width="208" height="96" rx="8" fill="#1E293B" stroke="#FBBF24" stroke-width="1.5" />
      <circle cx="28" cy="28" r="14" fill="#D97706" />
      <text x="28" y="33" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3</text>
      <text x="50" y="32" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#FBBF24">Monetary Value</text>
      <text x="14" y="56" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">Objectively measurable</text>
      <text x="14" y="72" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8">in currency (e.g. KES).</text>
    </g>

    <!-- Pillar 4: Source Document -->
    <g transform="translate(672, 0)" filter="url(#t13_card_shadow)">
      <rect width="208" height="96" rx="8" fill="#1E293B" stroke="#A78BFA" stroke-width="1.5" />
      <circle cx="28" cy="28" r="14" fill="#7C3AED" />
      <text x="28" y="33" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4</text>
      <text x="50" y="32" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#A78BFA">Source Document</text>
      <text x="14" y="56" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">Backed by written proof</text>
      <text x="14" y="72" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8">(Receipt, Invoice, ETR).</text>
    </g>
  </g>

  <!-- Central Dual Branching (External vs Internal vs Non-Transaction) -->
  <g transform="translate(40, 206)">
    <!-- External Transactions Column -->
    <g transform="translate(0, 0)" filter="url(#t13_card_shadow)">
      <rect width="280" height="200" rx="10" fill="#1E293B" stroke="#0284C7" stroke-width="2" />
      <rect x="0" y="0" width="280" height="36" rx="10" fill="url(#t13_blue)" />
      <text x="140" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">EXTERNAL TRANSACTIONS</text>
      
      <text x="16" y="60" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#38BDF8">Exchanges with Outside Parties:</text>
      <text x="16" y="80" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Cash / Credit sales to buyers</text>
      <text x="16" y="98" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Stock purchases from suppliers</text>
      <text x="16" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Paying Kenya Power electricity bills</text>
      <text x="16" y="134" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Borrowing loan from commercial bank</text>

      <rect x="12" y="152" width="256" height="36" rx="6" fill="#0F172A" stroke="#0284C7" stroke-width="1" />
      <text x="140" y="174" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#38BDF8" text-anchor="middle">Impacts Cash, Debtors &amp; Creditors</text>
    </g>

    <!-- Internal Transactions Column -->
    <g transform="translate(300, 0)" filter="url(#t13_card_shadow)">
      <rect width="280" height="200" rx="10" fill="#1E293B" stroke="#059669" stroke-width="2" />
      <rect x="0" y="0" width="280" height="36" rx="10" fill="url(#t13_emerald)" />
      <text x="140" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">INTERNAL TRANSACTIONS</text>
      
      <text x="16" y="60" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#34D399">Events Within the Business Entity:</text>
      <text x="16" y="80" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Depreciating delivery van value</text>
      <text x="16" y="98" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Stock transfer: Warehouse to shop</text>
      <text x="16" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Writing off obsolete damaged stock</text>
      <text x="16" y="134" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Capitalizing factory repair costs</text>

      <rect x="12" y="152" width="256" height="36" rx="6" fill="#0F172A" stroke="#059669" stroke-width="1" />
      <text x="140" y="174" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#34D399" text-anchor="middle">Adjusts Internal Asset Book Values</text>
    </g>

    <!-- Non-Transaction Events Column (Filtered Out) -->
    <g transform="translate(600, 0)" filter="url(#t13_card_shadow)">
      <rect width="280" height="200" rx="10" fill="#1E293B" stroke="#EF4444" stroke-width="2" />
      <rect x="0" y="0" width="280" height="36" rx="10" fill="#991B1B" />
      <text x="140" y="24" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">NON-TRANSACTION EVENTS</text>
      
      <text x="16" y="60" font-family="system-ui, sans-serif" font-size="12" font-weight="600" fill="#F87171">Events With NO Accounting Entry:</text>
      <text x="16" y="80" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Discussing order over tea with client</text>
      <text x="16" y="98" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Wiping dust off phone displays</text>
      <text x="16" y="116" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Signing worker contract (before start)</text>
      <text x="16" y="134" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• Requesting supplier price catalogues</text>

      <rect x="12" y="152" width="256" height="36" rx="6" fill="#0F172A" stroke="#EF4444" stroke-width="1" />
      <text x="140" y="174" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#F87171" text-anchor="middle">NEVER Recorded in Financial Books</text>
    </g>
  </g>

  <!-- Bottom Summary Strip: Fundamental Accounting Rule -->
  <g transform="translate(40, 420)">
    <rect width="880" height="76" rx="10" fill="#1E293B" stroke="#475569" stroke-width="1" />
    <text x="24" y="28" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#38BDF8">Fundamental Accounting Equation Test:</text>
    <text x="24" y="52" font-family="system-ui, sans-serif" font-size="12" fill="#E2E8F0">Every valid transaction alters: <tspan fill="#38BDF8" font-weight="bold">Assets (A)</tspan> = <tspan fill="#FBBF24" font-weight="bold">Liabilities (L)</tspan> + <tspan fill="#34D399" font-weight="bold">Owner's Equity (OE)</tspan>. If an event has $0 financial impact, it is excluded.</text>
    <rect x="740" y="18" width="120" height="40" rx="6" fill="#0284C7" />
    <text x="800" y="43" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">Δ A = Δ L + Δ OE</text>
  </g>
</svg>"""


# =============================================================================
# LESSON 2: Cash Transactions
# =============================================================================
SVG_CASH_TRANSACTION_DYNAMICS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="c_bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="c_emerald_grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <linearGradient id="c_blue_grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0EA5E9" />
      <stop offset="100%" stop-color="#0369A1" />
    </linearGradient>
    <filter id="c_shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.35" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="960" height="520" fill="url(#c_bg)" rx="16" />

  <!-- Header -->
  <g transform="translate(40, 24)">
    <rect x="0" y="0" width="880" height="60" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1.5" />
    <text x="440" y="28" font-family="system-ui, sans-serif" font-size="18" font-weight="700" fill="#F8FAFC" text-anchor="middle">Cash Transaction Settlement Mechanism &amp; Liquidity Flow</text>
    <text x="440" y="48" font-family="system-ui, sans-serif" font-size="12" fill="#94A3B8" text-anchor="middle">Immediate Value Exchange, Cash Discount Mechanics, and Working Capital Acceleration</text>
  </g>

  <!-- Left: Instant Settlement Loop -->
  <g transform="translate(40, 96)" filter="url(#c_shadow)">
    <rect width="424" height="290" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="1.5" />
    <rect x="0" y="0" width="424" height="34" rx="10" fill="url(#c_emerald_grad)" />
    <text x="212" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">IMMEDIATE SETTLEMENT ARCHITECTURE</text>

    <!-- Buyer to Seller Exchange -->
    <g transform="translate(20, 50)">
      <!-- Buyer Box -->
      <rect x="0" y="0" width="110" height="60" rx="8" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5" />
      <text x="55" y="26" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#38BDF8" text-anchor="middle">BUYER</text>
      <text x="55" y="44" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">(Instant Payer)</text>

      <!-- Flow Arrows -->
      <path d="M 120 18 L 264 18" stroke="#10B981" stroke-width="3" />
      <text x="192" y="12" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#34D399" text-anchor="middle">Immediate Cash (KES)</text>

      <path d="M 264 42 L 120 42" stroke="#38BDF8" stroke-width="3" />
      <text x="192" y="56" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8" text-anchor="middle">Goods / Receipt Issued</text>

      <!-- Seller Box -->
      <rect x="274" y="0" width="110" height="60" rx="8" fill="#0F172A" stroke="#10B981" stroke-width="1.5" />
      <text x="329" y="26" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#34D399" text-anchor="middle">SELLER</text>
      <text x="329" y="44" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">(Instant Cash In)</text>
    </g>

    <!-- Cash Formats in Kenya -->
    <g transform="translate(20, 130)">
      <text x="0" y="14" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#F8FAFC">Accepted Instant Cash Instruments:</text>
      <rect x="0" y="24" width="88" height="44" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="44" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#FBBF24" text-anchor="middle">Physical</text>
      <text x="44" y="56" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">Notes &amp; Coins</text>

      <rect x="98" y="24" width="88" height="44" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="142" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#34D399" text-anchor="middle">Mobile Money</text>
      <text x="142" y="56" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">M-Pesa / Till</text>

      <rect x="196" y="24" width="88" height="44" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="240" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8" text-anchor="middle">Debit Card</text>
      <text x="240" y="56" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">POS Swipe</text>

      <rect x="294" y="24" width="88" height="44" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="338" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#A78BFA" text-anchor="middle">Instant Transfer</text>
      <text x="338" y="56" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">PesaLink</text>
    </g>

    <!-- Key Outcome Box -->
    <rect x="20" y="218" width="384" height="52" rx="6" fill="#0F172A" stroke="#10B981" stroke-dasharray="3" />
    <text x="212" y="238" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#34D399" text-anchor="middle">Zero Bad Debt Risk &amp; 100% Immediate Liquidity</text>
    <text x="212" y="256" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">No accounts receivable to track, zero debtor collection expenses.</text>
  </g>

  <!-- Right: Discount & Trade-Off Architecture -->
  <g transform="translate(488, 96)" filter="url(#c_shadow)">
    <rect width="432" height="290" rx="10" fill="#1E293B" stroke="#0EA5E9" stroke-width="1.5" />
    <rect x="0" y="0" width="432" height="34" rx="10" fill="url(#c_blue_grad)" />
    <text x="216" y="22" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">TRADE DISCOUNT VS. CASH DISCOUNT</text>

    <!-- Step Calculation Flow -->
    <g transform="translate(20, 48)">
      <rect x="0" y="0" width="392" height="50" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="14" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FBBF24">Step 1: Trade Discount (TD)</text>
      <text x="14" y="38" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">Deducted from Catalogue List Price for bulk orders -> Yields <tspan fill="#38BDF8" font-weight="bold">Net Invoice Price</tspan>.</text>

      <rect x="0" y="60" width="392" height="50" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="14" y="82" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34D399">Step 2: Cash Discount (CD)</text>
      <text x="14" y="98" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">Calculated on Net Invoice Price for instant payment -> Yields <tspan fill="#34D399" font-weight="bold">Final Cash Settled</tspan>.</text>
    </g>

    <!-- Pros vs Cons Quick Grid -->
    <g transform="translate(20, 172)">
      <!-- Advantages -->
      <rect x="0" y="0" width="190" height="98" rx="6" fill="#0F172A" stroke="#10B981" />
      <text x="10" y="18" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34D399">✓ Cash Advantages:</text>
      <text x="10" y="36" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Instant cash re-invested</text>
      <text x="10" y="52" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Zero customer default loss</text>
      <text x="10" y="68" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Higher supplier discounts</text>
      <text x="10" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Reduced paperwork</text>

      <!-- Disadvantages -->
      <rect x="202" y="0" width="190" height="98" rx="6" fill="#0F172A" stroke="#EF4444" />
      <text x="212" y="18" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#F87171">✗ Cash Limitations:</text>
      <text x="212" y="36" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Caps sales to cash-at-hand</text>
      <text x="212" y="52" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Physical cash theft risk</text>
      <text x="212" y="68" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Mobile / POS merchant fees</text>
      <text x="212" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Inconvenient for large sums</text>
    </g>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(40, 400)">
    <rect width="880" height="96" rx="10" fill="#1E293B" stroke="#475569" stroke-width="1" />
    <text x="24" y="28" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#38BDF8">Kenyan MSME Insight — The Working Capital Flywheel:</text>
    <text x="24" y="50" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">When wholesale kiosk owners in Kisumu collect cash instantly via M-Pesa Till, they restock daily from farmers, capturing supplier cash discounts (3-5%)</text>
    <text x="24" y="70" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8">and avoiding bank overdraft interest. Cash velocity dramatically increases return on working capital.</text>
  </g>
</svg>"""


# =============================================================================
# LESSON 3: Credit Transactions
# =============================================================================
SVG_CREDIT_LIFECYCLE_AND_RISK_FRAMEWORK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="cr_bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="cr_purple_grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8B5CF6" />
      <stop offset="100%" stop-color="#6D28D9" />
    </linearGradient>
    <linearGradient id="cr_amber_grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#B45309" />
    </linearGradient>
    <filter id="cr_shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="960" height="520" fill="url(#cr_bg)" rx="16" />

  <!-- Header -->
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="880" height="56" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1.5" />
    <text x="440" y="26" font-family="system-ui, sans-serif" font-size="18" font-weight="700" fill="#F8FAFC" text-anchor="middle">Credit Transaction Lifecycle &amp; The 5 Cs Appraisal Model</text>
    <text x="440" y="44" font-family="system-ui, sans-serif" font-size="12" fill="#94A3B8" text-anchor="middle">Deferred Settlement, Debtors vs. Creditors, Credit Terms (2/10, net 30), and Bad Debt Mitigation</text>
  </g>

  <!-- 5-Stage Credit Lifecycle Flow (Top Section) -->
  <g transform="translate(40, 88)">
    <text x="0" y="14" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#38BDF8">STAGES OF A COMMERCIAL CREDIT SALE:</text>

    <!-- Stage 1 -->
    <g transform="translate(0, 24)" filter="url(#cr_shadow)">
      <rect width="164" height="74" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5" />
      <text x="82" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8" text-anchor="middle">1. Application</text>
      <text x="82" y="42" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0" text-anchor="middle">Buyer requests goods</text>
      <text x="82" y="58" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">on deferred payment</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 168 61 L 176 61" stroke="#38BDF8" stroke-width="2" />

    <!-- Stage 2 -->
    <g transform="translate(178, 24)" filter="url(#cr_shadow)">
      <rect width="164" height="74" rx="8" fill="#1E293B" stroke="#818CF8" stroke-width="1.5" />
      <text x="82" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#818CF8" text-anchor="middle">2. Credit Appraisal</text>
      <text x="82" y="42" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0" text-anchor="middle">5 Cs evaluation &amp;</text>
      <text x="82" y="58" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">CRB score check</text>
    </g>

    <!-- Arrow 2 -->
    <path d="M 346 61 L 354 61" stroke="#818CF8" stroke-width="2" />

    <!-- Stage 3 -->
    <g transform="translate(356, 24)" filter="url(#cr_shadow)">
      <rect width="164" height="74" rx="8" fill="#1E293B" stroke="#FBBF24" stroke-width="1.5" />
      <text x="82" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FBBF24" text-anchor="middle">3. Invoice &amp; Delivery</text>
      <text x="82" y="42" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0" text-anchor="middle">Sales Invoice issued</text>
      <text x="82" y="58" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">e.g. "2/10, net 30"</text>
    </g>

    <!-- Arrow 3 -->
    <path d="M 524 61 L 532 61" stroke="#FBBF24" stroke-width="2" />

    <!-- Stage 4 -->
    <g transform="translate(534, 24)" filter="url(#cr_shadow)">
      <rect width="164" height="74" rx="8" fill="#1E293B" stroke="#34D399" stroke-width="1.5" />
      <text x="82" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34D399" text-anchor="middle">4. Aging &amp; Debtors</text>
      <text x="82" y="42" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0" text-anchor="middle">Recorded as Asset</text>
      <text x="82" y="58" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8" text-anchor="middle">Tracked in ledger</text>
    </g>

    <!-- Arrow 4 -->
    <path d="M 702 61 L 710 61" stroke="#34D399" stroke-width="2" />

    <!-- Stage 5 -->
    <g transform="translate(712, 24)" filter="url(#cr_shadow)">
      <rect width="168" height="74" rx="8" fill="#1E293B" stroke="#F87171" stroke-width="1.5" />
      <text x="84" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#F87171" text-anchor="middle">5. Final Settlement</text>
      <text x="84" y="42" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0" text-anchor="middle">Cash received OR</text>
      <text x="84" y="58" font-family="system-ui, sans-serif" font-size="9" fill="#F87171" text-anchor="middle">Bad Debt written off</text>
    </g>
  </g>

  <!-- Middle Section: The 5 Cs of Credit Appraisal Grid -->
  <g transform="translate(40, 200)">
    <rect width="570" height="204" rx="10" fill="#1E293B" stroke="#8B5CF6" stroke-width="1.5" filter="url(#cr_shadow)" />
    <rect x="0" y="0" width="570" height="32" rx="10" fill="url(#cr_purple_grad)" />
    <text x="285" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">THE 5 Cs OF CREDIT APPRAISAL (RISK PREVENTION)</text>

    <g transform="translate(16, 44)">
      <!-- C1: Character -->
      <rect x="0" y="0" width="102" height="68" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="51" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8" text-anchor="middle">Character</text>
      <text x="51" y="36" font-family="system-ui, sans-serif" font-size="9" fill="#E2E8F0" text-anchor="middle">Integrity &amp; CRB</text>
      <text x="51" y="50" font-family="system-ui, sans-serif" font-size="8" fill="#94A3B8" text-anchor="middle">credit history</text>

      <!-- C2: Capacity -->
      <rect x="110" y="0" width="102" height="68" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="161" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34D399" text-anchor="middle">Capacity</text>
      <text x="161" y="36" font-family="system-ui, sans-serif" font-size="9" fill="#E2E8F0" text-anchor="middle">Cash turnover</text>
      <text x="161" y="50" font-family="system-ui, sans-serif" font-size="8" fill="#94A3B8" text-anchor="middle">to service debt</text>

      <!-- C3: Capital -->
      <rect x="220" y="0" width="102" height="68" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="271" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FBBF24" text-anchor="middle">Capital</text>
      <text x="271" y="36" font-family="system-ui, sans-serif" font-size="9" fill="#E2E8F0" text-anchor="middle">Net worth &amp;</text>
      <text x="271" y="50" font-family="system-ui, sans-serif" font-size="8" fill="#94A3B8" text-anchor="middle">owner equity</text>

      <!-- C4: Collateral -->
      <rect x="330" y="0" width="102" height="68" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="381" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#F87171" text-anchor="middle">Collateral</text>
      <text x="381" y="36" font-family="system-ui, sans-serif" font-size="9" fill="#E2E8F0" text-anchor="middle">Pledged assets</text>
      <text x="381" y="50" font-family="system-ui, sans-serif" font-size="8" fill="#94A3B8" text-anchor="middle">to secure loan</text>

      <!-- C5: Conditions -->
      <rect x="440" y="0" width="98" height="68" rx="6" fill="#0F172A" stroke="#334155" />
      <text x="489" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#A78BFA" text-anchor="middle">Conditions</text>
      <text x="489" y="36" font-family="system-ui, sans-serif" font-size="9" fill="#E2E8F0" text-anchor="middle">Market trends</text>
      <text x="489" y="50" font-family="system-ui, sans-serif" font-size="8" fill="#94A3B8" text-anchor="middle">&amp; inflation factors</text>
    </g>

    <!-- Credit Terms Breakdown Box -->
    <g transform="translate(16, 124)">
      <rect width="538" height="68" rx="6" fill="#0F172A" stroke="#475569" />
      <text x="14" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FBBF24">Understanding Standard Credit Terms (e.g. "2/10, net 30"):</text>
      <text x="14" y="42" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• <tspan fill="#34D399" font-weight="bold">2/10:</tspan> Buyer receives <tspan fill="#34D399" font-weight="bold">2% Cash Discount</tspan> if payment is settled within 10 days.</text>
      <text x="14" y="58" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• <tspan fill="#38BDF8" font-weight="bold">net 30:</tspan> Full invoice price is legally due within 30 days. Forgoing discount = <tspan fill="#F87171" font-weight="bold">37.2% APR Cost</tspan>.</text>
    </g>
  </g>

  <!-- Right Section: Balance Sheet Dichotomy (Debtors vs Creditors) -->
  <g transform="translate(626, 200)">
    <rect width="294" height="204" rx="10" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5" filter="url(#cr_shadow)" />
    <rect x="0" y="0" width="294" height="32" rx="10" fill="url(#cr_amber_grad)" />
    <text x="147" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">DEBTORS VS. CREDITORS</text>

    <!-- Debtors Card -->
    <g transform="translate(14, 44)">
      <rect width="266" height="68" rx="6" fill="#0F172A" stroke="#10B981" />
      <text x="12" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34D399">DEBTORS (Accounts Receivable)</text>
      <text x="12" y="38" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Customers who owe the business</text>
      <text x="12" y="54" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#34D399">Classification: CURRENT ASSET</text>
    </g>

    <!-- Creditors Card -->
    <g transform="translate(14, 122)">
      <rect width="266" height="68" rx="6" fill="#0F172A" stroke="#EF4444" />
      <text x="12" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#F87171">CREDITORS (Accounts Payable)</text>
      <text x="12" y="38" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• Suppliers the business owes cash to</text>
      <text x="12" y="54" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#F87171">Classification: CURRENT LIABILITY</text>
    </g>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(40, 418)">
    <rect width="880" height="82" rx="10" fill="#1E293B" stroke="#475569" stroke-width="1" />
    <text x="24" y="26" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#38BDF8">Strategic Trade Credit Rule for Kenyan Entrepreneurs:</text>
    <text x="24" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">Offering credit dramatically expands sales turnover, but unmonitored debtors destroy liquidity. Maintain an Aging Schedule (0-30, 31-60, 61-90+ days)</text>
    <text x="24" y="68" font-family="system-ui, sans-serif" font-size="11" fill="#94A3B8">and enforce credit limits strictly to keep bad debts below 2% of annual turnover.</text>
  </g>
</svg>"""


# =============================================================================
# LESSON 4: Payment Methods in Transactions
# =============================================================================
SVG_PAYMENT_METHODS_TAXONOMY_AND_TRADE_OFFS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="pm_bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="pm_cyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891B2" />
      <stop offset="100%" stop-color="#0E7490" />
    </linearGradient>
    <filter id="pm_shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.35" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="960" height="520" fill="url(#pm_bg)" rx="16" />

  <!-- Header -->
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="880" height="56" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1.5" />
    <text x="440" y="26" font-family="system-ui, sans-serif" font-size="18" font-weight="700" fill="#F8FAFC" text-anchor="middle">Payment Methods Taxonomy &amp; Strategic Selection Matrix</text>
    <text x="440" y="44" font-family="system-ui, sans-serif" font-size="12" fill="#94A3B8" text-anchor="middle">Comparing Settlement Speed, Transaction Risk, Cost Structures, and Legal Thresholds in Kenya</text>
  </g>

  <!-- 6 Major Payment Methods Grid (Middle Section) -->
  <g transform="translate(40, 88)">
    <!-- Method 1: Physical Cash -->
    <g transform="translate(0, 0)" filter="url(#pm_shadow)">
      <rect width="280" height="136" rx="8" fill="#1E293B" stroke="#FBBF24" stroke-width="1.5" />
      <rect x="0" y="0" width="280" height="28" rx="8" fill="#B45309" />
      <text x="140" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. PHYSICAL CASH (Notes &amp; Coins)</text>
      <text x="14" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#FBBF24">Speed:</tspan> Instantaneous (Seconds)</text>
      <text x="14" y="66" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#F87171">Risk:</tspan> HIGH (Theft, loss, robbery, counterfeit)</text>
      <text x="14" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#34D399">Cost:</tspan> Nil direct transaction fee</text>
      <text x="14" y="102" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#38BDF8">Scope:</tspan> Micro retail (&lt; KES 2,000)</text>
      <text x="14" y="122" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8">Ideal: Matatu fares, kiosk snacks, vegetable stalls.</text>
    </g>

    <!-- Method 2: Mobile Money (M-Pesa/Airtel) -->
    <g transform="translate(300, 0)" filter="url(#pm_shadow)">
      <rect width="280" height="136" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="1.5" />
      <rect x="0" y="0" width="280" height="28" rx="8" fill="#047857" />
      <text x="140" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. MOBILE MONEY (Till / Paybill)</text>
      <text x="14" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#34D399">Speed:</tspan> Instantaneous (Real-time 24/7)</text>
      <text x="14" y="66" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#FBBF24">Risk:</tspan> Medium (SIM swap, PIN fraud, wrong number)</text>
      <text x="14" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#38BDF8">Cost:</tspan> Tiered merchant tariff (0.5% - 1.5%)</text>
      <text x="14" y="102" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#38BDF8">Scope:</tspan> Up to KES 250,000 per tx</text>
      <text x="14" y="122" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8">Ideal: MSME sales, utility payments, grocery restock.</text>
    </g>

    <!-- Method 3: Commercial Cheque -->
    <g transform="translate(600, 0)" filter="url(#pm_shadow)">
      <rect width="280" height="136" rx="8" fill="#1E293B" stroke="#818CF8" stroke-width="1.5" />
      <rect x="0" y="0" width="280" height="28" rx="8" fill="#4338CA" />
      <text x="140" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. BANK CHEQUES (Crossed / Order)</text>
      <text x="14" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#F87171">Speed:</tspan> SLOW (2 - 3 business days clearing)</text>
      <text x="14" y="66" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#FBBF24">Risk:</tspan> Medium (Bounced cheques, signature forgery)</text>
      <text x="14" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#34D399">Cost:</tspan> Low (Cheque leaf fee KES 20 - 50)</text>
      <text x="14" y="102" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#38BDF8">Scope:</tspan> B2B up to &lt; KES 1,000,000</text>
      <text x="14" y="122" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8">Ideal: School fees, monthly rent, factory supplies.</text>
    </g>

    <!-- Method 4: EFT (Electronic Funds Transfer) -->
    <g transform="translate(0, 150)" filter="url(#pm_shadow)">
      <rect width="280" height="136" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5" />
      <rect x="0" y="0" width="280" height="28" rx="8" fill="#0369A1" />
      <text x="140" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4. EFT (Electronic Funds Transfer)</text>
      <text x="14" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#FBBF24">Speed:</tspan> Moderate (24 - 48 hours batch)</text>
      <text x="14" y="66" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#34D399">Risk:</tspan> VERY LOW (Bank automated files)</text>
      <text x="14" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#34D399">Cost:</tspan> Low flat batch fee (KES 50 - 150)</text>
      <text x="14" y="102" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#38BDF8">Scope:</tspan> Bulk payments &lt; KES 1M</text>
      <text x="14" y="122" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8">Ideal: Monthly staff salaries, routine vendor payments.</text>
    </g>

    <!-- Method 5: RTGS (Real Time Gross Settlement) -->
    <g transform="translate(300, 150)" filter="url(#pm_shadow)">
      <rect width="280" height="136" rx="8" fill="#1E293B" stroke="#A855F7" stroke-width="1.5" />
      <rect x="0" y="0" width="280" height="28" rx="8" fill="#6B21A8" />
      <text x="140" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">5. RTGS (Central Bank Settlement)</text>
      <text x="14" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#34D399">Speed:</tspan> Real-Time (Instant gross clearance)</text>
      <text x="14" y="66" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#34D399">Risk:</tspan> ZERO DEFAULT (CBK-backed, irreversible)</text>
      <text x="14" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#FBBF24">Cost:</tspan> Premium flat fee (KES 500 - 1,000)</text>
      <text x="14" y="102" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#A855F7">Scope:</tspan> MANDATORY for &#8805; KES 1,000,000</text>
      <text x="14" y="122" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8">Ideal: Land buying, heavy machinery import, tenders.</text>
    </g>

    <!-- Method 6: Debit / Credit Card POS -->
    <g transform="translate(600, 150)" filter="url(#pm_shadow)">
      <rect width="280" height="136" rx="8" fill="#1E293B" stroke="#EC4899" stroke-width="1.5" />
      <rect x="0" y="0" width="280" height="28" rx="8" fill="#9D174D" />
      <text x="140" y="19" font-family="system-ui, sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF" text-anchor="middle">6. DEBIT / CREDIT CARDS (POS)</text>
      <text x="14" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#34D399">Speed:</tspan> Instant authorization at terminal</text>
      <text x="14" y="66" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#FBBF24">Risk:</tspan> Low-Medium (Card skimming, chargebacks)</text>
      <text x="14" y="84" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#F87171">Cost:</tspan> 1.5% - 3.0% Merchant Discount Rate</text>
      <text x="14" y="102" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0"><tspan font-weight="bold" fill="#38BDF8">Scope:</tspan> Retail &amp; hospitality POS checkout</text>
      <text x="14" y="122" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8">Ideal: Supermarkets, tourist lodges, online stores.</text>
    </g>
  </g>

  <!-- Bottom Regulatory Guideline Strip -->
  <g transform="translate(40, 396)">
    <rect width="880" height="104" rx="10" fill="#1E293B" stroke="#475569" stroke-width="1" />
    <text x="24" y="26" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#38BDF8">Central Bank of Kenya (CBK) Strategic Payment Decision Rule:</text>
    <text x="24" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• For <tspan fill="#FBBF24" font-weight="bold">Micro / Retail (&lt; KES 10,000):</tspan> Use Mobile Money (Lipa Na M-Pesa) or physical cash for rapid customer checkout.</text>
    <text x="24" y="68" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• For <tspan fill="#34D399" font-weight="bold">Payroll / B2B Batches (&lt; KES 1M):</tspan> Use EFT batch processing or crossed Cheques to minimize per-transaction charges.</text>
    <text x="24" y="88" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">• For <tspan fill="#A855F7" font-weight="bold">Large Capital Outlays (&#8805; KES 1M):</tspan> CBK rules mandate RTGS settlement for total clearing security and real-time legal finality.</text>
  </g>
</svg>"""


# =============================================================================
# LESSON 5: Practical Project: Managing Business Payments
# =============================================================================
SVG_ENTERPRISE_PAYMENT_POLICY_ARCHITECTURE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <linearGradient id="pol_bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="50%" stop-color="#1E293B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="pol_header" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB" />
      <stop offset="100%" stop-color="#1D4ED8" />
    </linearGradient>
    <filter id="pol_shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.35" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="960" height="520" fill="url(#pol_bg)" rx="16" />

  <!-- Header -->
  <g transform="translate(40, 20)">
    <rect x="0" y="0" width="880" height="56" rx="10" fill="#1E293B" stroke="#334155" stroke-width="1.5" />
    <text x="440" y="26" font-family="system-ui, sans-serif" font-size="18" font-weight="700" fill="#F8FAFC" text-anchor="middle">Enterprise Payment Policy &amp; Petty Cash Imprest Architecture</text>
    <text x="440" y="44" font-family="system-ui, sans-serif" font-size="12" fill="#94A3B8" text-anchor="middle">3-Tier Payment Policy Design, Inflow/Outflow Controls, and Imprest Cash Reconciliation</text>
  </g>

  <!-- Left: 3-Tier Policy Framework -->
  <g transform="translate(40, 88)" filter="url(#pol_shadow)">
    <rect width="424" height="300" rx="10" fill="#1E293B" stroke="#2563EB" stroke-width="1.5" />
    <rect x="0" y="0" width="424" height="32" rx="10" fill="url(#pol_header)" />
    <text x="212" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">BARAKA BAKERY PAYMENT POLICY FRAMEWORK</text>

    <!-- Tier 1: Customer Inflows -->
    <g transform="translate(16, 44)">
      <rect width="392" height="66" rx="6" fill="#0F172A" stroke="#10B981" />
      <text x="12" y="18" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34D399">Tier 1: Customer Sales Inflows (Revenue)</text>
      <text x="12" y="36" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• <tspan fill="#38BDF8" font-weight="bold">Primary Channel:</tspan> Lipa Na M-Pesa Buy Goods Till (Instant record)</text>
      <text x="12" y="52" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• <tspan fill="#FBBF24" font-weight="bold">Cash Limit:</tspan> Coins accepted only for purchases &lt; KES 100</text>
    </g>

    <!-- Tier 2: Supplier Outflows -->
    <g transform="translate(16, 120)">
      <rect width="392" height="66" rx="6" fill="#0F172A" stroke="#38BDF8" />
      <text x="12" y="18" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Tier 2: Wholesale Procurement Outflows (&#8805; KES 5,000)</text>
      <text x="12" y="36" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• <tspan fill="#38BDF8" font-weight="bold">Primary Channel:</tspan> Bank EFT / Crossed Cheque (Full audit trail)</text>
      <text x="12" y="52" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• <tspan fill="#F87171" font-weight="bold">Rule:</tspan> Two authorized signatures required (Manager + Treasurer)</text>
    </g>

    <!-- Tier 3: Casual & Daily Expenses -->
    <g transform="translate(16, 196)">
      <rect width="392" height="66" rx="6" fill="#0F172A" stroke="#F59E0B" />
      <text x="12" y="18" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FBBF24">Tier 3: Petty Expenses &amp; Casual Wages (&lt; KES 5,000)</text>
      <text x="12" y="36" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• <tspan fill="#34D399" font-weight="bold">Casual Labour:</tspan> Paid via B2C Mobile Money with signed voucher</text>
      <text x="12" y="52" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">• <tspan fill="#FBBF24" font-weight="bold">Incidental Repairs:</tspan> Settled from Imprest Petty Cash fund</text>
    </g>

    <text x="212" y="286" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#38BDF8" text-anchor="middle">Internal Control: Segregation of Cash Handling vs. Accounting Ledger</text>
  </g>

  <!-- Right: Imprest Petty Cash System Loop -->
  <g transform="translate(488, 88)" filter="url(#pol_shadow)">
    <rect width="432" height="300" rx="10" fill="#1E293B" stroke="#10B981" stroke-width="1.5" />
    <rect x="0" y="0" width="432" height="32" rx="10" fill="#047857" />
    <text x="216" y="21" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">THE IMPREST PETTY CASH RECONCILIATION CYCLE</text>

    <!-- Circular Step 1: Fixed Float -->
    <g transform="translate(20, 48)">
      <rect x="0" y="0" width="180" height="74" rx="8" fill="#0F172A" stroke="#10B981" />
      <circle cx="24" cy="24" r="12" fill="#047857" />
      <text x="24" y="28" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1</text>
      <text x="44" y="28" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#34D399">Fixed Float Setup</text>
      <text x="12" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">Establish float (e.g. KES 5,000)</text>
      <text x="12" y="62" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8">in locked petty cash box.</text>
    </g>

    <!-- Arrow Top -->
    <path d="M 206 85 L 226 85" stroke="#34D399" stroke-width="2" />

    <!-- Circular Step 2: Voucher Expense -->
    <g transform="translate(232, 48)">
      <rect x="0" y="0" width="180" height="74" rx="8" fill="#0F172A" stroke="#FBBF24" />
      <circle cx="24" cy="24" r="12" fill="#B45309" />
      <text x="24" y="28" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2</text>
      <text x="44" y="28" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#FBBF24">Voucher Payments</text>
      <text x="12" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">Pay micro-expenses and</text>
      <text x="12" y="62" font-family="system-ui, sans-serif" font-size="9" fill="#94A3B8">retain signed receipts.</text>
    </g>

    <!-- Circular Step 3: Cash Count Audit -->
    <g transform="translate(232, 140)">
      <rect x="0" y="0" width="180" height="74" rx="8" fill="#0F172A" stroke="#38BDF8" />
      <circle cx="24" cy="24" r="12" fill="#0369A1" />
      <text x="24" y="28" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3</text>
      <text x="44" y="28" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#38BDF8">Physical Audit</text>
      <text x="12" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">Cash Count + Vouchers</text>
      <text x="12" y="62" font-family="system-ui, sans-serif" font-size="9" fill="#34D399">= Exactly KES 5,000 Float</text>
    </g>

    <!-- Arrow Down -->
    <path d="M 322 124 L 322 138" stroke="#34D399" stroke-width="2" />

    <!-- Circular Step 4: Reimbursement -->
    <g transform="translate(20, 140)">
      <rect x="0" y="0" width="180" height="74" rx="8" fill="#0F172A" stroke="#A855F7" />
      <circle cx="24" cy="24" r="12" fill="#6B21A8" />
      <text x="24" y="28" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4</text>
      <text x="44" y="28" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#A855F7">Reimbursement</text>
      <text x="12" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0">Cheque drawn for sum of</text>
      <text x="12" y="62" font-family="system-ui, sans-serif" font-size="9" fill="#A855F7">vouchers -> Restores Float</text>
    </g>

    <!-- Arrow Left -->
    <path d="M 230 177 L 206 177" stroke="#34D399" stroke-width="2" />
    <!-- Arrow Up -->
    <path d="M 110 138 L 110 124" stroke="#34D399" stroke-width="2" />

    <!-- Summary Box -->
    <rect x="20" y="228" width="392" height="56" rx="6" fill="#0F172A" stroke="#475569" />
    <text x="216" y="248" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#34D399" text-anchor="middle">Golden Imprest Rule:</text>
    <text x="216" y="266" font-family="system-ui, sans-serif" font-size="10" fill="#E2E8F0" text-anchor="middle">Reimbursement Cheque = Sum of Vouchers = Float - Cash on Hand</text>
  </g>

  <!-- Bottom Synthesis Banner -->
  <g transform="translate(40, 402)">
    <rect width="880" height="98" rx="10" fill="#1E293B" stroke="#475569" stroke-width="1" />
    <text x="24" y="26" font-family="system-ui, sans-serif" font-size="13" font-weight="700" fill="#38BDF8">Enterprise Risk Management Takeaway:</text>
    <text x="24" y="48" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">A robust payment policy protects the business from three fatal vulnerabilities: (1) Cashier shrinkage and theft of daily counter proceeds,</text>
    <text x="24" y="68" font-family="system-ui, sans-serif" font-size="11" fill="#E2E8F0">(2) Double-payments or unauthorized procurement from ghost suppliers, and (3) Excessive transaction fee erosion on micro-revenue streams.</text>
  </g>
</svg>"""
