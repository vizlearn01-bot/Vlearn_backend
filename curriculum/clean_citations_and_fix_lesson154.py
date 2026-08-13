import os
import sys
import re
import django

sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import LessonBlock

def run_cleanup():
    print('=== 1. Repairing Block 4058 (Lesson 154: How We Use Radioisotopes) ===')
    try:
        b4058 = LessonBlock.objects.get(id=4058)
        b4058.content = {
            'text': '''Almost all modern applications of radioisotopes rely on two basic scientific principles:

```
                          HOW WE USE RADIOISOTOPES
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
   PRINCIPLE 1: AS TRACERS                                 PRINCIPLE 2: AS ENERGY SOURCES
 (Penetration & Easy Detection)                          (Ionization & Cell Destruction)
 • Small, harmless amounts introduced.                   • High-energy, intense radiation beams.
 • Radiation tracked externally by GM counters.          • Destroys targeted cancer cells / microbes.
 • Detects underground pipe leaks.                       • Radiotherapy (Cobalt-60).
 • Medical diagnosis (e.g. Iodine-131 thyroid scans).    • Food preservation and gamma sterilization.
```

### 1. Principle 1: Radioactive Tracers (Tracking Movement and Location)
Because radioactive isotopes emit radiation ($\\alpha$, $\\beta$, or $\\gamma$) that passes through materials and can be detected by Geiger-Müller (GM) counters even in minute quantities, they act as sensitive "chemical detectives."
* **Medical Diagnostics**: A patient ingests or is injected with a tiny, short-lived radioactive tracer. As the isotope travels through organs, doctors use external radiation detectors to image organ function and locate blockages without invasive surgery.
* **Engineering & Industry**: Tracers added to liquids in underground pipes reveal the exact position of hidden cracks or leaks without digging up miles of pipeline.
* **Agricultural Research**: Radioactive phosphorus-32 added to fertilizer allows scientists to measure how quickly and efficiently plant roots absorb vital nutrients.

### 2. Principle 2: High-Energy Radiation Sources (Targeted Destruction and Modification)
High doses of ionizing radiation (especially energetic gamma rays) carry sufficient energy to break chemical bonds and damage the DNA of living cells or microorganisms.
* **Medicine (Cancer Radiotherapy)**: Targeted beams of gamma rays from Cobalt-60 destroy rapidly dividing cancer cells while minimizing damage to surrounding healthy tissue.
* **Food Preservation & Sterilization**: High-dose gamma radiation kills harmful bacteria, molds, and insects on packaged food and sterilizes medical equipment (syringes, gloves, scalpel blades) without heat or moisture.
* **Thickness Control in Manufacturing**: The degree of beta or gamma penetration through moving sheets of paper, plastic, or metal foil is continuously measured to maintain uniform product thickness.'''
        }
        b4058.save()
        print('Successfully updated Block 4058 with complete text and full ASCII chart!')
    except Exception as e:
        print(f'Error updating Block 4058: {e}')

    print('\n=== 2. Stripping Citation Markers from all Curriculum Blocks ===')
    citation_re = re.compile(r'\s*\[\s*\d+(?:\s*,\s*\d+)*\s*\]')

    def clean_data(data):
        if isinstance(data, str):
            return citation_re.sub('', data)
        elif isinstance(data, dict):
            return {k: clean_data(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [clean_data(item) for item in data]
        return data

    cleaned_count = 0
    for b in LessonBlock.objects.all():
        orig_str = str(b.content)
        if citation_re.search(orig_str):
            b.content = clean_data(b.content)
            b.save()
            cleaned_count += 1

    print(f'Cleaned citation numbers from {cleaned_count} lesson blocks across the curriculum!')

if __name__ == '__main__':
    run_cleanup()
