import os, sys, django, json, re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

print("1. Fixing Boyle's Law Misconception (Block 5745)...")
b5745 = LessonBlock.objects.get(id=5745)
b5745.content = {
    "text": (
        "### Does doubling the pressure double the volume?\n"
        "No! Pressure and volume have an **inverse** relationship, not a direct one. "
        "If you double the pressure ($2 \\times P$), the volume is cut in half ($\\frac{1}{2} V$).\n\n"
        "### Does Boyle's Law apply if temperature changes?\n"
        "No. Boyle's Law is strictly valid only when the temperature remains perfectly constant. "
        "If the gas heats up while being compressed, temperature expansion will interfere with the pressure-volume ratio."
    )
}
b5745.save()
print("  Block 5745 content set cleanly.")

print("2. Fixing Charles's Law Misconception (Block 5757)...")
b5757 = LessonBlock.objects.get(id=5757)
b5757.content = {
    "text": (
        "### Why can't we use Celsius directly in Charles's Law calculations?\n"
        "The Celsius scale sets its zero at the arbitrary freezing point of water ($0^\\circ\\text{C}$), "
        "which is not the point of zero kinetic energy. If you calculated $\\frac{V_1}{0^\\circ\\text{C}}$, "
        "you would be dividing by zero, which is mathematically undefined!\n\n"
        "Only the Kelvin scale starts at true physical zero energy ($0\\text{ K}$), making $V$ directly proportional to $T$."
    )
}
b5757.save()
print("  Block 5757 content set cleanly.")

print("3. Fixing Combined Gas Law Misconception (Block 5769)...")
b5769 = LessonBlock.objects.get(id=5769)
b5769.content = {
    "text": (
        "### How do we handle different pressure units?\n"
        "$760\\text{ mmHg}$, $1\\text{ atm}$, and $1.01325 \\times 10^5\\text{ Pa}$ all describe identical standard atmospheric pressure. "
        "When solving $\\frac{P_1V_1}{T_1} = \\frac{P_2V_2}{T_2}$, you do not need to convert to Pascals as long as $P_1$ and $P_2$ are in the **same unit**.\n\n"
        "### But what about temperature?\n"
        "**Never calculate with Celsius!** Temperatures MUST always be in Kelvin ($T = t + 273$) because the gas laws depend on absolute kinetic energy."
    )
}
b5769.save()
print("  Block 5769 content set cleanly.")

print("4. Fixing Graham's Law Misconception (Block 5780)...")
b5780 = LessonBlock.objects.get(id=5780)
b5780.content = {
    "text": (
        "### Does a gas with twice the mass take twice as long to diffuse?\n"
        "No! Diffusion rates depend on the **square root** of the molecular mass ($\\sqrt{M_r}$), not a direct linear ratio.\n\n"
        "If Gas B has $4\\times$ the molar mass of Gas A, it diffuses $\\sqrt{4} = 2\\times$ slower (takes twice as long), not 4 times as long!\n\n"
        "### Does a higher rate mean more or less time?\n"
        "A faster rate means **less time** ($R \\propto \\frac{1}{t}$). Thus, the time ratio is inverted compared to the rate ratio:\n"
        "$$\\frac{t_2}{t_1} = \\frac{R_1}{R_2} = \\sqrt{\\frac{M_2}{M_1}}$$"
    )
}
b5780.save()
print("  Block 5780 content set cleanly.")

print("5. Auditing all other common_misconception blocks across the entire database...")
COMMON_WORDS = set(['the', 'and', 'that', 'have', 'for', 'not', 'with', 'you', 'this', 'but', 'from', 'they', 'say', 'her', 'she', 'will', 'one', 'all', 'would', 'there', 'their', 'what', 'out', 'about', 'who', 'get', 'which', 'when', 'make', 'can', 'like', 'time', 'just', 'know', 'take', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'inverse', 'relationship', 'cut', 'half', 'double', 'doubles', 'doubling', 'pressure', 'volume', 'temperature'])

mis_count = 0
for b in LessonBlock.objects.filter(block_type='common_misconception'):
    raw = json.dumps(b.content)
    text_val = b.content.get('text', '') if isinstance(b.content, dict) else (b.content if isinstance(b.content, str) else '')
    if not text_val: continue
    
    # Check if text_val has display math wrapping prose or unescaped control chars
    new_text = text_val
    # Strip control chars
    new_text = new_text.replace('\x0c', '\\f').replace('\x0b', '\\v').replace('\x08', '\\b').replace('\x07', '\\a')
    new_text = re.sub(r'(?<!\\)frac\{', r'\\frac{', new_text)
    new_text = re.sub(r'(?<!\\)times\b', r'\\times', new_text)
    
    # Check for prose in $...$
    def fix_inline(match):
        inner = match.group(1).strip()
        words = re.findall(r'[a-zA-Z]{3,}', inner)
        prose_words = [w.lower() for w in words if w.lower() in COMMON_WORDS]
        if len(prose_words) >= 2:
            # Unwrap prose, re-wrap variables
            clean = inner.replace('$$', '')
            clean = re.sub(r'([a-zA-Z])_([0-9a-zA-Z]+)', r'$\1_\2$', clean)
            clean = re.sub(r'(?<!\$)\\(?:frac|sqrt)\{[^}]+\}(?:\{[^}]+\})?(?!\$)', r'$\g<0>$', clean)
            return clean
        return match.group(0)

    new_text = re.sub(r'\$([^\$\n]+)\$', fix_inline, new_text)
    
    if new_text != text_val:
        if isinstance(b.content, dict):
            b.content['text'] = new_text
        else:
            b.content = new_text
        b.save()
        mis_count += 1
        print(f"  Fixed misconception Block {b.id} in Lesson {b.lesson_id}: {b.title}")

print(f"\nCompleted! Fixed {mis_count} misconception blocks.")
