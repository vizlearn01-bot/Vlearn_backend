import os, sys, re, django
sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from django.db import transaction
from curriculum.models import Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset

g9 = Grade.objects.get(id=18)
cre = Subject.objects.get(id=50)

with transaction.atomic():
    # ─── 1. TOPIC 1 LESSON 5: Industrial Action, Child Labor, and the Role of the Church ───
    t1 = Topic.objects.get(subject=cre, order=1)
    u1_5, _ = LearningUnit.objects.get_or_create(
        topic=t1, order=5,
        defaults={'name': 'Industrial Action, Child Labor, and the Role of the Church', 'description': 'Christian perspectives on industrial disputes, strikes, child labor, and the prophetic role of the Church in protecting vulnerable children.'}
    )
    u1_5.name = 'Industrial Action, Child Labor, and the Role of the Church'
    u1_5.save()
    u1_5.lessons.all().delete()
    
    l1_5 = Lesson.objects.create(
        topic=t1, learning_unit=u1_5,
        title='Industrial Action, Child Labor, and the Role of the Church',
        status='published', version=1,
        immutable_metadata={'grade': 'Grade 9', 'subject': 'CRE', 'topic_order': 1, 'unit_order': 5}
    )

    svg1_5 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Cycle of Child Labor vs. Educated Youth &amp; Church Intervention</text>
  <rect x="40" y="80" width="320" height="320" fill="#1e293b" stroke="#ef4444" stroke-width="2" rx="10"/>
  <text x="200" y="115" text-anchor="middle" fill="#f87171" font-family="sans-serif" font-size="16" font-weight="bold">Cycle of Child Labor (Poverty Trap)</text>
  <rect x="60" y="135" width="280" height="45" fill="#334155" rx="6"/>
  <text x="200" y="162" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="13">1. Extreme Family Poverty &amp; Greed</text>
  <rect x="60" y="195" width="280" height="45" fill="#334155" rx="6"/>
  <text x="200" y="222" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="13">2. School Dropout &amp; Hazardous Labor</text>
  <rect x="60" y="255" width="280" height="45" fill="#334155" rx="6"/>
  <text x="200" y="282" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="13">3. Stunted Physical &amp; Mental Growth</text>
  <rect x="60" y="315" width="280" height="45" fill="#334155" rx="6"/>
  <text x="200" y="342" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="13">4. Chronic Lifelong Disempowerment</text>
  <rect x="440" y="80" width="320" height="320" fill="#1e293b" stroke="#10b981" stroke-width="2" rx="10"/>
  <text x="600" y="115" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="16" font-weight="bold">Church &amp; Community Empowerment</text>
  <rect x="460" y="135" width="280" height="45" fill="#334155" rx="6"/>
  <text x="600" y="162" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="13">1. Rescue Centers &amp; Feeding Programs</text>
  <rect x="460" y="195" width="280" height="45" fill="#334155" rx="6"/>
  <text x="600" y="222" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="13">2. Free Basic Education &amp; TVET Skills</text>
  <rect x="460" y="255" width="280" height="45" fill="#334155" rx="6"/>
  <text x="600" y="282" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="13">3. Holistic Pastoral Care &amp; Mentorship</text>
  <rect x="460" y="315" width="280" height="45" fill="#334155" rx="6"/>
  <text x="600" y="342" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="13">4. Empowered, Self-Reliant Adults</text>
</svg>"""

    img1_5 = LessonAsset.objects.create(
        lesson=l1_5, asset_type='image', source_type='external', storage_type='url', status='attached',
        title='Children in Education Overcoming Child Labor',
        description='Kenyan school children engaged in classroom learning, reflecting the right to basic education.',
        url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Kenyan_pupils_in_class.jpg/800px-Kenyan_pupils_in_class.jpg',
        metadata={'author': 'USAID Kenya', 'licensing': 'Public Domain'}
    )
    svg_a1_5 = LessonAsset.objects.create(
        lesson=l1_5, asset_type='diagram', source_type='ai_generated', storage_type='url', status='attached',
        title='Cycle of Child Labor vs Church Empowerment',
        url='https://vlearn.africa/assets/cre/t1_l5.svg',
        metadata={'svg_xml': svg1_5, 'viewBox': '0 0 800 450', 'theme': '#0f172a'}
    )
    yt1_5 = LessonAsset.objects.create(
        lesson=l1_5, asset_type='youtube', source_type='external', storage_type='url', status='attached',
        title='BibleProject: Generosity and Justice in the Kingdom',
        url='https://www.youtube.com/watch?v=A14THPoc4-4',
        metadata={'youtube_id': 'A14THPoc4-4'}
    )

    # Card 1
    b = LessonBlock.objects.create(
        lesson=l1_5, page_number=1, page_title='Discovery & Objectives', order=10, component_order=1,
        block_type='suggested_image', component_type='suggested_image', title='Children in Education Overcoming Child Labor',
        content={'title': 'Children in Education Overcoming Child Labor', 'url': img1_5.url, 'caption': img1_5.description, 'licensing': 'Public Domain'}
    )
    b.assets.add(img1_5)
    LessonBlock.objects.create(
        lesson=l1_5, page_number=1, page_title='Discovery & Objectives', order=20, component_order=2,
        block_type='learning_goal', component_type='learning_goal', title='Lesson Objectives',
        content={'goals': ['Explain Christian teachings on fair wages and prompt payment', 'Analyze the causes and consequences of industrial action (strikes)', 'Describe the physical and psychological effects of child labor and the response of the Church']}
    )
    LessonBlock.objects.create(
        lesson=l1_5, page_number=1, page_title='Discovery & Objectives', order=30, component_order=3,
        block_type='concept_explanation', component_type='concept_explanation', title='Fair Wages and Child Protection Hook',
        content={'markdown': 'Every person who works deserves fair pay, and every child deserves an education. When employers exploit workers or force children to do dangerous manual labor, social justice is broken. How does Christianity respond to strikes and child exploitation?'}
    )

    # Card 2
    LessonBlock.objects.create(
        lesson=l1_5, page_number=2, page_title='Scriptural Exegesis', order=40, component_order=1,
        block_type='concept_explanation', component_type='concept_explanation', title='Core Biblical Foundations on Wages and Justice',
        content={'markdown': 'Deuteronomy 24:14-15 teaches that we must not take advantage of a hired worker who is poor and needy. Pay them their wages each day before sunset. Jeremiah 22:13 warns woe to him who makes his neighbors work for nothing without paying wages.'}
    )
    LessonBlock.objects.create(
        lesson=l1_5, page_number=2, page_title='Scriptural Exegesis', order=45, component_order=2,
        block_type='concept_explanation', component_type='concept_explanation', title='Theological Principles of Workplace Justice',
        content={'markdown': 'The Bible teaches that withholding wages from vulnerable laborers is a grievous sin. Human beings are created in God image, and children are a sacred heritage. Exploiting children for cheap labor denies their God-given dignity and education.'}
    )

    # Card 3
    b_diag = LessonBlock.objects.create(
        lesson=l1_5, page_number=3, page_title='Pedagogical Diagram', order=50, component_order=1,
        block_type='suggested_diagram', component_type='suggested_diagram', title='The Cycle of Child Labor vs Church Intervention',
        content={'title': 'The Cycle of Child Labor vs Church Intervention', 'svg': svg1_5, 'svg_xml': svg1_5}
    )
    b_diag.assets.add(svg_a1_5)
    LessonBlock.objects.create(
        lesson=l1_5, page_number=3, page_title='Pedagogical Diagram', order=60, component_order=2,
        block_type='concept_explanation', component_type='concept_explanation', title='Deep Dive: Industrial Action, Strikes, and Child Exploitation',
        content={'markdown': 'Strikes occur when workers collectively stop working to protest poor pay or dangerous conditions. While workers have the right to fair treatment, Christian ethics encourage peaceful dialogue, collective bargaining, and avoiding violence or property damage.'}
    )

    # Card 4
    LessonBlock.objects.create(
        lesson=l1_5, page_number=4, page_title='Practical Application', order=70, component_order=1,
        block_type='step_process', component_type='step_process', title='Framework: 4-Step Christian Conflict Resolution and Child Protection',
        content={'title': 'Framework: 4-Step Christian Conflict Resolution and Child Protection', 'steps': [{'step': 1, 'title': 'Early Grievance Recognition', 'description': 'Identify unfair workplace conditions or child distress before escalation.'}, {'step': 2, 'title': 'Honest & Peaceful Dialogue', 'description': 'Engage in open negotiation between workers and management without property destruction.'}, {'step': 3, 'title': 'Community Intervention & Reporting', 'description': 'Report child labor cases to Childline 116, village elders, and local authorities.'}, {'step': 4, 'title': 'Restorative Support & Education', 'description': 'Reintegrate rescued children into schools with holistic psychosocial support.'}]}
    )
    LessonBlock.objects.create(
        lesson=l1_5, page_number=4, page_title='Practical Application', order=75, component_order=2,
        block_type='concept_explanation', component_type='concept_explanation', title='Kenyan Real-World Context & Child Protection Laws',
        content={'markdown': 'Under Kenya Children Act (2022) and Constitution (Article 53), every child has the right to free and compulsory basic education and protection from hazardous work. The Church collaborates with Childline Kenya (Toll-Free 116) and local administrators to rescue vulnerable minors.'}
    )

    # Card 5
    b_yt = LessonBlock.objects.create(
        lesson=l1_5, page_number=5, page_title='Multimedia & Reflection', order=80, component_order=1,
        block_type='suggested_video', component_type='suggested_video', title='BibleProject: Justice and Compassion in Society',
        content={'title': 'BibleProject: Justice and Compassion in Society', 'url': yt1_5.url, 'youtube_id': 'A14THPoc4-4', 'description': yt1_5.description}
    )
    b_yt.assets.add(yt1_5)
    LessonBlock.objects.create(
        lesson=l1_5, page_number=5, page_title='Multimedia & Reflection', order=90, component_order=2,
        block_type='concept_explanation', component_type='concept_explanation', title='Ethical Reflection on Greed vs Compassion',
        content={'markdown': 'Reflect on how human greed drives people to exploit others for cheap labor. How can you be a voice of compassion and justice for vulnerable children in your community?'}
    )

    # Card 6
    LessonBlock.objects.create(
        lesson=l1_5, page_number=6, page_title='Mastery Check', order=100, component_order=1,
        block_type='summary', component_type='summary', title='Summary & Key Takeaways',
        content={'points': ['The Bible mandates timely and fair wages for all laborers (Deut 24:14-15).', 'Industrial disputes must be resolved through peaceful dialogue, fairness, and mutual respect.', 'Child labor is a violation of children's rights that perpetuates cycles of poverty.', 'The Church plays a vital prophetic and practical role in rescuing vulnerable children and providing education.']}
    )
    LessonBlock.objects.create(
        lesson=l1_5, page_number=6, page_title='Mastery Check', order=110, component_order=2,
        block_type='knowledge_check', component_type='knowledge_check', title='Knowledge Check: Labor Disputes and Christian Ethics',
        content={'check_type': 'multiple_choice', 'question': 'What is the Christian view on resolving labor disputes and strikes?', 'options': ['A) Workers should destroy company property to get their demands met quickly.', 'B) Employers should ignore workers and hire children to replace them.', 'C) Both parties should engage in honest dialogue, ensure fair wages, and maintain peaceful communication.', 'D) Workers should go on strike indefinitely without seeking negotiation.'], 'answer': 'C', 'explanation': 'Christian ethics advocate for peace, fairness, and open communication to resolve labor disputes constructively without violence.'}
    )

    print('Topic 1 Lesson 5 ingested successfully!')

    # ─── 2. TOPIC 2 LESSON 3: Responsible Sexual Behavior and Fostering Purity ───
    t2 = Topic.objects.get(subject=cre, order=2)
    u2_3, _ = LearningUnit.objects.get_or_create(
        topic=t2, order=3,
        defaults={'name': 'Responsible Sexual Behavior and Fostering Purity', 'description': 'Christian moral values and practical life skills including assertiveness and self-control to maintain sexual purity.'}
    )
    u2_3.name = 'Responsible Sexual Behavior and Fostering Purity'
    u2_3.save()
    u2_3.lessons.all().delete()

    l2_3 = Lesson.objects.create(
        topic=t2, learning_unit=u2_3,
        title='Responsible Sexual Behavior and Fostering Purity',
        status='published', version=1,
        immutable_metadata={'grade': 'Grade 9', 'subject': 'CRE', 'topic_order': 2, 'unit_order': 3}
    )

    svg2_3 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" fill="#0f172a" rx="12"/>
  <text x="400" y="40" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="20" font-weight="bold">The Purity Shield: Moral Values &amp; Life Skills</text>
  <circle cx="400" cy="240" r="160" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="400" cy="240" r="115" fill="#0f172a" stroke="#34d399" stroke-width="3"/>
  <circle cx="400" cy="240" r="70" fill="#334155" stroke="#f59e0b" stroke-width="3"/>
  <text x="400" y="235" text-anchor="middle" fill="#fbbf24" font-family="sans-serif" font-size="14" font-weight="bold">SELF-CONTROL</text>
  <text x="400" y="255" text-anchor="middle" fill="#cbd5e1" font-family="sans-serif" font-size="11">Holy Spirit Power</text>
  <text x="400" y="160" text-anchor="middle" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold">DECISION-MAKING &amp; VALUES</text>
  <text x="400" y="110" text-anchor="middle" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">ASSERTIVENESS (SAYING NO)</text>
  <text x="160" y="410" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="12">Outer Layer: Clear Boundaries</text>
  <text x="400" y="410" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="12">Middle Layer: Ethical Reflection</text>
  <text x="640" y="410" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="12">Core: Spiritual Armor (1 Cor 6:19)</text>
</svg>"""

    img2_3 = LessonAsset.objects.create(
        lesson=l2_3, asset_type='image', source_type='external', storage_type='url', status='attached',
        title='Christian Youth Mentorship and Fellowship',
        description='Youth engaging in positive peer fellowship, character development, and mentorship.',
        url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Youth_Group_Fellowship.jpg/800px-Youth_Group_Fellowship.jpg',
        metadata={'author': 'Wikimedia Commons', 'licensing': 'CC BY-SA 4.0'}
    )
    svg_a2_3 = LessonAsset.objects.create(
        lesson=l2_3, asset_type='diagram', source_type='ai_generated', storage_type='url', status='attached',
        title='The Purity Shield Diagram',
        url='https://vlearn.africa/assets/cre/t2_l3.svg',
        metadata={'svg_xml': svg2_3, 'viewBox': '0 0 800 450', 'theme': '#0f172a'}
    )
    yt2_3 = LessonAsset.objects.create(
        lesson=l2_3, asset_type='youtube', source_type='external', storage_type='url', status='attached',
        title='BibleProject: 1 Corinthians — The Body as the Temple of the Spirit',
        url='https://www.youtube.com/watch?v=yiSjX3q3hdc',
        metadata={'youtube_id': 'yiSjX3q3hdc'}
    )

    # Card 1
    b = LessonBlock.objects.create(
        lesson=l2_3, page_number=1, page_title='Discovery & Objectives', order=10, component_order=1,
        block_type='suggested_image', component_type='suggested_image', title='Christian Youth Mentorship and Fellowship',
        content={'title': 'Christian Youth Mentorship and Fellowship', 'url': img2_3.url, 'caption': img2_3.description, 'licensing': 'CC BY-SA 4.0'}
    )
    b.assets.add(img2_3)
    LessonBlock.objects.create(
        lesson=l2_3, page_number=1, page_title='Discovery & Objectives', order=20, component_order=2,
        block_type='learning_goal', component_type='learning_goal', title='Lesson Objectives',
        content={'goals': ['Define responsible sexual behavior and the practice of chastity (abstinence)', 'List core Christian moral values needed to maintain sexual purity', 'Apply key life skills (assertiveness, decision-making, self-awareness) to resist negative peer pressure']}
    )
    LessonBlock.objects.create(
        lesson=l2_3, page_number=1, page_title='Discovery & Objectives', order=30, component_order=3,
        block_type='concept_explanation', component_type='concept_explanation', title='Standing Strong Against Peer Pressure Hook',
        content={'markdown': 'Have you ever felt pressured by peers to compromise your moral standards? Saying "No" with confidence requires courage, clear boundaries, and internal spiritual convictions. This lesson equips you with the moral armor and life skills to maintain purity.'}
    )

    # Card 2
    LessonBlock.objects.create(
        lesson=l2_3, page_number=2, page_title='Scriptural Exegesis', order=40, component_order=1,
        block_type='concept_explanation', component_type='concept_explanation', title='Core Biblical Texts on Sanctification and Purity',
        content={'markdown': '1 Corinthians 6:18-20 commands us to flee from sexual immorality. Our bodies are temples of the Holy Spirit who is in us. You are not your own; you were bought at a price. 1 Thessalonians 4:3-4 teaches that it is God's will for us to be sanctified and avoid sexual immorality.'}
    )
    LessonBlock.objects.create(
        lesson=l2_3, page_number=2, page_title='Scriptural Exegesis', order=45, component_order=2,
        block_type='concept_explanation', component_type='concept_explanation', title='Theological Meaning: The Body as God Temple',
        content={'markdown': 'Christians believe our physical bodies are sacred sanctuaries where the Holy Spirit resides. Fleeing sexual immorality is not merely an external rule, but a response of love and reverence for God who created and redeemed us.'}
    )

    # Card 3
    b_diag = LessonBlock.objects.create(
        lesson=l2_3, page_number=3, page_title='Pedagogical Diagram', order=50, component_order=1,
        block_type='suggested_diagram', component_type='suggested_diagram', title='The Purity Shield Architecture',
        content={'title': 'The Purity Shield Architecture', 'svg': svg2_3, 'svg_xml': svg2_3}
    )
    b_diag.assets.add(svg_a2_3)
    LessonBlock.objects.create(
        lesson=l2_3, page_number=3, page_title='Pedagogical Diagram', order=60, component_order=2,
        block_type='concept_explanation', component_type='concept_explanation', title='Deep Dive: Moral Values and Defensive Life Skills',
        content={'markdown': 'Responsible sexual behavior means exercising complete self-control in obedience to God's commands, practicing chastity and abstinence before marriage. Key life skills include assertiveness, decision-making, and self-awareness.'}
    )

    # Card 4
    LessonBlock.objects.create(
        lesson=l2_3, page_number=4, page_title='Practical Application', order=70, component_order=1,
        block_type='step_process', component_type='step_process', title='Framework: 4-Step Boundary Setting Guide for Teenage Friendships',
        content={'title': 'Framework: 4-Step Boundary Setting Guide for Teenage Friendships', 'steps': [{'step': 1, 'title': 'Define Non-Negotiable Boundaries', 'description': 'Decide in advance never to compromise on physical purity or suggestive media.'}, {'step': 2, 'title': 'Communicate Assertively', 'description': 'Clearly state your values to friends: "I choose to honor God and stay pure."' }, {'step': 3, 'title': 'Avoid High-Risk Environments', 'description': 'Refuse unchaperoned isolated settings and unsupervised late-night parties.'}, {'step': 4, 'title': 'Cultivate Positive Accountability', 'description': 'Surround yourself with like-minded friends, mentors, and church youth leaders.'}]}
    )
    LessonBlock.objects.create(
        lesson=l2_3, page_number=4, page_title='Practical Application', order=75, component_order=2,
        block_type='concept_explanation', component_type='concept_explanation', title='Kenyan Real-World Context: Navigating Digital Media & Peer Pressure',
        content={'markdown': 'In modern Kenya, teenagers encounter suggestive content on social media and peer pressure. Practicing digital hygiene, unfollowing inappropriate pages, and participating in Christian unions (CU) or youth mentorship clubs provide essential community support.'}
    )

    # Card 5
    b_yt = LessonBlock.objects.create(
        lesson=l2_3, page_number=5, page_title='Multimedia & Reflection', order=80, component_order=1,
        block_type='suggested_video', component_type='suggested_video', title='BibleProject: 1 Corinthians — The Body as the Temple of the Spirit',
        content={'title': 'BibleProject: 1 Corinthians — The Body as the Temple of the Spirit', 'url': yt2_3.url, 'youtube_id': 'yiSjX3q3hdc', 'description': yt2_3.description}
    )
    b_yt.assets.add(yt2_3)
    LessonBlock.objects.create(
        lesson=l2_3, page_number=5, page_title='Multimedia & Reflection', order=90, component_order=2,
        block_type='concept_explanation', component_type='concept_explanation', title='Spiritual Reflection on Living as God Temple',
        content={'markdown': 'Pray for the strength of the Holy Spirit to guard your heart, eyes, and mind daily. How can setting proactive boundaries protect your future, health, and relationship with God?'}
    )

    # Card 6
    LessonBlock.objects.create(
        lesson=l2_3, page_number=6, page_title='Mastery Check', order=100, component_order=1,
        block_type='summary', component_type='summary', title='Summary & Key Takeaways',
        content={'points': ['Our bodies are holy temples of the Holy Spirit redeemed by Christ (1 Cor 6:19-20).', 'Responsible sexual behavior for unmarried youth means practicing chastity and complete abstinence.', 'Moral values like self-respect and self-control provide the spiritual foundation for purity.', 'Life skills such as assertiveness and decision-making empower learners to resist negative peer pressure.']}
    )
    LessonBlock.objects.create(
        lesson=l2_3, page_number=6, page_title='Mastery Check', order=110, component_order=2,
        block_type='knowledge_check', component_type='knowledge_check', title='Knowledge Check: Assertiveness and Peer Resistance',
        content={'check_type': 'multiple_choice', 'question': 'What life skill enables a Grade 9 learner to firmly say "No" to negative peer pressure regarding sexual relationships without being rude?', 'options': ['A) Aggressiveness', 'B) Assertiveness', 'C) Compliance', 'D) Low self-esteem'], 'answer': 'B', 'explanation': 'Assertiveness allows a person to confidently express moral convictions and set firm boundaries with respect and clarity.'}
    )

    print('Topic 2 Lesson 3 ingested successfully!')
