"""
VLearn CBC Grade 10 Computer Science — Topic 11: Network Topologies
Production Ingestion & Enrichment Engine

Curriculum: CBC (ID: 5)
Grade: Grade 10 (ID: 5, Level: 10)
Subject: Computer Science (ID: 38)
Topic: Network Topologies (Topic Order: 11)

Decomposed into 5 Comprehensive Learning Units & 5 Published Lessons:
  1. Introduction to Physical and Logical Topologies (Lesson 37: Introduction to Physical and Logical Topologies)
  2. Bus, Star, Ring, Mesh, Tree, and Hybrid Topologies (Lesson 38: Bus, Star, Ring, Mesh, and Related Topologies)
  3. Selecting an Appropriate Network Topology (Lesson 39: Selecting an Appropriate Network Topology)
  4. Creating a Physical Network Topology (Lesson 40: Creating a Physical Network Topology)
  5. Appreciation and Evaluation of Network Topologies (Lesson 41: Appreciation and Evaluation of Network Topologies)
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
# HIGH PRECISION VECTOR SVGS FOR TOPIC 11
# =====================================================================

SVG_PHYSICAL_VS_LOGICAL = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Physical vs. Logical Network Topologies: The Hub Crossover</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Physical Wiring (What You Touch) vs. Logical Signal Flow (How Packets Travel)</text>

  <!-- Left Side: Physical Star Layout -->
  <g transform="translate(50, 95)">
    <rect width="410" height="385" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="410" height="28" rx="8" fill="#0284c7"/>
    <text x="205" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">A. Physical Topology (Star Wiring)</text>

    <!-- Central Hub -->
    <rect x="155" y="160" width="100" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="205" y="185" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">Central Hub</text>
    <text x="205" y="200" font-size="8.5" fill="#94a3b8" text-anchor="middle">(Layer 1 Repeater)</text>

    <!-- Node 1: Top -->
    <rect x="165" y="45" width="80" height="45" rx="6" fill="#1e293b" stroke="#0ea5e9"/>
    <text x="205" y="72" font-size="10" font-weight="bold" fill="#7dd3fc" text-anchor="middle">PC A (Sender)</text>
    <line x1="205" y1="90" x2="205" y2="160" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Node 2: Left -->
    <rect x="25" y="165" width="80" height="45" rx="6" fill="#1e293b" stroke="#0ea5e9"/>
    <text x="65" y="192" font-size="10" font-weight="bold" fill="#cbd5e1" text-anchor="middle">PC B</text>
    <line x1="105" y1="187" x2="155" y2="187" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Node 3: Right -->
    <rect x="305" y="165" width="80" height="45" rx="6" fill="#1e293b" stroke="#0ea5e9"/>
    <text x="345" y="192" font-size="10" font-weight="bold" fill="#cbd5e1" text-anchor="middle">PC C</text>
    <line x1="255" y1="187" x2="305" y2="187" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Node 4: Bottom -->
    <rect x="165" y="275" width="80" height="45" rx="6" fill="#1e293b" stroke="#0ea5e9"/>
    <text x="205" y="302" font-size="10" font-weight="bold" fill="#cbd5e1" text-anchor="middle">PC D</text>
    <line x1="205" y1="210" x2="205" y2="275" stroke="#38bdf8" stroke-width="2.5"/>

    <!-- Legend/Notes -->
    <rect x="20" y="335" width="370" height="38" rx="6" fill="#1e293b"/>
    <text x="205" y="352" font-size="9" fill="#94a3b8" text-anchor="middle">Tangible cables run radially from workstations to the central hub.</text>
    <text x="205" y="365" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Physical Shape: STAR</text>
  </g>

  <!-- Right Side: Logical Bus Behavior -->
  <g transform="translate(500, 95)">
    <rect width="410" height="385" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="410" height="28" rx="8" fill="#059669"/>
    <text x="205" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">B. Logical Topology (Shared Bus Broadcast)</text>

    <!-- Logical Bus Backbone -->
    <line x1="40" y1="180" x2="370" y2="180" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
    
    <!-- Terminators -->
    <rect x="28" y="168" width="12" height="24" rx="2" fill="#ef4444"/>
    <text x="34" y="205" font-size="8" fill="#f87171" text-anchor="middle">Term</text>
    <rect x="370" y="168" width="12" height="24" rx="2" fill="#ef4444"/>
    <text x="376" y="205" font-size="8" fill="#f87171" text-anchor="middle">Term</text>

    <!-- Drops & Nodes -->
    <!-- PC A -->
    <rect x="45" y="65" width="70" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="80" y="89" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">PC A [Tx]</text>
    <line x1="80" y1="105" x2="80" y2="180" stroke="#38bdf8" stroke-width="2"/>
    <text x="80" y="145" font-size="8.5" fill="#38bdf8" text-anchor="middle">&#9660; Signal</text>

    <!-- PC B -->
    <rect x="135" y="65" width="70" height="40" rx="6" fill="#1e293b" stroke="#64748b"/>
    <text x="170" y="89" font-size="9.5" font-weight="bold" fill="#cbd5e1" text-anchor="middle">PC B</text>
    <line x1="170" y1="105" x2="170" y2="180" stroke="#64748b" stroke-width="2"/>
    <text x="170" y="145" font-size="8.5" fill="#94a3b8" text-anchor="middle">&#9650; Hears</text>

    <!-- PC C -->
    <rect x="225" y="65" width="70" height="40" rx="6" fill="#1e293b" stroke="#64748b"/>
    <text x="260" y="89" font-size="9.5" font-weight="bold" fill="#cbd5e1" text-anchor="middle">PC C</text>
    <line x1="260" y1="105" x2="260" y2="180" stroke="#64748b" stroke-width="2"/>
    <text x="260" y="145" font-size="8.5" fill="#94a3b8" text-anchor="middle">&#9650; Hears</text>

    <!-- PC D -->
    <rect x="315" y="65" width="70" height="40" rx="6" fill="#1e293b" stroke="#64748b"/>
    <text x="350" y="89" font-size="9.5" font-weight="bold" fill="#cbd5e1" text-anchor="middle">PC D</text>
    <line x1="350" y1="105" x2="350" y2="180" stroke="#64748b" stroke-width="2"/>
    <text x="350" y="145" font-size="8.5" fill="#94a3b8" text-anchor="middle">&#9650; Hears</text>

    <!-- Broadcast Waves -->
    <g transform="translate(60, 225)">
      <rect width="300" height="95" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
      <text x="150" y="22" font-size="10" font-weight="bold" fill="#fbbf24" text-anchor="middle">Broadcast Collision Domain</text>
      <text x="150" y="42" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Hub repeats electrical signal out of all ports.</text>
      <text x="150" y="60" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; All nodes share one bandwidth collision zone.</text>
      <text x="150" y="78" font-size="8.5" fill="#fca5a5" text-anchor="middle">&#8226; Only 1 computer can transmit at any single instant.</text>
    </g>

    <!-- Legend/Notes -->
    <rect x="20" y="335" width="370" height="38" rx="6" fill="#1e293b"/>
    <text x="205" y="352" font-size="9" fill="#94a3b8" text-anchor="middle">Data signal floods all ports simultaneously as a shared bus.</text>
    <text x="205" y="365" font-size="9" font-weight="bold" fill="#34d399" text-anchor="middle">Logical Behavior: BUS (Shared Medium)</text>
  </g>
</svg>
""")

SVG_FIVE_TOPOLOGIES = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">The Five Fundamental Computer Network Topologies</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Architectural Layouts, Connection Mechanics, and Fault Profiles</text>

  <!-- Topology 1: BUS -->
  <g transform="translate(45, 90)">
    <rect width="260" height="185" rx="8" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="260" height="24" rx="6" fill="#0284c7"/>
    <text x="130" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Bus Topology</text>

    <!-- Backbone -->
    <line x1="25" y1="95" x2="235" y2="95" stroke="#38bdf8" stroke-width="4"/>
    <rect x="18" y="87" width="7" height="16" rx="2" fill="#ef4444"/>
    <rect x="235" y="87" width="7" height="16" rx="2" fill="#ef4444"/>

    <!-- Nodes -->
    <circle cx="60" cy="55" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="60" y="59" font-size="9" fill="#38bdf8" text-anchor="middle">N1</text>
    <line x1="60" y1="69" x2="60" y2="95" stroke="#38bdf8" stroke-width="1.5"/>

    <circle cx="130" cy="55" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="130" y="59" font-size="9" fill="#38bdf8" text-anchor="middle">N2</text>
    <line x1="130" y1="69" x2="130" y2="95" stroke="#38bdf8" stroke-width="1.5"/>

    <circle cx="200" cy="55" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="200" y="59" font-size="9" fill="#38bdf8" text-anchor="middle">N3</text>
    <line x1="200" y1="69" x2="200" y2="95" stroke="#38bdf8" stroke-width="1.5"/>

    <text x="130" y="135" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Shared central backbone cable</text>
    <text x="130" y="152" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; End terminators prevent bounce</text>
    <text x="130" y="170" font-size="8.5" font-weight="bold" fill="#f87171" text-anchor="middle">Backbone cut = Whole Net Down</text>
  </g>

  <!-- Topology 2: STAR -->
  <g transform="translate(350, 90)">
    <rect width="260" height="185" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="260" height="24" rx="6" fill="#059669"/>
    <text x="130" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Star Topology</text>

    <!-- Center Switch -->
    <rect x="105" y="70" width="50" height="30" rx="4" fill="#059669" stroke="#34d399"/>
    <text x="130" y="88" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Switch</text>

    <!-- Outer Nodes -->
    <circle cx="60" cy="45" r="12" fill="#1e293b" stroke="#34d399"/>
    <text x="60" y="48" font-size="8" fill="#34d399" text-anchor="middle">A</text>
    <line x1="70" y1="53" x2="105" y2="75" stroke="#34d399" stroke-width="1.5"/>

    <circle cx="200" cy="45" r="12" fill="#1e293b" stroke="#34d399"/>
    <text x="200" y="48" font-size="8" fill="#34d399" text-anchor="middle">B</text>
    <line x1="190" y1="53" x2="155" y2="75" stroke="#34d399" stroke-width="1.5"/>

    <circle cx="60" cy="120" r="12" fill="#1e293b" stroke="#34d399"/>
    <text x="60" y="123" font-size="8" fill="#34d399" text-anchor="middle">C</text>
    <line x1="70" y1="113" x2="105" y2="95" stroke="#34d399" stroke-width="1.5"/>

    <circle cx="200" cy="120" r="12" fill="#1e293b" stroke="#34d399"/>
    <text x="200" y="123" font-size="8" fill="#34d399" text-anchor="middle">D</text>
    <line x1="190" y1="113" x2="155" y2="95" stroke="#34d399" stroke-width="1.5"/>

    <text x="130" y="148" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Dedicated point-to-point links</text>
    <text x="130" y="165" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Cable break isolated to 1 node</text>
    <text x="130" y="178" font-size="8" fill="#94a3b8" text-anchor="middle">Standard for Modern LANs</text>
  </g>

  <!-- Topology 3: RING -->
  <g transform="translate(655, 90)">
    <rect width="260" height="185" rx="8" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="260" height="24" rx="6" fill="#6366f1"/>
    <text x="130" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Ring Topology</text>

    <!-- Circular Loop -->
    <ellipse cx="130" cy="80" rx="75" ry="40" fill="none" stroke="#818cf8" stroke-width="2" stroke-dasharray="4,3"/>

    <!-- Nodes on ring -->
    <circle cx="130" cy="40" r="12" fill="#1e293b" stroke="#a5b4fc"/>
    <text x="130" y="44" font-size="8" fill="#a5b4fc" text-anchor="middle">1</text>

    <circle cx="205" cy="80" r="12" fill="#1e293b" stroke="#a5b4fc"/>
    <text x="205" y="84" font-size="8" fill="#a5b4fc" text-anchor="middle">2</text>

    <circle cx="130" cy="120" r="12" fill="#1e293b" stroke="#a5b4fc"/>
    <text x="130" y="124" font-size="8" fill="#a5b4fc" text-anchor="middle">3</text>

    <circle cx="55" cy="80" r="12" fill="#1e293b" stroke="#a5b4fc"/>
    <text x="55" y="84" font-size="8" fill="#a5b4fc" text-anchor="middle">4</text>

    <!-- Token Arrow -->
    <text x="175" y="55" font-size="9" fill="#fbbf24">&#10140;</text>

    <text x="130" y="148" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Closed loop; Token Passing</text>
    <text x="130" y="165" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Deterministic, zero collisions</text>
    <text x="130" y="178" font-size="8" fill="#f87171" text-anchor="middle">One break halts entire loop</text>
  </g>

  <!-- Topology 4: MESH -->
  <g transform="translate(180, 295)">
    <rect width="280" height="190" rx="8" fill="#0f172a" stroke="#f472b6" stroke-width="1.5"/>
    <rect width="280" height="24" rx="6" fill="#db2777"/>
    <text x="140" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Full Mesh Topology</text>

    <!-- 5 Nodes Full Mesh (10 links) -->
    <line x1="140" y1="55" x2="200" y2="80" stroke="#f472b6" stroke-width="1.2"/>
    <line x1="140" y1="55" x2="180" y2="125" stroke="#f472b6" stroke-width="1.2"/>
    <line x1="140" y1="55" x2="100" y2="125" stroke="#f472b6" stroke-width="1.2"/>
    <line x1="140" y1="55" x2="80" y2="80" stroke="#f472b6" stroke-width="1.2"/>

    <line x1="200" y1="80" x2="180" y2="125" stroke="#f472b6" stroke-width="1.2"/>
    <line x1="200" y1="80" x2="100" y2="125" stroke="#f472b6" stroke-width="1.2"/>
    <line x1="200" y1="80" x2="80" y2="80" stroke="#f472b6" stroke-width="1.2"/>

    <line x1="180" y1="125" x2="100" y2="125" stroke="#f472b6" stroke-width="1.2"/>
    <line x1="180" y1="125" x2="80" y2="80" stroke="#f472b6" stroke-width="1.2"/>

    <line x1="100" y1="125" x2="80" y2="80" stroke="#f472b6" stroke-width="1.2"/>

    <circle cx="140" cy="55" r="10" fill="#1e293b" stroke="#f472b6"/>
    <circle cx="200" cy="80" r="10" fill="#1e293b" stroke="#f472b6"/>
    <circle cx="180" cy="125" r="10" fill="#1e293b" stroke="#f472b6"/>
    <circle cx="100" cy="125" r="10" fill="#1e293b" stroke="#f472b6"/>
    <circle cx="80" cy="80" r="10" fill="#1e293b" stroke="#f472b6"/>

    <text x="140" y="152" font-size="8.5" font-weight="bold" fill="#f472b6" text-anchor="middle">Formula: Links = N(N-1) / 2</text>
    <text x="140" y="168" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Maximum redundancy &amp; fault tolerance</text>
    <text x="140" y="182" font-size="8" fill="#94a3b8" text-anchor="middle">Extremely costly; for critical data centers</text>
  </g>

  <!-- Topology 5: TREE / HYBRID -->
  <g transform="translate(500, 295)">
    <rect width="280" height="190" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <rect width="280" height="24" rx="6" fill="#d97706"/>
    <text x="140" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Tree / Hybrid Topology</text>

    <!-- Backbone trunk line -->
    <line x1="70" y1="65" x2="210" y2="65" stroke="#f59e0b" stroke-width="3"/>
    <text x="140" y="58" font-size="7.5" fill="#fbbf24" text-anchor="middle">Trunk Backbone</text>

    <!-- Star Cluster 1 -->
    <rect x="50" y="75" width="40" height="20" rx="3" fill="#1e293b" stroke="#fbbf24"/>
    <text x="70" y="88" font-size="7" fill="#fbbf24" text-anchor="middle">Sw 1</text>
    <line x1="70" y1="65" x2="70" y2="75" stroke="#fbbf24" stroke-width="1.5"/>
    <line x1="55" y1="95" x2="45" y2="120" stroke="#fbbf24" stroke-width="1"/>
    <line x1="85" y1="95" x2="95" y2="120" stroke="#fbbf24" stroke-width="1"/>
    <circle cx="45" cy="120" r="7" fill="#1e293b" stroke="#cbd5e1"/>
    <circle cx="95" cy="120" r="7" fill="#1e293b" stroke="#cbd5e1"/>

    <!-- Star Cluster 2 -->
    <rect x="190" y="75" width="40" height="20" rx="3" fill="#1e293b" stroke="#fbbf24"/>
    <text x="210" y="88" font-size="7" fill="#fbbf24" text-anchor="middle">Sw 2</text>
    <line x1="210" y1="65" x2="210" y2="75" stroke="#fbbf24" stroke-width="1.5"/>
    <line x1="195" y1="95" x2="185" y2="120" stroke="#fbbf24" stroke-width="1"/>
    <line x1="225" y1="95" x2="235" y2="120" stroke="#fbbf24" stroke-width="1"/>
    <circle cx="185" cy="120" r="7" fill="#1e293b" stroke="#cbd5e1"/>
    <circle cx="235" cy="120" r="7" fill="#1e293b" stroke="#cbd5e1"/>

    <text x="140" y="152" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Hierarchical star clusters on bus trunk</text>
    <text x="140" y="168" font-size="8.5" fill="#cbd5e1" text-anchor="middle">&#8226; Ideal for multi-floor school buildings</text>
    <text x="140" y="182" font-size="8" fill="#94a3b8" text-anchor="middle">Trunk failure severs inter-branch talk only</text>
  </g>
</svg>
""")

SVG_MESH_MATH_FORMULA = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="45" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Full Mesh Mathematical Modeling &amp; Scalability Complexity</text>
  <text x="480" y="68" font-size="12" fill="#94a3b8" text-anchor="middle">Calculating Physical Link Overhead L = N(N-1)/2 and Interface Port Exhaustion</text>

  <!-- Left: Formula Card & Breakdown -->
  <g transform="translate(45, 95)">
    <rect width="400" height="385" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="400" height="28" rx="8" fill="#0284c7"/>
    <text x="200" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">The Full Mesh Formula &amp; Port Equation</text>

    <!-- Formula Box -->
    <rect x="25" y="45" width="350" height="85" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="200" y="78" font-family="monospace" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">L = [ N &#215; (N - 1) ] / 2</text>
    <text x="200" y="105" font-size="10.5" fill="#cbd5e1" text-anchor="middle">Ports Required per Node = (N - 1)</text>

    <!-- Variable Definitions -->
    <text x="35" y="155" font-size="10.5" font-weight="bold" fill="#7dd3fc">&#8226; N : Number of active nodes (servers/hosts)</text>
    <text x="35" y="175" font-size="10.5" font-weight="bold" fill="#7dd3fc">&#8226; L : Total physical duplex communication cables</text>
    <text x="35" y="195" font-size="10.5" font-weight="bold" fill="#7dd3fc">&#8226; / 2 : Division by 2 eliminates bidirectional double-counting</text>

    <!-- Worked Example Box -->
    <rect x="25" y="215" width="350" height="150" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="40" y="238" font-size="11" font-weight="bold" fill="#34d399">Step-by-Step Worked Example (8 Servers):</text>
    <text x="40" y="262" font-size="9.5" fill="#cbd5e1">1. Identify Nodes: N = 8</text>
    <text x="40" y="282" font-size="9.5" fill="#cbd5e1">2. Ports per node: (8 - 1) = 7 ports each</text>
    <text x="40" y="302" font-size="9.5" fill="#cbd5e1">3. Formula: L = (8 &#215; 7) / 2 = 56 / 2 = <tspan font-weight="bold" fill="#38bdf8">28 Cables</tspan></text>
    <text x="40" y="325" font-size="9.5" fill="#fbbf24">&#9888; Expanding from 8 to 12 servers:</text>
    <text x="40" y="345" font-size="9" fill="#cbd5e1">L = (12 &#215; 11) / 2 = 66 cables! (<tspan fill="#f87171">+38 new cables</tspan> for just 4 servers!)</text>
  </g>

  <!-- Right: Growth Comparison Table & Topology Graphic -->
  <g transform="translate(470, 95)">
    <rect width="445" height="385" rx="12" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="445" height="28" rx="8" fill="#6366f1"/>
    <text x="222" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Scalability Scaling Matrix: Star vs. Full Mesh</text>

    <!-- Table Graphic -->
    <g transform="translate(15, 45)">
      <!-- Header -->
      <rect width="415" height="26" fill="#1e293b" stroke="#334155"/>
      <text x="35" y="17" font-size="9.5" font-weight="bold" fill="#38bdf8">Nodes (N)</text>
      <text x="125" y="17" font-size="9.5" font-weight="bold" fill="#34d399">Star Cables (N)</text>
      <text x="235" y="17" font-size="9.5" font-weight="bold" fill="#f472b6">Mesh Cables L</text>
      <text x="345" y="17" font-size="9.5" font-weight="bold" fill="#fbbf24">Mesh Ports/NIC</text>

      <!-- Rows -->
      <g transform="translate(0, 26)">
        <rect width="415" height="24" fill="#0f172a" stroke="#334155"/>
        <text x="35" y="16" font-size="9.5" fill="#cbd5e1">4 Nodes</text>
        <text x="125" y="16" font-size="9.5" fill="#34d399">4</text>
        <text x="235" y="16" font-size="9.5" fill="#f472b6">6</text>
        <text x="345" y="16" font-size="9.5" fill="#fbbf24">3 ports</text>
      </g>
      <g transform="translate(0, 50)">
        <rect width="415" height="24" fill="#1e293b" stroke="#334155"/>
        <text x="35" y="16" font-size="9.5" fill="#cbd5e1">6 Nodes</text>
        <text x="125" y="16" font-size="9.5" fill="#34d399">6</text>
        <text x="235" y="16" font-size="9.5" fill="#f472b6">15</text>
        <text x="345" y="16" font-size="9.5" fill="#fbbf24">5 ports</text>
      </g>
      <g transform="translate(0, 74)">
        <rect width="415" height="24" fill="#0f172a" stroke="#334155"/>
        <text x="35" y="16" font-size="9.5" fill="#cbd5e1">8 Nodes</text>
        <text x="125" y="16" font-size="9.5" fill="#34d399">8</text>
        <text x="235" y="16" font-size="9.5" fill="#f472b6">28</text>
        <text x="345" y="16" font-size="9.5" fill="#fbbf24">7 ports</text>
      </g>
      <g transform="translate(0, 98)">
        <rect width="415" height="24" fill="#1e293b" stroke="#334155"/>
        <text x="35" y="16" font-size="9.5" fill="#cbd5e1">12 Nodes</text>
        <text x="125" y="16" font-size="9.5" fill="#34d399">12</text>
        <text x="235" y="16" font-size="9.5" fill="#f472b6">66</text>
        <text x="345" y="16" font-size="9.5" fill="#fbbf24">11 ports</text>
      </g>
      <g transform="translate(0, 122)">
        <rect width="415" height="24" fill="#0f172a" stroke="#334155"/>
        <text x="35" y="16" font-size="9.5" fill="#cbd5e1">20 Nodes</text>
        <text x="125" y="16" font-size="9.5" fill="#34d399">20</text>
        <text x="235" y="16" font-size="9.5" font-weight="bold" fill="#f87171">190</text>
        <text x="345" y="16" font-size="9.5" font-weight="bold" fill="#f87171">19 ports</text>
      </g>
      <g transform="translate(0, 146)">
        <rect width="415" height="24" fill="#0f172a" stroke="#334155"/>
        <text x="35" y="16" font-size="9.5" fill="#cbd5e1">50 Nodes</text>
        <text x="125" y="16" font-size="9.5" fill="#34d399">50</text>
        <text x="235" y="16" font-size="9.5" font-weight="bold" fill="#f87171">1,225</text>
        <text x="345" y="16" font-size="9.5" font-weight="bold" fill="#f87171">49 ports</text>
      </g>
    </g>

    <!-- Key Takeaway Box -->
    <rect x="15" y="235" width="415" height="135" rx="8" fill="#1e293b" stroke="#f59e0b"/>
    <text x="30" y="258" font-size="10.5" font-weight="bold" fill="#fbbf24">Architectural Conclusion: O(N&#178;) Complexity</text>
    <text x="30" y="280" font-size="9" fill="#cbd5e1">&#8226; Star topology scales linearly (O(N)): Adding 1 node needs 1 cable.</text>
    <text x="30" y="300" font-size="9" fill="#cbd5e1">&#8226; Full mesh scales quadratically (O(N&#178;)): Adding nodes rapidly exhausts</text>
    <text x="30" y="318" font-size="9" fill="#cbd5e1">   physical cable trays and server PCIe expansion slots.</text>
    <text x="30" y="342" font-size="9" font-weight="bold" fill="#34d399">&#8594; Solution: Partial Mesh or Hybrid Star-Mesh in modern data centers.</text>
  </g>
</svg>
""")

SVG_TOPOLOGY_SELECTION_FLOWCHART = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Network Topology Selection Decision Framework Flowchart</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Systematic decision path balancing uptime requirements, building geography, and financial budgets</text>

  <!-- Start Node -->
  <g transform="translate(390, 85)">
    <rect width="180" height="35" rx="17" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="90" y="22" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Start: Client Requirements</text>
  </g>

  <!-- Down Arrow to Decision 1 -->
  <line x1="480" y1="120" x2="480" y2="150" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="476,150 484,150 480,157" fill="#38bdf8"/>

  <!-- Decision 1: 100% Zero Downtime Critical? -->
  <g transform="translate(360, 157)">
    <polygon points="120,0 240,40 120,80 0,40" fill="#1e293b" stroke="#f472b6" stroke-width="2"/>
    <text x="120" y="36" font-size="9.5" font-weight="bold" fill="#f472b6" text-anchor="middle">Is 100% Uptime</text>
    <text x="120" y="50" font-size="9.5" font-weight="bold" fill="#f472b6" text-anchor="middle">Mission-Critical?</text>
  </g>

  <!-- Decision 1 -> YES -> Mesh -->
  <g transform="translate(600, 197)">
    <line x1="0" y1="0" x2="80" y2="0" stroke="#f472b6" stroke-width="2"/>
    <polygon points="80,-4 80,4 87,0" fill="#f472b6"/>
    <text x="35" y="-8" font-size="9.5" font-weight="bold" fill="#f472b6">YES</text>

    <!-- Mesh Result Box -->
    <rect x="87" y="-35" width="220" height="70" rx="8" fill="#0f172a" stroke="#f472b6" stroke-width="2"/>
    <text x="197" y="-12" font-size="11" font-weight="bold" fill="#f472b6" text-anchor="middle">FULL / PARTIAL MESH</text>
    <text x="197" y="6" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Banks, Air Traffic, Military, ICU</text>
    <text x="197" y="22" font-size="8" fill="#94a3b8" text-anchor="middle">Budget: High | Redundancy: Max</text>
  </g>

  <!-- Decision 1 -> NO -> Decision 2 -->
  <g transform="translate(480, 237)">
    <line x1="0" y1="0" x2="0" y2="40" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="-4,40 4,40 0,47" fill="#38bdf8"/>
    <text x="10" y="25" font-size="9.5" font-weight="bold" fill="#38bdf8">NO</text>
  </g>

  <!-- Decision 2: Multi-floor / Multi-building? -->
  <g transform="translate(360, 284)">
    <polygon points="120,0 240,40 120,80 0,40" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <text x="120" y="36" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Multi-Floor or</text>
    <text x="120" y="50" font-size="9.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Multi-Building?</text>
  </g>

  <!-- Decision 2 -> YES -> Tree / Hybrid -->
  <g transform="translate(600, 324)">
    <line x1="0" y1="0" x2="80" y2="0" stroke="#fbbf24" stroke-width="2"/>
    <polygon points="80,-4 80,4 87,0" fill="#fbbf24"/>
    <text x="35" y="-8" font-size="9.5" font-weight="bold" fill="#fbbf24">YES</text>

    <!-- Tree Result Box -->
    <rect x="87" y="-35" width="220" height="70" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="2"/>
    <text x="197" y="-12" font-size="11" font-weight="bold" fill="#fbbf24" text-anchor="middle">TREE / HYBRID TOPOLOGY</text>
    <text x="197" y="6" font-size="8.5" fill="#cbd5e1" text-anchor="middle">School Campuses, Office Towers</text>
    <text x="197" y="22" font-size="8" fill="#94a3b8" text-anchor="middle">Hierarchical Switches on Trunk Backbone</text>
  </g>

  <!-- Decision 2 -> NO -> Decision 3 -->
  <g transform="translate(480, 364)">
    <line x1="0" y1="0" x2="0" y2="35" stroke="#38bdf8" stroke-width="2"/>
    <polygon points="-4,35 4,35 0,42" fill="#38bdf8"/>
    <text x="10" y="22" font-size="9.5" font-weight="bold" fill="#38bdf8">NO</text>
  </g>

  <!-- Final Selection: Star Topology -->
  <g transform="translate(320, 406)">
    <rect width="320" height="85" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2.5"/>
    <rect width="320" height="24" rx="8" fill="#059669"/>
    <text x="160" y="16" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&#10003; STANDARD CHOICE: STAR TOPOLOGY</text>
    <text x="160" y="44" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">School Computer Labs, Small Clinics, Retail Offices</text>
    <text x="160" y="62" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Best balance of cost, fault isolation, scalability, and easy maintenance.</text>
    <text x="160" y="76" font-size="8" fill="#94a3b8" text-anchor="middle">Single switch connects all workstations with individual Cat6 UTP cables.</text>
  </g>

  <!-- Legacy Note on Left -->
  <g transform="translate(45, 280)">
    <rect width="260" height="110" rx="8" fill="#1e293b" stroke="#64748b"/>
    <text x="130" y="22" font-size="10" font-weight="bold" fill="#94a3b8" text-anchor="middle">Legacy Alternatives:</text>
    <text x="15" y="44" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#f87171">Bus Topology</tspan>: Avoid for new builds;</text>
    <text x="23" y="58" font-size="8.5" fill="#cbd5e1">single backbone cut breaks entire lab.</text>
    <text x="15" y="78" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#a5b4fc">Ring Topology</tspan>: Specialized industrial /</text>
    <text x="23" y="92" font-size="8.5" fill="#cbd5e1">telemetry rings with dual counter-rotating fiber.</text>
  </g>
</svg>
""")

SVG_STAR_CABLING_WORKFLOW = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Step-by-Step Structured Assembly &amp; Testing of a Physical Star Network</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">From Blueprint Planning and Mechanical Locking to LED Diagnostics and Ping Verification</text>

  <!-- Step 1: Blueprint & Audit -->
  <g transform="translate(45, 90)">
    <rect width="195" height="385" rx="10" fill="#0f172a" stroke="#0ea5e9" stroke-width="1.5"/>
    <rect width="195" height="26" rx="8" fill="#0284c7"/>
    <text x="97" y="17" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Plan &amp; Audit</text>

    <rect x="15" y="40" width="165" height="70" rx="6" fill="#1e293b" stroke="#38bdf8"/>
    <text x="97" y="60" font-size="9.5" font-weight="bold" fill="#38bdf8" text-anchor="middle">Hardware Bill of Materials</text>
    <text x="25" y="80" font-size="8.5" fill="#cbd5e1">&#8226; 5 Workstations + 1 Printer</text>
    <text x="25" y="96" font-size="8.5" fill="#cbd5e1">&#8226; 1 8-Port Gigabit Switch</text>

    <text x="15" y="135" font-size="9.5" font-weight="bold" fill="#7dd3fc">&#8226; Draft Port Map Table:</text>
    <text x="15" y="155" font-size="8.5" fill="#cbd5e1">Match PC labels to physical switch port numbers (1–6).</text>

    <text x="15" y="195" font-size="9.5" font-weight="bold" fill="#7dd3fc">&#8226; Safety Inspection:</text>
    <text x="15" y="215" font-size="8.5" fill="#cbd5e1">Check cables for kink damage. Verify surge protector.</text>

    <rect x="15" y="270" width="165" height="90" rx="6" fill="#1e293b" stroke="#f59e0b"/>
    <text x="25" y="292" font-size="9" font-weight="bold" fill="#fbbf24">Lab Safety Rule:</text>
    <text x="25" y="312" font-size="8" fill="#cbd5e1">&#8226; Unplug power before</text>
    <text x="25" y="326" font-size="8" fill="#cbd5e1">  running cables.</text>
    <text x="25" y="342" font-size="8" fill="#cbd5e1">&#8226; Never pull across floor.</text>
  </g>

  <!-- Step 2: Structured Trunking -->
  <g transform="translate(265, 90)">
    <rect width="195" height="385" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="195" height="26" rx="8" fill="#059669"/>
    <text x="97" y="17" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Route &amp; Trunk</text>

    <rect x="15" y="40" width="165" height="70" rx="6" fill="#1e293b" stroke="#34d399"/>
    <text x="97" y="60" font-size="9.5" font-weight="bold" fill="#34d399" text-anchor="middle">Central Core Placement</text>
    <text x="25" y="80" font-size="8.5" fill="#cbd5e1">&#8226; Mount switch in rack</text>
    <text x="25" y="96" font-size="8.5" fill="#cbd5e1">&#8226; Away from dust &amp; heat</text>

    <text x="15" y="135" font-size="9.5" font-weight="bold" fill="#6ee7b7">&#8226; PVC Wall Trunking:</text>
    <text x="15" y="155" font-size="8.5" fill="#cbd5e1">Route Cat6 UTP cables neatly inside protective raceways.</text>

    <text x="15" y="195" font-size="9.5" font-weight="bold" fill="#6ee7b7">&#8226; Service Slack:</text>
    <text x="15" y="215" font-size="8.5" fill="#cbd5e1">Leave 15 cm of slack at both ends to prevent port strain.</text>

    <rect x="15" y="270" width="165" height="90" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="25" y="292" font-size="9" font-weight="bold" fill="#34d399">Cable Management:</text>
    <text x="25" y="312" font-size="8" fill="#cbd5e1">&#8226; Use velcro ties.</text>
    <text x="25" y="326" font-size="8" fill="#cbd5e1">&#8226; Label both ends (e.g.,</text>
    <text x="25" y="342" font-size="8" fill="#cbd5e1">  "PC-03 -&gt; Switch Port 3").</text>
  </g>

  <!-- Step 3: Mechanical Lock -->
  <g transform="translate(485, 90)">
    <rect width="195" height="385" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1.5"/>
    <rect width="195" height="26" rx="8" fill="#6366f1"/>
    <text x="97" y="17" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Click &amp; Power On</text>

    <rect x="15" y="40" width="165" height="70" rx="6" fill="#1e293b" stroke="#818cf8"/>
    <text x="97" y="60" font-size="9.5" font-weight="bold" fill="#a5b4fc" text-anchor="middle">RJ-45 Spring Latch</text>
    <text x="25" y="80" font-size="8.5" fill="#cbd5e1">&#8226; Push into PC NIC port</text>
    <text x="25" y="96" font-size="8.5" font-weight="bold" fill="#a5b4fc">&#8226; Listen for solid "CLICK"</text>

    <text x="15" y="135" font-size="9.5" font-weight="bold" fill="#a5b4fc">&#8226; Switch Terminus:</text>
    <text x="15" y="155" font-size="8.5" fill="#cbd5e1">Insert opposite RJ-45 plug into corresponding switch port.</text>

    <text x="15" y="195" font-size="9.5" font-weight="bold" fill="#a5b4fc">&#8226; Power-Up Order:</text>
    <text x="15" y="215" font-size="8.5" fill="#cbd5e1">1. Power switch on first.</text>
    <text x="15" y="232" font-size="8.5" fill="#cbd5e1">2. Boot client PCs &amp; printer.</text>

    <rect x="15" y="270" width="165" height="90" rx="6" fill="#1e293b" stroke="#818cf8"/>
    <text x="25" y="292" font-size="9" font-weight="bold" fill="#a5b4fc">Physical Connection:</text>
    <text x="25" y="312" font-size="8" fill="#cbd5e1">Gold 8P8C pins make contact</text>
    <text x="25" y="326" font-size="8" fill="#cbd5e1">with spring clip locked</text>
    <text x="25" y="342" font-size="8" fill="#cbd5e1">in place securely.</text>
  </g>

  <!-- Step 4: Verify & Ping -->
  <g transform="translate(705, 90)">
    <rect width="205" height="385" rx="10" fill="#0f172a" stroke="#f472b6" stroke-width="1.5"/>
    <rect width="205" height="26" rx="8" fill="#db2777"/>
    <text x="102" y="17" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Test &amp; Verify</text>

    <!-- LED Status Box -->
    <rect x="15" y="40" width="175" height="90" rx="6" fill="#1e293b" stroke="#10b981"/>
    <circle cx="35" cy="65" r="6" fill="#22c55e"/>
    <text x="48" y="69" font-size="9" font-weight="bold" fill="#4ade80">Link LED: Solid Green</text>
    <text x="35" y="85" font-size="8" fill="#cbd5e1">(Physical Carrier Good)</text>
    <circle cx="35" cy="105" r="6" fill="#f59e0b"/>
    <text x="48" y="109" font-size="9" font-weight="bold" fill="#fbbf24">Act LED: Blinking</text>
    <text x="35" y="122" font-size="8" fill="#cbd5e1">(Frames Transmitting)</text>

    <!-- Ping Terminal Box -->
    <rect x="15" y="145" width="175" height="110" rx="6" fill="#000000" stroke="#334155"/>
    <text x="25" y="165" font-family="monospace" font-size="8" fill="#4ade80">C:\&gt; ping 192.168.1.2</text>
    <text x="25" y="180" font-family="monospace" font-size="7.5" fill="#94a3b8">Reply from 192.168.1.2:</text>
    <text x="25" y="195" font-family="monospace" font-size="7.5" fill="#94a3b8">bytes=32 time&lt;1ms TTL=64</text>
    <text x="25" y="212" font-family="monospace" font-size="7.5" fill="#94a3b8">bytes=32 time&lt;1ms TTL=64</text>
    <text x="25" y="232" font-family="monospace" font-size="8" font-weight="bold" fill="#38bdf8">Packets: Sent=4, Rcvd=4</text>
    <text x="25" y="247" font-family="monospace" font-size="8" font-weight="bold" fill="#34d399">Loss = 0% (SUCCESS!)</text>

    <rect x="15" y="270" width="175" height="90" rx="6" fill="#1e293b" stroke="#10b981"/>
    <text x="25" y="292" font-size="9" font-weight="bold" fill="#34d399">Verification Complete:</text>
    <text x="25" y="312" font-size="8" fill="#cbd5e1">&#10003; Layer 1 (Physical Wire)</text>
    <text x="25" y="328" font-size="8" fill="#cbd5e1">&#10003; Layer 2 (Switching)</text>
    <text x="25" y="344" font-size="8" fill="#cbd5e1">&#10003; Layer 3 (IP Delivery)</text>
  </g>
</svg>
""")

SVG_ECO_LODGE_TOPOLOGY_EVALUATION = sanitize_svg(r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" style="background: #0f172a; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="20" y="15" width="920" height="490" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <text x="480" y="42" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">Comparative Topology Evaluation: Safari Eco-Lodge Redesign</text>
  <text x="480" y="65" font-size="12" fill="#94a3b8" text-anchor="middle">Maasai Mara Eco-Lodge: Legacy Fragile Ring vs. Evaluated Resilient Star Architecture</text>

  <!-- Left: Legacy Ring Architecture (Vulnerable) -->
  <g transform="translate(45, 90)">
    <rect width="410" height="385" rx="12" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
    <rect width="410" height="28" rx="8" fill="#b91c1c"/>
    <text x="205" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Design A: Legacy Physical Ring (High Vulnerability)</text>

    <!-- Ring Layout -->
    <ellipse cx="205" cy="140" rx="130" ry="60" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6,4"/>

    <!-- Cabins -->
    <rect x="180" y="65" width="50" height="26" rx="4" fill="#1e293b" stroke="#cbd5e1"/>
    <text x="205" y="82" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Office</text>

    <rect x="300" y="110" width="50" height="26" rx="4" fill="#1e293b" stroke="#cbd5e1"/>
    <text x="325" y="127" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Cabin 1</text>

    <rect x="280" y="175" width="50" height="26" rx="4" fill="#1e293b" stroke="#cbd5e1"/>
    <text x="305" y="192" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Cabin 2</text>

    <rect x="130" y="175" width="50" height="26" rx="4" fill="#1e293b" stroke="#cbd5e1"/>
    <text x="155" y="192" font-size="8.5" fill="#cbd5e1" text-anchor="middle">Cabin 3</text>

    <!-- Animal Bite Cable Cut -->
    <g transform="translate(60, 110)">
      <rect width="55" height="26" rx="4" fill="#1e293b" stroke="#ef4444"/>
      <text x="27" y="127" font-size="8.5" fill="#f87171" text-anchor="middle">Cabin 4</text>
      <!-- Cut symbol -->
      <line x1="27" y1="-15" x2="45" y2="5" stroke="#ef4444" stroke-width="3"/>
      <line x1="45" y1="-15" x2="27" y2="5" stroke="#ef4444" stroke-width="3"/>
      <text x="95" y="-5" font-size="8" font-weight="bold" fill="#f87171">&#9888; Cable Cut!</text>
    </g>

    <!-- Failure Evaluation Box -->
    <rect x="20" y="240" width="370" height="120" rx="8" fill="#1e293b" stroke="#ef4444"/>
    <text x="35" y="262" font-size="10" font-weight="bold" fill="#f87171">Evaluation Matrix Verdict: REJECTED</text>
    <text x="35" y="282" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#fca5a5">Fault Tolerance</tspan>: Zero. One animal bite halts entire token ring.</text>
    <text x="35" y="300" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#fca5a5">Troubleshooting</tspan>: Technician must walk 1.5 km searching wire.</text>
    <text x="35" y="318" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#fca5a5">Expansion</tspan>: Adding Cabin 5 requires breaking live network.</text>
    <text x="35" y="340" font-size="8" font-weight="bold" fill="#f87171">&#10007; Unacceptable for modern hospitality guest operations.</text>
  </g>

  <!-- Right: Evaluated Star/Hybrid Architecture (Superior) -->
  <g transform="translate(500, 90)">
    <rect width="410" height="385" rx="12" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <rect width="410" height="28" rx="8" fill="#059669"/>
    <text x="205" y="19" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Design B: Central Star with Underground Armored Cables</text>

    <!-- Central Hub Office -->
    <rect x="155" y="115" width="100" height="50" rx="8" fill="#059669" stroke="#34d399" stroke-width="2"/>
    <text x="205" y="137" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Core Switch Rack</text>
    <text x="205" y="152" font-size="8" fill="#dcfce7" text-anchor="middle">(Office + Starlink WAN)</text>

    <!-- Dedicated Star Links to Cabins -->
    <line x1="155" y1="130" x2="65" y2="85" stroke="#34d399" stroke-width="2"/>
    <line x1="255" y1="130" x2="345" y2="85" stroke="#34d399" stroke-width="2"/>
    <line x1="155" y1="150" x2="65" y2="195" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,2"/>
    <line x1="255" y1="150" x2="345" y2="195" stroke="#34d399" stroke-width="2"/>

    <!-- Cabins in Star -->
    <rect x="35" y="70" width="60" height="28" rx="4" fill="#1e293b" stroke="#34d399"/>
    <text x="65" y="88" font-size="8.5" fill="#34d399" text-anchor="middle">Cabin 1 &#10003;</text>

    <rect x="315" y="70" width="60" height="28" rx="4" fill="#1e293b" stroke="#34d399"/>
    <text x="345" y="88" font-size="8.5" fill="#34d399" text-anchor="middle">Cabin 2 &#10003;</text>

    <rect x="35" y="180" width="60" height="28" rx="4" fill="#1e293b" stroke="#ef4444"/>
    <text x="65" y="198" font-size="8.5" fill="#f87171" text-anchor="middle">Cabin 3 (Cut)</text>

    <rect x="315" y="180" width="60" height="28" rx="4" fill="#1e293b" stroke="#34d399"/>
    <text x="345" y="198" font-size="8.5" fill="#34d399" text-anchor="middle">Cabin 4 &#10003;</text>

    <!-- Success Evaluation Box -->
    <rect x="20" y="240" width="370" height="120" rx="8" fill="#1e293b" stroke="#10b981"/>
    <text x="35" y="262" font-size="10" font-weight="bold" fill="#34d399">Evaluation Matrix Verdict: APPROVED</text>
    <text x="35" y="282" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#6ee7b7">Fault Isolation</tspan>: If Cabin 3 line breaks, Cabins 1, 2, 4 remain 100% up.</text>
    <text x="35" y="300" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#6ee7b7">Maintainability</tspan>: Switch port LED immediately pinpoints fault.</text>
    <text x="35" y="318" font-size="8.5" fill="#cbd5e1">&#8226; <tspan font-weight="bold" fill="#6ee7b7">Cost / Lifespan</tspan>: Underground PVC conduit shields from wildlife.</text>
    <text x="35" y="340" font-size="8" font-weight="bold" fill="#34d399">&#10003; Recommended standard for safari eco-lodges and resorts.</text>
  </g>
</svg>
""")

# =====================================================================
# DECOMPOSED CURRICULUM DATA STRUCTURE
# =====================================================================

def build_topic11_curriculum():
    return [
        # -------------------------------------------------------------
        # UNIT 1: Introduction to Physical and Logical Topologies (Lesson 37)
        # -------------------------------------------------------------
        {
            "unit_order": 1,
            "unit_name": "Introduction to Physical and Logical Topologies",
            "unit_description": "Foundations of network architecture: differentiating physical cabling layouts from logical signal flow pathways, analyzing crossover phenomena (Physical Star/Logical Bus and Physical Star/Logical Ring), and mastering core topology nomenclature.",
            "lesson_title": "Lesson 37: Introduction to Physical and Logical Topologies",
            "pages": [
                # Page 1: Physical vs Logical Foundations & Analogy
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Physical vs. Logical Topology Disambiguation",
                        "content": {
                            "goal": "Differentiate clearly between physical network topology (hardware layout, cables, ports) and logical network topology (signal flow, broadcast domains, token passing), and explain how a single network can diverge between both perspectives."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'City Map' Analogy & Core Definitions",
                        "content": {
                            "markdown": """### **The 'City Map' Analogy**
Imagine planning a new city:
- **Physical Streets and Bridges**: You lay down tarmac roads, concrete bridges, and street signs connecting homes, schools, and offices. This tangible layout is the **physical map**.
- **Delivery and Transit Routes**: How vehicles actually move may follow an entirely different path. A postal truck might follow a clockwise circular route, or a public transit bus might run back and forth along a single main street, regardless of the physical road grid. This movement of cargo is the **logical route**.

In computer networking, network architecture is evaluated from these exact two perspectives:
- **Physical Topology**: The tangible, geometric arrangement of physical cables, wireless access points, network interface cards (NICs), and hardware nodes. It is what you can see and touch in a computer laboratory.
- **Logical Topology**: The conceptual path, electrical protocols, and addressing rules that govern how data packets travel from node to node across the physical medium.

### **Core Networking Terminology**
- **Network Topology**: The structural blueprint of a network, defining how nodes (devices) and links (channels) are interconnected and how they interact.
- **Node**: Any active electronic device connected to a network capable of creating, receiving, or transmitting data (e.g., computers, switches, routers, network printers, servers).
- **Link**: The physical (copper, fiber) or wireless (radio frequency) communication pathway connecting two nodes.
- **Collision Domain**: A logical network segment where data packets can collide with one another when two or more devices transmit at the exact same instant."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Physical Star vs. Logical Bus Crossover",
                        "content": {
                            "svg_content": SVG_PHYSICAL_VS_LOGICAL,
                            "caption": "Figure 11.1: Comparative architectural schematic demonstrating how an Ethernet network wired as a physical star around an unmanaged hub operates logically as a shared broadcast bus."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Physical vs. Logical Separation",
                        "content": {
                            "text": "Physical topology represents physical cable geography and hardware ports; logical topology represents signal flow and data transmission protocol behavior. A network can be physically wired as a star while logically behaving as a bus or a ring."
                        }
                    }
                ],

                # Page 2: The Deep Dive into Topology Crossovers & Comparison Matrix
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Architectural Analysis of Crossover Networks",
                        "content": {
                            "goal": "Analyze classic crossover topologies including Star-Bus (Hub-based Ethernet) and Star-Ring (Token Ring MAU), and evaluate their structural differences across tangibility, dependency, and reconfigurability."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Crossover Phenomena & Comparison Matrix",
                        "content": {
                            "markdown": """### **Classical Topology Crossovers**

#### **1. The Star-Bus Crossover (Physical Star, Logical Bus)**
The most famous example occurs in an Ethernet local area network (LAN) connected via an **unmanaged hub**:
- **Physical Layout**: Each workstation has its own dedicated Cat6 Ethernet cable plugged into a central hub in the middle of the room, creating a physical **Star**.
- **Logical Behavior**: An unmanaged hub is a Layer 1 physical device with no memory or MAC address table. When Node A transmits a frame, the hub simply amplifies the electrical signal and **broadcasts it out of every other port simultaneously**. All connected workstations share a single collision domain, exactly like tapping into a single shared horizontal line. Hence, it functions logically as a **Bus**.

#### **2. The Star-Ring Crossover (Physical Star, Logical Ring)**
In classic IBM Token Ring networks:
- **Physical Layout**: Workstations connect individually to a central device called a **Multistation Access Unit (MAU)**. Visually and physically, cables radiate outward as a **Star**.
- **Logical Behavior**: Inside the MAU's internal circuitry, the signal is passed in a sequential, unidirectional closed loop from port 1 to port 2 to port 3, and back. Workstations must capture a circulating **token** to transmit. Hence, it functions logically as a **Ring**.

---

### **Physical vs. Logical Comparison Matrix**

| Feature | Physical Topology | Logical Topology |
| :--- | :--- | :--- |
| **Focus** | Physical arrangement of hardware, cables, and ports. | Signal pathways, protocols, and data flow rules. |
| **Tangibility** | Tangible; physically inspected, measured, and touched. | Intangible; exists as electrical, optical, or radio frame rules. |
| **Dependency** | Dictated by room architecture, cable conduits, and hardware ports. | Dictated by Network Interface Cards (NICs), switches, and network protocols. |
| **Modification** | High effort; requires running new cables and moving hardware. | Low effort; reconfigurable via software settings, VLANs, or device upgrades. |"""
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Structured Ethernet Patch Panel and Switch Hub",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Patch_panel_and_ethernet_switch.jpg/800px-Patch_panel_and_ethernet_switch.jpg",
                            "caption": "Figure 11.2: A structured cabling patch panel and switch rack illustrating a physical star topology where individual workstation drops terminate at a central distribution point.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Physical vs Logical Network Topologies Explained",
                        "content": {
                            "youtube_id": "b-Xg_nZ2U_U",
                            "description": "An intuitive tutorial exploring the difference between physical wiring arrangements and logical data flow paths with animated signal broadcasts."
                        }
                    }
                ],

                # Page 3: Interactive Activity & Worked Scenario
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Engineering Scenario: The Virtual Classroom Conflict",
                        "content": {
                            "markdown": """### **Worked Scenario: The Virtual Classroom Conflict**

#### **Problem Context**
A secondary school computer laboratory has 20 desktop computers plugged into a central networking **hub**. The computer teacher observes that whenever Student A and Student B attempt to copy video files across the lab simultaneously, the network slows down to a near halt for all 20 computers. 

#### **Architectural Diagnosis**
1. **Physical State**: The laboratory is wired as a **Physical Star** (20 individual Cat6 cables running to the central hub).
2. **Logical State**: Because a hub is a dumb multiport repeater, the network behaves as a **Logical Bus**. When Student A transmits, the hub floods all 20 ports with electrical signals.
3. **The Bottleneck**: All 20 workstations share a single **100 Mbps collision domain**. When Student A and Student B transmit at the same time, their packets collide repeatedly, triggering back-off timers and saturating the shared bus bandwidth.

#### **Engineering Solution & Topology Transformation**
- **Action**: Replace the central **hub** with a **Layer 2 Network Switch**.
- **Physical Result**: Remains an identical **Physical Star** (no cables need to be moved or replaced).
- **Logical Result**: Transforms into a **Logical Star** (Point-to-Point Micro-segmented Switching). The switch inspects destination MAC addresses and forwards frames exclusively to the intended recipient port.
- **Outcome**: Student A and Student B can transmit simultaneously at full wire speed without colliding or slowing down the remaining 18 workstations!"""
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Classroom Roleplay: The Invisible Mailman",
                        "content": {
                            "markdown": """### **Interactive Activity: The Invisible Mailman**
**Objective**: Experience physical vs. logical separation through physical simulation.

1. **Setup**: Arrange 6 student desks in a physical circle (Physical Ring).
2. **Round 1 (Physical Ring / Logical Ring)**: Hand a tennis ball clockwise from desk to desk. Students can only speak when holding the ball (Token Passing).
3. **Round 2 (Physical Ring / Logical Star)**: Assign one student in the center as the Switch. Desks remain in a circle, but whenever a student has a message, they must throw the ball to the center student, who passes it directly to the designated recipient.
4. **Round 3 (Physical Ring / Logical Bus)**: Keep the circular desks. Student 1 shouts a message out loud. Everyone hears the broadcast, but only the student whose name is called writes it down."""
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (Lesson 37)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Logical Topology Definition",
                        "content": {
                            "question": "What does the 'Logical Topology' of a computer network primarily describe?",
                            "options": [
                                "The physical length and color of copper Ethernet cables",
                                "The brand, model, and physical weight of the network switch",
                                "The conceptual pathway, addressing rules, and signal flow data packets follow",
                                "The electrical AC voltage supplied to the server room wall sockets"
                            ],
                            "answer": "The conceptual pathway, addressing rules, and signal flow data packets follow",
                            "explanation": "Logical topology describes how signals and data packets conceptually travel through the network medium between nodes, regardless of physical cable layout."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Hub Crossover Behavior",
                        "content": {
                            "question": "If 10 computers are physically wired in a star to an unmanaged network hub, why is its logical topology considered a bus?",
                            "options": [
                                "Because the hub physically rolls back and forth along the floor",
                                "Because the hub broadcasts incoming signals out of all ports, forcing all nodes to share a single collision domain",
                                "Because it requires a 50-ohm terminator resistor at each computer's network card",
                                "Because data packets circulate continuously in a unidirectional circle"
                            ],
                            "answer": "Because the hub broadcasts incoming signals out of all ports, forcing all nodes to share a single collision domain",
                            "explanation": "An unmanaged hub cannot filter MAC addresses; it repeats incoming electrical bits across all connected ports simultaneously, creating a single shared logical bus collision domain."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Modifying Topologies",
                        "content": {
                            "question": "Which of the following modifications can change a network's logical topology from a bus to a star without re-running any physical wall cables?",
                            "options": [
                                "Replacing a central unmanaged hub with an intelligent network switch",
                                "Painting the Ethernet cables blue instead of gray",
                                "Increasing the screen resolution on all desktop monitors",
                                "Installing a larger hard disk drive in the file server"
                            ],
                            "answer": "Replacing a central unmanaged hub with an intelligent network switch",
                            "explanation": "Replacing a hub with a switch upgrades the network logic from a shared broadcast bus into dedicated point-to-point switched links (logical star) using the existing physical star cables."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: Token Ring MAU Architecture",
                        "content": {
                            "question": "In a classic IBM Token Ring network connected to a Multistation Access Unit (MAU), how are the physical and logical topologies classified?",
                            "options": [
                                "Physical Bus, Logical Star",
                                "Physical Star, Logical Ring",
                                "Physical Mesh, Logical Bus",
                                "Physical Tree, Logical Mesh"
                            ],
                            "answer": "Physical Star, Logical Ring",
                            "explanation": "Cables physically radiate from workstations to the central MAU (physical star), while the MAU internally routes data sequentially in a closed loop (logical ring)."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # UNIT 2: Bus, Star, Ring, Mesh, Tree, and Hybrid Topologies (Lesson 38)
        # -------------------------------------------------------------
        {
            "unit_order": 2,
            "unit_name": "Bus, Star, Ring, Mesh, Tree, and Hybrid Topologies",
            "unit_description": "Comprehensive structural analysis of the five core network topologies: signal mechanics, termination physics, token-passing protocols, full mesh link calculations, tree hierarchies, and comparative tradeoff matrices.",
            "lesson_title": "Lesson 38: Bus, Star, Ring, Mesh, and Related Topologies",
            "pages": [
                # Page 1: The Five Core Topologies Overview
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Structural Mechanics of Core Network Topologies",
                        "content": {
                            "goal": "Explain the physical architecture, operational principles, single-point-of-failure vulnerabilities, and advantages of Bus, Star, Ring, Mesh, Tree, and Hybrid network topologies."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Architectural Overview of the Five Classic Shapes",
                        "content": {
                            "markdown": """### **The Five Core Topologies**

#### **1. Bus Topology**
- **Structure**: All nodes attach via short drop cables to a single continuous central coaxial or twisted-pair cable called the **backbone**.
- **Terminator Physics**: At both physical ends of the backbone cable, a hardware resistor (typically 50-ohm) called a **terminator** must be installed. The terminator absorbs electrical energy when signals reach the end of the wire, preventing **signal reflection** (signal echo) that would collide with and corrupt subsequent transmissions.
- **Tradeoffs**: Extremely cheap and minimal cabling, but the central backbone is a catastrophic **single point of failure** (a single cable cut halts the entire network).

#### **2. Star Topology**
- **Structure**: Every node has a dedicated, point-to-point cable connecting directly to a central multiport device, typically a **network switch**.
- **Isolation Principle**: If one workstation's cable is severed, only that single workstation loses connectivity; all other nodes continue communicating at full speed.
- **Tradeoffs**: Highly reliable, easy to troubleshoot and expand, but requires more cabling, and the central switch is a single point of failure.

#### **3. Ring Topology**
- **Structure**: Each node connects to exactly two neighboring nodes, forming a closed circular loop.
- **Token Passing**: A unique 3-byte control frame called the **token** circulates continuously. Only the device holding the token is permitted to transmit data, eliminating packet collisions completely.
- **Tradeoffs**: Deterministic performance under heavy loads, but a single broken link or powered-down node breaks the ring loop and shuts down all communication.

#### **4. Full Mesh Topology**
- **Structure**: Every single node has a direct, dedicated physical communication link to every other node in the network.
- **Tradeoffs**: Maximum possible fault tolerance and zero contention, but astronomical cabling costs and port requirements.

#### **5. Tree & Hybrid Topologies**
- **Tree Topology**: Multiple star-network clusters connected along a central backbone trunk cable (hierarchical star-bus).
- **Hybrid Topology**: An engineered combination of two or more distinct topologies (e.g., Star-Ring or Star-Mesh) tailored to organizational needs."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "The Five Fundamental Network Topologies",
                        "content": {
                            "svg_content": SVG_FIVE_TOPOLOGIES,
                            "caption": "Figure 11.3: Architectural layout schematics for Bus, Star, Ring, Full Mesh, and Tree/Hybrid network topologies illustrating node interconnections and single points of failure."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Topology Architectural Tradeoffs",
                        "content": {
                            "text": "Bus offers lowest cost but zero fault tolerance; Star provides isolated fault domains and is the modern LAN standard; Ring provides deterministic token passing; Mesh delivers maximum redundancy at extreme cost; Tree enables multi-level hierarchical campus expansion."
                        }
                    }
                ],

                # Page 2: Mesh Mathematics & Comparative Tradeoffs Matrix
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Mathematical Modeling of Mesh Topology",
                        "content": {
                            "goal": "Calculate the exact number of physical duplex links and hardware interface ports required for any N-node Full Mesh network using the formula L = N(N-1)/2, and evaluate scalability constraints."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Mathematics of Full Mesh & The Tradeoff Matrix",
                        "content": {
                            "markdown": """### **The Full Mesh Mathematical Formula**
To connect $N$ nodes in a **Full Mesh** topology, the number of required physical duplex links ($L$) is calculated as:

$$L = \\frac{N(N - 1)}{2}$$

Furthermore:
- **Physical Ports per Node**: Every individual node must possess exactly $(N - 1)$ dedicated network interface ports.
- **Total Interface Ports in Network**: $N \\times (N - 1)$.
- **Quadratic Growth**: The cabling requirement grows at $O(N^2)$, making full mesh impractical for general office LANs with dozens of computers.

---

### **Comprehensive Topology Tradeoffs Matrix**

| Topology | Installation Cost | Cable Volume | Fault Tolerance | Scalability | Troubleshooting | Primary Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Bus** | Very Low | Minimal | **None** (Backbone cut kills all) | Poor | Very Difficult | Legacy industrial sensors, temporary test benches. |
| **Star** | Moderate | Moderate/High | **High** (Cable break isolated to 1 node) | **Excellent** | Very Easy | Modern standard LANs (schools, offices, homes). |
| **Ring** | Moderate | Moderate | **None** (Unless dual-ring counter-rotating) | Moderate | Difficult | Token-passing industrial automation, FDDI backbones. |
| **Mesh (Full)** | **Extremely High** | **Extreme** | **Maximum** (Multiple redundant paths) | Poor | Complex | Mission-critical server centers, military, air traffic control. |
| **Tree** | High | High | **Moderate** (Trunk cut isolates branches) | **High** | Moderate | Multi-floor school campuses, large corporate headquarters. |"""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Full Mesh Mathematical Modeling & Scalability Matrix",
                        "content": {
                            "svg_content": SVG_MESH_MATH_FORMULA,
                            "caption": "Figure 11.4: Mathematical formula breakdown and comparative scalability matrix illustrating how Full Mesh cabling and port counts expand rapidly compared to Star topology."
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "Network Topologies Explained: Bus, Star, Ring, Mesh, Tree",
                        "content": {
                            "youtube_id": "zbqrNg4C98U",
                            "description": "A comprehensive deep dive into the physical configurations, pros, cons, and data transmission methods across all major network topologies."
                        }
                    }
                ],

                # Page 3: Step-by-Step Worked Math Problem & Hospital Audit
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Math Problem: High-Security Data Center Full Mesh",
                        "content": {
                            "markdown": """### **Worked Problem 1: Full Mesh Cable & Port Calculation**

#### **Scenario**
A commercial bank is designing a high-security disaster recovery data center with **8 core database servers** arranged in a Full Mesh topology to guarantee 100% uptime.

#### **Step-by-Step Calculation**
1. **Identify Node Count**: $N = 8$.
2. **Calculate Required Physical Duplex Cables ($L$)**:
   $$L = \\frac{N(N - 1)}{2} = \\frac{8 \\times (8 - 1)}{2} = \\frac{8 \\times 7}{2} = \\frac{56}{2} = \\mathbf{28\\text{ cables}}$$
3. **Calculate Required NIC Ports per Server**:
   $$\\text{Ports per Server} = N - 1 = 8 - 1 = \\mathbf{7\\text{ ports}}$$
4. **Expansion Analysis (Expanding from 8 to 12 Servers)**:
   - For $N = 12$:
     $$L_{12} = \\frac{12 \\times 11}{2} = \\frac{132}{2} = 66\\text{ cables}$$
   - **Additional Cables to Purchase**: $66 - 28 = \\mathbf{38\\text{ additional cables}}$ to add just 4 servers!
   - **New Ports Required per Server**: $(12 - 1) = \\mathbf{11\\text{ ports}}$.

---

### **Worked Scenario 2: The Hospital Network Audit**

#### **Problem**
A regional hospital connects 15 vital patient-monitoring terminals across three wards using an old coaxial **Bus Topology**. During air conditioning repairs, a technician accidentally cuts the coaxial cable in Ward B.
- **Immediate Consequence**: The bus is split into two unterminated segments. Signal reflections immediately corrupt all data transmissions, causing **every monitoring terminal in Ward A, B, and C to go offline simultaneously**.
- **Architectural Solution**: Upgrade immediately to a **Star Topology** with a centralized medical-grade switch. If a cable to a single bed in Ward B is damaged, only that single bed is affected; the remaining 14 monitors remain 100% operational."""
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Data Center High-Density Cabling Rack",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Data_Center_Cable_Management.jpg/800px-Data_Center_Cable_Management.jpg",
                            "caption": "Figure 11.5: High-density structured cabling in an enterprise data center demonstrating the extensive physical cable management required for high-redundancy network topologies.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (Lesson 38)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Bus Topology Terminator Function",
                        "content": {
                            "question": "What is the critical function of a terminator resistor installed at both ends of a bus topology cable?",
                            "options": [
                                "To boost the electrical voltage for long-distance transmissions",
                                "To absorb electrical signal energy and prevent signal reflection collisions",
                                "To assign dynamic IP addresses to newly attached workstations",
                                "To convert analog audio signals into digital packets"
                            ],
                            "answer": "To absorb electrical signal energy and prevent signal reflection collisions",
                            "explanation": "Terminators absorb the electrical signal when it reaches the physical end of the backbone wire, preventing it from bouncing back (echoing) and corrupting active transmissions."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Star Topology Fault Isolation",
                        "content": {
                            "question": "If a single workstation's Cat6 cable is accidentally cut in a physical star network, what happens to the remaining computers?",
                            "options": [
                                "The entire network immediately shuts down",
                                "All other computers continue communicating normally without interruption",
                                "The central switch automatically shuts off its internal power supply",
                                "The network immediately degrades into an unmanaged bus"
                            ],
                            "answer": "All other computers continue communicating normally without interruption",
                            "explanation": "Because each node in a star topology has a dedicated point-to-point link to the central switch, a severed cable isolates only that single node."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Full Mesh Link Calculation",
                        "content": {
                            "question": "How many physical duplex communication links are required to connect 6 servers in a Full Mesh topology?",
                            "options": [
                                "6 links",
                                "12 links",
                                "15 links",
                                "30 links"
                            ],
                            "answer": "15 links",
                            "explanation": "Using the formula L = N(N - 1) / 2: for N = 6, L = (6 * 5) / 2 = 30 / 2 = 15 physical links."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: Tree Topology Architecture",
                        "content": {
                            "question": "How is a Tree network topology structurally constructed?",
                            "options": [
                                "By connecting individual computers directly to one another in a closed circular loop",
                                "By connecting multiple star-network switch clusters to a central shared backbone trunk line",
                                "By wiring every computer directly to every other computer with dedicated cables",
                                "By broadcasting data exclusively via omnidirectional wireless radio waves"
                            ],
                            "answer": "By connecting multiple star-network switch clusters to a central shared backbone trunk line",
                            "explanation": "A Tree topology is a hierarchical combination where multiple star-configured switch clusters branch off a main central backbone trunk cable."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # UNIT 3: Selecting an Appropriate Network Topology (Lesson 39)
        # -------------------------------------------------------------
        {
            "unit_order": 3,
            "unit_name": "Selecting an Appropriate Network Topology",
            "unit_description": "Systematic architectural methodology for evaluating and selecting network topologies: analyzing organizational constraints (budget, fault tolerance, scalability, geography, expertise), decision flowcharts, and Kenyan case studies.",
            "lesson_title": "Lesson 39: Selecting an Appropriate Network Topology",
            "pages": [
                # Page 1: Evaluation Framework & Six Core Criteria
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Multi-Factor Topology Selection Methodology",
                        "content": {
                            "goal": "Evaluate the six core criteria for selecting an optimal network topology (installation cost, fault tolerance, scalability, physical building geography, traffic volume, and technical expertise) and apply them to realistic organizational scenarios."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The 'Transport Fleet' Analogy & Selection Criteria",
                        "content": {
                            "markdown": """### **The 'Transport Fleet' Analogy**
Imagine launching a delivery business. Should you buy a fleet of massive cargo trucks, agile motorbikes, or passenger vans? 
- If you are delivering hot pizzas in city traffic, a 20-ton semi-truck is too slow, expensive, and impossible to park.
- If you are hauling 50 tons of structural steel, a motorbike is physically useless.

Choosing a network topology follows the exact same logic. **There is no single 'best' topology.** An IT architect must systematically balance competing organizational constraints:

### **The Six Core Selection Criteria**

1. **Financial Budget (Installation & Maintenance Cost)**
   - *Hardware & Cable Capex*: Purchasing cables, patch panels, switches, and multi-port NICs.
   - *Opex*: Replacing broken lines and paying specialized network administrators.
   - *Rule*: Bus is cheapest; Star is moderate; Full Mesh is prohibitively expensive.

2. **Reliability & Uptime Targets (Fault Tolerance)**
   - Can the organization survive 30 minutes of network downtime? A school lab can, but a bank transaction server or hospital ICU cannot.

3. **Scalability (Future Growth Potential)**
   - How easy is it to add 15 new computers next term? Star allows simple plug-and-play into spare switch ports; Bus requires cutting the main backbone.

4. **Physical Building Geography & Architecture**
   - Are devices located in a single compact room, across multiple floors, or in detached campus buildings?
   - *Single room*: Star. *Multi-floor*: Tree/Hybrid.

5. **Bandwidth Demands & Data Traffic Volume**
   - High-throughput video streaming and database clustering require dedicated switched links (Star/Mesh) to eliminate packet collisions.

6. **Available Technical Expertise (Maintainability)**
   - Complex topologies (Mesh, Hybrid) require skilled network engineers to configure and maintain. Small primary schools benefit from simple, automated Star setups."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Topology Selection Decision Framework Flowchart",
                        "content": {
                            "svg_content": SVG_TOPOLOGY_SELECTION_FLOWCHART,
                            "caption": "Figure 11.6: Decision tree flowchart guiding network engineers from business constraints (uptime criticality, physical layout, budget) to the recommended physical topology."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Context-Driven Topology Selection",
                        "content": {
                            "text": "Topology selection is an engineering optimization problem: match client constraints (budget, geography, required uptime) to the structural advantages of Star (standard LAN), Tree (multi-floor campus), or Mesh (zero-downtime server cores)."
                        }
                    }
                ],

                # Page 2: Real-World Case Studies Matrix
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Applying Selection Criteria to Kenyan Organizational Scenarios",
                        "content": {
                            "goal": "Analyze real-world organizational case studies (rural health clinic, national banking center, multi-story school, agri-fair) and formulate justified topology recommendations."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Case Studies: Matching Topologies to Real-World Needs",
                        "content": {
                            "markdown": """### **Case Study Matrix: Real-World Scenarios in Kenya**

| Scenario | Operational Constraints | Recommended Topology | Technical Justification |
| :--- | :--- | :--- | :--- |
| **1. Rural Health Clinic (Kitui)** | • Low initial budget<br>• No on-site IT specialist<br>• 6 computers for patient records | **Star Topology** | Highly reliable for daily outpatient services. If one clinic PC or cable fails, others stay operational. Standard 8-port switch is plug-and-play with zero configuration needed. |
| **2. National Bank Data Center (Nairobi)** | • Zero-downtime mission critical<br>• Millions of KES in financial transactions per minute<br>• High budget | **Full Mesh (or Partial Mesh Core)** | Guarantees multiple redundant physical routes between core database servers. If a fiber link is severed, traffic reroutes automatically with 0% packet loss. |
| **3. Four-Story Secondary School (Nakuru)** | • Admin on Ground Floor<br>• Computer Labs on 2nd and 3rd Floors<br>• 120 total computers | **Tree / Hierarchical Star Topology** | Each floor operates an independent Star switch cluster. All floor switches link back to a high-capacity fiber backbone trunk in the server room, isolating local traffic. |
| **4. Mombasa Agricultural Trade Fair Tent** | • 5 registration computers<br>• 3-day temporary event<br>• Fast setup and teardown | **WLAN / Simple Star** | Eliminates physical floor cable trip hazards in high-foot-traffic exhibition tents and allows rapid equipment teardown after the event. |"""
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "School Computer Laboratory Star Network Setup",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Computer_lab_at_a_high_school.jpg/800px-Computer_lab_at_a_high_school.jpg",
                            "caption": "Figure 11.7: A secondary school computer laboratory featuring workstations connected via structured star cabling to provide isolated fault domains and easy maintenance.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How to Choose the Right Network Topology for Your Business",
                        "content": {
                            "youtube_id": "921LzG_0350",
                            "description": "An architectural walkthrough explaining the decision-making process for designing small business and enterprise network layouts."
                        }
                    }
                ],

                # Page 3: Architectural Design Problem: The Tea Export Warehouse
                [
                    {
                        "type": "worked_example",
                        "title": "Architectural Design Challenge: Mombasa Tea Export Warehouse",
                        "content": {
                            "markdown": """### **Design Challenge: The Mombasa Tea Export Warehouse**

#### **Client Requirements**
An agricultural export warehouse in Mombasa requires a new computer network:
1. **Administrative Office**: 12 desktop computers and 2 shared label printers.
2. **Shipping & Weighbridge Dock**: 3 ruggedized terminal PCs located 150 meters away, where forklifts and heavy trucks operate daily.
3. **Quality Testing Lab**: 4 computers located on the mezzanine floor.
4. **Critical Reliability Rule**: Administrative billing computers must never lose connection if heavy machinery accidentally severs a cable at the shipping dock.

---

#### **Proposed Architectural Solution: Hierarchical Tree / Hybrid Star**
- **Core Server Room (Admin Office)**: Install a 24-Port Gigabit Core Switch. Wire the 12 admin PCs and 2 printers in a dedicated **Local Star**.
- **Shipping Dock Sub-Cluster**: Install an industrial 8-port switch at the dock. Connect the 3 dock terminals to this switch in a local star.
- **Inter-Building Trunk**: Run an armored, shielded fiber-optic cable in protective steel conduit underground from the Main Switch to the Shipping Dock Switch.
- **Testing Lab Sub-Cluster**: Connect the 4 lab computers to a dedicated 8-port switch on the mezzanine, linked via a Cat6 vertical trunk.

#### **Technical Evaluation & Justification**
- **Fault Isolation**: If a forklift crushes a cable at the shipping dock, only that specific terminal (or at worst, only the dock switch) goes offline. The administrative office and testing lab continue running without interruption.
- **Distance Compliance**: The 150-meter run exceeds standard copper Cat6 limits (100m); using a fiber-optic trunk guarantees zero signal degradation.
- **Scalability**: New scales or barcode scanners can be added to the dock switch without running new cables all the way back to the main office."""
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (Lesson 39)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Financial Institution Priority",
                        "content": {
                            "question": "Which criterion is the single most critical consideration when selecting a network topology for a commercial bank's primary core transaction servers?",
                            "options": [
                                "Minimizing total initial cable purchase costs",
                                "Maximum fault tolerance and automatic link redundancy",
                                "The aesthetic color scheme of the server cabinets",
                                "Ensuring all computers share a single collision domain"
                            ],
                            "answer": "Maximum fault tolerance and automatic link redundancy",
                            "explanation": "Financial transaction servers cannot tolerate downtime; Full or Partial Mesh provides multiple redundant physical paths so transactions never drop even during fiber cuts."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Multi-Story School Topology",
                        "content": {
                            "question": "Why is a Tree (hierarchical star) topology recommended for a four-story school building rather than a single massive bus topology?",
                            "options": [
                                "Tree topology allows each floor to operate its own star switch cluster connected via a central vertical backbone trunk",
                                "Tree topology requires no physical switches or routers",
                                "Bus topology is too fast for student computers to process",
                                "Tree topology uses circulating token frames to eliminate all cabling"
                            ],
                            "answer": "Tree topology allows each floor to operate its own star switch cluster connected via a central vertical backbone trunk",
                            "explanation": "A Tree topology groups each floor into a manageable star cluster connected to a vertical backbone, localizing network traffic and isolating faults."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Rural Clinic Architecture",
                        "content": {
                            "question": "Why would a small rural clinic with 5 computers and no on-site IT specialist select a Star topology over a Full Mesh topology?",
                            "options": [
                                "Full Mesh is too complex and expensive to install and maintain, whereas Star is simple, cost-effective, and plug-and-play",
                                "Star topology provides faster long-distance satellite internet",
                                "Full Mesh cannot connect more than 2 computers",
                                "Star topology does not require any network cables"
                            ],
                            "answer": "Full Mesh is too complex and expensive to install and maintain, whereas Star is simple, cost-effective, and plug-and-play",
                            "explanation": "A Full Mesh topology requires specialized multi-port cards and complex routing, which is unnecessarily expensive and difficult to maintain for a simple 5-PC rural clinic."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: Expansion Tradeoff",
                        "content": {
                            "question": "What is the primary operational disadvantage of expanding an existing Bus network by adding 10 new computers?",
                            "options": [
                                "The central switch will overheat immediately",
                                "The main backbone must be spliced/cut, and increased traffic causes frequent packet collisions that degrade overall performance",
                                "The network will automatically switch to token passing",
                                "The physical cables will convert from copper into fiber"
                            ],
                            "answer": "The main backbone must be spliced/cut, and increased traffic causes frequent packet collisions that degrade overall performance",
                            "explanation": "Adding devices to a bus requires altering the main backbone cable and increases contention across the shared bandwidth, leading to severe performance degradation."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # UNIT 4: Creating a Physical Network Topology (Lesson 40)
        # -------------------------------------------------------------
        {
            "unit_order": 4,
            "unit_name": "Creating a Physical Network Topology",
            "unit_description": "Practical hands-on methodology for building a physical star network: laboratory safety rules, cable management and trunking, RJ-45 mechanical latching, power-on sequences, port LED diagnostics, and CLI ping verification.",
            "lesson_title": "Lesson 40: Creating a Physical Network Topology",
            "pages": [
                # Page 1: Lab Safety & Structured Star Assembly Workflow
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Practical Star Network Assembly & Safety Protocol",
                        "content": {
                            "goal": "Execute the end-to-end practical assembly of a physical star network following laboratory safety standards, structured cable routing, mechanical connection verification, and port LED link diagnostics."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Laboratory Safety & Structured Cabling Rules",
                        "content": {
                            "markdown": """### **Laboratory Safety & Cable Management Protocols**
Building a physical computer network is a precision engineering task. Careless cable installation creates dangerous trip hazards, damages expensive ports, and introduces electromagnetic signal corruption.

#### **The Four Golden Lab Safety Rules**
1. **Power Isolation Before Cabling**: Always turn off and unplug power cords from computers and switches before running or inserting network cabling.
2. **Bend Radius & Tension Limits**: Never pull Cat6 copper cables with excessive force or bend them at sharp 90-degree angles. Kinking fractures internal copper pairs, causing signal loss and crosstalk.
3. **Structured Cable Routing (No Floor Traps)**: Route all Ethernet cables neatly through protective PVC wall trunking, under-desk cable trays, or floor raceways. Never leave cables exposed in walking aisles.
4. **Velcro Bundling & Dual-End Labeling**: Group cables using velcro ties (avoid tight zip-ties that pinch wires). Label both ends of every cable (e.g., `PC-03 -> Switch Port 3`) for rapid troubleshooting."""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Step-by-Step Star Network Assembly & Testing Workflow",
                        "content": {
                            "svg_content": SVG_STAR_CABLING_WORKFLOW,
                            "caption": "Figure 11.8: Structured procedural workflow for assembling a 6-node physical star network: blueprint planning, PVC wall trunking, RJ-45 mechanical locking, power-up sequence, and LED link verification."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Structured Network Installation",
                        "content": {
                            "text": "Professional network assembly requires structured planning, protective PVC trunking, dual-end cable labeling, verifying mechanical RJ-45 click-latches, and confirming hardware carrier synchronization via solid green port LEDs."
                        }
                    }
                ],

                # Page 2: Step-by-Step Lab Guide: Building a 6-Node Star LAN
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Step-by-Step Physical & Logical Verification",
                        "content": {
                            "goal": "Demonstrate the complete physical assembly sequence for a small office/lab star network and perform two-stage diagnostic verification (hardware LED check and software ping test)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Step-by-Step Assembly & Verification Procedure",
                        "content": {
                            "markdown": """### **Laboratory Guide: Building a 6-Node Physical Star LAN**

#### **Phase 1: Hardware Preparation & Core Placement**
1. **Inventory Audit**: Assemble 5 Workstations (DTEs), 1 Network Printer, 1 8-Port Fast Ethernet/Gigabit Switch, and 6 tested Cat6 UTP patch cords.
2. **Core Placement**: Secure the switch in a central, well-ventilated equipment rack near a surge-protected AC power outlet.

#### **Phase 2: Structured Cable Laying**
3. **Measure & Lay**: Run individual Cat6 cables from each workstation back to the switch rack inside wall trunking. Leave approximately 15 cm of service slack at each end to eliminate tension on RJ-45 ports.

#### **Phase 3: Making the Connections (The Mechanical Lock)**
4. **Workstation Termination**: Insert the RJ-45 connector firmly into the workstation onboard NIC port until you hear a distinct **'click'** sound (indicating the plastic spring clip is locked).
5. **Switch Termination**: Insert the opposite end into the designated switch port (Ports 1–6) according to your Port Mapping Table.

#### **Phase 4: Power-Up & Physical Link LED Diagnostics**
6. **Power Sequence**: Power on the network switch first. Verify its master power LED is solid green. Then power on the workstations and printer.
7. **Inspect Port LEDs**:
   - **Solid Green LED**: Physical Layer 1 link established at 1 Gbps.
   - **Solid Amber LED**: Physical link established at lower speed (100 Mbps).
   - **Flashing Green/Amber LED**: Active data frame transmission/reception.
   - **Unlit / Dark LED**: Physical connection failure (bad cable, unseated RJ-45 plug, or unpowered device).

#### **Phase 5: Software Connectivity Verification (CLI Ping)**
8. Open the Command-Line Interface (CLI) on PC 1 (`192.168.1.10`) and send ICMP echo requests to PC 2 (`192.168.1.20`):
   ```bash
   ping 192.168.1.20
   ```
   A response of `4 packets transmitted, 4 received, 0% packet loss` confirms that both the physical star wiring and logical Layer 2/3 delivery are operational!"""
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "RJ-45 Modular Plug and Ethernet Port Interface",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Ethernet_8P8C_RJ45_modular_connector.jpg/800px-Ethernet_8P8C_RJ45_modular_connector.jpg",
                            "caption": "Figure 11.9: Close-up view of an 8P8C (RJ-45) modular connector with its retention spring latch that provides the critical mechanical lock inside Ethernet ports.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How to Cable a Small Office Network Step by Step",
                        "content": {
                            "youtube_id": "bga8iYnO6rM",
                            "description": "A hands-on demonstration of running Ethernet cables through trunking, clicking into switch ports, and testing link lights."
                        }
                    }
                ],

                # Page 3: Troubleshooting Practical Scenario: The Silent Classroom
                [
                    {
                        "type": "worked_example",
                        "title": "Diagnostic Scenario: The Silent Classroom",
                        "content": {
                            "markdown": """### **Diagnostic Scenario: The Silent Classroom**

#### **Problem Description**
A student sets up a 5-computer physical star network connected to an 8-port switch. Upon powering on the equipment:
- Computers 1, 2, 3, and 4 show solid green link lights and can successfully ping one another.
- Computer 5's switch port LED and NIC LED remain completely **dark (unlit)**, and the operating system reports **'Network Cable Unplugged'**.

---

#### **Step-by-Step Troubleshooting Checklist**

1. **Step 1: Check the Mechanical Latch**
   - *Action*: Inspect the RJ-45 plug at Computer 5's NIC and at Switch Port 5.
   - *Check*: Did the retention clip break off? Push the plug firmly until the plastic latch clicks into place.

2. **Step 2: Port Swap Isolation Test**
   - *Action*: Move the cable from Switch Port 5 into a known-working switch port (e.g., Port 7).
   - *Result A*: If Port 7 lights up green, Switch Port 5 has a hardware failure.
   - *Result B*: If Port 7 remains dark, the fault is in the cable or Computer 5's NIC.

3. **Step 3: Cable Swap Test**
   - *Action*: Replace Computer 5's patch cord with a known-working cable from Computer 1.
   - *Result A*: If Computer 5 now connects, the original cable has internal wire fractures or bad crimping.
   - *Result B*: If Computer 5 remains dark with a known-good cable, Computer 5's onboard NIC hardware or driver is defective."""
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (Lesson 40)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Mechanical RJ-45 Verification",
                        "content": {
                            "question": "When connecting a Cat6 Ethernet cable into a computer's network interface card, what indicates that a secure physical connection has been made?",
                            "options": [
                                "The computer immediately emits a loud continuous beep",
                                "You feel and hear a distinct mechanical 'click' as the plastic spring clip locks into the port",
                                "The computer screen automatically resets to factory resolution",
                                "The cable begins to heat up rapidly"
                            ],
                            "answer": "You feel and hear a distinct mechanical 'click' as the plastic spring clip locks into the port",
                            "explanation": "The RJ-45 8P8C connector features a flexible plastic retention clip that clicks firmly into the jack recess, preventing accidental disconnects."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Dark Switch Port LED Meaning",
                        "content": {
                            "question": "What does an unlit (completely dark) LED light on a network switch port signify after connecting a workstation?",
                            "options": [
                                "The computer is transmitting at maximum gigabit speed",
                                "There is a physical layer connection failure (e.g., unplugged cable, broken wire, or unpowered device)",
                                "The switch has enabled firewall token filtering",
                                "The workstation is waiting for a DNS lookup"
                            ],
                            "answer": "There is a physical layer connection failure (e.g., unplugged cable, broken wire, or unpowered device)",
                            "explanation": "A dark LED indicates that no electrical or optical carrier signal is detected between the two network interfaces (Layer 1 failure)."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Cable Management Safety",
                        "content": {
                            "question": "Why should network cables never be run loosely across classroom walkways and footpaths?",
                            "options": [
                                "Because student footsteps will compress digital packets into smaller bytes",
                                "Because loose cables create trip-and-fall hazards for people and risk tearing physical ports out of computers",
                                "Because sunlight will degrade the IP addresses inside copper cables",
                                "Because computers will automatically change their operating system"
                            ],
                            "answer": "Because loose cables create trip-and-fall hazards for people and risk tearing physical ports out of computers",
                            "explanation": "Exposed floor cables are severe safety hazards that can injure people and cause physical hardware damage when snagged."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: Software Connectivity Test",
                        "content": {
                            "question": "Which command-line utility is used to verify that a newly assembled physical topology is successfully transmitting logical packets to a neighboring node?",
                            "options": [
                                "format C:",
                                "ping <IP Address>",
                                "delete system32",
                                "chkdsk /f"
                            ],
                            "answer": "ping <IP Address>",
                            "explanation": "The ping utility sends ICMP Echo Request packets to a target IP address to verify Layer 3 end-to-end network reachability and measure round-trip latency."
                        }
                    }
                ]
            ]
        },

        # -------------------------------------------------------------
        # UNIT 5: Appreciation and Evaluation of Network Topologies (Lesson 41)
        # -------------------------------------------------------------
        {
            "unit_order": 5,
            "unit_name": "Appreciation and Evaluation of Network Topologies",
            "unit_description": "Comprehensive evaluative synthesis of network architecture: grading operational metrics (fault tolerance, cost efficiency, scalability, maintainability), conducting peer design reviews, and analyzing complex Kenyan rural and eco-lodge infrastructure case studies.",
            "lesson_title": "Lesson 41: Appreciation and Evaluation of Network Topologies",
            "pages": [
                # Page 1: The Evaluative Mindset & Core Metrics
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Evaluative Metrics and Design Tradeoff Synthesis",
                        "content": {
                            "goal": "Evaluate network architecture designs against core operational performance metrics (fault tolerance, cost-to-performance ratio, ease of maintenance, scalability) and conduct systematic peer design audits."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Evaluative Mindset & Architectural Tradeoffs",
                        "content": {
                            "markdown": """### **The Evaluative Mindset**
An excellent computer scientist does not simply choose the newest, most complex, or most expensive technology. They evaluate constraints, assess risks, and design the most balanced, cost-effective, and resilient solution for the specific client environment.

If a local fruit merchant with 3 computers asks for a network, designing an expensive Full Mesh fiber network with 10-gigabit switches is an engineering failure—it costs more than their annual revenue. Conversely, installing a single bus coaxial cable in a regional trauma hospital is equally negligent.

---

### **The Five Core Evaluative Metrics**

1. **Fault Tolerance (System Resilience)**
   - The ability of the network to maintain uninterrupted service when a cable, switch, or node experiences hardware failure.
   - *High*: Mesh (multiple dynamic redundant paths). *Low*: Bus/Ring (single failure halts network).

2. **Cost-to-Performance Efficiency**
   - The ratio of delivered network throughput and uptime to total financial expenditure (Capex + Opex).
   - *Optimal*: Switched Star (inexpensive switches, high 1 Gbps dedicated bandwidth per port).

3. **Scalability (Expansion Flexibility)**
   - The ease with which additional nodes, rooms, or wings can be connected without requiring architectural redesign or disruptive system downtime.

4. **Maintainability & Administrative Simplicity**
   - How rapidly can a local technician isolate a physical fault and replace a damaged component?
   - *Star*: Excellent (switch LEDs pinpoint exact failed port). *Bus*: Poor (requires inspecting entire ceiling cable).

5. **Environmental & Physical Durability**
   - How well does the cabling and hardware withstand environmental hazards (rodents, wildlife, high humidity, dust, and electrical lightning surges)?"""
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "Comparative Topology Evaluation: Safari Eco-Lodge Redesign",
                        "content": {
                            "svg_content": SVG_ECO_LODGE_TOPOLOGY_EVALUATION,
                            "caption": "Figure 11.10: Architectural audit matrix comparing a fragile legacy ring topology against an evaluated central star topology with underground armored conduit for a luxury safari eco-lodge."
                        }
                    },
                    {
                        "type": "key_takeaway",
                        "title": "Key Takeaway: Engineering Evaluation Principles",
                        "content": {
                            "text": "True engineering excellence lies in balancing uptime requirements against real-world economic and environmental constraints. Star topology provides the optimal balance of fault isolation, maintainability, and cost efficiency for modern local networks."
                        }
                    }
                ],

                # Page 2: Peer Review Rubric & Audit Framework
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Goal: Conducting Professional Network Design Audits",
                        "content": {
                            "goal": "Apply a structured peer review rubric to audit network diagrams, identify single points of failure, verify structured cabling safety, and formulate corrective recommendations."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Network Design Peer Review Rubric",
                        "content": {
                            "markdown": """### **The Peer Review Audit Rubric**
When evaluating a colleague's network architecture proposal, use this systematic 4-pillar audit rubric:

| Evaluation Pillar | Score 3 (Exemplary) | Score 2 (Satisfactory) | Score 1 (Needs Revision) |
| :--- | :--- | :--- | :--- |
| **1. Fault Isolation** | Dedicated point-to-point links; single cable break has zero impact on other nodes. | Most nodes isolated; some shared trunk dependencies without failover. | Single point of failure (e.g., unsegmented bus/ring) halts entire network. |
| **2. Cabling & Safety** | Structured routing in PVC trunking; labeled at both ends; no floor hazards; service slack included. | Cables routed along walls but lack labels or service slack. | Loose cables exposed across walkways; sharp bends exceeding copper bend radius. |
| **3. Budget & Resource Fit** | Uses standard, easily replaceable hardware matching client financial and technical capacity. | Slightly over-budget or uses proprietary connectors that are hard to source locally. | Prohibitively expensive hardware or inappropriate overkill (e.g., Full Mesh for 5 PCs). |
| **4. Maintainability** | Front-panel LED diagnostics; clear port map documentation; plug-and-play replacement. | Basic port documentation; requires some manual cable tracing during faults. | No documentation; hidden unmanaged splices inside ceiling spaces. |"""
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Network Architecture Documentation and Port Map",
                        "content": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Network_diagram_sample.png/800px-Network_diagram_sample.png",
                            "caption": "Figure 11.11: Professional network architecture documentation diagram detailing hardware nodes, IP subnets, switch port assignments, and physical link pathways.",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0"
                        }
                    },
                    {
                        "type": "suggested_video",
                        "title": "How to Review and Audit a Network Diagram Layout",
                        "content": {
                            "youtube_id": "9p9p_yG5c0Y",
                            "description": "A practical guide to auditing network topology diagrams, identifying architectural bottlenecks, and evaluating fault tolerance."
                        }
                    }
                ],

                # Page 3: Case Study Evaluation: Mount Kenya Agricultural Cooperative & Mara Eco-Lodge
                [
                    {
                        "type": "worked_example",
                        "title": "Comprehensive Evaluative Case Studies",
                        "content": {
                            "markdown": """### **Case Study 1: Mount Kenya Agricultural Cooperative**

#### **Background & Challenge**
An agricultural cooperative in Nyeri unites 150 smallholder farmers. They operate a central administrative office, a grain silo 100 meters away, and a tool distribution depot 50 meters away. They need to share real-time inventory and grain weight data. High winds frequently blow tree branches down onto overhead cables.

#### **Evaluation of Three Competing Designs**
- **Design A (The Bus)**: Run a single long cable from the office, through the grain silo, to the tool depot.
  - *Verdict*: **REJECTED**. A single fallen branch snapping the cable between the office and silo isolates the entire network and halts all operations.
- **Design B (The Full Mesh)**: Run multiple redundant cables directly interconnecting every building to every other building.
  - *Verdict*: **REJECTED**. Prohibitively expensive and unnecessarily complex for a 3-building rural co-op with basic IT needs.
- **Design C (Central Star with Underground Conduit)**: Install a central switch in the office. Run direct, shielded cables through underground PVC pipes to the silo and depot.
  - *Verdict*: **APPROVED**. Underground pipes protect cables from falling branches. If the silo cable fails, the tool depot stays online. Matches their modest budget and is simple for a local technician to maintain.

---

### **Case Study 2: Maasai Mara Safari Eco-Lodge**

#### **Background & The Incident**
A safari eco-lodge has 6 guest cottages arranged in a wide circle around a central dining lounge. The lodge previously used a physical **Ring Topology** where a single fiber cable daisy-chained sequentially from cottage to cottage.
During a storm, wildlife chewed through the cable between Cottage 3 and Cottage 4, breaking the token loop and **cutting off internet access for all 6 cottages**.

#### **Evaluated Redesign**
- Transform into a **Central Star Topology** anchored by a core switch in the main dining lodge.
- Lay direct, armored cables inside underground PVC conduit radiating outward to each individual cottage.
- **Outcome**: Wildlife damage to Cottage 3's cable leaves Cottages 1, 2, 4, 5, and 6 completely unaffected, and the switch port LED immediately identifies the broken link."""
                        }
                    }
                ],

                # Page 4: Formative Knowledge Checks (Lesson 41)
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 1: Definition of Fault Tolerance",
                        "content": {
                            "question": "In the context of evaluating network topology architecture, what does 'Fault Tolerance' mean?",
                            "options": [
                                "The speed at which a network technician can type command-line syntax",
                                "The capacity of a hard drive partition to store audit logs",
                                "The ability of a network to continue functioning properly when a cable, node, or port fails",
                                "The maximum power voltage an Ethernet switch can withstand during a storm"
                            ],
                            "answer": "The ability of a network to continue functioning properly when a cable, node, or port fails",
                            "explanation": "Fault tolerance measures a network's resilience—its capability to maintain continuous operation and data delivery despite component failures."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 2: Balanced Design Evaluation",
                        "content": {
                            "question": "Why is the 'best' network design not always the one with the most cables and most expensive equipment?",
                            "options": [
                                "Because expensive equipment always transmits data more slowly than cheap cables",
                                "Because effective network design must balance performance against real-world client budget, technical expertise, and maintenance constraints",
                                "Because modern computers cannot interface with high-end switches",
                                "Because mesh networks do not support TCP/IP protocols"
                            ],
                            "answer": "Because effective network design must balance performance against real-world client budget, technical expertise, and maintenance constraints",
                            "explanation": "Engineering design is an optimization problem; an ideal solution delivers required reliability and speed while remaining within the client's financial and operational capabilities."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 3: Mount Kenya Co-op Evaluation",
                        "content": {
                            "question": "Why did the Mount Kenya Agricultural Cooperative reject a Bus topology in favor of a Star topology with underground conduit?",
                            "options": [
                                "Bus topology does not support database applications",
                                "A single overhead branch fall would sever the bus backbone and bring down all 3 buildings simultaneously",
                                "Bus topology requires too many complex network switches",
                                "Star topology requires no physical cables"
                            ],
                            "answer": "A single overhead branch fall would sever the bus backbone and bring down all 3 buildings simultaneously",
                            "explanation": "In a bus topology, the backbone is a single point of failure; an environmental break disconnects the entire organization."
                        }
                    },
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Check 4: Maintainability of Star vs Ring",
                        "content": {
                            "question": "How does the maintainability of a Star topology compare to a legacy Ring topology when troubleshooting a broken connection?",
                            "options": [
                                "Star is much easier because the central switch port LEDs instantly identify the exact failed workstation line without affecting others",
                                "Ring is easier because the broken node illuminates a red laser beam across the ceiling",
                                "Both topologies require replacing all cables simultaneously",
                                "Star requires physically dismantling every workstation in the laboratory"
                            ],
                            "answer": "Star is much easier because the central switch port LEDs instantly identify the exact failed workstation line without affecting others",
                            "explanation": "In a star topology, dedicated port LEDs immediately pinpoint the faulty link, while a ring failure requires inspecting the entire circular loop."
                        }
                    }
                ]
            ]
        }
    ]

# =====================================================================
# INGESTION ENGINE
# =====================================================================

def ingest_grade10_topic11(replace: bool = True):
    print("=" * 80)
    print("STARTING VLEARN PRODUCTION INGESTION: CBC GRADE 10 CS — TOPIC 11")
    print("=" * 80)

    with transaction.atomic():
        curriculum = Curriculum.objects.get(id=5)
        grade = Grade.objects.get(id=5, level=10)
        subject = Subject.objects.get(id=38, grade=grade)

        print(f"[*] Target Curriculum: {curriculum.name} (ID: {curriculum.id})")
        print(f"[*] Target Grade:      {grade.name} (ID: {grade.id})")
        print(f"[*] Target Subject:    {subject.name} (ID: {subject.id})")

        topic, created = Topic.objects.get_or_create(
            subject=subject,
            order=11,
            defaults={
                "name": "Network Topologies",
                "description": "Comprehensive structural analysis of physical and logical network topologies: Bus, Star, Ring, Mesh, Tree, and Hybrid architectures, mathematical mesh link modeling, selection frameworks, structured star cabling installation, and diagnostic evaluation."
            }
        )

        if not created and replace:
            print(f"[*] Topic 11 already exists (ID: {topic.id}). Performing clean replacement of units and lessons...")
            topic.learning_units.all().delete()
            topic.lessons.all().delete()
            topic.name = "Network Topologies"
            topic.description = "Comprehensive structural analysis of physical and logical network topologies: Bus, Star, Ring, Mesh, Tree, and Hybrid architectures, mathematical mesh link modeling, selection frameworks, structured star cabling installation, and diagnostic evaluation."
            topic.save()
        else:
            print(f"[+] Created Topic 11 (ID: {topic.id})")

        curriculum_data = build_topic11_curriculum()

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
                    "topic_order": 11,
                    "unit_order": u_order
                }
            )
            total_lessons += 1

            block_counter = 1
            for page_idx, page_blocks in enumerate(pages, start=1):
                total_pages += 1
                for comp_idx, block_def in enumerate(page_blocks, start=1):
                    b_type = block_def["type"]
                    if b_type in ["step_by_step_worked_example", "step_process"]:
                        b_type = "worked_example"
                    elif b_type == "concept":
                        b_type = "concept_explanation"
                    elif b_type in ["key_takeaways", "summary"]:
                        b_type = "key_takeaway"

                    b_title = clean_text(block_def.get("title", ""))
                    b_content = clean_dict(block_def.get("content", {}))

                    if b_type == "knowledge_check" and isinstance(b_content, dict):
                        options = b_content.get("options", [])
                        ans = b_content.get("correct_answer") or b_content.get("answer")
                        idx = b_content.get("correct_option_index")
                        if idx is None and isinstance(ans, int) and 0 <= ans < len(options):
                            idx = ans
                            ans = options[idx]
                        elif idx is None and isinstance(ans, str) and ans in options:
                            idx = options.index(ans)
                        elif ans is None and isinstance(idx, int) and 0 <= idx < len(options):
                            ans = options[idx]
                        b_content["correct_answer"] = ans
                        b_content["correct_option_index"] = idx

                    block = LessonBlock.objects.create(
                        lesson=lesson,
                        block_id=f"g10_cs_t11_u{u_order}_p{page_idx}_b{comp_idx}",
                        block_type=b_type,
                        component_type=b_type,
                        title=b_title,
                        content=b_content,
                        order=block_counter,
                        page_number=page_idx,
                        component_order=comp_idx,
                        page_title=b_title if comp_idx == 1 else None,
                        metadata={"topic_order": 11, "unit_order": u_order, "page": page_idx}
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
    print(f"TOPIC 11 INGESTION COMPLETE:")
    print(f"  Units Created:   {total_units}")
    print(f"  Lessons Created: {total_lessons}")
    print(f"  Pages Created:   {total_pages}")
    print(f"  Blocks Created:  {total_blocks}")
    print(f"  Assets Attached: {total_assets}")
    print("=" * 80)

if __name__ == "__main__":
    ingest_grade10_topic11(replace=True)
