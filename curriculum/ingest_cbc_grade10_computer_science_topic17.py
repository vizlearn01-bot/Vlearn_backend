"""
VLearn CBC Grade 10 Computer Science — Topic 17: Functions
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (Level: 10)
Subject: Computer Science
Topic: Functions (Topic Order: 17)

Deconstructed into 5 Comprehensive Learning Units & 5 Published Lessons:
  Unit 1: Modular Programming, Decomposition, & Function Anatomy (Lessons 92 & 93)
  Unit 2: Parameters, Arguments, & Return Values (Lessons 94, 95 & 96)
  Unit 3: Scope, Variable Lifetimes, & Call Stack Tracing (Lessons 97 & 98)
  Unit 4: Abstraction, Standard Libraries, Mutable Containers, & Recursion (Lessons 99, 101 & 102)
  Unit 5: Defensive Programming, Refactoring Workshop, & Grand Project Integration (Lessons 100, 103 & 104)
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

def clean_text(text: str) -> str:
    """Removes bracket citations and normalizes unicode bullets into standard markdown list items."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    text = re.sub(r'^([^\n\-\*\d\>#][^\n]*)\n(- |\* )', r'\1\n\n\2', text, flags=re.MULTILINE)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

def sanitize_svg(svg: str) -> str:
    svg = re.sub(r'<\?xml.*?\?>', '', svg)
    svg = re.sub(r'<!DOCTYPE.*?>', '', svg)
    return svg.strip()

# =====================================================================
# HIGH PRECISION VECTOR SVGS FOR TOPIC 17 (DARK THEME 960x520)
# =====================================================================

SVG_MODULAR_DECOMPOSITION = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Modular Programming &amp; Functional Decomposition Architecture</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Contrasting Monolithic Spaghetti Code with a Hierarchically Decomposed Modular System</text>

  <!-- Left: Monolithic Code (Spaghetti) -->
  <g transform="translate(45, 95)">
    <rect width="380" height="385" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="380" height="30" rx="8" fill="#dc2626"/>
    <text x="190" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">&#9888; Monolithic Flat Script (1000+ Lines)</text>

    <!-- Code Mockup with tangled lines -->
    <g transform="translate(20, 45)">
      <rect width="340" height="230" rx="6" fill="#1e1b4b" stroke="#475569"/>
      <text x="15" y="22" font-family="monospace" font-size="9.5" fill="#f87171"># 1 continuous 1000-line script</text>
      <text x="15" y="38" font-family="monospace" font-size="9.5" fill="#94a3b8">line 12: user_id = input()</text>
      <text x="15" y="54" font-family="monospace" font-size="9.5" fill="#94a3b8">line 45: if user_id == "admin":</text>
      <text x="15" y="70" font-family="monospace" font-size="9.5" fill="#fca5a5">line 120: tax = price * 0.16  &lt;-- Duplicate 1</text>
      <text x="15" y="86" font-family="monospace" font-size="9.5" fill="#94a3b8">line 340: for item in cart:</text>
      <text x="15" y="102" font-family="monospace" font-size="9.5" fill="#fca5a5">line 512: tax = price * 0.16  &lt;-- Duplicate 2</text>
      <text x="15" y="118" font-family="monospace" font-size="9.5" fill="#94a3b8">line 680: print_invoice()</text>
      <text x="15" y="134" font-family="monospace" font-size="9.5" fill="#fca5a5">line 850: tax = price * 0.18  &lt;-- INCONSISTENT BUG!</text>
      <text x="15" y="150" font-family="monospace" font-size="9.5" fill="#94a3b8">line 999: exit()</text>

      <!-- Tangled jump lines -->
      <path d="M 300 70 C 330 70, 330 134, 300 134" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
      <path d="M 280 102 C 340 102, 340 38, 260 38" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,3"/>
    </g>

    <!-- Disadvantages Callout -->
    <g transform="translate(20, 290)">
      <rect width="340" height="75" rx="6" fill="#1e293b" stroke="#b91c1c"/>
      <text x="15" y="18" font-size="10" font-weight="bold" fill="#f87171">&#10007; Critical Flaws of Monolithic Architecture:</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">&#8226; Massive code duplication across multiple pages.</text>
      <text x="15" y="48" font-size="8.5" fill="#cbd5e1">&#8226; Bug on line 12 cascades unpredictably to line 850.</text>
      <text x="15" y="62" font-size="8.5" fill="#cbd5e1">&#8226; Impossible for teams of programmers to collaborate.</text>
    </g>
  </g>

  <!-- Right: Decomposed Modular Tree -->
  <g transform="translate(470, 95)">
    <rect width="445" height="385" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="445" height="30" rx="8" fill="#059669"/>
    <text x="222" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">&#10003; Modular Functional Decomposition Tree</text>

    <!-- Level 1: Main Controller -->
    <g transform="translate(142, 45)">
      <rect width="160" height="38" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="80" y="24" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Main Program Loop</text>
    </g>

    <!-- Connector Lines Level 1 to 2 -->
    <path d="M 222 83 L 75 125" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 222 83 L 222 125" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <path d="M 222 83 L 370 125" fill="none" stroke="#38bdf8" stroke-width="2"/>

    <!-- Level 2: Sub-modules -->
    <!-- Module A -->
    <g transform="translate(15, 125)">
      <rect width="120" height="50" rx="6" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.5"/>
      <text x="60" y="20" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">User Auth</text>
      <text x="60" y="36" font-family="monospace" font-size="8.5" fill="#cbd5e1" text-anchor="middle">login_user()</text>
    </g>

    <!-- Module B -->
    <g transform="translate(162, 125)">
      <rect width="120" height="50" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
      <text x="60" y="20" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Transactions</text>
      <text x="60" y="36" font-family="monospace" font-size="8.5" fill="#cbd5e1" text-anchor="middle">process_cart()</text>
    </g>

    <!-- Module C -->
    <g transform="translate(310, 125)">
      <rect width="120" height="50" rx="6" fill="#1e293b" stroke="#ec4899" stroke-width="1.5"/>
      <text x="60" y="20" font-size="9.5" font-weight="bold" fill="#f472b6" text-anchor="middle">Reporting</text>
      <text x="60" y="36" font-family="monospace" font-size="8.5" fill="#cbd5e1" text-anchor="middle">send_invoice()</text>
    </g>

    <!-- Connector Lines Level 2 to 3 (under Module B) -->
    <path d="M 222 175 L 140 215" fill="none" stroke="#fbbf24" stroke-width="1.5"/>
    <path d="M 222 175 L 305 215" fill="none" stroke="#fbbf24" stroke-width="1.5"/>

    <!-- Level 3: Sub-submodules -->
    <g transform="translate(75, 215)">
      <rect width="130" height="48" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-width="1.2"/>
      <text x="65" y="18" font-size="9" font-weight="bold" fill="#c084fc" text-anchor="middle">Tax Module</text>
      <text x="65" y="34" font-family="monospace" font-size="8" fill="#e9d5ff" text-anchor="middle">calc_tax(rate=0.16)</text>
    </g>

    <g transform="translate(240, 215)">
      <rect width="130" height="48" rx="6" fill="#1e1b4b" stroke="#a855f7" stroke-width="1.2"/>
      <text x="65" y="18" font-size="9" font-weight="bold" fill="#c084fc" text-anchor="middle">Currency Converter</text>
      <text x="65" y="34" font-family="monospace" font-size="8" fill="#e9d5ff" text-anchor="middle">usd_to_kes(rate)</text>
    </g>

    <!-- Advantages Callout -->
    <g transform="translate(20, 290)">
      <rect width="405" height="75" rx="6" fill="#1e293b" stroke="#059669"/>
      <text x="15" y="18" font-size="10" font-weight="bold" fill="#34d399">&#10003; Engineering Advantages:</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">&#8226; Write once, invoke 50+ times without duplication.</text>
      <text x="15" y="48" font-size="8.5" fill="#cbd5e1">&#8226; Isolated unit testing: debug calc_tax() without breaking billing.</text>
      <text x="15" y="62" font-size="8.5" fill="#cbd5e1">&#8226; Parallel team development with contract interfaces.</text>
    </g>
  </g>
</svg>
""")

SVG_FUNCTION_ANATOMY = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Anatomy of a Function Definition &amp; Call Mechanics</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Dissecting Keywords, Identifiers, Parameters, Type Hints, Docstrings, and Return Statements</text>

  <!-- Top Code Banner Breakdown -->
  <g transform="translate(45, 90)">
    <rect width="870" height="75" rx="10" fill="#000000" stroke="#38bdf8" stroke-width="2"/>
    <text x="25" y="45" font-family="monospace" font-size="16">
      <tspan fill="#f43f5e" font-weight="bold">def </tspan>
      <tspan fill="#38bdf8" font-weight="bold">calculate_tax</tspan>
      <tspan fill="#cbd5e1">(</tspan>
      <tspan fill="#fbbf24">subtotal</tspan>
      <tspan fill="#94a3b8">: float, </tspan>
      <tspan fill="#34d399">tax_rate</tspan>
      <tspan fill="#94a3b8">: float = </tspan>
      <tspan fill="#a78bfa">0.16</tspan>
      <tspan fill="#cbd5e1">) -&gt; </tspan>
      <tspan fill="#38bdf8">float</tspan>
      <tspan fill="#cbd5e1">:</tspan>
    </text>
  </g>

  <!-- Explanatory Pointers (6 Cards) -->
  <g transform="translate(45, 185)">
    <!-- Card 1: def keyword -->
    <g transform="translate(0, 0)">
      <rect width="270" height="135" rx="8" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
      <rect width="270" height="26" rx="6" fill="#be123c"/>
      <text x="135" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. 'def' Keyword</text>
      <text x="12" y="46" font-size="9.5" font-weight="bold" fill="#fda4af">&#8226; Compiler Signal:</text>
      <text x="12" y="62" font-size="8.5" fill="#cbd5e1">Short for 'define'. Tells interpreter that a</text>
      <text x="12" y="76" font-size="8.5" fill="#cbd5e1">reusable callable subroutine is being created.</text>
      <rect x="12" y="88" width="246" height="34" rx="4" fill="#1e293b"/>
      <text x="135" y="108" font-size="8.5" fill="#fda4af" text-anchor="middle">Pre-allocated Python keyword token</text>
    </g>

    <!-- Card 2: Identifier Name -->
    <g transform="translate(300, 0)">
      <rect width="270" height="135" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
      <rect width="270" height="26" rx="6" fill="#0284c7"/>
      <text x="135" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Identifier Name</text>
      <text x="12" y="46" font-size="9.5" font-weight="bold" fill="#38bdf8">&#8226; Function Identifier:</text>
      <text x="12" y="62" font-size="8.5" fill="#cbd5e1">Follows snake_case naming conventions.</text>
      <text x="12" y="76" font-size="8.5" fill="#cbd5e1">Describes the action (verb + noun).</text>
      <rect x="12" y="88" width="246" height="34" rx="4" fill="#1e293b"/>
      <text x="135" y="108" font-size="8.5" fill="#7dd3fc" text-anchor="middle">Stored in symbol table as callable pointer</text>
    </g>

    <!-- Card 3: Parameter List -->
    <g transform="translate(600, 0)">
      <rect width="270" height="135" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
      <rect width="270" height="26" rx="6" fill="#d97706"/>
      <text x="135" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Parameters &amp; Defaults</text>
      <text x="12" y="46" font-size="9.5" font-weight="bold" fill="#fbbf24">&#8226; Input Placeholders:</text>
      <text x="12" y="62" font-size="8.5" fill="#cbd5e1">subtotal is required positional input.</text>
      <text x="12" y="76" font-size="8.5" fill="#cbd5e1">tax_rate=0.16 is optional default value.</text>
      <rect x="12" y="88" width="246" height="34" rx="4" fill="#1e293b"/>
      <text x="135" y="108" font-size="8.5" fill="#fde68a" text-anchor="middle">Defaults MUST come after required params</text>
    </g>

    <!-- Row 2 -->
    <!-- Card 4: Type Hints & Colon -->
    <g transform="translate(0, 150)">
      <rect width="270" height="145" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="1.5"/>
      <rect width="270" height="26" rx="6" fill="#7e22ce"/>
      <text x="135" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Type Hints &amp; Colon</text>
      <text x="12" y="46" font-size="9.5" font-weight="bold" fill="#c084fc">&#8226; Structural Contract:</text>
      <text x="12" y="62" font-size="8.5" fill="#cbd5e1">-&gt; float specifies expected return type.</text>
      <text x="12" y="76" font-size="8.5" fill="#cbd5e1">Colon (:) initiates the indented body block.</text>
      <rect x="12" y="94" width="246" height="36" rx="4" fill="#1e293b"/>
      <text x="135" y="116" font-size="8.5" fill="#e9d5ff" text-anchor="middle">Omitting colon causes SyntaxError</text>
    </g>

    <!-- Card 5: Function Body & Docstring -->
    <g transform="translate(300, 150)">
      <rect width="270" height="145" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
      <rect width="270" height="26" rx="6" fill="#047857"/>
      <text x="135" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Indented Body &amp; Docstring</text>
      <text x="12" y="46" font-size="9.5" font-weight="bold" fill="#34d399">&#8226; Execution Statements:</text>
      <text x="12" y="62" font-size="8.5" fill="#cbd5e1">Must be consistently indented (4 spaces).</text>
      <text x="12" y="76" font-size="8.5" fill="#cbd5e1">&quot;&quot;&quot;Docstrings&quot;&quot;&quot; provide internal API docs.</text>
      <rect x="12" y="94" width="246" height="36" rx="4" fill="#1e293b"/>
      <text x="135" y="116" font-size="8.5" fill="#a7f3d0" text-anchor="middle">Accessible via help(calculate_tax)</text>
    </g>

    <!-- Card 6: Return Statement -->
    <g transform="translate(600, 150)">
      <rect width="270" height="145" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
      <rect width="270" height="26" rx="6" fill="#0369a1"/>
      <text x="135" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">6. Return Statement</text>
      <text x="12" y="46" font-size="9.5" font-weight="bold" fill="#38bdf8">&#8226; Terminate &amp; Dispatch:</text>
      <text x="12" y="62" font-size="8.5" fill="#cbd5e1">Sends computed value back to caller.</text>
      <text x="12" y="76" font-size="8.5" fill="#cbd5e1">Immediately halts function execution.</text>
      <rect x="12" y="94" width="246" height="36" rx="4" fill="#1e293b"/>
      <text x="135" y="116" font-size="8.5" fill="#bae6fd" text-anchor="middle">Omission causes implicit return None</text>
    </g>
  </g>
</svg>
""")

SVG_CALL_STACK_LIFECYCLE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Call Stack Lifecycle &amp; Activation Frame Management</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">How the CPU pushes stack frames on invocation and pops memory registers upon return</text>

  <!-- 3 Beakers representing Call Stack States -->
  
  <!-- State 1: Initial Push -->
  <g transform="translate(45, 90)">
    <rect width="265" height="385" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="265" height="28" rx="8" fill="#0284c7"/>
    <text x="132" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">State 1: Step 3 (accumulate Called)</text>

    <!-- Stack Container -->
    <g transform="translate(18, 45)">
      <rect width="230" height="250" rx="6" fill="#1e293b" stroke="#334155" stroke-width="2"/>
      
      <!-- Top Frame -->
      <g transform="translate(10, 110)">
        <rect width="210" height="60" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="105" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Frame: accumulate()</text>
        <text x="105" y="35" font-family="monospace" font-size="8.5" fill="#bae6fd" text-anchor="middle">base_val = 5, factor = 3</text>
        <text x="105" y="50" font-family="monospace" font-size="8.5" fill="#fde68a" text-anchor="middle">step1 = ? [PENDING]</text>
      </g>

      <!-- Bottom Frame -->
      <g transform="translate(10, 180)">
        <rect width="210" height="55" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
        <text x="105" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Frame: __main__</text>
        <text x="105" y="35" font-family="monospace" font-size="8.5" fill="#c7d2fe" text-anchor="middle">start_num = 5</text>
        <text x="105" y="48" font-family="monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">final_score = ? [WAITING]</text>
      </g>
    </g>

    <g transform="translate(18, 310)">
      <text x="115" y="15" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">&#8595; Push accumulate frame</text>
      <text x="115" y="32" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Paused main; branch to func</text>
    </g>
  </g>

  <!-- State 2: Nested Push -->
  <g transform="translate(345, 90)">
    <rect width="265" height="385" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
    <rect width="265" height="28" rx="8" fill="#d97706"/>
    <text x="132" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">State 2: Step 5 (double_value Peak)</text>

    <!-- Stack Container -->
    <g transform="translate(18, 45)">
      <rect width="230" height="250" rx="6" fill="#1e293b" stroke="#334155" stroke-width="2"/>
      
      <!-- Top Frame (Active) -->
      <g transform="translate(10, 40)">
        <rect width="210" height="60" rx="6" fill="#b45309" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="105" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">&#9654; Frame: double_value() [ACTIVE]</text>
        <text x="105" y="35" font-family="monospace" font-size="8.5" fill="#fde68a" text-anchor="middle">x = 5, result = 10</text>
        <text x="105" y="50" font-size="8" font-weight="bold" fill="#a7f3d0" text-anchor="middle">&#10003; Return 10 to caller</text>
      </g>

      <!-- Middle Frame -->
      <g transform="translate(10, 110)">
        <rect width="210" height="60" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="105" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Frame: accumulate() [PAUSED]</text>
        <text x="105" y="35" font-family="monospace" font-size="8.5" fill="#bae6fd" text-anchor="middle">base_val = 5, factor = 3</text>
        <text x="105" y="48" font-size="8" fill="#94a3b8" text-anchor="middle">Waiting for return at line 6</text>
      </g>

      <!-- Bottom Frame -->
      <g transform="translate(10, 180)">
        <rect width="210" height="55" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
        <text x="105" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Frame: __main__</text>
        <text x="105" y="35" font-family="monospace" font-size="8.5" fill="#c7d2fe" text-anchor="middle">start_num = 5</text>
      </g>
    </g>

    <g transform="translate(18, 310)">
      <text x="115" y="15" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">&#9650; Stack Depth = 3 Frames</text>
      <text x="115" y="32" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Peak memory allocation</text>
    </g>
  </g>

  <!-- State 3: Popped & Resolved -->
  <g transform="translate(645, 90)">
    <rect width="265" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="265" height="28" rx="8" fill="#059669"/>
    <text x="132" y="19" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">State 3: Step 9 (Popped &amp; Resumed)</text>

    <!-- Stack Container -->
    <g transform="translate(18, 45)">
      <rect width="230" height="250" rx="6" fill="#1e293b" stroke="#334155" stroke-width="2"/>
      
      <!-- Evaporating Vapor Line -->
      <g transform="translate(10, 30)">
        <rect width="210" height="30" rx="4" fill="none" stroke="#ef4444" stroke-dasharray="4,4"/>
        <text x="105" y="20" font-size="8.5" fill="#f87171" text-anchor="middle">&#128168; double_value() Frame POPPED/FREED</text>
      </g>

      <!-- Resumed Top Frame -->
      <g transform="translate(10, 110)">
        <rect width="210" height="60" rx="6" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
        <text x="105" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">&#9654; Frame: accumulate() [RESUMED]</text>
        <text x="105" y="34" font-family="monospace" font-size="8.5" fill="#a7f3d0" text-anchor="middle">step1 = 10 (from double_value)</text>
        <text x="105" y="48" font-family="monospace" font-size="8.5" fill="#6ee7b7" text-anchor="middle">total = 10 + 3 = 13 &#8594; RETURN</text>
      </g>

      <!-- Bottom Frame -->
      <g transform="translate(10, 180)">
        <rect width="210" height="55" rx="6" fill="#1e1b4b" stroke="#6366f1" stroke-width="1.5"/>
        <text x="105" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Frame: __main__</text>
        <text x="105" y="35" font-family="monospace" font-size="8.5" fill="#c7d2fe" text-anchor="middle">Receives 13 into final_score</text>
      </g>
    </g>

    <g transform="translate(18, 310)">
      <text x="115" y="15" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">&#10003; Stack Unwinding Completed</text>
      <text x="115" y="32" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Local registers freed from RAM</text>
    </g>
  </g>
</svg>
""")

SVG_MUTABILITY_PASSING = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Memory Semantics: Pass-By-Value vs. Pass-By-Reference</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Physics of Immutable Value Clones vs. Mutable Shared Memory Pointers</text>

  <!-- Left: Pass By Value (Immutable) -->
  <g transform="translate(45, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#0284c7"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Case A: Immutable Primitives (Integers, Floats, Strings)</text>

    <!-- Visual Memory Cells -->
    <g transform="translate(20, 45)">
      <!-- Caller Memory -->
      <rect width="170" height="90" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="85" y="22" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">Caller Scope (__main__)</text>
      <text x="85" y="45" font-family="monospace" font-size="10" fill="#ffffff" text-anchor="middle">score = 100</text>
      <text x="85" y="70" font-family="monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">Address: 0x7FFF01</text>

      <!-- Arrow: Clone / Copy -->
      <g transform="translate(180, 35)">
        <line x1="0" y1="10" x2="30" y2="10" stroke="#38bdf8" stroke-width="2"/>
        <polygon points="30,6 38,10 30,14" fill="#38bdf8"/>
        <text x="20" y="28" font-size="8" fill="#7dd3fc" text-anchor="middle">COPY</text>
      </g>

      <!-- Function Local Memory -->
      <g transform="translate(225, 0)">
        <rect width="155" height="90" rx="6" fill="#1e293b" stroke="#fbbf24"/>
        <text x="77" y="22" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Function Local Scope</text>
        <text x="77" y="45" font-family="monospace" font-size="10" fill="#fde68a" text-anchor="middle">number = 200</text>
        <text x="77" y="70" font-family="monospace" font-size="8.5" fill="#94a3b8" text-anchor="middle">Address: 0x7FFF88</text>
      </g>
    </g>

    <!-- Code & Outcome -->
    <g transform="translate(20, 150)">
      <rect width="380" height="120" rx="6" fill="#000000" stroke="#334155"/>
      <text x="15" y="22" font-family="monospace" font-size="9" fill="#38bdf8">def double_integer(number):</text>
      <text x="35" y="38" font-family="monospace" font-size="9" fill="#cbd5e1">number = number * 2   # Modifies local copy</text>
      <text x="15" y="58" font-family="monospace" font-size="9" fill="#38bdf8">score = 100</text>
      <text x="15" y="74" font-family="monospace" font-size="9" fill="#cbd5e1">double_integer(score)</text>
      <text x="15" y="92" font-family="monospace" font-size="9" fill="#34d399">print(score)  # Output: 100 (UNCHANGED!)</text>
    </g>

    <g transform="translate(20, 285)">
      <rect width="380" height="80" rx="6" fill="#1e293b" stroke="#0ea5e9"/>
      <text x="15" y="18" font-size="9.5" font-weight="bold" fill="#38bdf8">&#128737; Shielded External State:</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">Primitive types pass by value. The function receives an isolated</text>
      <text x="15" y="48" font-size="8.5" fill="#cbd5e1">clone at a new RAM memory register. Changes cannot affect</text>
      <text x="15" y="62" font-size="8.5" fill="#cbd5e1">the caller's original variable.</text>
    </g>
  </g>

  <!-- Right: Pass By Reference (Mutable List) -->
  <g transform="translate(495, 95)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="420" height="30" rx="8" fill="#059669"/>
    <text x="210" y="20" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Case B: Mutable Collections (Lists, Dictionaries)</text>

    <!-- Visual Shared Pointer -->
    <g transform="translate(20, 45)">
      <!-- Variable A -->
      <rect width="115" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="57" y="20" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">my_grades</text>
      <text x="57" y="36" font-family="monospace" font-size="8" fill="#94a3b8" text-anchor="middle">ptr: 0x9A40</text>

      <!-- Variable B -->
      <g transform="translate(0, 55)">
        <rect width="115" height="50" rx="6" fill="#1e293b" stroke="#fbbf24"/>
        <text x="57" y="20" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">grades_list</text>
        <text x="57" y="36" font-family="monospace" font-size="8" fill="#94a3b8" text-anchor="middle">ptr: 0x9A40</text>
      </g>

      <!-- Arrows pointing to shared heap container -->
      <path d="M 120 25 L 180 50" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <polygon points="180,46 188,52 179,56" fill="#38bdf8"/>
      <path d="M 120 80 L 180 55" fill="none" stroke="#fbbf24" stroke-width="2"/>
      <polygon points="179,51 188,55 180,61" fill="#fbbf24"/>

      <!-- Shared Heap Memory Container -->
      <g transform="translate(195, 10)">
        <rect width="185" height="85" rx="6" fill="#1e1b4b" stroke="#34d399" stroke-width="1.5"/>
        <text x="92" y="20" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">Shared Heap Object [0x9A40]</text>
        <rect x="10" y="30" width="165" height="28" rx="4" fill="#0f172a"/>
        <text x="92" y="48" font-family="monospace" font-size="9" fill="#ffffff" text-anchor="middle">[82, 90, 78, <tspan fill="#f43f5e" font-weight="bold">95</tspan>]</text>
        <text x="92" y="72" font-size="8" fill="#a7f3d0" text-anchor="middle">&#9888; .append(95) alters RAM in-place!</text>
      </g>
    </g>

    <!-- Code & Outcome -->
    <g transform="translate(20, 160)">
      <rect width="380" height="110" rx="6" fill="#000000" stroke="#334155"/>
      <text x="15" y="20" font-family="monospace" font-size="9" fill="#38bdf8">def add_grade(grades_list, new_grade):</text>
      <text x="35" y="36" font-family="monospace" font-size="9" fill="#cbd5e1">grades_list.append(new_grade)  # Mutates object</text>
      <text x="15" y="56" font-family="monospace" font-size="9" fill="#38bdf8">my_grades = [82, 90, 78]</text>
      <text x="15" y="72" font-family="monospace" font-size="9" fill="#cbd5e1">add_grade(my_grades, 95)</text>
      <text x="15" y="90" font-family="monospace" font-size="9" fill="#f87171">print(my_grades)  # Output: [82, 90, 78, 95] (ALTERED!)</text>
    </g>

    <g transform="translate(20, 285)">
      <rect width="380" height="80" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="15" y="18" font-size="9.5" font-weight="bold" fill="#34d399">&#9888; Direct Side-Effect Risk:</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">Collections pass by object reference. Both caller and function</text>
      <text x="15" y="48" font-size="8.5" fill="#cbd5e1">share the same memory address. Mutating the parameter</text>
      <text x="15" y="62" font-size="8.5" fill="#cbd5e1">permanently alters the caller's data in RAM.</text>
    </g>
  </g>
</svg>
""")

SVG_RECURSION_DECOMPOSITION = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Recursive Decomposition &amp; Call Stack Unwinding: Factorial(4)</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Visualizing the Two Phases of Recursion: Downward Expansion (Push) and Upward Resolution (Pop)</text>

  <!-- Left Column: Expansion Phase -->
  <g transform="translate(45, 90)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#0284c7"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Phase 1: Downward Stack Expansion (Pushing)</text>

    <!-- Step 1 -->
    <g transform="translate(15, 38)">
      <rect width="390" height="45" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <circle cx="22" cy="22" r="12" fill="#0284c7"/>
      <text x="22" y="26" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1</text>
      <text x="45" y="18" font-family="monospace" font-size="10" fill="#38bdf8">factorial(4)</text>
      <text x="45" y="34" font-size="9" fill="#cbd5e1">Needs <tspan font-family="monospace" fill="#fde68a">4 * factorial(3)</tspan> &#8594; Suspends &amp; calls factorial(3)</text>
    </g>

    <!-- Down arrow -->
    <path d="M 210 88 L 210 98" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="206,98 210,104 214,98" fill="#38bdf8"/>

    <!-- Step 2 -->
    <g transform="translate(15, 105)">
      <rect width="390" height="45" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <circle cx="22" cy="22" r="12" fill="#0284c7"/>
      <text x="22" y="26" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2</text>
      <text x="45" y="18" font-family="monospace" font-size="10" fill="#38bdf8">factorial(3)</text>
      <text x="45" y="34" font-size="9" fill="#cbd5e1">Needs <tspan font-family="monospace" fill="#fde68a">3 * factorial(2)</tspan> &#8594; Suspends &amp; calls factorial(2)</text>
    </g>

    <!-- Down arrow -->
    <path d="M 210 155 L 210 165" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="206,165 210,171 214,165" fill="#38bdf8"/>

    <!-- Step 3 -->
    <g transform="translate(15, 172)">
      <rect width="390" height="45" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <circle cx="22" cy="22" r="12" fill="#0284c7"/>
      <text x="22" y="26" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3</text>
      <text x="45" y="18" font-family="monospace" font-size="10" fill="#38bdf8">factorial(2)</text>
      <text x="45" y="34" font-size="9" fill="#cbd5e1">Needs <tspan font-family="monospace" fill="#fde68a">2 * factorial(1)</tspan> &#8594; Suspends &amp; calls factorial(1)</text>
    </g>

    <!-- Down arrow -->
    <path d="M 210 222 L 210 232" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="206,232 210,238 214,232" fill="#38bdf8"/>

    <!-- Step 4: Base Case -->
    <g transform="translate(15, 239)">
      <rect width="390" height="55" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
      <circle cx="22" cy="27" r="12" fill="#059669"/>
      <text x="22" y="31" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">&#9733;</text>
      <text x="45" y="20" font-family="monospace" font-size="10" font-weight="bold" fill="#34d399">factorial(1) &#8594; BASE CASE REACHED!</text>
      <text x="45" y="36" font-size="9" fill="#a7f3d0">Condition <tspan font-family="monospace">if n == 1:</tspan> triggers &#8594; Returns direct value <tspan font-weight="bold" fill="#ffffff">1</tspan></text>
      <text x="45" y="48" font-size="8.5" fill="#6ee7b7">Halts recursion; begins stack unrolling phase</text>
    </g>

    <g transform="translate(15, 305)">
      <rect width="390" height="65" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="15" y="18" font-size="9.5" font-weight="bold" fill="#fbbf24">&#9888; The Risk of Missing Base Case:</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">Without a base case, recursion continues infinitely,</text>
      <text x="15" y="48" font-size="8.5" fill="#cbd5e1">exhausting call stack memory and triggering</text>
      <text x="15" y="60" font-size="8.5" font-family="monospace" fill="#f87171">RecursionError: maximum recursion depth exceeded</text>
    </g>
  </g>

  <!-- Right Column: Resolution Phase -->
  <g transform="translate(495, 90)">
    <rect width="420" height="385" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="420" height="28" rx="8" fill="#059669"/>
    <text x="210" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Phase 2: Upward Stack Resolution (Popping &amp; Unwinding)</text>

    <!-- Return 1 -->
    <g transform="translate(15, 38)">
      <rect width="390" height="45" rx="6" fill="#1e293b" stroke="#34d399"/>
      <text x="15" y="18" font-family="monospace" font-size="9.5" fill="#a7f3d0">factorial(1) returns 1</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">Substituted into suspended factorial(2) frame</text>
    </g>

    <!-- Up arrow -->
    <path d="M 210 98 L 210 88" fill="none" stroke="#34d399" stroke-width="2"/>
    <polygon points="206,92 210,86 214,92" fill="#34d399"/>

    <!-- Return 2 -->
    <g transform="translate(15, 105)">
      <rect width="390" height="45" rx="6" fill="#1e293b" stroke="#34d399"/>
      <text x="15" y="18" font-family="monospace" font-size="9.5" fill="#a7f3d0">factorial(2) = 2 * 1 = 2</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">Returns 2 &#8594; Substituted into factorial(3) frame</text>
    </g>

    <!-- Up arrow -->
    <path d="M 210 165 L 210 155" fill="none" stroke="#34d399" stroke-width="2"/>
    <polygon points="206,159 210,153 214,159" fill="#34d399"/>

    <!-- Return 3 -->
    <g transform="translate(15, 172)">
      <rect width="390" height="45" rx="6" fill="#1e293b" stroke="#34d399"/>
      <text x="15" y="18" font-family="monospace" font-size="9.5" fill="#a7f3d0">factorial(3) = 3 * 2 = 6</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">Returns 6 &#8594; Substituted into original factorial(4) frame</text>
    </g>

    <!-- Up arrow -->
    <path d="M 210 232 L 210 222" fill="none" stroke="#34d399" stroke-width="2"/>
    <polygon points="206,226 210,220 214,226" fill="#34d399"/>

    <!-- Final Result Box -->
    <g transform="translate(15, 239)">
      <rect width="390" height="65" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
      <text x="195" y="24" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">FINAL COMPUTED RETURN VALUE</text>
      <text x="195" y="48" font-family="monospace" font-size="14" font-weight="bold" fill="#6ee7b7" text-anchor="middle">factorial(4) = 4 * 6 = 24</text>
    </g>

    <g transform="translate(15, 315)">
      <rect width="390" height="55" rx="6" fill="#1e293b" stroke="#818cf8"/>
      <text x="15" y="18" font-size="9.5" font-weight="bold" fill="#a5b4fc">&#128161; Mathematical Elegance:</text>
      <text x="15" y="34" font-size="8.5" fill="#cbd5e1">N! = N * (N - 1)! translates directly into self-calling code</text>
      <text x="15" y="46" font-size="8.5" fill="#cbd5e1">with mathematical symmetry and clarity.</text>
    </g>
  </g>
</svg>
""")

SVG_NAIROBI_PARK_ARCHITECTURE = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Grand Strand 3 Capstone: Nairobi Park Ticketing Terminal</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Full Functional Integration: Defensive Gateways, Modular Formulas, Collections, and Group Discounts</text>

  <!-- Left: Defensive Gateway & I/O -->
  <g transform="translate(45, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#0284c7"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Input &amp; Defensive Gateways</text>

    <g transform="translate(15, 40)">
      <rect width="240" height="75" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#f87171">&#128737; Defensive Validation:</text>
      <text x="15" y="38" font-family="monospace" font-size="8.5" fill="#cbd5e1">try / except ValueError</text>
      <text x="15" y="52" font-family="monospace" font-size="8.5" fill="#fca5a5">if age &lt; 0 or age &gt; 110:</text>
      <text x="15" y="66" font-size="8" fill="#f87171">&#10007; Reject invalid age input</text>
    </g>

    <g transform="translate(15, 125)">
      <rect width="240" height="90" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#38bdf8">&#128229; Sentinel Input Loop:</text>
      <text x="15" y="38" font-family="monospace" font-size="8.5" fill="#cbd5e1">while True:</text>
      <text x="15" y="52" font-family="monospace" font-size="8.5" fill="#cbd5e1">  input("Age or -1")</text>
      <text x="15" y="66" font-family="monospace" font-size="8.5" fill="#fbbf24">  if input == -1: break</text>
      <text x="15" y="80" font-family="monospace" font-size="8.5" fill="#a7f3d0">  group.append(age)</text>
    </g>

    <g transform="translate(15, 225)">
      <rect width="240" height="140" rx="6" fill="#1e1b4b" stroke="#818cf8"/>
      <text x="15" y="20" font-size="10" font-weight="bold" fill="#c7d2fe">&#128203; Active Container:</text>
      <text x="15" y="38" font-family="monospace" font-size="8.5" fill="#ffffff">active_group = [8, 34, 70, 22, 11]</text>
      <text x="15" y="60" font-size="8.5" fill="#cbd5e1">&#8226; Child (8): KES 300</text>
      <text x="15" y="76" font-size="8.5" fill="#cbd5e1">&#8226; Adults (34, 22): 2 x 1000</text>
      <text x="15" y="92" font-size="8.5" fill="#cbd5e1">&#8226; Senior (70): KES 500</text>
      <text x="15" y="108" font-size="8.5" fill="#cbd5e1">&#8226; Child (11): KES 300</text>
      <text x="15" y="125" font-size="8.5" font-weight="bold" fill="#fbbf24">&#8226; Total Visitors = 5</text>
    </g>
  </g>

  <!-- Middle: Modular Functions -->
  <g transform="translate(345, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#4f46e5"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Modular Business Logic</text>

    <!-- Function 1 -->
    <g transform="translate(15, 40)">
      <rect width="240" height="110" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#38bdf8">Module 1: calculate_single_ticket()</text>
      <text x="10" y="34" font-family="monospace" font-size="8" fill="#ffffff">def calculate_single_ticket(age):</text>
      <text x="10" y="50" font-family="monospace" font-size="8" fill="#cbd5e1">  if age &lt; 12: return 300</text>
      <text x="10" y="66" font-family="monospace" font-size="8" fill="#cbd5e1">  elif age &lt; 65: return 1000</text>
      <text x="10" y="82" font-family="monospace" font-size="8" fill="#cbd5e1">  else: return 500</text>
      <text x="10" y="98" font-size="8" fill="#a7f3d0">&#10003; Pure Fruitful Function</text>
    </g>

    <!-- Function 2 -->
    <g transform="translate(15, 160)">
      <rect width="240" height="130" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#fbbf24">Module 2: compute_group_total()</text>
      <text x="10" y="34" font-family="monospace" font-size="8" fill="#ffffff">def compute_group_total(ages):</text>
      <text x="10" y="50" font-family="monospace" font-size="8" fill="#cbd5e1">  total = sum(calc(a) for a in ages)</text>
      <text x="10" y="66" font-family="monospace" font-size="8" fill="#fde68a">  if len(ages) &gt;= 5:</text>
      <text x="10" y="82" font-family="monospace" font-size="8" fill="#fde68a">    total = total * 0.90 # 10% OFF</text>
      <text x="10" y="98" font-family="monospace" font-size="8" fill="#a7f3d0">  return total</text>
      <text x="10" y="116" font-size="8" font-weight="bold" fill="#34d399">&#10003; 3100 * 0.90 = KES 2,790.00</text>
    </g>

    <g transform="translate(15, 300)">
      <rect width="240" height="65" rx="6" fill="#1e1b4b" stroke="#10b981"/>
      <text x="10" y="18" font-size="9" font-weight="bold" fill="#34d399">&#127919; Separation of Concerns:</text>
      <text x="10" y="34" font-size="8" fill="#cbd5e1">&#8226; Single ticket pricing isolated from discounts.</text>
      <text x="10" y="48" font-size="8" fill="#cbd5e1">&#8226; Reusable across mobile app, POS, and web.</text>
    </g>
  </g>

  <!-- Right: Terminal Receipt Output -->
  <g transform="translate(645, 95)">
    <rect width="270" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="270" height="28" rx="8" fill="#059669"/>
    <text x="135" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Automated Terminal Receipt</text>

    <!-- Console Output Simulation -->
    <g transform="translate(15, 40)">
      <rect width="240" height="325" rx="8" fill="#000000" stroke="#334155"/>
      <text x="120" y="24" font-family="monospace" font-size="9" font-weight="bold" fill="#fbbf24" text-anchor="middle">NAIROBI NATIONAL PARK</text>
      <text x="120" y="38" font-family="monospace" font-size="8" fill="#64748b" text-anchor="middle">=========================</text>
      
      <text x="15" y="60" font-family="monospace" font-size="8.5" fill="#cbd5e1">Visitor Ages: <tspan fill="#38bdf8">[8, 34, 70, 22, 11]</tspan></text>
      <text x="15" y="80" font-family="monospace" font-size="8.5" fill="#cbd5e1">Total Visitors: <tspan fill="#ffffff">5 Persons</tspan></text>
      <text x="15" y="100" font-family="monospace" font-size="8.5" fill="#cbd5e1">Subtotal: <tspan fill="#ffffff">KES 3,100.00</tspan></text>
      <text x="15" y="125" font-family="monospace" font-size="8.5" fill="#34d399">Group Discount: 10% APPLIED</text>
      <text x="15" y="145" font-family="monospace" font-size="8.5" fill="#fbbf24">Discount Amount: -KES 310.00</text>
      
      <text x="120" y="175" font-family="monospace" font-size="8" fill="#64748b" text-anchor="middle">-------------------------</text>
      <text x="15" y="198" font-family="monospace" font-size="10" font-weight="bold" fill="#38bdf8">GRAND TOTAL DUE:</text>
      <text x="15" y="218" font-family="monospace" font-size="12" font-weight="bold" fill="#34d399">KES 2,790.00</text>
      <text x="120" y="245" font-family="monospace" font-size="8" fill="#64748b" text-anchor="middle">=========================</text>
      <text x="120" y="270" font-family="monospace" font-size="8" fill="#38bdf8" text-anchor="middle">GATE PASS ISSUED #NP-8894</text>
      <text x="120" y="290" font-family="monospace" font-size="7.5" fill="#94a3b8" text-anchor="middle">Thank you for conserving wildlife!</text>
    </g>
  </g>
</svg>
""")

# =====================================================================
# CURRICULUM DATA BUILDER (TOPIC 17: 5 UNITS, 5 LESSONS)
# =====================================================================

def build_topic17_curriculum():
    return [
        # -------------------------------------------------------------
        # UNIT 1: Modular Programming, Decomposition, & Function Anatomy
        # -------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Modular Programming, Decomposition, & Function Anatomy",
            "unit_description": "Foundations of modular programming, problem decomposition, code reusability, function syntax structure, parameters, docstrings, and return statements.",
            "lesson_title": "Introduction to Modular Programming & Function Anatomy",
            "pages": [
                # Page 1: Introduction & The Construction Site Analogy
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Construction Site Analogy: Why We Decompose",
                        "content": {
                            "text": "Imagine a single construction worker attempting to build a massive 50-story skyscraper entirely on their own. This lone worker would have to excavate the foundation, pour concrete, weld structural steel, install copper plumbing, wire high-voltage electrical grids, mount exterior glass, and paint hundreds of rooms. The project would quickly descend into chaos. If a water pipe leaked on the 2nd floor, the entire construction would grind to a halt because the same person must stop framing the 40th floor to fix the leak.\n\nIn the physical world, skyscrapers are built through **modular labor delegation**. Work is partitioned into specialized, independent teams:\n- A plumbing crew that only installs water systems.\n- An electrical crew that only runs wiring.\n- A glazing crew that only mounts glass.\n\nEach crew performs its specific task through a well-defined interface (blueprints). If a water pipe leaks, the plumbing crew is dispatched to repair it without interrupting the electrical crew working on the floor above.\n\nIn computer science, software programs are like skyscrapers. Writing thousands of lines in a single flat file creates **monolithic spaghetti code** that is fragile and unmaintainable. **Modular programming** decomposes monolithic systems into small, independent, specialized building blocks called **functions** (or subroutines)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Modular Programming & Functional Decomposition Architecture",
                        "content": {
                            "svg_content": SVG_MODULAR_DECOMPOSITION,
                            "caption": "Architectural comparison: Monolithic spaghetti code vs. a clean, hierarchically decomposed modular system with isolated responsibilities."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Core Definitions in Modular Software Engineering",
                        "content": {
                            "text": "Understanding the fundamental vocabulary of modular programming is essential:\n\n- **Modular Programming**: A software design technique that splits a large program into independent, interchangeable, and self-contained sub-units (modules), each responsible for executing one specific task.\n- **Decomposition**: The computational thinking process of breaking a complex system or problem down into smaller, more manageable sub-problems.\n- **Function (or Subroutine)**: A named, self-contained block of program statements that performs a specific operational task and can be executed (called) from other parts of the program whenever needed.\n- **Code Reusability**: The practice of writing a block of code once and invoking it multiple times throughout a system without duplicating physical statements.\n\n**The 4 Practical Values of Decomposition**:\n1. *Elimination of Code Duplication*: Write once, invoke everywhere.\n2. *Simplified Debugging and Isolation*: Test and fix individual functions without risking the wider system.\n3. *Collaborative Development*: Multiple programmers work on distinct functions simultaneously using agreed interfaces.\n4. *Improved Readability and Abstraction*: Complex algorithms are hidden behind intuitive function names (e.g., `calculate_tax()`, `send_receipt()`)."
                        }
                    }
                ],

                # Page 2: Anatomy of a Function & The Vending Machine Analogy
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Vending Machine Analogy & Structural Syntax",
                        "content": {
                            "text": "A function behaves exactly like a mechanical **Vending Machine**:\n- **The Input**: You insert coins and press a selection button (arguments passed into parameters).\n- **The Black Box**: You do not see the internal motors or gears spin (this is called **encapsulation** and **abstraction**).\n- **The Output**: A cold beverage drops into the retrieval slot (the returned result).\n\n### Function Syntax in Pseudocode & Python\nIn standardized pseudocode, a function is defined with explicit types and return markers:\n\n```pseudocode\nFUNCTION calculateArea(width: REAL, height: REAL) : REAL\n    DECLARE area : REAL\n    area <- width * height\n    RETURN area\nENDFUNCTION\n```\n\nIn Python, we use the `def` keyword, followed by the identifier name, parenthesized parameters, type hints, a colon, and an indented block:\n\n```python\ndef calculate_area(width: float, height: float) -> float:\n    \"\"\"\n    Calculates the area of a rectangle.\n    Parameters: width (float), height (float)\n    Returns: area (float)\n    \"\"\"\n    area = width * height\n    return area\n```"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Anatomy of a Function Definition & Call Mechanics",
                        "content": {
                            "svg_content": SVG_FUNCTION_ANATOMY,
                            "caption": "Dissection of Python function syntax: def keyword, descriptive identifier, typed parameters, default arguments, docstrings, and return statements."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Functional Decomposition in Software Engineering",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Functional_decomposition.png/800px-Functional_decomposition.png",
                            "caption": "Functional decomposition chart illustrating how top-level operational commands branch into discrete sub-functions in software engineering.",
                            "author": "Wikimedia Commons",
                            "licensing": "Public Domain"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Decomposition in Computer Science Explained",
                        "content": {
                            "youtube_id": "r7pdUswl8qM",
                            "url": "https://www.youtube.com/watch?v=r7pdUswl8qM",
                            "description": "Educational guide exploring decomposition and how breaking problems into modular subroutines enables scalable programming."
                        }
                    }
                ],

                # Page 3: Worked Example: Deconstructing & Building a Function
                [
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Designing a Fuel Economy Subroutine",
                        "content": {
                            "goal": "Design, define, and execute a modular Python function that computes vehicle fuel efficiency in kilometers per liter (km/L).",
                            "problem": "A logistics fleet in Mombasa needs a reusable function named `calculate_fuel_efficiency` that takes distance traveled in kilometers and fuel consumed in liters, computes efficiency, and returns the result rounded to 2 decimal places.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Draft the Function Header",
                                    "step_description": "Use the `def` keyword, descriptive name `calculate_fuel_efficiency`, and parameters `(distance_km: float, fuel_liters: float) -> float:`."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Implement Defensive Input Guard",
                                    "step_description": "Ensure fuel consumed is greater than zero to prevent division-by-zero crashes: `if fuel_liters <= 0: return 0.0`."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Compute Efficiency & Format Output",
                                    "step_description": "Calculate `km_per_liter = distance_km / fuel_liters` and return `round(km_per_liter, 2)`."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Invoke Function with Concrete Arguments",
                                    "step_description": "Call `truck_efficiency = calculate_fuel_efficiency(480.5, 65.0)` and print the returned value."
                                }
                            ],
                            "conclusion": "The function returns 7.39 km/L. The calculation logic is encapsulated and can be called thousands of times across the fleet without repeating the division formula."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Purpose of Modular Decomposition",
                        "content": {
                            "question": "What is the primary computational benefit of decomposing a monolithic program into modular functions?",
                            "options": [
                                "It increases file size to maximize disk storage utilization.",
                                "It eliminates code duplication, isolates bugs for easier debugging, and enables team collaboration.",
                                "It forces the CPU to run all statements concurrently on a single thread.",
                                "It automatically converts Python code into binary machine bytecode without an interpreter."
                            ],
                            "correct_answer": "It eliminates code duplication, isolates bugs for easier debugging, and enables team collaboration.",
                            "explanation": "Decomposition splits complex problems into manageable sub-units. This eliminates redundant copy-pasted code, isolates errors within specific functions, and allows multiple engineers to collaborate seamlessly."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Function Header Syntax",
                        "content": {
                            "question": "In Python, which keyword must precede every function definition header?",
                            "options": [
                                "function",
                                "subroutine",
                                "def",
                                "declare"
                            ],
                            "correct_answer": "def",
                            "explanation": "Python uses the reserved keyword 'def' (short for define) to declare a new function header."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Encapsulation & Abstraction",
                        "content": {
                            "question": "When a programmer calls 'math.sqrt(144)' without knowing the underlying iterative mathematical algorithm used by the CPU, which programming concept is being demonstrated?",
                            "options": [
                                "Abstraction",
                                "Spaghetti Coding",
                                "Dynamic Memory Leak",
                                "Hardware Thrashing"
                            ],
                            "correct_answer": "Abstraction",
                            "explanation": "Abstraction is the principle of hiding complex backend implementation details behind a clean, simple, and standard interface."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Return Statement Mechanics",
                        "content": {
                            "question": "What happens when a CPU encounters a 'return' statement inside an executing function?",
                            "options": [
                                "It pauses execution for 5 seconds before resuming the next line in the function.",
                                "It immediately halts the function and sends the resulting value back to the calling statement.",
                                "It loops back to the first line of the function and restarts execution.",
                                "It clears all global variables from RAM memory."
                            ],
                            "correct_answer": "It immediately halts the function and sends the resulting value back to the calling statement.",
                            "explanation": "The 'return' statement evaluates the expression, terminates the function immediately, and passes the result back to the caller."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # UNIT 2: Parameters, Arguments, & Return Values
        # -------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Parameters, Arguments, & Return Values",
            "unit_description": "Deep dive into parameters vs. arguments, positional vs. keyword mapping, default parameters, and fruitful value-returning functions vs. void procedures.",
            "lesson_title": "Parameters, Argument Mechanics, and Return Types",
            "pages": [
                # Page 1: Parameters vs. Arguments
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Conceptual Distinction: The Role vs. The Actor",
                        "content": {
                            "text": "A frequent point of confusion for beginning programmers is the precise distinction between a **parameter** and an **argument**:\n\n- **Parameter (The Role / Placeholder)**: Think of a character script in a theatrical play—for example, *\"The Detective\"*. The script defines what *\"The Detective\"* says and does, but *\"The Detective\"* is not a physical human being. It is an abstract role waiting to be filled.\n- **Argument (The Actor / Concrete Value)**: When opening night arrives, a real person (e.g., *John*) steps onto the stage and fills the role of *\"The Detective\"*.\n\nIn computer programming:\n- A **parameter** is the placeholder variable listed in the function definition header.\n- An **argument** is the actual, concrete data value passed into that parameter when the function is invoked (called).\n\n```python\n# 'width' and 'height' are PARAMETERS (placeholders in the definition header)\ndef print_box(width: int, height: int):\n    print(f\"Box Dimensions: {width} x {height}\")\n\n# 10 and 5 are ARGUMENTS (concrete values passed during invocation)\nprint_box(10, 5)\n```"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Positional vs. Keyword (Named) Arguments",
                        "content": {
                            "text": "When calling functions, arguments can be mapped to parameters in two distinct ways:\n\n### 1. Positional Arguments\nArguments are matched to parameters strictly based on their **physical order** in the call:\n```python\ndef subtract(a, b):\n    return a - b\n\nprint(subtract(10, 3))  # a=10, b=3 -> Returns 7\nprint(subtract(3, 10))  # a=3, b=10 -> Returns -7\n```\n\n### 2. Keyword (Named) Arguments\nYou explicitly specify parameter names during invocation, allowing you to pass values in any arbitrary order:\n```python\nprint(subtract(b=3, a=10))  # Explicitly names targets -> Returns 7\n```"
                        }
                    }
                ],

                # Page 2: Fruitful (Value-Returning) vs. Void Functions & Default Parameters
                [
                    {
                        "type": "concept_explanation",
                        "title": "Fruitful Functions (The Courier) vs. Void Functions (The Postbox)",
                        "content": {
                            "text": "Functions are classified by how they conclude their operational cycle:\n\n- **Fruitful (Value-Returning) Functions**: Act like a **Courier**. You give them a parcel (arguments), they travel to a destination, perform a calculation, and return directly to your doorstep with a receipt (the returned value). You can store this value in a variable or use it in further mathematical expressions.\n- **Void (Non-Returning) Functions**: Act like a **Postbox**. You drop a letter inside. The postbox carries out an action (e.g., printing a banner, writing to a file, or triggering a sound), but it hands nothing back to you. In Python, attempting to capture the output of a void function yields `None`.\n\n```python\n# Fruitful Function: Sends back a computable value\ndef get_discount(price: float, rate: float) -> float:\n    return price * rate\n\nsavings = get_discount(1500, 0.10)  # savings stores 150.0\n\n# Void Function: Performs an action without return\ndef show_banner(user: str) -> None:\n    print(f\"=== WELCOME {user.upper()} ===\")\n\nresult = show_banner(\"Jane\")  # result stores None\n```\n\n### Default Parameters & The Ordering Rule\nDefault parameters provide fallback values if arguments are omitted. In Python, **default parameters must always be positioned at the end** of the parameter list. Placing a required parameter after a default parameter triggers a `SyntaxError`:\n\n```python\n# INVALID: SyntaxError: non-default parameter follows default parameter\ndef setup_user(country=\"Kenya\", username):\n    pass\n\n# VALID: Required parameters first, defaults last\ndef setup_user(username: str, country: str = \"Kenya\"):\n    print(f\"User: {username}, Country: {country}\")\n```"
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Function Mapping Diagram in Computer Science",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Function_machine2.svg/800px-Function_machine2.svg.png",
                            "caption": "A mathematical function machine diagram: input parameters x undergo an internal transform f(x) to yield output return values.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    }
                ],

                # Page 3: Step-by-Step Worked Example: Invoice Generator
                [
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Supermarket POS Discount Calculator",
                        "content": {
                            "goal": "Construct a fruitful function with default parameters and keyword arguments for a supermarket Point of Sale (POS) system.",
                            "problem": "Create a function `calculate_final_bill` that takes `gross_amount` (float), an optional `discount_rate` (default 0.05 for 5%), and an optional `loyalty_member` flag (default False). If `loyalty_member` is True, add an additional 2% discount.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Define Function Header with Default Arguments",
                                    "step_description": "`def calculate_final_bill(gross_amount: float, discount_rate: float = 0.05, loyalty_member: bool = False) -> float:`"
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Calculate Net Discount Rate",
                                    "step_description": "Initialize `effective_rate = discount_rate`. If `loyalty_member` is True, `effective_rate += 0.02`."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Compute and Return Net Bill",
                                    "step_description": "Calculate `discount_val = gross_amount * effective_rate` and `return round(gross_amount - discount_val, 2)`."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Test with Different Call Signatures",
                                    "step_description": "Call 1: `calculate_final_bill(2000)` -> Uses 5% default (KES 1,900).\nCall 2: `calculate_final_bill(2000, loyalty_member=True)` -> Uses 5% + 2% = 7% (KES 1,860).\nCall 3: `calculate_final_bill(2000, discount_rate=0.10, loyalty_member=True)` -> Uses 12% (KES 1,760)."
                                }
                            ],
                            "conclusion": "Default and keyword arguments provide flexibility, allowing callers to override standard settings only when specialized cases arise."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Parameters vs. Arguments",
                        "content": {
                            "question": "Which of the following statements accurately distinguishes a parameter from an argument?",
                            "options": [
                                "A parameter is the placeholder variable in the function definition header; an argument is the actual value passed in during the call.",
                                "A parameter is used only in loops; an argument is used only in if-statements.",
                                "Parameters can only accept integer numbers; arguments can only accept text strings.",
                                "A parameter is globally accessible across all files; an argument is destroyed upon compilation."
                            ],
                            "correct_answer": "A parameter is the placeholder variable in the function definition header; an argument is the actual value passed in during the call.",
                            "explanation": "Parameters are the formal variables defined in the function header. Arguments are the concrete expressions or values supplied when the function is called."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Default Parameter Evaluation",
                        "content": {
                            "question": "What will the following Python code output?\n\ndef add_nums(x, y=5):\n    return x + y\n\nprint(add_nums(10))",
                            "options": [
                                "10",
                                "5",
                                "15",
                                "SyntaxError: missing required positional argument 'y'"
                            ],
                            "correct_answer": "15",
                            "explanation": "Because argument 'y' is omitted, the function falls back to its default value of 5. Thus, 10 + 5 evaluates to 15."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Default Parameter Syntax Rule",
                        "content": {
                            "question": "Why does the function definition 'def register(country=\"Kenya\", name):' trigger a SyntaxError in Python?",
                            "options": [
                                "Parameter names cannot exceed 4 characters.",
                                "Default parameters must always follow all required positional parameters at the end of the list.",
                                "The string \"Kenya\" must be capitalized using uppercase constants only.",
                                "Python does not allow string values as default parameters."
                            ],
                            "correct_answer": "Default parameters must always follow all required positional parameters at the end of the list.",
                            "explanation": "Python requires non-default parameters to precede default parameters so that positional arguments can be matched unambiguously from left to right."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Return Value of Void Functions",
                        "content": {
                            "question": "If you assign the result of a void Python function (such as 'print()') to a variable 'val = print(\"Hello\")' and then inspect 'val', what value does it hold?",
                            "options": [
                                "\"Hello\"",
                                "0",
                                "True",
                                "None"
                            ],
                            "correct_answer": "None",
                            "explanation": "In Python, functions without an explicit return statement implicitly return the special singleton value 'None'."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # UNIT 3: Scope, Variable Lifetimes, & Call Stack Tracing
        # -------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Scope, Variable Lifetimes, & Call Stack Tracing",
            "unit_description": "Investigation of local vs. global variable scopes, memory lifetimes, call stack activation records (stack frames), and step-by-step trace tables.",
            "lesson_title": "Variable Scopes, Memory Lifetimes, and the Call Stack",
            "pages": [
                # Page 1: Local vs. Global Variable Scopes
                [
                    {
                        "type": "concept_explanation",
                        "title": "Household Rules vs. National Laws: The Scope Analogy",
                        "content": {
                            "text": "To understand variable visibility, consider the analogy of **Household Rules vs. National Laws**:\n- **Local Scope (Household Rules)**: Inside your family home, you may have a rule: *\"Shoes must be removed at the front door.\"* This rule is active inside your home. However, people walking down the public street outside do not follow it, nor will security guards at a shopping mall enforce it. Its visibility is strictly local.\n- **Global Scope (National Laws)**: In Kenya, there is a national traffic law: *\"Vehicles must drive on the left side of the road.\"* This law is globally active and visible everywhere across the country.\n\n### Core Scope Definitions\n- **Variable Scope**: The region of code where a variable is recognized, visible, and directly accessible.\n- **Local Variable**: A variable declared *inside* a function body. It can only be seen and modified within that specific function.\n- **Global Variable**: A variable declared *outside* of all functions at the top level of a script. It is visible to all functions throughout the file.\n- **Variable Lifetime**: The time span during which a variable remains allocated in the computer's active RAM memory.\n\n```python\n# Global variable (visible everywhere)\ncountry_name = \"Kenya\"\n\ndef calculate_yield():\n    # Local variable (invisible outside)\n    maize_bags = 450\n    print(f\"Harvested {maize_bags} bags in {country_name}.\")\n\ncalculate_yield()\n# Accessing maize_bags here raises NameError: name 'maize_bags' is not defined!\n```\n\n### The 3 Dangers of Global Variable Pollution\n1. *State Contamination*: Any function can accidentally overwrite a global variable, making bug tracking difficult.\n2. *Memory Waste*: Global variables stay in RAM for the entire program runtime, whereas local variables are deallocated the moment their function exits.\n3. *Namespace Collisions*: Different subroutines might accidentally reuse identical global names and overwrite each other's data."
                        }
                    }
                ],

                # Page 2: The Call Stack Lifecycle & Memory Frames
                [
                    {
                        "type": "concept_explanation",
                        "title": "Physics of the Call Stack & Stack Frames",
                        "content": {
                            "text": "How does the CPU remember where to return when a function completes? It utilizes a fundamental memory structure called the **Call Stack** (operating on Last-In, First-Out / LIFO principle).\n\nImagine a vertical stack of dinner plates:\n1. **Pushing a Frame**: When a function is called, the CPU allocates an **Activation Record (Stack Frame)** containing its local variables, parameters, and the return address. This frame is pushed onto the top of the Call Stack.\n2. **Execution Focus**: The CPU suspends the calling function and executes statements within the top active frame.\n3. **Nested Calls**: If that function calls another function, a new frame is pushed on top.\n4. **Popping a Frame**: When a function hits a `return` statement, its frame is popped off the stack, its local memory is freed, and the CPU resumes executing the caller from the saved return address."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Call Stack Lifecycle & Activation Frame Management",
                        "content": {
                            "svg_content": SVG_CALL_STACK_LIFECYCLE,
                            "caption": "Step-by-step visual of stack frame pushing during nested subroutine calls, followed by frame popping and register deallocation upon return."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "The Call Stack and Stack Frames Explained",
                        "content": {
                            "youtube_id": "W8KCJ3w9cgE",
                            "url": "https://www.youtube.com/watch?v=W8KCJ3w9cgE",
                            "description": "Visual guide to how computer memory manages activation records, function calls, and return addresses on the call stack."
                        }
                    }
                ],

                # Page 3: Program Execution Trace Table
                [
                    {
                        "type": "concept_explanation",
                        "title": "Multi-Function Trace Table Analysis",
                        "content": {
                            "text": "Let us trace the execution of the following nested Python program step-by-step:\n\n```python\n1: def double_val(x):\n2:     result = x * 2\n3:     return result\n4: \n5: def accumulate(base_val, factor):\n6:     step1 = double_val(base_val)\n7:     total = step1 + factor\n8:     return total\n9: \n10: start_num = 5\n11: final_score = accumulate(start_num, 3)\n12: print(final_score)\n```"
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Call Stack Trace Table",
                        "content": {
                            "goal": "Construct a formal 12-step trace table tracking variable registers, return values, and call stack states.",
                            "problem": "Trace lines 1-12 of the nested accumulation program.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Line 10 (__main__)",
                                    "step_description": "`start_num = 5`. Stack: `[__main__]`."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Line 11 (__main__ calls accumulate)",
                                    "step_description": "`accumulate(5, 3)` called. Frame pushed. Stack: `[accumulate -> __main__]`. `base_val=5`, `factor=3`."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Line 6 (accumulate calls double_val)",
                                    "step_description": "`double_val(5)` called. Frame pushed. Stack: `[double_val -> accumulate -> __main__]`. `x=5`."
                                },
                                {
                                    "step_number": 4,
                                    "step_title": "Lines 2-3 (double_val returns)",
                                    "step_description": "`result = 10`. Returns `10`. Frame POPPED from stack. Stack: `[accumulate -> __main__]`."
                                },
                                {
                                    "step_number": 5,
                                    "step_title": "Lines 6-8 (accumulate resolves)",
                                    "step_description": "`step1 = 10`, `total = 10 + 3 = 13`. Returns `13`. Frame POPPED. Stack: `[__main__]`."
                                },
                                {
                                    "step_number": 6,
                                    "step_title": "Lines 11-12 (__main__ completes)",
                                    "step_description": "`final_score = 13`. Console outputs `13`. Stack empty."
                                }
                            ],
                            "conclusion": "The trace confirms how activation records isolate local variables and how return values unwind back down the call stack to produce the final output 13."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Variable Scopes & Visibility",
                        "content": {
                            "question": "What happens when a statement outside any function attempts to read a local variable declared inside a function?",
                            "options": [
                                "The computer fetches the variable from virtual swap memory.",
                                "A NameError is raised because the local variable does not exist in the global scope.",
                                "The local variable is automatically promoted to global status.",
                                "The operating system restarts the Python interpreter."
                            ],
                            "correct_answer": "A NameError is raised because the local variable does not exist in the global scope.",
                            "explanation": "Local variables exist only within the scope and lifetime of their parent function. Accessing them from the global scope results in a NameError."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Lifetime of Local Variables",
                        "content": {
                            "question": "When is the memory allocated for a function's local variables deallocated and returned to the system?",
                            "options": [
                                "Only when the computer is physically powered down.",
                                "The instant the function hits a return statement and terminates its execution frame.",
                                "When the next print statement is executed.",
                                "When the hard drive undergoes disk defragmentation."
                            ],
                            "correct_answer": "The instant the function hits a return statement and terminates its execution frame.",
                            "explanation": "Local variables are stored inside the function's stack frame. When the function returns, its frame is popped from the stack and its memory is immediately freed."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Dangers of Global Variables",
                        "content": {
                            "question": "Why do software engineers strongly discourage over-using global variables in modular program design?",
                            "options": [
                                "Global variables make code run too fast for human monitors to display.",
                                "They increase the risk of accidental modification across unrelated functions and consume memory for the entire runtime.",
                                "Global variables cannot store numerical data types.",
                                "Compilers convert global variables into read-only constants automatically."
                            ],
                            "correct_answer": "They increase the risk of accidental modification across unrelated functions and consume memory for the entire runtime.",
                            "explanation": "Global variables persist throughout the entire program lifecycle and can be modified by any function, leading to unintended side effects and state contamination."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Call Stack Architecture",
                        "content": {
                            "question": "Which data structure mechanism governs how the CPU tracks active subroutines and their return addresses?",
                            "options": [
                                "First-In, First-Out (FIFO) Queue",
                                "Last-In, First-Out (LIFO) Call Stack",
                                "Circular Linked Buffer",
                                "Binary Search Hash Matrix"
                            ],
                            "correct_answer": "Last-In, First-Out (LIFO) Call Stack",
                            "explanation": "The Call Stack operates as a LIFO structure: the most recently called subroutine's frame sits on top and must finish before execution returns to the caller below."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # UNIT 4: Abstraction, Standard Libraries, Mutable Containers, & Recursion
        # -------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Abstraction, Standard Libraries, Mutable Containers, & Recursion",
            "unit_description": "Exploration of standard library modules (math, random), memory physics of passing immutable values vs. mutable collections, and recursive decomposition mechanics.",
            "lesson_title": "Standard Libraries, Mutable Side-Effects, and Recursion",
            "pages": [
                # Page 1: Standard Libraries (math, random)
                [
                    {
                        "type": "concept_explanation",
                        "title": "Abstraction & Built-In Standard Libraries",
                        "content": {
                            "text": "When driving an automobile, you interact with the steering wheel and pedals without needing to calculate thermodynamic gas expansion or piston compression ratios. The complexity of the engine is **abstracted** behind a clean dashboard.\n\nIn programming, **Standard Libraries** embody abstraction—they provide pre-written, highly optimized subroutines that can be imported and executed instantly:\n\n### 1. The `math` Module\n```python\nimport math\n\nprint(math.sqrt(64))      # 8.0 (Square Root)\nprint(math.pow(2, 5))      # 32.0 (Exponentiation)\nprint(math.ceil(4.15))     # 5 (Rounds UP to nearest integer)\nprint(math.floor(4.99))    # 4 (Rounds DOWN to nearest integer)\nprint(math.pi)             # 3.141592653589793 (Mathematical Pi Constant)\n```\n\n### 2. The `random` Module\n```python\nimport random\n\n# Random integer from 1 to 100 inclusive (e.g. for games or simulations)\nlucky_number = random.randint(1, 100)\n\n# Random selection from a list container\nteams = [\"Harambee Stars\", \"Gor Mahia\", \"AFC Leopards\", \"Tusker FC\"]\nselected_team = random.choice(teams)\n```"
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Software Library Architecture Diagram",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Software_library_structure.svg/800px-Software_library_structure.svg.png",
                            "caption": "Software architecture diagram showing an application linking dynamically to pre-compiled shared library subroutines.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    }
                ],

                # Page 2: Passing Primitives vs. Passing Mutable Containers
                [
                    {
                        "type": "concept_explanation",
                        "title": "Pass-by-Value (Immutable) vs. Pass-by-Reference (Mutable)",
                        "content": {
                            "text": "How does computer RAM respond when arguments are passed into a function?\n\n- **Immutable Primitives (Pass-by-Value)**: Primitive types (integers, floats, strings, booleans) create an **isolated copy** in the function's local frame. Modifications inside the function only affect the local copy; the caller's original variable is completely shielded.\n- **Mutable Collections (Pass-by-Reference)**: Complex containers (like lists and dictionaries) do **not** get copied. Instead, the function receives the **actual memory address** of the container. Both the caller and the function share the exact same memory cells in RAM! Modifying the collection inside the function permanently alters the original container."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Memory Semantics: Pass-By-Value vs. Pass-By-Reference",
                        "content": {
                            "svg_content": SVG_MUTABILITY_PASSING,
                            "caption": "RAM memory register models contrasting immutable value cloning with shared mutable container references."
                        }
                    }
                ],

                # Page 3: Conceptual Foundations of Recursion
                [
                    {
                        "type": "concept_explanation",
                        "title": "Recursion: The Infinite Mirror & The Two Golden Rules",
                        "content": {
                            "text": "Imagine standing in an elevator with mirrors mounted on opposite walls. Looking into one mirror reveals a reflection of yourself looking into a mirror, repeating into an infinite tunnel of reflections.\n\nIn computer science, **recursion** occurs when a function calls itself within its own body.\n\n### The Two Mandatory Rules of Recursion\nTo prevent an infinite loop that crashes memory (causing a **Stack Overflow / RecursionError**), every recursive function must have:\n1. **The Base Case**: A terminal conditional check that stops further self-calls and returns a direct, non-recursive value.\n2. **The Recursive Step**: The statement where the function calls itself with a reduced argument that moves closer toward the base case.\n\n### Factorial Case Study ($N!$)\nMathematically: $N! = N \\times (N-1)!$, with Base Case $0! = 1$ and $1! = 1$.\n\n```python\ndef factorial(n: int) -> int:\n    # 1. Base Case\n    if n <= 1:\n        return 1\n    # 2. Recursive Step\n    else:\n        return n * factorial(n - 1)\n\nprint(factorial(4))  # Output: 24\n```"
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Recursive Decomposition & Call Stack Unwinding: Factorial(4)",
                        "content": {
                            "svg_content": SVG_RECURSION_DECOMPOSITION,
                            "caption": "Two-phase recursive timeline: Downward stack accumulation to the base case, followed by upward substitution and frame resolution."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Recursion in Programming Explained with Visuals",
                        "content": {
                            "youtube_id": "ngCos392W4w",
                            "url": "https://www.youtube.com/watch?v=ngCos392W4w",
                            "description": "Clear step-by-step tutorial explaining base cases, recursive cases, and stack frames during recursive execution."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Mutable Side Effects",
                        "content": {
                            "question": "What will the following Python code output?\n\ndef add_item(basket):\n    basket.append(\"Mango\")\n\nmy_cart = [\"Apple\", \"Banana\"]\nadd_item(my_cart)\nprint(my_cart)",
                            "options": [
                                "['Apple', 'Banana']",
                                "['Apple', 'Banana', 'Mango']",
                                "['Mango']",
                                "TypeError: list object is immutable"
                            ],
                            "correct_answer": "['Apple', 'Banana', 'Mango']",
                            "explanation": "Lists are mutable objects passed by reference. The append method modifies the original list object in RAM, persisting the change outside the function."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Mandatory Components of Recursion",
                        "content": {
                            "question": "What two elements are strictly required for every valid recursive function?",
                            "options": [
                                "A global variable and a while loop.",
                                "A Base Case to stop recursion and a Recursive Step that progresses toward the base case.",
                                "A try-except block and an import statement.",
                                "A floating-point parameter and a void return type."
                            ],
                            "correct_answer": "A Base Case to stop recursion and a Recursive Step that progresses toward the base case.",
                            "explanation": "Without a base case, recursion continues infinitely; without a progressive recursive step, the base case will never be reached."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Stack Overflow Root Cause",
                        "content": {
                            "question": "What causes a Stack Overflow Error (or RecursionError in Python) during recursive execution?",
                            "options": [
                                "The computer's monitor running out of display pixels.",
                                "The function calls itself infinitely without hitting a base case, exhausting the memory allocated for stack frames.",
                                "A variable identifier containing more than 255 characters.",
                                "Importing both the math and random libraries in the same script."
                            ],
                            "correct_answer": "The function calls itself infinitely without hitting a base case, exhausting the memory allocated for stack frames.",
                            "explanation": "Every recursive call pushes a new frame onto the call stack. If the recursion never hits a base case, memory is exhausted and a stack overflow occurs."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Standard Library Math Ceil",
                        "content": {
                            "question": "What is the return value of 'math.ceil(7.12)' in Python?",
                            "options": [
                                "7",
                                "7.0",
                                "8",
                                "7.1"
                            ],
                            "correct_answer": "8",
                            "explanation": "The math.ceil() function rounds a floating-point number UP to the nearest integer ceiling, returning 8."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # UNIT 5: Defensive Programming, Refactoring Workshop, & Grand Project Integration
        # -------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "Defensive Programming, Refactoring Workshop, & Grand Project Integration",
            "unit_description": "Defensive validation gateways, program refactoring workshop (Nakuru water billing), and the Grand Strand 3 Capstone Project (Nairobi Park Ticketing Terminal).",
            "lesson_title": "Defensive Programming, Refactoring, and Capstone Integration",
            "pages": [
                # Page 1: Defensive Programming Principles
                [
                    {
                        "type": "concept_explanation",
                        "title": "The Bouncer Analogy: Defensive Input Validation",
                        "content": {
                            "text": "Imagine a high-security facility. Before you enter, a security guard checks your credentials at the front gate. If your pass is invalid or expired, entry is denied at the perimeter. The guard does not let unauthorized individuals inside to \"try\" door locks.\n\nIn software engineering, **defensive programming** designs functions under the assumption that external inputs are likely to be invalid, malformed, or malicious. A robust function validates its parameters at the entry threshold. If verification fails, it rejects the input immediately before processing corrupted calculations.\n\n```python\ndef register_intern_age(age_arg: int) -> str:\n    \"\"\"\n    Registers intern applicant age with defensive validation blocks.\n    \"\"\"\n    # Defense 1: Type Validation\n    if not isinstance(age_arg, int):\n        return \"ERROR: Age must be a whole number.\"\n        \n    # Defense 2: Range Boundary Validation\n    if age_arg < 16 or age_arg > 25:\n        return f\"ERROR: Age {age_arg} is outside allowed bounds (16 to 25).\"\n        \n    # Proceed safely once verified\n    return f\"Registration Successful! Intern ID: CS-{age_arg * 104}\"\n\nprint(register_intern_age(\"twenty\"))  # Rejection: Invalid type\nprint(register_intern_age(14))        # Rejection: Out of bounds\nprint(register_intern_age(20))        # Success: CS-2080\n```"
                        }
                    }
                ],

                # Page 2: Program Refactoring Workshop: Nakuru Water Billing
                [
                    {
                        "type": "concept_explanation",
                        "title": "Workshop: Refactoring Monolithic Code into Modular Functions",
                        "content": {
                            "text": "Analyze the following fragile monolithic script used by a cooperative in Nakuru, where step-based water bill logic is copy-pasted for every customer:\n\n```python\n# FRAGILE MONOLITHIC CODE (Repeated Logic)\nuse1 = 45.5\nbill1 = (10 * 50) + (10 * 80) + ((use1 - 20) * 120) + 150\nprint(f\"Invoice for Arap Sang: KES {bill1}\")\n\nuse2 = 8.0\nbill2 = (use2 * 50) + 150\nprint(f\"Invoice for Wanjiku: KES {bill2}\")\n```\n\n### The Modular Refactored Solution\nBy extracting calculation and formatting into dedicated functions, maintenance becomes effortless:\n\n```python\ndef calculate_water_charge(consumption: float) -> float:\n    \"\"\"Computes step-based water charges based on cubic meters.\"\"\"\n    BASE_RATE, MID_RATE, HIGH_RATE = 50.0, 80.0, 120.0\n    MAINTENANCE_TAX = 150.0\n    \n    if consumption <= 10.0:\n        charge = consumption * BASE_RATE\n    elif consumption <= 20.0:\n        charge = (10 * BASE_RATE) + ((consumption - 10) * MID_RATE)\n    else:\n        charge = (10 * BASE_RATE) + (10 * MID_RATE) + ((consumption - 20) * HIGH_RATE)\n        \n    return charge + MAINTENANCE_TAX\n\ndef generate_invoice(customer_name: str, consumption: float) -> None:\n    \"\"\"Formats and displays an official municipal invoice.\"\"\"\n    total = calculate_water_charge(consumption)\n    print(f\"Invoice for {customer_name}: KES {total:.2f}\")\n\ngenerate_invoice(\"Arap Sang\", 45.5)\ngenerate_invoice(\"Wanjiku\", 8.0)\n```"
                        }
                    }
                ],

                # Page 3: Grand Strand 3 Capstone: Nairobi Park Ticketing Terminal
                [
                    {
                        "type": "concept_explanation",
                        "title": "Grand Strand 3 Capstone: Nairobi Park Ticketing Terminal",
                        "content": {
                            "text": "To conclude **Strand 3 (Software Development)**, students synthesize all concepts studied throughout Grade 10:\n- Sequential execution\n- Conditional selection (`if/elif/else`)\n- Sentinel-controlled loops (`while True`)\n- Collection containers (lists)\n- Modular fruitful and void functions\n- Defensive input validation\n\n### System Blueprint\n1. **Age-Based Pricing**: Children (<12) KES 300, Adults (12-64) KES 1,000, Seniors (65+) KES 500.\n2. **Group Discount**: Groups of 5 or more receive a 10% discount on the total bill.\n3. **Sentinel Input**: Cashier enters ages continuously until `-1` signals checkout.\n4. **Defensive Gateway**: Rejects non-integers and invalid ages (< 0 or > 110)."
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Grand Strand 3 Capstone: Nairobi Park Ticketing Terminal",
                        "content": {
                            "svg_content": SVG_NAIROBI_PARK_ARCHITECTURE,
                            "caption": "Full architectural pipeline: Defensive input filtering, collection container tracking, modular pricing algorithms, and terminal invoice rendering."
                        }
                    },
                    {
                        "type": "step_by_step_worked_example",
                        "title": "Worked Example: Complete Nairobi Park Terminal Implementation",
                        "content": {
                            "goal": "Implement and execute the full modular Nairobi National Park Ticketing Terminal program in Python.",
                            "problem": "Write clean, modular code with separate functions for single ticket pricing, group total computation, and terminal interface loop.",
                            "steps": [
                                {
                                    "step_number": 1,
                                    "step_title": "Implement calculate_single_ticket Function",
                                    "step_description": "Pure fruitful function taking `age: int` and returning base price (300, 1000, or 500)."
                                },
                                {
                                    "step_number": 2,
                                    "step_title": "Implement compute_group_total Function",
                                    "step_description": "Takes `ages_list: list`, sums single tickets, and applies `0.90` multiplier if `len(ages_list) >= 5`."
                                },
                                {
                                    "step_number": 3,
                                    "step_title": "Implement main_ticketing_loop Void Controller",
                                    "step_description": "Runs `while True` loop with `try/except ValueError`, collects visitor ages into list, handles `-1` break, and prints formatted summary receipt."
                                }
                            ],
                            "conclusion": "The resulting program is robust, fully modular, defensively secured against bad inputs, and integrates all Strand 3 programming competencies."
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (4 MCQs)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 1: Defensive Programming Principle",
                        "content": {
                            "question": "What is the core philosophy behind defensive programming?",
                            "options": [
                                "Assuming user inputs may be invalid or erroneous and validating parameters at function entry before execution.",
                                "Encrypting all variable names with 256-bit passwords.",
                                "Writing programs entirely without functions to avoid stack frame overhead.",
                                "Preventing users from running Python scripts on Linux operating systems."
                            ],
                            "correct_answer": "Assuming user inputs may be invalid or erroneous and validating parameters at function entry before execution.",
                            "explanation": "Defensive programming validates data types and value ranges at the threshold of a function to prevent downstream computation errors or application crashes."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 2: Refactoring Definition",
                        "content": {
                            "question": "What does the term 'code refactoring' mean in software engineering?",
                            "options": [
                                "Rewriting an application in a completely different language.",
                                "Restructuring existing code to improve readability, eliminate duplication, and enhance maintainability without altering external behavior.",
                                "Compiling source code directly into hardware transistors.",
                                "Deleting all docstrings and comments to compress file size."
                            ],
                            "correct_answer": "Restructuring existing code to improve readability, eliminate duplication, and enhance maintainability without altering external behavior.",
                            "explanation": "Refactoring improves internal code architecture, modularity, and maintainability while preserving the program's observable external behavior."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 3: Capstone Group Discount Calculation",
                        "content": {
                            "question": "In the Nairobi Park system, a family group of 5 visitors has raw ticket prices totaling KES 3,100. With the 10% group discount applied, what is the final grand total due?",
                            "options": [
                                "KES 3,100.00",
                                "KES 2,790.00",
                                "KES 2,500.00",
                                "KES 310.00"
                            ],
                            "correct_answer": "KES 2,790.00",
                            "explanation": "A 10% discount on KES 3,100 equals KES 310. Subtracting the discount yields KES 2,790.00 (or 3100 * 0.90 = 2790.00)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Formative Check 4: Sentinel Loop Termination",
                        "content": {
                            "question": "In a console input loop collecting visitor ages, what is the special trigger value '-1' called?",
                            "options": [
                                "A Compiler Flag",
                                "A Sentinel Value",
                                "A Dynamic Stack Pointer",
                                "A Global Literal"
                            ],
                            "correct_answer": "A Sentinel Value",
                            "explanation": "A sentinel value is a special input value used to signal the termination of an indefinite loop."
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION EXECUTOR
# =====================================================================

def ingest_grade10_topic17(replace: bool = True):
    print("=" * 80)
    print("STARTING INGESTION: CBC Grade 10 Computer Science — Topic 17")
    print("Topic: Functions")
    print("=" * 80)

    curriculum = Curriculum.objects.get(id=5)
    grade = Grade.objects.get(curriculum=curriculum, level=10)
    subject, _ = Subject.objects.get_or_create(grade=grade, name="Computer Science")

    with transaction.atomic():
        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=17,
            defaults={
                "name": "Functions",
                "description": "Comprehensive study of modular programming, problem decomposition, function anatomy, parameters and arguments, fruitful vs. void subroutines, local/global variable scopes and lifetimes, call stack execution mechanics, standard libraries, mutable container side-effects, recursion, defensive programming, and integrated capstone development."
            }
        )

        if not created and replace:
            print(f"[*] Topic 17 already exists (ID: {topic.id}). Performing clean replacement of units and lessons...")
            topic.learning_units.all().delete()
            topic.lessons.all().delete()
            topic.name = "Functions"
            topic.description = "Comprehensive study of modular programming, problem decomposition, function anatomy, parameters and arguments, fruitful vs. void subroutines, local/global variable scopes and lifetimes, call stack execution mechanics, standard libraries, mutable container side-effects, recursion, defensive programming, and integrated capstone development."
            topic.save()

        curriculum_data = build_topic17_curriculum()

        total_units = 0
        total_lessons = 0
        total_pages = 0
        total_blocks = 0
        total_assets = 0

        for u_data in curriculum_data:
            u_order = u_data["unit_order"]
            u_name = clean_text(u_data["unit_name"])
            u_desc = clean_text(u_data["unit_description"])
            l_title = clean_text(u_data["lesson_title"])
            pages = u_data["pages"]

            unit = LearningUnit.objects.create(
                topic=topic,
                order=u_order,
                name=u_name,
                description=u_desc
            )
            total_units += 1

            lesson = Lesson.objects.create(
                topic=topic,
                learning_unit=unit,
                title=l_title,
                status="published",
                version=1,
                immutable_metadata={
                    "author": "VLearn Senior Computer Science Curriculum Ingestion Specialist",
                    "curriculum_id": 5,
                    "grade": "Grade 10",
                    "subject": "Computer Science",
                    "topic_order": 17,
                    "unit_order": u_order
                }
            )
            total_lessons += 1

            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cs_t17_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 17, "unit_order": u_order, "page": page_idx}
                    )
                    block_counter += 1
                    total_blocks += 1

                    # Attach LessonAssets
                    if b_type == "suggested_diagram" and "svg_content" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="diagram",
                            source_type="ai_generated",
                            storage_type="embed",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            metadata={"svg_content": b_content["svg_content"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_image" and "url" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="image",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("caption", b_title),
                            url=b_content["url"],
                            metadata={
                                "author": b_content.get("author", "Wikimedia Commons"),
                                "licensing": b_content.get("licensing", "CC BY-SA"),
                                "caption": b_content.get("caption", "")
                            }
                        )
                        block.assets.add(asset)
                        total_assets += 1

                    elif b_type == "suggested_video" and "youtube_id" in b_content:
                        asset = LessonAsset.objects.create(
                            lesson=lesson,
                            asset_type="youtube",
                            source_type="external",
                            storage_type="url",
                            status="attached",
                            title=b_title,
                            description=b_content.get("description", b_title),
                            url=b_content.get("url", f"https://www.youtube.com/watch?v={b_content['youtube_id']}"),
                            metadata={"youtube_id": b_content["youtube_id"]}
                        )
                        block.assets.add(asset)
                        total_assets += 1

            print(f"  [+] Ingested Unit {u_order}: '{u_name}' -> Lesson '{l_title}' ({len(pages)} Pages, {block_counter - 1} Blocks)")

    print("=" * 80)
    print(f"TOPIC 17 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic17(replace=True)
