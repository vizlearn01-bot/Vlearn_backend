"""
VLearn CBC Grade 6 Home Science — Fix Script
Fixes:
1. Unavailable video: Needs/Wants → Ubongo Kids Budgeting 101 (2r1o5y-6IeM)
2. Unavailable video: Food Preservation → TED-Ed "Are food preservatives bad for you?" (ZJU34yTJL4M)
3. Unavailable video: Baking/Cookery → TED-Ed "Science of baking cookies" (n6wpNhyPqM4)
4. Jumbled SVG: "Local Food Mineral Map: Iron & Iodine Sources" — rebuilt with correct coords
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Curriculum, Grade, Subject, Topic, LessonBlock, LessonAsset


def get_lesson(subject, topic_order, title_contains):
    topic = Topic.objects.filter(subject=subject, order=topic_order).first()
    if not topic:
        return None
    for unit in topic.learning_units.all():
        lesson = unit.lessons.filter(title__icontains=title_contains).first()
        if lesson:
            return lesson
    return None


def replace_video_block(lesson, old_url_fragment, new_url, new_title, new_description, new_author):
    """Replace a suggested_video block and its LessonAsset in-place."""
    block = lesson.blocks.filter(block_type="suggested_video", page_number__gte=9).first()
    if not block:
        print(f"  [SKIP] No video block found on page 9+ for '{lesson.title}'")
        return False

    block.title = new_title
    block.content = {
        "url": new_url,
        "text": new_description,
        "author": new_author,
        "licensing": "Standard YouTube License"
    }
    block.save()

    # Update the companion callout title is fine as-is, just update the asset
    asset = lesson.assets.filter(url__icontains=old_url_fragment).first()
    if asset:
        asset.url = new_url
        asset.title = new_title
        asset.description = new_description
        asset.metadata = {
            "author": new_author,
            "licensing": "Standard YouTube License",
            "caption": new_description
        }
        asset.save()
    else:
        # Create fresh asset
        LessonAsset.objects.update_or_create(
            lesson=lesson,
            title=new_title,
            defaults={
                "asset_type": "video",
                "source_type": "external",
                "storage_type": "url",
                "status": "attached",
                "url": new_url,
                "description": new_description,
                "metadata": {
                    "author": new_author,
                    "licensing": "Standard YouTube License",
                    "caption": new_description
                }
            }
        )
    print(f"  [OK] '{lesson.title}' → {new_url}")
    return True


# ── Fixed SVG: no emojis, correct absolute y coordinates, clean layout ──────
MINERAL_MAP_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 480" width="100%" height="100%">
  <defs>
    <filter id="sh" x="-4%" y="-4%" width="108%" height="108%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.10"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="820" height="480" fill="#f8fafc" rx="14"/>
  <rect x="18" y="18" width="784" height="444" fill="#ffffff" rx="10"
        stroke="#e2e8f0" stroke-width="1.5" filter="url(#sh)"/>

  <!-- Title Banner -->
  <rect x="36" y="28" width="748" height="44" fill="#0f172a" rx="8"/>
  <text x="410" y="55" fill="#ffffff"
        font-family="Georgia, serif" font-size="16" font-weight="700"
        text-anchor="middle" letter-spacing="0.5">
    LOCAL FOOD MINERAL MAP: IRON &amp; IODINE SOURCES
  </text>

  <!-- ── LEFT PANEL: IRON ── -->
  <g transform="translate(38, 84)">
    <!-- Panel background -->
    <rect x="0" y="0" width="362" height="362" fill="#fef2f2" rx="8"
          stroke="#fecaca" stroke-width="1.5"/>

    <!-- Panel header -->
    <rect x="12" y="12" width="338" height="34" fill="#dc2626" rx="6"/>
    <text x="181" y="33" fill="#ffffff"
          font-family="Arial, sans-serif" font-size="13" font-weight="700"
          text-anchor="middle">IRON — Haemoglobin &amp; Oxygen Transport</text>

    <!-- Row 1: Spinach -->
    <rect x="12" y="58" width="338" height="58" fill="#ffffff" rx="6"
          stroke="#fca5a5" stroke-width="1"/>
    <rect x="12" y="58" width="6" height="58" fill="#dc2626" rx="3"/>
    <text x="30" y="76" fill="#991b1b"
          font-family="Arial, sans-serif" font-size="11.5" font-weight="700">
      Dark Leafy Greens: Sukuma Wiki, Spinach, Terere
    </text>
    <text x="30" y="93" fill="#475569" font-family="Arial, sans-serif" font-size="10.5">
      Rich plant-based iron; builds oxygen-carrying blood cells.
    </text>
    <text x="30" y="108" fill="#64748b" font-family="Arial, sans-serif" font-size="9.5"
          font-style="italic">Eat with lemon juice (Vitamin C) to boost absorption.</text>

    <!-- Row 2: Liver -->
    <rect x="12" y="126" width="338" height="58" fill="#ffffff" rx="6"
          stroke="#fca5a5" stroke-width="1"/>
    <rect x="12" y="126" width="6" height="58" fill="#dc2626" rx="3"/>
    <text x="30" y="144" fill="#991b1b"
          font-family="Arial, sans-serif" font-size="11.5" font-weight="700">
      Beef Liver &amp; Organ Meats
    </text>
    <text x="30" y="161" fill="#475569" font-family="Arial, sans-serif" font-size="10.5">
      Easily absorbed animal (heme) iron; prevents anaemia.
    </text>
    <text x="30" y="176" fill="#64748b" font-family="Arial, sans-serif" font-size="9.5"
          font-style="italic">Best source of iron for girls during menstruation.</text>

    <!-- Row 3: Beans -->
    <rect x="12" y="194" width="338" height="58" fill="#ffffff" rx="6"
          stroke="#fca5a5" stroke-width="1"/>
    <rect x="12" y="194" width="6" height="58" fill="#dc2626" rx="3"/>
    <text x="30" y="212" fill="#991b1b"
          font-family="Arial, sans-serif" font-size="11.5" font-weight="700">
      Red Kidney Beans, Lentils &amp; Groundnuts
    </text>
    <text x="30" y="229" fill="#475569" font-family="Arial, sans-serif" font-size="10.5">
      Affordable plant proteins; rebuilds adolescent blood stores.
    </text>
    <text x="30" y="244" fill="#64748b" font-family="Arial, sans-serif" font-size="9.5"
          font-style="italic">Combine with Vitamin C foods for maximum iron uptake.</text>

    <!-- Tip box -->
    <rect x="12" y="263" width="338" height="86" fill="#fee2e2" rx="6"
          stroke="#fca5a5" stroke-width="1"/>
    <text x="181" y="284" fill="#991b1b"
          font-family="Arial, sans-serif" font-size="11" font-weight="700"
          text-anchor="middle">Deficiency Disorder: Nutritional Anaemia</text>
    <text x="181" y="300" fill="#7f1d1d"
          font-family="Arial, sans-serif" font-size="10" text-anchor="middle">
      Signs: extreme fatigue, pale eyelids &amp; fingernails,
    </text>
    <text x="181" y="316" fill="#7f1d1d"
          font-family="Arial, sans-serif" font-size="10" text-anchor="middle">
      dizziness, and poor concentration in class.
    </text>
    <text x="181" y="337" fill="#991b1b"
          font-family="Arial, sans-serif" font-size="9.5" font-weight="600"
          text-anchor="middle">Prevention: eat iron-rich foods daily.</text>
  </g>

  <!-- ── RIGHT PANEL: IODINE ── -->
  <g transform="translate(420, 84)">
    <!-- Panel background -->
    <rect x="0" y="0" width="362" height="362" fill="#eff6ff" rx="8"
          stroke="#bfdbfe" stroke-width="1.5"/>

    <!-- Panel header -->
    <rect x="12" y="12" width="338" height="34" fill="#2563eb" rx="6"/>
    <text x="181" y="33" fill="#ffffff"
          font-family="Arial, sans-serif" font-size="13" font-weight="700"
          text-anchor="middle">IODINE — Thyroid Health &amp; Brain Alertness</text>

    <!-- Row 1: Iodized Salt -->
    <rect x="12" y="58" width="338" height="58" fill="#ffffff" rx="6"
          stroke="#93c5fd" stroke-width="1"/>
    <rect x="12" y="58" width="6" height="58" fill="#2563eb" rx="3"/>
    <text x="30" y="76" fill="#1d4ed8"
          font-family="Arial, sans-serif" font-size="11.5" font-weight="700">
      Packaged Iodized Table Salt (KEBS Certified)
    </text>
    <text x="30" y="93" fill="#475569" font-family="Arial, sans-serif" font-size="10.5">
      Fortified daily seasoning; prevents thyroid goitre.
    </text>
    <text x="30" y="108" fill="#64748b" font-family="Arial, sans-serif" font-size="9.5"
          font-style="italic">Always check for the KEBS quality seal on the packet.</text>

    <!-- Row 2: Fish -->
    <rect x="12" y="126" width="338" height="58" fill="#ffffff" rx="6"
          stroke="#93c5fd" stroke-width="1"/>
    <rect x="12" y="126" width="6" height="58" fill="#2563eb" rx="3"/>
    <text x="30" y="144" fill="#1d4ed8"
          font-family="Arial, sans-serif" font-size="11.5" font-weight="700">
      Fresh Lake Fish: Tilapia &amp; Omena (Dagaa)
    </text>
    <text x="30" y="161" fill="#475569" font-family="Arial, sans-serif" font-size="10.5">
      Rich natural marine mineral and complete protein source.
    </text>
    <text x="30" y="176" fill="#64748b" font-family="Arial, sans-serif" font-size="9.5"
          font-style="italic">Widely available and affordable across Kenya.</text>

    <!-- Row 3: Eggs & Milk -->
    <rect x="12" y="194" width="338" height="58" fill="#ffffff" rx="6"
          stroke="#93c5fd" stroke-width="1"/>
    <rect x="12" y="194" width="6" height="58" fill="#2563eb" rx="3"/>
    <text x="30" y="212" fill="#1d4ed8"
          font-family="Arial, sans-serif" font-size="11.5" font-weight="700">
      Dairy Milk &amp; Boiled Eggs
    </text>
    <text x="30" y="229" fill="#475569" font-family="Arial, sans-serif" font-size="10.5">
      Supports sharp brain development and physical growth.
    </text>
    <text x="30" y="244" fill="#64748b" font-family="Arial, sans-serif" font-size="9.5"
          font-style="italic">Add to breakfast daily for sustained energy and focus.</text>

    <!-- Tip box -->
    <rect x="12" y="263" width="338" height="86" fill="#dbeafe" rx="6"
          stroke="#93c5fd" stroke-width="1"/>
    <text x="181" y="284" fill="#1d4ed8"
          font-family="Arial, sans-serif" font-size="11" font-weight="700"
          text-anchor="middle">Deficiency Disorder: Goitre</text>
    <text x="181" y="300" fill="#1e3a8a"
          font-family="Arial, sans-serif" font-size="10" text-anchor="middle">
      Signs: visible swelling or lump at the front
    </text>
    <text x="181" y="316" fill="#1e3a8a"
          font-family="Arial, sans-serif" font-size="10" text-anchor="middle">
      of the neck (enlarged thyroid gland).
    </text>
    <text x="181" y="337" fill="#1d4ed8"
          font-family="Arial, sans-serif" font-size="9.5" font-weight="600"
          text-anchor="middle">Prevention: use iodized salt in every meal.</text>
  </g>

  <!-- Footer -->
  <rect x="36" y="460" width="748" height="1" fill="#e2e8f0"/>
  <text x="410" y="474" fill="#94a3b8"
        font-family="Arial, sans-serif" font-size="9" text-anchor="middle">
    CBC Grade 6 Home Science — Topic 3: Foods and Nutrition
  </text>
</svg>"""


def run_fixes():
    print("=" * 80)
    print("[START] CBC Grade 6 Home Science — Video Replacements + SVG Fix")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
    grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
    subject = Subject.objects.filter(grade=grade, name="Home Science").first()

    # ── Fix 1: Needs, Wants & Budgets video ──────────────────────────────────
    print("\n[1] Needs, Wants & Budgets → Ubongo Kids: Budgeting 101")
    lesson = get_lesson(subject, 2, "Needs, Wants")
    if lesson:
        replace_video_block(
            lesson=lesson,
            old_url_fragment="1F_4-pM-w5U",
            new_url="https://www.youtube.com/watch?v=2r1o5y-6IeM",
            new_title="Watch: Budgeting 101 — Needs, Wants & Making Smart Money Choices",
            new_description=(
                "Ubongo Kids — an African animated educational series — follows Kiduchu "
                "and friends as they receive a limited amount of money to build a new "
                "classroom. The episode teaches learners to list Needs first, separate "
                "Wants, and build a simple budget plan to stretch every shilling further."
            ),
            new_author="Ubongo Kids"
        )

    # ── Fix 2: Food Preservation video ───────────────────────────────────────
    print("\n[2] Food Preservation → TED-Ed: Are Food Preservatives Bad for You?")
    lesson = get_lesson(subject, 3, "Preservation")
    if lesson:
        replace_video_block(
            lesson=lesson,
            old_url_fragment="gPz41u5_J7U",
            new_url="https://www.youtube.com/watch?v=ZJU34yTJL4M",
            new_title="Watch: Are Food Preservatives Bad for You? — The Science of Keeping Food Safe",
            new_description=(
                "TED-Ed explains the science behind how ancient and modern food preservation "
                "methods — salting, smoking, drying, vinegar, and controlled additives — "
                "work by removing the moisture and environment that bacteria need to grow, "
                "keeping food nutritious and safe for weeks or months."
            ),
            new_author="TED-Ed"
        )

    # ── Fix 3: Baking / Cookery video ────────────────────────────────────────
    print("\n[3] Practical Cookery → TED-Ed: The Science of Baking")
    lesson = get_lesson(subject, 3, "Cookery")
    if lesson:
        replace_video_block(
            lesson=lesson,
            old_url_fragment="y6U36582528",
            new_url="https://www.youtube.com/watch?v=n6wpNhyPqM4",
            new_title="Watch: The Science Behind Baking — What Happens Inside an Oven",
            new_description=(
                "TED-Ed uses the example of baking cookies to explain the fascinating "
                "chemistry of dry heat cooking — how the Maillard reaction browns the outer "
                "surface, how CO2 from baking powder makes the dough rise, and why precise "
                "temperature control is the key to perfectly baked goods every time."
            ),
            new_author="TED-Ed"
        )

    # ── Fix 4: Rebuild jumbled Mineral Map SVG ────────────────────────────────
    print("\n[4] Rebuilding 'Local Food Mineral Map: Iron & Iodine Sources' SVG...")
    block = LessonBlock.objects.filter(id=24737).first()
    if block:
        block.content = {
            "title": "Local Food Mineral Map: Iron & Iodine Sources Blueprint",
            "viewBox": "0 0 820 480",
            "description": (
                "Split comparative infographic. Left (red panel): Iron sources — "
                "sukuma wiki/spinach, beef liver, red beans/lentils, deficiency info. "
                "Right (blue panel): Iodine sources — iodized salt, tilapia/omena, "
                "milk/eggs, deficiency info. No emojis. Clean SVG text coordinates."
            ),
            "svg_content": MINERAL_MAP_SVG
        }
        block.save()
        print("  [OK] Mineral Map SVG rebuilt cleanly.")
    else:
        print("  [WARN] Block ID 24737 not found — searching by title...")
        curriculum = Curriculum.objects.filter(name__iexact="CBC").first()
        grade = Grade.objects.filter(curriculum=curriculum, name="Grade 6").first()
        subject2 = Subject.objects.filter(grade=grade, name="Home Science").first()
        topic = subject2.topics.get(order=3)
        for unit in topic.learning_units.all():
            for lesson in unit.lessons.filter(title__icontains="Minerals"):
                b = lesson.blocks.filter(title__icontains="Mineral Map").first()
                if b:
                    b.content = {
                        "title": "Local Food Mineral Map: Iron & Iodine Sources Blueprint",
                        "viewBox": "0 0 820 480",
                        "description": "Rebuilt clean SVG without emojis.",
                        "svg_content": MINERAL_MAP_SVG
                    }
                    b.save()
                    print(f"  [OK] Found and fixed block ID {b.id}.")

    print("\n" + "=" * 80)
    print("[SUCCESS] All 4 fixes applied.")
    print("=" * 80)


if __name__ == "__main__":
    run_fixes()
