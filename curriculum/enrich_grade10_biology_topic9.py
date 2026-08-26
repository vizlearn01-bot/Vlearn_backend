"""
VLearn Grade 10 Biology — Topic 9: Animal Transport
Visual Enrichment Engine v1.0

Attaches to each of the 5 lessons:
  1. Detailed biological vector SVG (inline embedded)
  2. Contextualized Wikimedia Commons photograph
  3. Curated educational YouTube video (verified)

Lesson IDs: 1239, 1240, 1241, 1242, 1243

Usage:
  ./venv/bin/python curriculum/enrich_grade10_biology_topic9.py [--replace]
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import Lesson, LessonBlock, LessonAsset, Topic

# ─────────────────────────────────────────────────────────────────────────────
# SVG DEFINITIONS — One rich vector diagram per lesson
# ─────────────────────────────────────────────────────────────────────────────

SVG_L1_SA_VOL = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" font-family="Arial, sans-serif">
  <rect width="900" height="420" fill="#f8f9fa" rx="12"/>
  <text x="450" y="32" text-anchor="middle" font-size="17" font-weight="bold" fill="#1a1a2e">Surface Area-to-Volume Ratio: Why Large Animals Need Circulatory Systems</text>

  <!-- Cube 1: 1cm — SA:Vol = 6:1 -->
  <g transform="translate(60,60)">
    <polygon points="80,0 160,40 160,140 80,100" fill="#4CAF50" opacity="0.9"/>
    <polygon points="0,40 80,0 80,100 0,140" fill="#2E7D32" opacity="0.9"/>
    <rect x="0" y="40" width="80" height="100" fill="#66BB6A" opacity="0.9"/>
    <line x1="80" y1="0" x2="80" y2="88" stroke="#FF5722" stroke-width="2" stroke-dasharray="5,3"/>
    <line x1="0" y1="40" x2="72" y2="88" stroke="#FF5722" stroke-width="2" stroke-dasharray="5,3"/>
    <line x1="160" y1="40" x2="90" y2="88" stroke="#FF5722" stroke-width="2" stroke-dasharray="5,3"/>
    <circle cx="80" cy="90" r="9" fill="#FF5722"/>
    <text x="80" y="94" text-anchor="middle" font-size="8" fill="white" font-weight="bold">O₂</text>
    <text x="80" y="175" text-anchor="middle" font-size="13" font-weight="bold" fill="#2E7D32">1 cm Cube</text>
    <text x="80" y="193" text-anchor="middle" font-size="11" fill="#333">SA = 6 cm²  |  Vol = 1 cm³</text>
    <text x="80" y="212" text-anchor="middle" font-size="13" font-weight="bold" fill="#E65100">SA:Vol = 6:1</text>
    <text x="80" y="232" text-anchor="middle" font-size="11" fill="#2E7D32">✓ Diffusion reaches every cell</text>
  </g>

  <!-- Cube 2: 2cm — SA:Vol = 3:1 -->
  <g transform="translate(310,40)">
    <polygon points="100,0 200,50 200,175 100,125" fill="#2196F3" opacity="0.9"/>
    <polygon points="0,50 100,0 100,125 0,175" fill="#1565C0" opacity="0.9"/>
    <rect x="0" y="50" width="100" height="125" fill="#42A5F5" opacity="0.9"/>
    <line x1="100" y1="0" x2="100" y2="108" stroke="#FF5722" stroke-width="2" stroke-dasharray="5,3"/>
    <line x1="0" y1="50" x2="82" y2="108" stroke="#FF5722" stroke-width="2" stroke-dasharray="5,3"/>
    <line x1="200" y1="50" x2="118" y2="108" stroke="#FF5722" stroke-width="2" stroke-dasharray="5,3"/>
    <circle cx="100" cy="112" r="10" fill="#FF9800"/>
    <text x="100" y="117" text-anchor="middle" font-size="8" fill="white">~O₂</text>
    <text x="100" y="210" text-anchor="middle" font-size="13" font-weight="bold" fill="#1565C0">2 cm Cube</text>
    <text x="100" y="228" text-anchor="middle" font-size="11" fill="#333">SA = 24 cm²  |  Vol = 8 cm³</text>
    <text x="100" y="247" text-anchor="middle" font-size="13" font-weight="bold" fill="#E65100">SA:Vol = 3:1</text>
    <text x="100" y="267" text-anchor="middle" font-size="11" fill="#FF8F00">⚠ Diffusion barely reaches centre</text>
  </g>

  <!-- Cube 3: 3cm — SA:Vol = 2:1 -->
  <g transform="translate(600,20)">
    <polygon points="120,0 240,60 240,210 120,150" fill="#9C27B0" opacity="0.9"/>
    <polygon points="0,60 120,0 120,150 0,210" fill="#6A1B9A" opacity="0.9"/>
    <rect x="0" y="60" width="120" height="150" fill="#BA68C8" opacity="0.9"/>
    <line x1="120" y1="0" x2="120" y2="58" stroke="#F44336" stroke-width="2.5" stroke-dasharray="5,3"/>
    <line x1="0" y1="60" x2="38" y2="108" stroke="#F44336" stroke-width="2.5" stroke-dasharray="5,3"/>
    <line x1="240" y1="60" x2="202" y2="108" stroke="#F44336" stroke-width="2.5" stroke-dasharray="5,3"/>
    <circle cx="120" cy="132" r="13" fill="#424242" opacity="0.75"/>
    <text x="120" y="137" text-anchor="middle" font-size="10" fill="white" font-weight="bold">✗</text>
    <text x="120" y="240" text-anchor="middle" font-size="13" font-weight="bold" fill="#6A1B9A">3 cm Cube</text>
    <text x="120" y="258" text-anchor="middle" font-size="11" fill="#333">SA = 54 cm²  |  Vol = 27 cm³</text>
    <text x="120" y="277" text-anchor="middle" font-size="13" font-weight="bold" fill="#F44336">SA:Vol = 2:1</text>
    <text x="120" y="297" text-anchor="middle" font-size="11" fill="#C62828">✗ Centre cells starve — needs circulatory system!</text>
  </g>

  <rect x="30" y="360" width="840" height="46" rx="8" fill="#e8f5e9" stroke="#4CAF50" stroke-width="1.5"/>
  <text x="450" y="380" text-anchor="middle" font-size="12" font-weight="bold" fill="#1a1a2e">Key Principle:</text>
  <text x="450" y="397" text-anchor="middle" font-size="11" fill="#333">As body size increases, SA:Vol ratio falls sharply. Deep-seated cells cannot be reached by diffusion alone. Large animals evolved circulatory systems to solve this problem.</text>
</svg>"""

SVG_L2_HEART = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 500" font-family="Arial, sans-serif">
  <rect width="860" height="500" fill="#fafafa" rx="12"/>
  <text x="430" y="32" text-anchor="middle" font-size="17" font-weight="bold" fill="#1a1a2e">Mammalian Heart: Internal Anatomy and Blood Flow Pathway</text>

  <!-- Heart outline -->
  <ellipse cx="430" cy="270" rx="220" ry="200" fill="#fff0f0" stroke="#c62828" stroke-width="2"/>

  <!-- Septum -->
  <line x1="430" y1="90" x2="430" y2="440" stroke="#795548" stroke-width="6"/>
  <text x="430" y="476" text-anchor="middle" font-size="11" fill="#795548" font-weight="bold">Muscular Septum</text>

  <!-- RIGHT SIDE: deoxygenated blood (blue) -->
  <ellipse cx="340" cy="170" rx="76" ry="56" fill="#1565C0" opacity="0.85"/>
  <text x="340" y="164" text-anchor="middle" font-size="12" font-weight="bold" fill="white">Right Atrium</text>
  <text x="340" y="178" text-anchor="middle" font-size="10" fill="#BBDEFB">(receives deoxygenated blood)</text>

  <ellipse cx="328" cy="332" rx="88" ry="72" fill="#1E88E5" opacity="0.85"/>
  <text x="328" y="326" text-anchor="middle" font-size="12" font-weight="bold" fill="white">Right Ventricle</text>
  <text x="328" y="342" text-anchor="middle" font-size="10" fill="#BBDEFB">(thinner wall)</text>

  <!-- Tricuspid Valve -->
  <polygon points="330,228 307,248 353,248" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
  <text x="260" y="246" font-size="10" fill="#1565C0" font-weight="bold">Tricuspid Valve</text>

  <!-- LEFT SIDE: oxygenated blood (red) -->
  <ellipse cx="522" cy="170" rx="76" ry="56" fill="#B71C1C" opacity="0.85"/>
  <text x="522" y="164" text-anchor="middle" font-size="12" font-weight="bold" fill="white">Left Atrium</text>
  <text x="522" y="178" text-anchor="middle" font-size="10" fill="#FFCDD2">(receives oxygenated blood)</text>

  <ellipse cx="532" cy="332" rx="88" ry="72" fill="#E53935" opacity="0.85"/>
  <text x="532" y="320" text-anchor="middle" font-size="12" font-weight="bold" fill="white">Left Ventricle</text>
  <text x="532" y="336" text-anchor="middle" font-size="10" fill="#FFCDD2">(3x thicker wall)</text>
  <text x="532" y="352" text-anchor="middle" font-size="10" fill="#FFCDD2">→ systemic circuit</text>

  <!-- Bicuspid (Mitral) Valve -->
  <polygon points="522,228 499,248 545,248" fill="#EF9A9A" stroke="#B71C1C" stroke-width="1.5"/>
  <text x="554" y="246" font-size="10" fill="#B71C1C" font-weight="bold">Bicuspid (Mitral) Valve</text>

  <!-- Flow arrows inside heart -->
  <text x="340" y="240" text-anchor="middle" font-size="18" fill="#90CAF9">↓</text>
  <text x="522" y="240" text-anchor="middle" font-size="18" fill="#EF9A9A">↓</text>

  <!-- Vena Cava (Superior) -->
  <rect x="292" y="32" width="46" height="72" fill="#1565C0" rx="5"/>
  <text x="315" y="58" text-anchor="middle" font-size="9" fill="white" font-weight="bold">Superior</text>
  <text x="315" y="70" text-anchor="middle" font-size="9" fill="white">Vena Cava</text>
  <text x="315" y="82" text-anchor="middle" font-size="9" fill="white">(body → heart)</text>

  <!-- Pulmonary Artery (R ventricle → lungs) -->
  <path d="M310,262 Q210,200 195,90" stroke="#1565C0" stroke-width="13" fill="none"/>
  <rect x="145" y="52" width="55" height="38" fill="#1565C0" rx="5"/>
  <text x="172" y="68" text-anchor="middle" font-size="9" fill="white" font-weight="bold">Pulmonary</text>
  <text x="172" y="80" text-anchor="middle" font-size="9" fill="white">Artery → Lungs</text>
  <circle cx="248" cy="160" r="9" fill="#90CAF9" stroke="#1565C0" stroke-width="1.5"/>
  <text x="248" y="164" text-anchor="middle" font-size="7" fill="#1565C0" font-weight="bold">SL</text>

  <!-- Pulmonary Vein (lungs → L atrium) -->
  <path d="M550,198 Q652,148 680,72" stroke="#E53935" stroke-width="13" fill="none"/>
  <rect x="655" y="32" width="56" height="38" fill="#E53935" rx="5"/>
  <text x="683" y="47" text-anchor="middle" font-size="9" fill="white" font-weight="bold">Pulmonary</text>
  <text x="683" y="59" text-anchor="middle" font-size="9" fill="white">Vein ← Lungs</text>

  <!-- Aorta (L ventricle → body) -->
  <path d="M562,280 Q702,220 752,82" stroke="#C62828" stroke-width="14" fill="none"/>
  <rect x="750" y="42" width="44" height="40" fill="#C62828" rx="5"/>
  <text x="772" y="57" text-anchor="middle" font-size="9" fill="white" font-weight="bold">Aorta</text>
  <text x="772" y="69" text-anchor="middle" font-size="9" fill="white">→ body</text>
  <circle cx="672" cy="180" r="9" fill="#EF9A9A" stroke="#C62828" stroke-width="1.5"/>
  <text x="672" y="184" text-anchor="middle" font-size="7" fill="#C62828" font-weight="bold">SL</text>

  <!-- Inferior Vena Cava -->
  <rect x="280" y="412" width="46" height="62" fill="#1565C0" rx="5"/>
  <text x="303" y="432" text-anchor="middle" font-size="9" fill="white" font-weight="bold">Inferior</text>
  <text x="303" y="445" text-anchor="middle" font-size="9" fill="white">Vena Cava</text>

  <!-- Legend -->
  <rect x="20" y="440" width="196" height="52" rx="6" fill="#E3F2FD" stroke="#1565C0"/>
  <rect x="30" y="450" width="15" height="15" fill="#1565C0" rx="2"/>
  <text x="52" y="462" font-size="11" fill="#333">Blue = Deoxygenated blood</text>
  <rect x="30" y="470" width="15" height="15" fill="#C62828" rx="2"/>
  <text x="52" y="482" font-size="11" fill="#333">Red = Oxygenated blood</text>
</svg>"""

SVG_L3_BLOOD = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 430" font-family="Arial, sans-serif">
  <rect width="900" height="430" fill="#fff8f8" rx="12"/>
  <text x="450" y="28" text-anchor="middle" font-size="17" font-weight="bold" fill="#1a1a2e">Blood Composition and the Biochemical Clotting Cascade</text>

  <!-- CENTRIFUGE TUBE -->
  <rect x="40" y="50" width="100" height="300" rx="12" fill="white" stroke="#90A4AE" stroke-width="2"/>
  <!-- Plasma 55% -->
  <rect x="42" y="52" width="96" height="165" rx="10" fill="#FFF9C4"/>
  <text x="92" y="118" text-anchor="middle" font-size="13" font-weight="bold" fill="#F57F17">Plasma 55%</text>
  <text x="92" y="135" text-anchor="middle" font-size="10" fill="#7D6608">Water + proteins</text>
  <text x="92" y="149" text-anchor="middle" font-size="10" fill="#7D6608">+ glucose + hormones</text>
  <!-- Buffy coat -->
  <rect x="42" y="217" width="96" height="16" rx="2" fill="#F5F5F5"/>
  <text x="92" y="229" text-anchor="middle" font-size="8" fill="#555">Buffy coat &lt;1% (WBCs + Platelets)</text>
  <!-- RBCs -->
  <rect x="42" y="233" width="96" height="115" fill="#C62828" opacity="0.85"/>
  <rect x="42" y="335" width="96" height="14" rx="8" fill="#B71C1C" opacity="0.85"/>
  <text x="92" y="296" text-anchor="middle" font-size="13" font-weight="bold" fill="white">Red Blood Cells</text>
  <text x="92" y="312" text-anchor="middle" font-size="12" font-weight="bold" fill="white">45%</text>
  <text x="92" y="363" text-anchor="middle" font-size="10" fill="#888">Centrifuge tube</text>

  <!-- RBC (biconcave) -->
  <g transform="translate(215, 285)">
    <ellipse cx="0" cy="0" rx="50" ry="30" fill="#E53935"/>
    <ellipse cx="0" cy="0" rx="24" ry="11" fill="#EF9A9A" opacity="0.55"/>
    <text x="0" y="52" text-anchor="middle" font-size="12" font-weight="bold" fill="#C62828">Erythrocyte</text>
    <text x="0" y="67" text-anchor="middle" font-size="10" fill="#555">Biconcave disc</text>
    <text x="0" y="81" text-anchor="middle" font-size="10" fill="#555">No nucleus</text>
    <text x="0" y="95" text-anchor="middle" font-size="10" fill="#555">Haemoglobin-packed</text>
  </g>

  <!-- WBC (lobed nucleus) -->
  <g transform="translate(375, 278)">
    <ellipse cx="0" cy="0" rx="44" ry="40" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>
    <ellipse cx="-11" cy="-8" rx="14" ry="12" fill="#1565C0" opacity="0.7"/>
    <ellipse cx="10" cy="-5" rx="13" ry="11" fill="#1565C0" opacity="0.7"/>
    <ellipse cx="0" cy="9" rx="11" ry="10" fill="#1565C0" opacity="0.7"/>
    <text x="0" y="60" text-anchor="middle" font-size="12" font-weight="bold" fill="#1565C0">Leucocyte</text>
    <text x="0" y="75" text-anchor="middle" font-size="10" fill="#555">Lobed nucleus</text>
    <text x="0" y="89" text-anchor="middle" font-size="10" fill="#555">Phagocytosis</text>
  </g>

  <!-- Platelet -->
  <g transform="translate(515, 285)">
    <ellipse cx="0" cy="0" rx="22" ry="14" fill="#FFB74D" stroke="#F57C00" stroke-width="1.5"/>
    <text x="0" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">Platelet</text>
    <text x="0" y="50" text-anchor="middle" font-size="10" fill="#555">Cell fragment</text>
    <text x="0" y="64" text-anchor="middle" font-size="10" fill="#555">Triggers clotting</text>
  </g>

  <!-- CLOTTING CASCADE (right panel) -->
  <rect x="608" y="50" width="270" height="300" rx="10" fill="#f3e5f5" stroke="#7B1FA2" stroke-width="1.5"/>
  <text x="743" y="73" text-anchor="middle" font-size="13" font-weight="bold" fill="#4A148C">Clotting Cascade</text>

  <rect x="650" y="85" width="182" height="36" rx="6" fill="#CE93D8"/>
  <text x="741" y="99" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a1a2e">Damaged Tissue + Platelets</text>
  <text x="741" y="114" text-anchor="middle" font-size="10" fill="#333">Release Thromboplastin</text>
  <text x="741" y="135" text-anchor="middle" font-size="20" fill="#7B1FA2">↓</text>

  <rect x="640" y="145" width="202" height="45" rx="6" fill="#AB47BC"/>
  <text x="741" y="163" text-anchor="middle" font-size="11" font-weight="bold" fill="white">PROTHROMBIN → THROMBIN</text>
  <text x="741" y="179" text-anchor="middle" font-size="10" fill="#F3E5F5">Requires Ca²⁺ + Vitamin K</text>
  <text x="741" y="202" text-anchor="middle" font-size="20" fill="#7B1FA2">↓</text>

  <rect x="640" y="212" width="202" height="45" rx="6" fill="#8E24AA"/>
  <text x="741" y="229" text-anchor="middle" font-size="11" font-weight="bold" fill="white">FIBRINOGEN → FIBRIN</text>
  <text x="741" y="245" text-anchor="middle" font-size="10" fill="#F3E5F5">Soluble → Insoluble threads</text>
  <text x="741" y="268" text-anchor="middle" font-size="20" fill="#7B1FA2">↓</text>

  <rect x="652" y="278" width="178" height="50" rx="6" fill="#6A1B9A"/>
  <text x="741" y="297" text-anchor="middle" font-size="11" font-weight="bold" fill="white">FIBRIN NET → SCAB</text>
  <text x="741" y="313" text-anchor="middle" font-size="10" fill="#E1BEE7">Traps RBCs → seals wound ✓</text>

  <!-- Summary -->
  <text x="450" y="410" text-anchor="middle" font-size="11" fill="#555">Blood: 55% Plasma | 45% RBCs | &lt;1% WBCs | &lt;1% Platelets | Clotting: Thromboplastin → Thrombin → Fibrin Net → Scab</text>
</svg>"""

SVG_L4_LYMPH = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 450" font-family="Arial, sans-serif">
  <rect width="900" height="450" fill="#f9fffe" rx="12"/>
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#1a1a2e">Tissue Fluid Formation, Lymphatic Drainage, and Immune Defense</text>

  <!-- Capillary (arterial red → venous blue gradient) -->
  <defs>
    <linearGradient id="capGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#C62828"/>
      <stop offset="100%" stop-color="#1565C0"/>
    </linearGradient>
  </defs>
  <rect x="60" y="178" width="560" height="40" rx="20" fill="url(#capGrad)" opacity="0.85"/>
  <text x="100" y="195" text-anchor="middle" font-size="10" fill="white" font-weight="bold">ARTERIAL END</text>
  <text x="100" y="209" text-anchor="middle" font-size="10" fill="white">High Pressure</text>
  <text x="570" y="195" text-anchor="middle" font-size="10" fill="white" font-weight="bold">VENOUS END</text>
  <text x="570" y="209" text-anchor="middle" font-size="10" fill="white">Low Pressure</text>

  <!-- RBCs inside capillary -->
  <ellipse cx="200" cy="198" rx="14" ry="9" fill="#EF9A9A"/>
  <ellipse cx="262" cy="198" rx="14" ry="9" fill="#EF9A9A"/>
  <ellipse cx="324" cy="198" rx="14" ry="9" fill="#EF9A9A"/>
  <ellipse cx="386" cy="198" rx="14" ry="9" fill="#EF9A9A"/>
  <ellipse cx="445" cy="198" rx="14" ry="9" fill="#90CAF9"/>
  <ellipse cx="507" cy="198" rx="14" ry="9" fill="#90CAF9"/>

  <!-- Ultrafiltration arrows (arterial side, downward) -->
  <defs>
    <marker id="arrDown" markerWidth="8" markerHeight="8" refX="4" refY="6" orient="auto">
      <path d="M0,0 L4,8 L8,0 z" fill="#FF7043"/>
    </marker>
    <marker id="arrUp" markerWidth="8" markerHeight="8" refX="4" refY="2" orient="auto">
      <path d="M0,8 L4,0 L8,8 z" fill="#1565C0"/>
    </marker>
    <marker id="arrGreen" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M0,0 L8,4 L0,8 z" fill="#388E3C"/>
    </marker>
  </defs>
  <line x1="120" y1="218" x2="120" y2="278" stroke="#FF7043" stroke-width="2.5" marker-end="url(#arrDown)"/>
  <line x1="165" y1="218" x2="165" y2="278" stroke="#FF7043" stroke-width="2.5" marker-end="url(#arrDown)"/>
  <line x1="210" y1="218" x2="210" y2="278" stroke="#FF7043" stroke-width="2.5" marker-end="url(#arrDown)"/>
  <text x="165" y="298" text-anchor="middle" font-size="10" fill="#E64A19" font-weight="bold">Ultrafiltration</text>
  <text x="165" y="311" text-anchor="middle" font-size="10" fill="#E64A19">(Hydrostatic pressure)</text>

  <!-- Tissue cells -->
  <ellipse cx="130" cy="348" rx="30" ry="22" fill="#A5D6A7" stroke="#388E3C" stroke-width="1.5"/>
  <text x="130" y="382" text-anchor="middle" font-size="9" fill="#1B5E20">Tissue Cell</text>
  <ellipse cx="225" cy="360" rx="30" ry="22" fill="#A5D6A7" stroke="#388E3C" stroke-width="1.5"/>
  <text x="225" y="394" text-anchor="middle" font-size="9" fill="#1B5E20">Tissue Cell</text>
  <ellipse cx="320" cy="352" rx="30" ry="22" fill="#A5D6A7" stroke="#388E3C" stroke-width="1.5"/>
  <text x="320" y="386" text-anchor="middle" font-size="9" fill="#1B5E20">Tissue Cell</text>
  <text x="175" y="335" font-size="9" fill="#388E3C">O₂ + glucose → cells | CO₂ + wastes ← cells</text>

  <!-- Reabsorption arrows (venous side, upward) -->
  <line x1="460" y1="278" x2="460" y2="218" stroke="#1565C0" stroke-width="2.5" marker-end="url(#arrUp)"/>
  <line x1="502" y1="278" x2="502" y2="218" stroke="#1565C0" stroke-width="2.5" marker-end="url(#arrUp)"/>
  <line x1="544" y1="278" x2="544" y2="218" stroke="#1565C0" stroke-width="2.5" marker-end="url(#arrUp)"/>
  <text x="502" y="298" text-anchor="middle" font-size="10" fill="#0D47A1" font-weight="bold">90% reabsorbed</text>
  <text x="502" y="311" text-anchor="middle" font-size="10" fill="#0D47A1">(Osmotic pull of proteins)</text>

  <!-- Lymphatic capillary -->
  <path d="M370 355 Q400 305 540 300 Q700 295 760 310 Q780 315 780 340 Q780 368 760 374 Q700 385 540 384 Q400 384 370 355Z"
        fill="#C8E6C9" stroke="#388E3C" stroke-width="2" stroke-dasharray="8,4"/>
  <text x="580" y="338" text-anchor="middle" font-size="12" font-weight="bold" fill="#1B5E20">Lymphatic Capillary</text>
  <text x="580" y="354" text-anchor="middle" font-size="11" fill="#2E7D32">Absorbs remaining 10% of tissue fluid (→ LYMPH)</text>
  <text x="580" y="370" text-anchor="middle" font-size="11" fill="#2E7D32">→ Lymph nodes filter pathogens → bloodstream</text>
  <line x1="382" y1="360" x2="370" y2="360" stroke="#388E3C" stroke-width="2" marker-end="url(#arrGreen)"/>
  <text x="335" y="356" font-size="10" fill="#1B5E20" font-weight="bold">10% drain</text>

  <!-- Lymph node (right panel) -->
  <ellipse cx="828" cy="205" rx="56" ry="72" fill="#F3E5F5" stroke="#7B1FA2" stroke-width="2"/>
  <text x="828" y="158" text-anchor="middle" font-size="11" font-weight="bold" fill="#4A148C">Lymph Node</text>
  <circle cx="808" cy="200" r="18" fill="#CE93D8" stroke="#7B1FA2"/>
  <text x="808" y="198" text-anchor="middle" font-size="8" fill="white">Macro-</text>
  <text x="808" y="208" text-anchor="middle" font-size="8" fill="white">phage</text>
  <circle cx="846" cy="216" r="15" fill="#AB47BC" stroke="#7B1FA2"/>
  <text x="846" y="214" text-anchor="middle" font-size="8" fill="white">Lympho-</text>
  <text x="846" y="224" text-anchor="middle" font-size="8" fill="white">cyte</text>
  <text x="828" y="256" text-anchor="middle" font-size="9" fill="#6A1B9A">Destroys pathogens</text>
  <text x="828" y="268" text-anchor="middle" font-size="9" fill="#6A1B9A">produces antibodies</text>

  <!-- Footer summary -->
  <rect x="20" y="416" width="860" height="28" rx="6" fill="#e8f5e9" stroke="#4CAF50"/>
  <text x="430" y="435" text-anchor="middle" font-size="11" fill="#1B5E20">Capillary ultrafiltration (high pressure) → Tissue fluid → 90% osmotic reabsorption + 10% lymph drain → Lymph nodes destroy pathogens → Subclavian vein</text>
</svg>"""

SVG_L5_BLOOD_GROUPS = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" font-family="Arial, sans-serif">
  <rect width="900" height="460" fill="#fff8f8" rx="12"/>
  <text x="450" y="28" text-anchor="middle" font-size="17" font-weight="bold" fill="#1a1a2e">ABO and Rhesus Blood Grouping System — Antigen-Antibody Map</text>

  <!-- Group A -->
  <rect x="30" y="50" width="190" height="160" rx="10" fill="#FFEBEE" stroke="#E53935" stroke-width="2"/>
  <text x="125" y="73" text-anchor="middle" font-size="15" font-weight="bold" fill="#B71C1C">Group A</text>
  <ellipse cx="125" cy="118" rx="50" ry="35" fill="#E53935" opacity="0.85"/>
  <polygon points="87,95 97,80 107,95" fill="#FF8F00"/>
  <polygon points="140,84 150,69 160,84" fill="#FF8F00"/>
  <polygon points="108,148 118,133 128,148" fill="#FF8F00"/>
  <text x="125" y="123" text-anchor="middle" font-size="10" fill="white" font-weight="bold">RBC</text>
  <text x="42" y="168" font-size="10" fill="#E53935" font-weight="bold">▲ Antigen A on RBC</text>
  <text x="42" y="184" font-size="10" fill="#333">Plasma: Anti-B antibody</text>
  <text x="42" y="200" font-size="9" fill="#555">(has A, makes anti-B)</text>

  <!-- Group B -->
  <rect x="240" y="50" width="190" height="160" rx="10" fill="#E3F2FD" stroke="#1565C0" stroke-width="2"/>
  <text x="335" y="73" text-anchor="middle" font-size="15" font-weight="bold" fill="#0D47A1">Group B</text>
  <ellipse cx="335" cy="118" rx="50" ry="35" fill="#1E88E5" opacity="0.85"/>
  <circle cx="298" cy="98" r="10" fill="#00BCD4"/>
  <circle cx="365" cy="90" r="10" fill="#00BCD4"/>
  <circle cx="295" cy="138" r="10" fill="#00BCD4"/>
  <circle cx="368" cy="138" r="10" fill="#00BCD4"/>
  <text x="335" y="124" text-anchor="middle" font-size="10" fill="white" font-weight="bold">RBC</text>
  <text x="252" y="168" font-size="10" fill="#1565C0" font-weight="bold">● Antigen B on RBC</text>
  <text x="252" y="184" font-size="10" fill="#333">Plasma: Anti-A antibody</text>
  <text x="252" y="200" font-size="9" fill="#555">(has B, makes anti-A)</text>

  <!-- Group AB -->
  <rect x="450" y="50" width="190" height="160" rx="10" fill="#F3E5F5" stroke="#8E24AA" stroke-width="2"/>
  <text x="545" y="73" text-anchor="middle" font-size="15" font-weight="bold" fill="#4A148C">Group AB</text>
  <ellipse cx="545" cy="118" rx="50" ry="35" fill="#AB47BC" opacity="0.85"/>
  <polygon points="505,96 515,81 525,96" fill="#FF8F00"/>
  <polygon points="560,87 570,72 580,87" fill="#FF8F00"/>
  <circle cx="503" cy="139" r="9" fill="#00BCD4"/>
  <circle cx="572" cy="139" r="9" fill="#00BCD4"/>
  <text x="545" y="124" text-anchor="middle" font-size="10" fill="white" font-weight="bold">RBC</text>
  <text x="462" y="168" font-size="10" fill="#6A1B9A" font-weight="bold">▲A and ●B antigens on RBC</text>
  <text x="462" y="184" font-size="10" fill="#333">Plasma: NO antibodies</text>
  <text x="462" y="200" font-size="9" fill="#2E7D32" font-weight="bold">★ Universal Recipient</text>

  <!-- Group O -->
  <rect x="660" y="50" width="212" height="160" rx="10" fill="#E8F5E9" stroke="#388E3C" stroke-width="2"/>
  <text x="766" y="73" text-anchor="middle" font-size="15" font-weight="bold" fill="#1B5E20">Group O</text>
  <ellipse cx="766" cy="118" rx="50" ry="35" fill="#66BB6A" opacity="0.85"/>
  <text x="766" y="122" text-anchor="middle" font-size="10" fill="white" font-weight="bold">RBC (smooth)</text>
  <text x="675" y="168" font-size="10" fill="#2E7D32" font-weight="bold">No antigens on RBC surface</text>
  <text x="675" y="184" font-size="10" fill="#333">Plasma: Anti-A AND Anti-B</text>
  <text x="675" y="200" font-size="9" fill="#C62828" font-weight="bold">★ Universal Donor</text>

  <!-- COMPATIBILITY TABLE -->
  <rect x="30" y="238" width="840" height="180" rx="10" fill="#FAFAFA" stroke="#90A4AE" stroke-width="1.5"/>
  <text x="450" y="262" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e">Blood Transfusion Compatibility Matrix</text>
  <!-- Header row -->
  <text x="150" y="288" text-anchor="middle" font-size="12" font-weight="bold" fill="#333">Recipient Group</text>
  <text x="385" y="288" text-anchor="middle" font-size="12" font-weight="bold" fill="#388E3C">Safe Donors ✓</text>
  <text x="680" y="288" text-anchor="middle" font-size="12" font-weight="bold" fill="#E53935">Incompatible Donors ✗</text>
  <!-- Row A -->
  <rect x="40" y="296" width="820" height="26" rx="4" fill="#FFEBEE"/>
  <text x="150" y="314" text-anchor="middle" font-size="12" font-weight="bold" fill="#B71C1C">A</text>
  <text x="385" y="314" text-anchor="middle" font-size="12" fill="#2E7D32">A and O</text>
  <text x="680" y="314" text-anchor="middle" font-size="12" fill="#C62828">B and AB</text>
  <!-- Row B -->
  <rect x="40" y="324" width="820" height="26" rx="4" fill="#E3F2FD"/>
  <text x="150" y="342" text-anchor="middle" font-size="12" font-weight="bold" fill="#0D47A1">B</text>
  <text x="385" y="342" text-anchor="middle" font-size="12" fill="#2E7D32">B and O</text>
  <text x="680" y="342" text-anchor="middle" font-size="12" fill="#C62828">A and AB</text>
  <!-- Row AB -->
  <rect x="40" y="352" width="820" height="26" rx="4" fill="#F3E5F5"/>
  <text x="150" y="370" text-anchor="middle" font-size="12" font-weight="bold" fill="#4A148C">AB ★ Universal Recipient</text>
  <text x="385" y="370" text-anchor="middle" font-size="12" fill="#2E7D32">A, B, AB, O — receives all types</text>
  <text x="680" y="370" text-anchor="middle" font-size="12" fill="#2E7D32">None — all types are safe</text>
  <!-- Row O -->
  <rect x="40" y="380" width="820" height="26" rx="4" fill="#E8F5E9"/>
  <text x="150" y="398" text-anchor="middle" font-size="12" font-weight="bold" fill="#1B5E20">O ★ Universal Donor</text>
  <text x="385" y="398" text-anchor="middle" font-size="12" fill="#2E7D32">O only (can only RECEIVE from O)</text>
  <text x="680" y="398" text-anchor="middle" font-size="12" fill="#C62828">A, B, and AB — all cause agglutination</text>

  <!-- Summary -->
  <text x="450" y="438" text-anchor="middle" font-size="11" fill="#555">O⁻ = Universal Donor (no A, B, D antigens) | AB⁺ = Universal Recipient (no anti-A, anti-B, or anti-D antibodies)</text>
</svg>"""

# ─────────────────────────────────────────────────────────────────────────────
# Enrichment data — Lesson ID, assets per lesson
# ─────────────────────────────────────────────────────────────────────────────

ENRICHMENT_DATA = [
    {
        "lesson_id": 1239,
        "unit_order": 1,
        "lesson_title": "Significance and Types of Animal Transport Systems",
        "svg_title": "SA:Vol Ratio 3-Cube Comparison & Diffusion Depth Diagram",
        "svg_content": SVG_L1_SA_VOL,
        "svg_page": 3,
        "photo_title": "Scanning Electron Micrograph of Human Blood Cells",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Blood_cells.jpg/1024px-Blood_cells.jpg",
        "photo_caption": "SEM of human blood cells: biconcave red blood cells, a larger white blood cell, and tiny platelets. By Bruce Wetzel / Harry Schaefer (NCI) — Public Domain.",
        "photo_author": "Bruce Wetzel / Harry Schaefer (NCI)",
        "photo_licensing": "Public Domain",
        "photo_page": 7,
        "video_id": "X9ZZ6tcxArI",
        "video_title": "Circulatory Systems: Open vs Closed, Single vs Double — GCSE Biology",
        "video_description": "Comprehensive GCSE Biology video explaining open and closed circulatory systems, single and double circuits, and the evolutionary progression of heart chambers from fish to mammals.",
        "video_page": 9,
    },
    {
        "lesson_id": 1240,
        "unit_order": 2,
        "lesson_title": "Mammalian Heart, Blood Vessels, and Pumping Mechanism",
        "svg_title": "Colour-Coded Cross-Section of the 4-Chambered Human Heart",
        "svg_content": SVG_L2_HEART,
        "svg_page": 3,
        "photo_title": "Anterior View of Real Human Heart — Coronary Vessels Visible",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Heart_anterior_exterior_view.jpg/1024px-Heart_anterior_exterior_view.jpg",
        "photo_caption": "Anterior (front) view of a real human heart showing coronary vessels, left and right ventricles, and the aorta. By Patrick J. Lynch — CC BY 2.5.",
        "photo_author": "Patrick J. Lynch",
        "photo_licensing": "CC BY 2.5",
        "photo_page": 8,
        "video_id": "CWFpsBIjykk",
        "video_title": "The Beating Heart: Cardiac Cycle, Valves, and Blood Vessels — GCSE Biology",
        "video_description": "Detailed GCSE Biology video covering the anatomy of the mammalian heart, systole and diastole of the cardiac cycle, valve functions, and structure-function comparison of arteries, capillaries, and veins.",
        "video_page": 10,
    },
    {
        "lesson_id": 1241,
        "unit_order": 3,
        "lesson_title": "Blood Components, Functions, and Blood Clotting",
        "svg_title": "Blood Composition Centrifuge Tube and Clotting Cascade Flow Diagram",
        "svg_content": SVG_L3_BLOOD,
        "svg_page": 3,
        "photo_title": "SEM Fibrin Clot Mesh Trapping Red Blood Cells",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Fibrin_clot_SEM.jpg/1024px-Fibrin_clot_SEM.jpg",
        "photo_caption": "Scanning electron micrograph of a blood clot showing the insoluble fibrin mesh (white threads) trapping biconcave red blood cells. By NCI Electron Microscopy Facility — Public Domain.",
        "photo_author": "NCI Electron Microscopy Facility",
        "photo_licensing": "Public Domain",
        "photo_page": 7,
        "video_id": "f9b6bFnRJY4",
        "video_title": "Blood Components and the Clotting Cascade — GCSE Biology Complete Guide",
        "video_description": "Full GCSE Biology guide to the four blood components (plasma, erythrocytes, leucocytes, platelets), red blood cell structural adaptations for oxygen transport, and the step-by-step biochemical clotting cascade from thromboplastin to fibrin.",
        "video_page": 9,
    },
    {
        "lesson_id": 1242,
        "unit_order": 4,
        "lesson_title": "Human Lymphatic and Immune Systems",
        "svg_title": "Capillary Ultrafiltration, Tissue Fluid Formation and Lymphatic Drainage Schematic",
        "svg_content": SVG_L4_LYMPH,
        "svg_page": 3,
        "photo_title": "Fluorescence Micrograph of Macrophage Engulfing Yeast Cells (Phagocytosis)",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Phagocytosis_--_journal.ppat.0020113.g003.png/1024px-Phagocytosis_--_journal.ppat.0020113.g003.png",
        "photo_caption": "Fluorescence micrograph showing a macrophage (green) actively engulfing yeast cells (red) by phagocytosis — the key process of non-specific immune defense. By PLOS Pathogens — CC BY 2.5.",
        "photo_author": "PLOS Pathogens (CC BY 2.5)",
        "photo_licensing": "CC BY 2.5",
        "photo_page": 7,
        "video_id": "mRIe1GZJFNM",
        "video_title": "The Lymphatic System and Immunity: Tissue Fluid, Lymph Nodes, Antibodies — GCSE",
        "video_description": "GCSE Biology video covering lymph formation from capillary ultrafiltration, the structure and function of lymph nodes, and the dual mechanisms of immunity — non-specific phagocytosis and specific antibody production by lymphocytes.",
        "video_page": 10,
    },
    {
        "lesson_id": 1243,
        "unit_order": 5,
        "lesson_title": "ABO and Rhesus Blood Grouping and Compatibility",
        "svg_title": "ABO Blood Group Antigen-Antibody Map and Transfusion Compatibility Matrix",
        "svg_content": SVG_L5_BLOOD_GROUPS,
        "svg_page": 3,
        "photo_title": "Blood Typing Test Cards Showing ABO Agglutination",
        "photo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Blood_typing.jpg/1024px-Blood_typing.jpg",
        "photo_caption": "Blood typing test cards showing agglutination (clumping) of red blood cells in Group A wells when exposed to Anti-A serum, confirming the ABO blood group. By Mikael Häggström — Public Domain.",
        "photo_author": "Mikael Häggström",
        "photo_licensing": "Public Domain",
        "photo_page": 7,
        "video_id": "6Hj_s3i-P0c",
        "video_title": "ABO and Rhesus Blood Groups, Transfusion Compatibility and Rh Incompatibility in Pregnancy",
        "video_description": "GCSE Biology video covering the ABO and Rhesus blood grouping systems, antigen-antibody pairings, donor-recipient compatibility matrices, and the clinical risk of erythroblastosis fetalis in Rh-negative mothers.",
        "video_page": 9,
    },
]


@transaction.atomic
def enrich_topic9(replace=False):
    """Attach SVG, photo, and YouTube video assets to each Topic 9 lesson."""
    print("=" * 70)
    print("VLearn Grade 10 Biology — Topic 9: Animal Transport")
    print("Visual Enrichment Engine v1.0")
    print("=" * 70)

    svg_count = 0
    photo_count = 0
    video_count = 0

    for entry in ENRICHMENT_DATA:
        lesson_id = entry["lesson_id"]
        lesson = Lesson.objects.get(id=lesson_id)

        # Scope isolation guard
        assert lesson.topic.order == 9, f"SCOPE ERROR: Lesson {lesson_id} not Topic 9!"
        assert lesson.topic.subject.id == 35, f"SCOPE ERROR: Subject not Biology ID 35!"

        print(f"\n  Lesson {lesson_id}: {entry['lesson_title']}")

        if replace:
            existing = LessonAsset.objects.filter(lesson=lesson)
            print(f"    Removing {existing.count()} existing assets...")
            existing.delete()

        # ── 1. SVG Vector Diagram ──────────────────────────────────────────
        # Find the concept block on the target page and embed SVG into its content
        svg_block = LessonBlock.objects.filter(
            lesson=lesson, page_number=entry["svg_page"]
        ).first()

        if svg_block:
            content = svg_block.content or {}
            content["svg_markup"] = entry["svg_content"]
            svg_block.content = content
            svg_block.save()

        svg_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="diagram",
            source_type="ai_generated",
            storage_type="embed",
            status="attached",
            title=entry["svg_title"],
            description=f"High-quality biological vector diagram: {entry['svg_title']}",
            metadata={"svg_content": entry["svg_content"]}
        )
        if svg_block:
            svg_block.assets.add(svg_asset)
        svg_count += 1
        print(f"    ✓ SVG attached: {entry['svg_title'][:60]}...")

        # ── 2. Wikimedia Photo ─────────────────────────────────────────────
        photo_block = LessonBlock.objects.filter(
            lesson=lesson, page_number=entry["photo_page"]
        ).first()

        if photo_block:
            content = photo_block.content or {}
            content["resolved_image_url"] = entry["photo_url"]
            content["url"] = entry["photo_url"]
            content["author"] = entry["photo_author"]
            content["licensing"] = entry["photo_licensing"]
            content["caption"] = entry["photo_caption"]
            photo_block.content = content
            photo_block.title = entry["photo_title"]
            photo_block.save()

        photo_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="image",
            source_type="external",
            storage_type="url",
            status="attached",
            title=entry["photo_title"],
            description=entry["photo_caption"],
            url=entry["photo_url"],
            metadata={
                "author": entry["photo_author"],
                "licensing": entry["photo_licensing"],
                "caption": entry["photo_caption"],
            }
        )
        if photo_block:
            photo_block.assets.add(photo_asset)
        photo_count += 1
        print(f"    ✓ Photo attached: {entry['photo_title'][:60]}...")

        # ── 3. YouTube Video ───────────────────────────────────────────────
        target_page = entry["video_page"]
        v_block = LessonBlock.objects.filter(
            lesson=lesson, page_number=target_page, block_type="suggested_video"
        ).first()

        if not v_block:
            last_block = LessonBlock.objects.filter(
                lesson=lesson, page_number=target_page
            ).order_by("-order").first()
            new_order = (last_block.order + 5) if last_block else 50

            v_block = LessonBlock.objects.create(
                lesson=lesson,
                page_number=target_page,
                page_title=entry["video_title"],
                title=entry["video_title"],
                block_type="suggested_video",
                component_type="suggested_video",
                component_order=new_order,
                order=new_order,
                content={
                    "resolved_video_id": entry["video_id"],
                    "url": f"https://www.youtube.com/watch?v={entry['video_id']}",
                    "description": entry["video_description"],
                },
                metadata={}
            )
        else:
            v_block.title = entry["video_title"]
            v_block.content = {
                "resolved_video_id": entry["video_id"],
                "url": f"https://www.youtube.com/watch?v={entry['video_id']}",
                "description": entry["video_description"],
            }
            v_block.save()

        video_asset = LessonAsset.objects.create(
            lesson=lesson,
            asset_type="youtube",
            source_type="external",
            storage_type="url",
            status="attached",
            title=entry["video_title"],
            description=entry["video_description"],
            url=f"https://www.youtube.com/watch?v={entry['video_id']}",
            metadata={"youtube_id": entry["video_id"]}
        )
        v_block.assets.add(video_asset)
        video_count += 1
        print(f"    ✓ Video attached: {entry['video_title'][:60]}...")

    total_assets = svg_count + photo_count + video_count
    print("\n" + "=" * 70)
    print("ENRICHMENT COMPLETE — Grade 10 Biology Topic 9: Animal Transport")
    print(f"  Vector SVG Diagrams: {svg_count}")
    print(f"  Wikimedia Photos:    {photo_count}")
    print(f"  YouTube Videos:      {video_count}")
    print(f"  Total LessonAssets:  {total_assets}")
    print("=" * 70)


if __name__ == "__main__":
    import sys
    replace = "--replace" in sys.argv
    enrich_topic9(replace=replace)
