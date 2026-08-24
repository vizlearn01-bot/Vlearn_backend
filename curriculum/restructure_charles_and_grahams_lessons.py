#!/usr/bin/env python
"""
restructure_charles_and_grahams_lessons.py
Restructures Lesson 161 (Charles's Law) and Lesson 163 (Graham's Law):
- Embeds scientific hot-air balloon video on Card 4 of Charles's Law.
- Contextually places all 5 Graham's Law videos on their corresponding concept cards.
- Updates introductory phrases to match their new positions.
"""
import sys, os, django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import Lesson, LessonBlock

# ===========================================================================
# 1. Lesson 161: Charles's Law
# ===========================================================================
print("=== Restructuring Lesson 161: Charles's Law ===")

# Update video block 28245 content with scientific hot air balloon video
b28245 = LessonBlock.objects.filter(id=28245).first()
if b28245:
    b28245.content = {
        "url": "https://www.youtube.com/watch?v=KdFxt6Zbmn0",
        "title": "Video Demonstration: The Science of Hot-Air Balloons & Charles's Law",
        "description": "An engaging scientific demonstration showing how heating air causes it to expand and become less dense, creating the buoyant lift that powers hot-air balloons per Charles's Law."
    }
    b28245.title = "Video Demonstration: The Science of Hot-Air Balloons & Charles's Law"
    b28245.page_number = 4
    b28245.order = 8.5
    b28245.save()
    print("  [+] Updated Block #28245 with Hot-Air Balloon video and moved to Card 4.")

# Update Card 4 text block 5754 with intro phrase
b5754 = LessonBlock.objects.filter(id=5754).first()
if b5754 and b5754.content:
    content = b5754.content
    text = content.get('text', '')
    # Remove any old intro callout if present, then append clean callout
    if "> 🎬" in text:
        text = text.split("> 🎬")[0].rstrip()
    intro = "\n\n> 🎬 **Real-World Scientific Demonstration**: Watch the video demonstration below to see how heating air causes thermal expansion, decreases density, and generates buoyant lift in real hot-air balloons!"
    content['text'] = text + intro
    b5754.content = content
    b5754.save()
    print("  [+] Appended hot-air balloon video intro to Block #5754.")

# Update Card 6 block 5757 intro phrase for lab video 28243
b5757 = LessonBlock.objects.filter(id=5757).first()
if b5757 and b5757.content:
    content = b5757.content
    text = content.get('text', '')
    if "> 🎬" in text:
        text = text.split("> 🎬")[0].rstrip()
    intro = "\n\n> 🎬 **Laboratory Experiment Demonstration**: Watch the laboratory experiment video below verifying Charles's Law using a trapped gas volume heated across varying temperatures!"
    content['text'] = text + intro
    b5757.content = content
    b5757.save()
    print("  [+] Updated lab video intro on Block #5757.")

# Renumber Lesson 161 blocks contiguously
for idx, b in enumerate(LessonBlock.objects.filter(lesson_id=161).order_by('page_number', 'order', 'id'), start=1):
    b.order = idx
    b.save(update_fields=['order'])
print("  [+] Renumbered Lesson 161 blocks.")


# ===========================================================================
# 2. Lesson 163: Graham's Law
# ===========================================================================
print("\n=== Restructuring Lesson 163: Graham's Law ===")

# Card 1: Hook & Introductory Diffusion
LessonBlock.objects.filter(id=5773).update(page_number=1, order=1) # learning_goal

b5774 = LessonBlock.objects.filter(id=5774).first()
if b5774 and b5774.content:
    content = b5774.content
    text = content.get('text', '')
    if "> 🎬" in text:
        text = text.split("> 🎬")[0].rstrip()
    intro = "\n\n> 🎬 **Observing Diffusion in Action**: Watch the laboratory demonstrations below showing diffusion in liquids (potassium permanganate in water) and the rapid diffusion of ammonia gas through air!"
    content['text'] = text + intro
    b5774.content = content
    b5774.page_number = 1
    b5774.order = 2
    b5774.save()

LessonBlock.objects.filter(id=28246).update(page_number=1, order=3) # liquid diffusion video
LessonBlock.objects.filter(id=28247).update(page_number=1, order=4) # ammonia in air video
print("  [+] Configured Card 1 (Liquid & Gas Diffusion Videos).")

# Card 2: Theory & Classic Diffusion Tube Setup
LessonBlock.objects.filter(id=28261).update(page_number=2, order=5) # definition_card
LessonBlock.objects.filter(id=5775).update(page_number=2, order=6) # statement
LessonBlock.objects.filter(id=5776).update(page_number=2, order=7) # tube diagram

b5777 = LessonBlock.objects.filter(id=5777).first()
if b5777 and b5777.content:
    content = b5777.content
    text = content.get('text', '')
    if "> 🎬" in text:
        text = text.split("> 🎬")[0].rstrip()
    if "> 🔬" in text:
        text = text.split("> 🔬")[0].rstrip()
    intro = "\n\n> 🎬 **Laboratory Experiment Demonstration**: Watch the classic diffusion tube experiment in action below to see ammonia and hydrochloric acid vapors meet to form a white ammonium chloride ring!\n\n> 🔬 **Interactive Virtual Lab Ahead**: On the next card, launch the interactive diffusion tube simulation to test different gas combinations!"
    content['text'] = text + intro
    b5777.content = content
    b5777.page_number = 2
    b5777.order = 8
    b5777.save()

LessonBlock.objects.filter(id=28248).update(page_number=2, order=9) # NH3 & HCl tube experiment video
print("  [+] Configured Card 2 (Classic Tube Experiment Video).")

# Card 3: Interactive Simulation
LessonBlock.objects.filter(id=28251).update(page_number=3, order=10) # suggested_simulation
print("  [+] Configured Card 3 (Interactive Simulation).")

# Card 4: Worked Calculations & Diffusion Rate Comparisons
LessonBlock.objects.filter(id=5778).update(page_number=4, order=11) # worked_example 1

b5779 = LessonBlock.objects.filter(id=5779).first()
if b5779 and b5779.content:
    content = b5779.content
    text = content.get('text', '')
    if "> 🎬" in text:
        text = text.split("> 🎬")[0].rstrip()
    intro = "\n\n> 🎬 **Comparing Diffusion Rates of Gases**: Watch these two laboratory demonstrations below comparing the diffusion speeds of different gases side-by-side to verify how molecular mass directly controls diffusion rate!"
    content['text'] = text + intro
    b5779.content = content
    b5779.page_number = 4
    b5779.order = 12
    b5779.save()

LessonBlock.objects.filter(id=28249).update(page_number=4, order=13) # Do All Gases Diffuse at Same Rate video
LessonBlock.objects.filter(id=28250).update(page_number=4, order=14) # Video Demonstration: Rate of Diffusion
print("  [+] Configured Card 4 (Comparing Diffusion Rate Videos).")

# Card 5: Common Misconceptions
b5780 = LessonBlock.objects.filter(id=5780).first()
if b5780 and b5780.content:
    content = b5780.content
    text = content.get('text', '')
    if "> 🎬" in text:
        text = text.split("> 🎬")[0].rstrip()
    content['text'] = text
    b5780.content = content
    b5780.page_number = 5
    b5780.order = 15
    b5780.save()
print("  [+] Configured Card 5 (Misconceptions).")

# Card 6: Knowledge Check Questions
LessonBlock.objects.filter(id=5781).update(page_number=6, order=16) # knowledge_check 1
LessonBlock.objects.filter(id=5782).update(page_number=6, order=17) # knowledge_check 2
print("  [+] Configured Card 6 (Practice Questions).")

# Card 7: Summary
LessonBlock.objects.filter(id=5783).update(page_number=7, order=18) # summary
print("  [+] Configured Card 7 (Summary).")

# Final contiguous order renumbering for Lesson 163
for idx, b in enumerate(LessonBlock.objects.filter(lesson_id=163).order_by('page_number', 'order', 'id'), start=1):
    b.order = idx
    b.save(update_fields=['order'])

print("\n✅ Lessons 161 and 163 successfully restructured.")
