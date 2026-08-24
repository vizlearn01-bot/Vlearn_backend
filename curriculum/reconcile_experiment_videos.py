import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import Lesson, LessonBlock, LessonAsset
from Resources.models import ExperimentVideo

RECONCILIATION_MAP = [
    {
        'video_id': 21,
        'lesson_id': 182,
        'page_number': 4,
        'page_title': 'Laboratory Preparation and Drying of Ammonia',
        'title': 'Laboratory Experiment: Preparation and Drying of Ammonia Gas',
        'description': 'Real laboratory demonstration showing the heating of ammonium chloride and calcium hydroxide, upward delivery collection, and drying with calcium oxide.',
    },
    {
        'video_id': 63,
        'lesson_id': 191,
        'page_number': 3,
        'page_title': 'Laboratory Preparation of Chlorine',
        'title': 'Laboratory Experiment: Preparation and Collection of Chlorine Gas',
        'description': 'Laboratory synthesis of chlorine gas via oxidation of concentrated hydrochloric acid using manganese(IV) oxide, gas scrubbing with water, and downward delivery.',
    },
    {
        'video_id': 5,
        'lesson_id': 163,
        'page_number': 4,
        'page_title': 'The Classic HCl and NH3 Diffusion Experiment',
        'title': 'Laboratory Experiment: Diffusion Rates of Ammonia and Hydrogen Chloride Gases',
        'description': 'Demonstration of Graham\'s Law in a glass tube: comparing the diffusion rates of NH3 and HCl gases to form a white ring of solid ammonium chloride.',
    },
    {
        'video_id': 7,
        'lesson_id': 166,
        'page_number': 3,
        'page_title': 'Experimental Determination: Magnesium Oxide',
        'title': 'Laboratory Experiment: Determining the Empirical Formula of Magnesium Oxide',
        'description': 'Crucible combustion of magnesium ribbon, periodic lid venting, and gravimetric calculations to determine the empirical formula MgO.',
    },
    {
        'video_id': 9,
        'lesson_id': 170,
        'page_number': 2,
        'page_title': 'Running a Laboratory Titration',
        'title': 'Laboratory Experiment: Direct Titration of an Acid and a Base',
        'description': 'Standard volumetric analysis technique: pipette handling, burette titration, and phenolphthalein/methyl orange endpoint determination.',
    },
    {
        'video_id': 55,
        'lesson_id': 177,
        'page_number': 2,
        'page_title': 'Laboratory Preparation of Ethene',
        'title': 'Laboratory Experiment: Laboratory Preparation of Ethene Gas',
        'description': 'Catalytic dehydration of ethanol using concentrated sulphuric(VI) acid at 170°C, collection of ethene over water, and bromine water test.',
    },
    {
        'video_id': 18,
        'lesson_id': 185,
        'page_number': 4,
        'page_title': 'The Brown Ring Test for Nitrate Ions',
        'title': 'Laboratory Experiment: The Brown Ring Test for Nitrate Ions',
        'description': 'Qualitative inorganic analysis: adding freshly prepared iron(II) sulphate and concentrated sulphuric(VI) acid to form the brown Fe(H2O)5NO²⁺ ring.',
    },
    {
        'video_id': 45,
        'lesson_id': 188,
        'page_number': 2,
        'page_title': 'Laboratory Synthesis and Bleaching Mechanism',
        'title': 'Laboratory Experiment: Preparation and Properties of Sulphur(IV) Oxide',
        'description': 'Reaction of sodium sulphite with dilute hydrochloric acid, gas collection by downward delivery, and reversible bleaching of litmus paper.',
    },
    {
        'video_id': 52,
        'lesson_id': 193,
        'page_number': 3,
        'page_title': 'Laboratory Preparation & Downward Delivery',
        'title': 'Laboratory Experiment: Laboratory Preparation of Hydrogen Chloride Gas',
        'description': 'Reaction of solid sodium chloride with concentrated sulphuric(VI) acid, drying through sulphuric acid wash bottle, and downward delivery.',
    },
    {
        'video_id': 29,
        'lesson_id': 31,
        'page_number': 5,
        'page_title': 'Laboratory Application: Preparing Insoluble Salts',
        'title': 'Laboratory Experiment: Precipitation of Insoluble Salts',
        'description': 'Double displacement reaction between aqueous solutions to synthesize, filter, wash, and dry pure insoluble salts.',
    },
]

print("=== RECONCILING 10 EXPERIMENT VIDEOS INTO LESSONS ===\n")

for item in RECONCILIATION_MAP:
    video = ExperimentVideo.objects.get(id=item['video_id'])
    lesson = Lesson.objects.get(id=item['lesson_id'])
    
    # 1. Check if a video_ref block already exists for this video in the lesson
    existing_blocks = LessonBlock.objects.filter(
        lesson=lesson,
        block_type='video_ref',
        content__cloudflare_video_id=video.cloudflare_video_id
    )
    
    if existing_blocks.exists():
        block = existing_blocks.first()
        print(f"[EXISTS] Block [{block.id}] in Lesson [{lesson.id}] {lesson.title}")
    else:
        # Check max order in lesson
        max_order = max([b.order for b in LessonBlock.objects.filter(lesson=lesson)] or [0])
        block = LessonBlock(
            lesson=lesson,
            order=max_order + 1
        )
    
    block.block_type = 'video_ref'
    block.component_type = 'video_ref'
    block.title = item['title']
    block.page_number = item['page_number']
    block.page_title = item['page_title']
    block.content = {
        'title': item['title'],
        'description': item['description'],
        'cloudflare_video_id': video.cloudflare_video_id,
        'playback_url': video.playback_url,
        'duration': video.duration,
        'difficulty': video.difficulty,
        'experiment_id': video.id,
        'resolved_url': video.playback_url,
    }
    block.metadata = {
        'video_type': 'experiment_video',
        'cloudflare_video_id': video.cloudflare_video_id,
        'playback_url': video.playback_url,
        'duration': video.duration,
        'experiment_id': video.id,
    }
    block.save()
    print(f"Saved Block [{block.id}] for Lesson [{lesson.id}] \"{lesson.title}\"")

    # 2. Attach / Update LessonAsset
    asset, created = LessonAsset.objects.get_or_create(
        lesson=lesson,
        title=item['title'],
        defaults={
            'asset_type': 'video',
            'source_type': 'knowledge_repository',
            'storage_type': 'url',
            'status': 'attached',
            'url': video.playback_url,
            'metadata': {
                'cloudflare_video_id': video.cloudflare_video_id,
                'playback_url': video.playback_url,
                'duration': video.duration,
                'experiment_id': video.id,
            }
        }
    )
    if not created:
        asset.asset_type = 'video'
        asset.url = video.playback_url
        asset.metadata = {
            'cloudflare_video_id': video.cloudflare_video_id,
            'playback_url': video.playback_url,
            'duration': video.duration,
            'experiment_id': video.id,
        }
        asset.status = 'attached'
        asset.save()
    
    asset.blocks.add(block)
    print(f"  -> Attached Asset [{asset.id}] to Block [{block.id}]\n")

print("All 10 experiment videos reconciled successfully!")
