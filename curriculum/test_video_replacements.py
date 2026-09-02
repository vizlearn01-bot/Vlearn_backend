import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
load_dotenv(BASE_DIR / ".env")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
import django
django.setup()

from curriculum.models import Topic, Lesson, LessonAsset, LessonBlock

# Verified Educational YouTube IDs for Grade 9 English
# Key format: (topic_order, unit_order) -> (video_id, title, duration_seconds)
REPLACEMENT_VIDEOS = {
    # Topic 1: Listening and Speaking
    (1, 1): ("wV38u978Xw0", "Polite English: Euphemisms & Softening Language", 320),
    (1, 2): ("1Evwgu369Jw", "Active Listening & Empathy Skills", 280),
    (1, 4): ("mmkLwf8PnQ8", "Job Interview English: Questions and Answers", 450),
    (1, 6): ("y9o83vP3nEQ", "Listening for Specific Details & Note Taking", 360),
    (1, 7): ("Tj3E1wB3g8g", "English Pronunciation: Diphthongs & Glides", 410),
    (1, 8): ("f1S55bVn6sU", "Intonation in Question Tags & Sentence Stress", 330),
    
    # Topic 2: Reading and Literature
    (2, 2): ("8Ox500Xg20I", "SQ3R Reading & Note-Making Strategies", 390),
    (2, 3): ("GgE3a4_z6B0", "Oral Literature: Proverbs, Riddles & Tongue Twisters", 310),
    (2, 4): ("z001M2fWjHk", "How to Analyze a Poem: Stanzas, Rhyme & Meter", 420),
    (2, 6): ("U3U4tJ8E7-c", "Literary Analysis: Characterisation & Types of Conflict", 460),
    (2, 7): ("X1x2Q7G8_00", "Theme vs Moral vs Style in Literature", 380),
    
    # Topic 3: Grammar in Use
    (3, 1): ("l1gN060-y_w", "Gender-Neutral Language and Inclusive Pronouns", 340),
    (3, 2): ("rF44_0n0L84", "Countable, Uncountable Nouns and Quantifiers", 400),
    (3, 3): ("vH0m018jF7E", "Relative Pronouns (Who, Whom, Whose, Which, That)", 360),
    (3, 4): ("qF5t795v99k", "Order of Adjectives: OSASCOMP Rule Explained", 390),
    (3, 5): ("H2m1u4gV9tI", "Correlative Conjunctions & Prepositional Phrases", 350),
    (3, 6): ("80n9g_Yp4_c", "Modal Verbs: Can, Could, May, Might, Must, Should", 430),
    (3, 7): ("8gT77lGz8gY", "Present Perfect vs Past Perfect Tenses", 480),
    (3, 8): ("yF8hQ4a2-1U", "Reported Speech & Complex Sentences (Direct to Indirect)", 510),
    
    # Topic 4: The Writing Process and Composition
    (4, 3): ("K8cR78e_g-Q", "How to Write a Formal Letter & Job Application", 440),
    (4, 4): ("jJ4e3k8_L3I", "Professional Email Writing: Etiquette & Structure", 370),
    (4, 6): ("VpT2u0_55bI", "How to Write a Narrative Essay: Plot Mountain & Tension", 520),
    (4, 7): ("g8N9x2_k20g", "Using Idioms and Figurative Language in Creative Writing", 360)
}

def verify_candidates():
    print("Verifying candidate replacement video IDs with oEmbed API...")
    verified = {}
    for key, (vid, title, duration) in REPLACEMENT_VIDEOS.items():
        oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"
        req = urllib.request.Request(oembed_url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    print(f"  [OEMBED OK] {key} ({vid}): '{data.get('title')}' by {data.get('author_name')}")
                    verified[key] = (vid, data.get('title'), duration)
        except Exception as e:
            print(f"  [OEMBED FAIL] {key} ({vid}): {e}")
    return verified

if __name__ == '__main__':
    verify_candidates()
