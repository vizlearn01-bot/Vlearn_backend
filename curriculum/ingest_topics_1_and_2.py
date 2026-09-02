"""
Master Ingestion & Enrichment Engine for CBC Grade 9 CRE — Topics 1 & 2
Ingests all 12 lessons (Topic 1: 6 lessons, Topic 2: 6 lessons)
"""

import os
import sys
import re
import django
from django.db import transaction

# Setup Django Environment
sys.path.append('/home/jason-bitega/Desktop/VL/vlearn_repositories/Vlearn_backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock, LessonAsset
)
from curriculum.svg_definitions import (
    get_svg_t1_l1, get_svg_t1_l2, get_svg_t1_l3, get_svg_t1_l4, get_svg_t1_l5, get_svg_t1_l6,
    get_svg_t2_l1, get_svg_t2_l2, get_svg_t2_l3, get_svg_t2_l4, get_svg_t2_l5, get_svg_t2_l6
)

def clean_text(text: str) -> str:
    if not text:
        return ''
    text = re.sub(r'\[(?:\d+(?:\.\d+)?(?:,\s*\d+(?:\.\d+)?)*|image_\d+|S\d+.*?|[\d,\s]{2,})\]', '', text)
    text = re.sub(r'\[(VISUAL|BIBLE REFERENCE|BIBLE PASSAGE|REAL WORLD APPLICATION|REFLECTION|CRITICAL THINKING|VALUES|MISCONCEPTION|INTERACTION|ETHICAL SCENARIO|KEY VERSE|BIBLICAL CONTEXT|PEDAGOGICAL ARCHITECTURE|PROJECT TITLE|SCENARIO|COMPARISON)[^\]]*\]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^[ \t]*[•\u2022][ \t]*', '- ', text, flags=re.MULTILINE)
    text = re.sub(r'([^\n])[ \t]+[•\u2022][ \t]+', r'\1\n- ', text)
    return text.strip()

grade9 = Grade.objects.get(id=18)
cre, _ = Subject.objects.get_or_create(grade=grade9, name='CRE', defaults={'description': 'CBC Grade 9 Christian Religious Education'})

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION FOR TOPIC 1 & TOPIC 2 (12 LESSONS)
# ─────────────────────────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    # TOPIC 1: WORK
    {
        'topic_order': 1,
        'topic_name': 'Work',
        'topic_desc': 'Christian ethics regarding work, vocation, traditional African labor, virtues, employer-employee rights, child labor, and entrepreneurship.',
        'unit_order': 1,
        'unit_name': 'Understanding Work, Vocation, and Careers',
        'unit_desc': 'Definitions of work, vocation, profession, trade, craft, career, and job from general and Christian perspectives.',
        'lesson_title': 'Understanding Work, Vocation, and Careers',
        'svg_fn': get_svg_t1_l1,
        'image': {
            'title': 'Saint Joseph the Carpenter at Work',
            'caption': 'Georges de La Tour depicting St. Joseph diligently working as a skilled carpenter, demonstrating the dignity of manual craftsmanship.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Georges_de_La_Tour_043.jpg/800px-Georges_de_La_Tour_043.jpg',
            'author': 'Georges de La Tour (Louvre Museum)',
            'licensing': 'Public Domain'
        },
        'youtube': {
            'title': 'BibleProject: Image of God & The Calling of Humanity',
            'description': 'How being created in the Image of God defines our vocation to work, cultivate, and care for creation.',
            'youtube_id': 'YbipxEDPryg'
        },
        'goals': [
            'Define and distinguish work, vocation, profession, trade, craft, career, and job',
            'Explain biblical teachings on work as a divine calling (Colossians 3:23, Genesis 1:28)',
            'Evaluate personal strengths and interests to discern future careers rooted in service'
        ],
        'intro': 'Think about your daily activities: washing dishes, studying, or helping on the farm. All these require energy, focus, and skill. Work is more than just earning money; it shapes human identity, builds community, and fulfills our God-given purpose.',
        'scripture': '### Genesis 1:28
> "God blessed them and said to them, 'Be fruitful and increase in number; fill the earth and subdue it. Rule over the fish in the sea and the birds in the sky and over every living creature.'"

### Colossians 3:23
> "Whatever you do, work at it with all your heart, as working for the Lord, not for human masters."

### Genesis 2:15
> "The Lord God took the man and put him in the Garden of Eden to work it and take care of it."',
        'theology': 'Work is part of God's original design before the fall. God is the first worker, and human beings are created as stewards (*Imago Dei*) to govern and care for creation. Work is not a punishment but a noble participation in God's creative purpose.',
        'deep_dive': '### The Spectrum of Labor
- **Work:** Physical or mental energy used to improve human life.
- **Vocation (*Vocare*):** A lifetime divine calling from God to serve Him and humanity.
- **Profession:** Work requiring specialized training and governed by a strict code of ethics (e.g. medicine, law).
- **Trade:** Practical occupation requiring specialized skill (e.g. carpentry, plumbing).
- **Craft:** Manual occupation utilizing artistic dexterity (e.g. pottery, weaving).
- **Career:** The chosen lifetime pursuit of an occupation.
- **Job:** Specific tasks performed for wages or salary.',
        'process': {
            'title': 'Action Framework: Discerning Your Calling and Choosing a Career Path',
            'steps': [
                {'step': 1, 'title': 'Identify God-Given Gifts', 'description': 'Assess your natural talents, academic strengths, and passions.'},
                {'step': 2, 'title': 'Seek Wise Counsel & Prayer', 'description': 'Consult teachers, parents, Christian mentors, and pray for divine guidance.'},
                {'step': 3, 'title': 'Acquire Specialized Skills', 'description': 'Pursue academic, technical (TVET), or artistic training with diligence.'},
                {'step': 4, 'title': 'Align Career with Service', 'description': 'Choose a career path dedicated to glorifying God and uplifting the needy.'}
            ]
        },
        'context': 'Kenya's Competency-Based Curriculum (CBC) and Vision 2030 emphasize vocational and technical pathways (TVETs). Christians honor technical and manual trades equally alongside white-collar careers.',
        'reflection': 'How does viewing your future career as a divine calling from God change your attitude toward studying and helping with chores today?',
        'summary': [
            'Work is the expenditure of physical or mental energy to improve human life.',
            'A vocation is a divine calling from God to serve the community through one's gifts.',
            'Christian work ethics require doing everything wholeheartedly as unto the Lord (Col 3:23).',
            'Technical trades and crafts carry equal dignity to professional white-collar careers.'
        ],
        'mcq': {
            'question': 'Which term refers to an occupation that requires specialized manual skills, such as woodcarving or pottery?',
            'options': ['A) Vocation', 'B) Profession', 'C) Craft', 'D) Career'],
            'answer': 'C',
            'explanation': 'A craft specifically involves manual dexterity and artistic skill to produce goods, whereas a profession requires advanced academic qualification and a vocation is a divine calling.'
        }
    },
    {
        'topic_order': 1,
        'topic_name': 'Work',
        'topic_desc': 'Christian ethics regarding work, vocation, traditional African labor, virtues, employer-employee rights, child labor, and entrepreneurship.',
        'unit_order': 2,
        'unit_name': 'Importance of Work: Traditional African vs. Christian Teachings',
        'unit_desc': 'Comparing traditional African communal labor practices with Christian biblical teachings on work and Sabbath rest.',
        'lesson_title': 'Importance of Work: Traditional African vs. Christian Teachings',
        'svg_fn': get_svg_t1_l2,
        'image': {
            'title': 'Communal Agricultural Harvest in Africa',
            'caption': 'African community members working together in agricultural harvest, exemplifying the spirit of communal solidarity (Mwethya/Harambee).',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Harvesting_in_Africa.jpg/800px-Harvesting_in_Africa.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC BY-SA 4.0'
        },
        'youtube': {
            'title': 'BibleProject: Sabbath & The Meaning of Rest',
            'description': 'Exploring how God instituted the Sabbath to balance creative labor with physical, emotional, and spiritual renewal.',
            'youtube_id': 'PFTVETgkZF8'
        },
        'goals': [
            'Analyze traditional African attitudes toward communal labor and division of tasks',
            'Examine Christian biblical teachings on work, stewardship, and condemnation of idleness',
            'Compare cultural practices with biblical principles regarding work and the Sabbath'
        ],
        'intro': 'Have you ever joined hands with neighbors to harvest crops, clear a path, or build a fence without payment? In traditional African society and biblical Christianity, work is central to community life and human flourishing.',
        'scripture': '### Genesis 2:1-3
> "By the seventh day God had finished the work he had been doing; so on the seventh day he rested from all his work. Then God blessed the seventh day and made it holy."

### 2 Thessalonians 3:10-12
> "'The one who is unwilling to work shall not eat.' We hear that some among you are idle and disruptive... Such people we command in the Lord Jesus Christ to settle down and earn the food they eat."

### Proverbs 6:6-8
> "Go to the ant, you sluggard; consider its ways and be wise! It has no commander, yet it stores its provisions in summer."',
        'theology': 'God established the rhythm of six days of labor followed by holy rest. Work sustains human life, while the Sabbath reminds us that we are human beings created for communion with God, not mere economic machines.',
        'deep_dive': '### Comparative Analysis
- **Traditional African:** Work was communal (Mwethya), divided by age and gender, rewarded by food and solidarity, and accompanied by prayers for rain and blessings.
- **Christian Biblical:** Work is stewardship under God, rewarded by meeting needs and glorifying God, open to all according to gifts, and balanced by mandatory Sabbath rest.',
        'process': {
            'title': 'Framework: The Ant's Strategy for Overcoming Procrastination',
            'steps': [
                {'step': 1, 'title': 'Self-Initiative', 'description': 'Begin your duties without waiting for supervision or compulsion.'},
                {'step': 2, 'title': 'Seasonal Foresight', 'description': 'Plan ahead for upcoming exams, chores, and responsibilities.'},
                {'step': 3, 'title': 'Consistent Action', 'description': 'Work incrementally every day to build sustainable mastery.'},
                {'step': 4, 'title': 'Balanced Sabbath Rest', 'description': 'Dedicate time for spiritual worship, family fellowship, and rest.'}
            ]
        },
        'context': 'In Kenya, communal labor concepts like Harambee (pulling together) and Mwethya reflect traditional values harmonized with Christian charity to construct schools, churches, and hospitals.',
        'reflection': 'Proverbs warns against being a "sluggard". In what areas of your life (academics, chores, prayer) are you tempted to be lazy? How does the ant inspire you?',
        'summary': [
            'Both African traditional society and Christianity strongly condemn idleness and praise industry.',
            'Traditional African labor emphasized communal solidarity and gender/age-based roles.',
            'Christianity teaches that work is co-creatorship with God, balanced by sacred Sabbath rest.',
            'Paul instructed that those unwilling to work should not eat (2 Thess 3:10).'
        ],
        'mcq': {
            'question': 'Why did God command human beings to observe the Sabbath day of rest?',
            'options': [
                'A) Because God ran out of energy and needed sleep.',
                'B) To establish a healthy pattern balancing diligent labor with physical, mental, and spiritual restoration.',
                'C) Because working on the seventh day is inherently evil.',
                'D) To ensure that slaves did not receive any food on that day.'
            ],
            'answer': 'B',
            'explanation': 'God instituted the Sabbath to prevent exploitation, ensure physical and mental renewal, and provide dedicated time for worship.'
        }
    },
    {
        'topic_order': 1,
        'topic_name': 'Work',
        'topic_desc': 'Christian ethics regarding work, vocation, traditional African labor, virtues, employer-employee rights, child labor, and entrepreneurship.',
        'unit_order': 3,
        'unit_name': 'Virtues, Ethics, and Professional Ethos',
        'unit_desc': 'The role of Christian virtues and professional codes of ethics in guiding workplace behavior and preventing corruption.',
        'lesson_title': 'Virtues, Ethics, and Professional Ethos',
        'svg_fn': get_svg_t1_l3,
        'image': {
            'title': 'Medical Professionals Upholding Clinical Ethics',
            'caption': 'Healthcare workers adhering to professional codes of conduct and compassionate patient care in a clinical setting.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Doctors_and_Nurses_Hospital.jpg/800px-Doctors_and_Nurses_Hospital.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC BY-SA 4.0'
        },
        'youtube': {
            'title': 'BibleProject: Justice & Righteousness',
            'description': 'Exploring the biblical meaning of justice (Mishpat) and righteousness (Tzedakah) in personal conduct and workplace integrity.',
            'youtube_id': 'A14THPoc4-4'
        },
        'goals': [
            'Define professional ethics, ethos, and professional codes of conduct',
            'Examine core Christian virtues related to work: diligence, honesty, integrity, and faithfulness',
            'Explain how professional codes protect the public and eliminate corruption in Kenya'
        ],
        'intro': 'Imagine visiting a doctor who was never trained, or hiring a builder who used substandard cement to save money. Professional rules and Christian moral character protect society from chaos, danger, and fraud.',
        'scripture': '### Proverbs 11:1
> "The Lord detests dishonest scales, but accurate weights find favor with him."

### Proverbs 22:29
> "Do you see someone skilled in their work? They will serve before kings; they will not serve before officials of low rank."

### Ephesians 4:28
> "Anyone who has been stealing must steal no longer, but must work, doing something useful with their own hands, that they may have something to share with those in need."',
        'theology': 'Marketplace honesty is a direct reflection of God's righteousness. God demands honest business dealings and honors skilled, faithful workers who use their labor to bless the community.',
        'deep_dive': '### Ethics & Virtues in the Workplace
- **Professional Ethics:** Rules and moral principles governing behavior in a specific profession.
- **Professional Ethos:** The unique character, spirit, and values distinguishing a professional group.
- **Code of Conduct:** Written regulations ensuring safety, accountability, and quality service.
- **Core Virtues:** Diligence (hard work), Honesty & Integrity (truthfulness unseen), Faithfulness (loyalty), Responsibility (accountability), and Tolerance (patience).',
        'process': {
            'title': 'Framework: Developing a Student Code of Personal & Academic Integrity',
            'steps': [
                {'step': 1, 'title': 'Absolute Academic Honesty', 'description': 'Refuse all forms of cheating, plagiarism, and exam malpractice.'},
                {'step': 2, 'title': 'Punctuality & Diligence', 'description': 'Complete school assignments thoroughly and submit on time.'},
                {'step': 3, 'title': 'Respect for Public Property', 'description': 'Care for school desks, laboratory apparatus, and library books.'},
                {'step': 4, 'title': 'Moral Courage & Truth', 'description': 'Stand up for truth and report dishonesty without fear of intimidation.'}
            ]
        },
        'context': 'In Kenya, regulatory bodies like the Teachers Service Commission (TSC), Kenya Medical Practitioners and Dentists Council (KMPDC), and Law Society of Kenya (LSK) enforce professional codes to combat corruption.',
        'reflection': 'If you witnessed a colleague or classmate cheating or taking a bribe, what would you do? How does Christian integrity guide your response?',
        'summary': [
            'Professional ethics regulate worker conduct and protect client rights.',
            'Christian virtues like honesty, diligence, and integrity form internal character.',
            'God detests dishonest scales and delights in fair, honest dealings (Prov 11:1).',
            'Regulatory bodies in Kenya enforce professional standards to maintain public trust.'
        ],
        'mcq': {
            'question': 'What is the primary role of a professional code of ethics in society?',
            'options': [
                'A) To ensure workers receive free housing from employers.',
                'B) To regulate worker behavior, protect client rights, and maintain public trust.',
                'C) To allow professionals to charge whatever prices they want.',
                'D) To eliminate the need for university education.'
            ],
            'answer': 'B',
            'explanation': 'Professional codes establish clear standards of conduct, safeguard clients from exploitation, and discipline errant members.'
        }
    },
    {
        'topic_order': 1,
        'topic_name': 'Work',
        'topic_desc': 'Christian ethics regarding work, vocation, traditional African labor, virtues, employer-employee rights, child labor, and entrepreneurship.',
        'unit_order': 4,
        'unit_name': 'Duties and Rights in Employment',
        'unit_desc': 'The reciprocal moral responsibilities and rights of employers and employees from a Christian and legal perspective.',
        'lesson_title': 'Duties and Rights in Employment',
        'svg_fn': get_svg_t1_l4,
        'image': {
            'title': 'Fair Employment Agreement and Just Workspace',
            'caption': 'Professional signing of an employment contract establishing mutual duties and protected rights in a just workplace.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Signing_Employment_Contract.jpg/800px-Signing_Employment_Contract.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC0'
        },
        'youtube': {
            'title': 'BibleProject: Justice / Mishpat',
            'description': 'How God commands equitable treatment, prompt payment of wages, and mutual respect in human relationships and labor.',
            'youtube_id': 'A14THPoc4-4'
        },
        'goals': [
            'Identify the moral and legal duties and rights of an employer',
            'Describe the responsibilities and protected rights of an employee',
            'Apply biblical principles of justice (Colossians 4:1, James 5:4) to workplace relationships'
        ],
        'intro': 'Have you ever agreed to do a job, only for the employer to refuse to pay on time? Or have you hired someone who did a sloppy, dishonest job? Employment is a reciprocal covenant requiring mutual fairness, honesty, and dignity.',
        'scripture': '### Colossians 4:1
> "Masters, provide your slaves with what is right and fair, because you know that you also have a Master in heaven."

### Ephesians 6:5-7
> "Slaves, obey your earthly masters with respect and fear, and with sincerity of heart, just as you would obey Christ. Serve wholeheartedly, as if you were serving the Lord, not people."

### James 5:4
> "Look! The wages you failed to pay the workers who mowed your fields are crying out against you. The cries of the harvesters have reached the ears of the Lord Almighty."',
        'theology': 'Both employers and employees are accountable to God. Employers must never exploit workers by withholding wages, and employees must work conscientiously with loyalty and integrity as serving Christ.',
        'deep_dive': '### The Reciprocal Covenant of Employment
- **Employer Duties:** Pay fair wages promptly, provide a safe work environment, grant agreed leave and medical rest, respect human dignity, and provide growth opportunities.
- **Employer Rights:** Receive a fair day's work, protect business property, and hire/dismiss in accordance with law.
- **Employee Duties:** Work diligently without constant supervision, protect company assets, honor contract terms, and resolve disputes peacefully.
- **Employee Rights:** Receive timely wages, work reasonable hours, join trade unions, and have safe working conditions.',
        'process': {
            'title': 'Framework: Resolving Workplace Disputes with Christian Mediation',
            'steps': [
                {'step': 1, 'title': 'Direct Dialogue', 'description': 'Discuss grievances calmly and privately with the concerned party.'},
                {'step': 2, 'title': 'Review the Contract', 'description': 'Examine agreed terms of employment and legal labor guidelines.'},
                {'step': 3, 'title': 'Engage Neutral Mediation', 'description': 'Involve trade union reps, human resource officers, or labor conciliators.'},
                {'step': 4, 'title': 'Reconcile with Fairness', 'description': 'Implement just restitution, respect worker rights, and restore harmony.'}
            ]
        },
        'context': 'Kenya's Employment Act (2007) and labor unions protect worker rights such as maternity leave, statutory rest, minimum wage, and severance benefits.',
        'reflection': 'How does the Christian teaching that "we all have a Master in heaven" shape how an employer should treat domestic workers or casual laborers?',
        'summary': [
            'Employment is a reciprocal relationship where rights are protected by reciprocal duties.',
            'Employers must pay fair wages promptly and provide a safe, dignified work environment.',
            'Employees must work diligently, be honest, and protect the employer's property.',
            'Withholding wages is condemned in Scripture as a direct sin against God (James 5:4).'
        ],
        'mcq': {
            'question': 'According to Christian teachings, what is a primary moral duty of an employee?',
            'options': [
                'A) To demand salary increases through violence and strikes.',
                'B) To work diligently, be loyal, and protect the employer's property without needing constant supervision.',
                'C) To perform only the tasks they find enjoyable each day.',
                'D) To take office supplies home as informal compensation.'
            ],
            'answer': 'B',
            'explanation': 'Employees are called to work wholeheartedly and faithfully as unto the Lord, protecting property and fulfilling contracts with integrity.'
        }
    },
    {
        'topic_order': 1,
        'topic_name': 'Work',
        'topic_desc': 'Christian ethics regarding work, vocation, traditional African labor, virtues, employer-employee rights, child labor, and entrepreneurship.',
        'unit_order': 5,
        'unit_name': 'Industrial Action, Child Labor, and the Role of the Church',
        'unit_desc': 'Christian approaches to labor disputes, strikes, the physical and psychological harm of child labor, and the protective role of the Church.',
        'lesson_title': 'Industrial Action, Child Labor, and the Role of the Church',
        'svg_fn': get_svg_t1_l5,
        'image': {
            'title': 'Kenyan Children in Classroom Learning',
            'caption': 'Pupils attending primary school, representing the fundamental human and constitutional right of every child to education free from child labor.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Kenyan_pupils_in_class.jpg/800px-Kenyan_pupils_in_class.jpg',
            'author': 'USAID Kenya',
            'licensing': 'Public Domain'
        },
        'youtube': {
            'title': 'BibleProject: Generosity and Justice in the Kingdom',
            'description': 'Exploring biblical economic justice, defending the vulnerable, and the prophetic call to protect children.',
            'youtube_id': 'A14THPoc4-4'
        },
        'goals': [
            'Explain Christian teachings on fair wages and prompt payment',
            'Analyze the causes, consequences, and peaceful resolution of industrial strikes',
            'Describe the effects of child labor and evaluate the response of the Church'
        ],
        'intro': 'Every laborer deserves fair pay, and every child deserves the opportunity to learn and grow safely. When greed leads to exploitation or strikes turn violent, society suffers. How does the Christian faith bring justice and peace?',
        'scripture': '### Deuteronomy 24:14-15
> "Do not take advantage of a hired worker who is poor and needy... Pay them their wages each day before sunset... otherwise they may cry to the Lord against you, and you will be guilty of sin."

### Jeremiah 22:13
> "Woe to him who builds his palace by unrighteousness... making his own people work for nothing, not paying them for their labor."

### Ephesians 6:4
> "Fathers, do not exasperate your children; instead, bring them up in the training and instruction of the Lord."',
        'theology': 'Withholding wages from the poor is an offense against God's righteousness. Children are a sacred heritage from the Lord (Psalm 127:3); exploiting them for cheap manual labor violates their dignity and robs them of their future.',
        'deep_dive': '### Strikes & Child Labor
- **Industrial Action (Strikes):** Collective withdrawal of labor protesting unfair pay or hazardous conditions. Consequences include financial losses, dismissals, and potential violence. Christianity urges peaceful collective bargaining and dialogue.
- **Child Labor:** Work that harms a child's physical, mental, or educational development. Caused by poverty, greed, and broken families.
- **Church Intervention:** Operating rescue centers, sponsoring underprivileged pupils, providing family counseling, and advocating for child protection laws.',
        'process': {
            'title': 'Framework: 4-Step Christian Conflict Resolution and Child Protection',
            'steps': [
                {'step': 1, 'title': 'Early Grievance Recognition', 'description': 'Identify unfair workplace conditions or child distress before escalation.'},
                {'step': 2, 'title': 'Honest & Peaceful Dialogue', 'description': 'Engage in open negotiation between workers and management without violence.'},
                {'step': 3, 'title': 'Community Intervention', 'description': 'Report child labor cases to Childline 116, village elders, and local authorities.'},
                {'step': 4, 'title': 'Restorative Education', 'description': 'Reintegrate rescued children into schools with holistic psychosocial support.'}
            ]
        },
        'context': 'Under Kenya's Children Act (2022) and the Constitution (Article 53), every child is protected from hazardous child labor. The Church partners with Childline Kenya (Toll-Free 116) to rescue and educate vulnerable children.',
        'reflection': 'Why do some employers prefer to hire children instead of adults? How does Jesus' command to "welcome the little children" contradict this greed?',
        'summary': [
            'The Bible commands prompt and fair wages for all laborers (Deut 24:14-15).',
            'Industrial disputes must be resolved through peaceful dialogue, fairness, and mutual respect.',
            'Child labor violates children's fundamental rights and perpetuates cycles of poverty.',
            'The Church actively rescues vulnerable children, builds schools, and defends children's rights.'
        ],
        'mcq': {
            'question': 'What is the Christian view on resolving labor disputes and strikes?',
            'options': [
                'A) Workers should destroy company property to force immediate concessions.',
                'B) Employers should fire all workers and hire children as replacements.',
                'C) Both parties should engage in honest dialogue, ensure fair wages, and maintain peaceful communication.',
                'D) Workers should go on strike indefinitely without seeking negotiation.'
            ],
            'answer': 'C',
            'explanation': 'Christian ethics advocate for peace, fairness, and open communication to resolve labor disputes constructively without violence or property destruction.'
        }
    },
    {
        'topic_order': 1,
        'topic_name': 'Work',
        'topic_desc': 'Christian ethics regarding work, vocation, traditional African labor, virtues, employer-employee rights, child labor, and entrepreneurship.',
        'unit_order': 6,
        'unit_name': 'Unemployment and Self-Employment',
        'unit_desc': 'Causes of unemployment, Christian attitudes to joblessness, and the benefits of entrepreneurship and self-employment.',
        'lesson_title': 'Unemployment and Self-Employment',
        'svg_fn': get_svg_t1_l6,
        'image': {
            'title': 'Young Kenyan Entrepreneur in the Jua Kali Sector',
            'caption': 'A skilled young artisan manufacturing metal products in Kenya's vibrant Jua Kali sector, demonstrating self-reliance and enterprise.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Jua_Kali_Artisan_Kenya.jpg/800px-Jua_Kali_Artisan_Kenya.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC BY-SA 4.0'
        },
        'youtube': {
            'title': 'BibleProject: Proverbs — Wisdom and the Blessing of Diligent Labor',
            'description': 'How biblical wisdom encourages industrious work, creative entrepreneurship, and overcoming poverty.',
            'youtube_id': 'AzmYV8GNDPE'
        },
        'goals': [
            'Analyze the root causes of unemployment among youth in Kenya',
            'Discuss Christian theological responses to joblessness and the condemnation of idleness',
            'Evaluate the benefits, challenges, and ethical management of self-employment micro-enterprises'
        ],
        'intro': 'Many school leavers wait for years to get an office job in a suit and tie. Yet some of the most self-reliant and prosperous members of our communities are entrepreneurs who started small businesses in farming, tailoring, or metalwork. God honors honest self-employment.',
        'scripture': '### Proverbs 14:23
> "All hard work brings a profit, but mere talk leads only to poverty."

### 1 Thessalonians 4:11-12
> "Make it your ambition to lead a quiet life: You should mind your own business and work with your hands, just as we told you, so that your daily life may win the respect of outsiders and so that you will not be dependent on anybody."

### Ecclesiastes 11:6
> "Sow your seed in the morning, and at evening let your hands not be idle, for you do not know which will succeed."',
        'theology': 'God created human beings with creative potential. Idleness is strongly condemned in Scripture. Working with our hands to create self-employment reflects the creative nature of God and provides for our families with dignity.',
        'deep_dive': '### Unemployment vs. Self-Employment
- **Causes of Unemployment:** White-collar preference, corruption/nepotism in hiring, lack of capital, and mismatch between school curricula and job market needs.
- **Christian Response:** Condemnation of idleness, church-sponsored TVET polytechnics, microfinance SACCOs, and teaching youth practical trades.
- **Benefits of Self-Employment:** Financial self-reliance, creative expression of gifts, creating jobs for others, and flexible work hours.
- **Challenges:** Lack of initial capital, market competition, and business management hurdles.',
        'process': {
            'title': 'Framework: 4 Steps for Youth to Launch a Micro-Enterprise with Integrity',
            'steps': [
                {'step': 1, 'title': 'Identify Community Needs', 'description': 'Find unmet needs in your neighborhood (e.g. vegetable farming, tutoring, crafts).'},
                {'step': 2, 'title': 'Bootstrap with Low Capital', 'description': 'Start small using available household resources and personal savings.'},
                {'step': 3, 'title': 'Operate with Financial Honesty', 'description': 'Keep accurate records, avoid dishonest shortcuts, and tithe faithfully.'},
                {'step': 4, 'title': 'Reinvest and Persevere', 'description': 'Reinvest profits to expand tools and services while maintaining excellence.'}
            ]
        },
        'context': 'In Kenya, the Jua Kali informal sector, agricultural agribusiness, and technical vocational institutes (TVETs) employ millions. The government's Youth Enterprise Development Fund (YEDF) supports youth-led start-ups.',
        'reflection': 'If God is a creator who designed a fruitful universe, how does starting a new small business show that we are made in His image?',
        'summary': [
            'Unemployment is exacerbated by negative attitudes toward manual labor and technical trades.',
            'Scripture urges Christians to work with their hands and avoid dependency (1 Thess 4:11-12).',
            'Self-employment fosters creativity, provides community services, and generates local employment.',
            'Hard work and persistence bring profit, while mere talk leads to poverty (Prov 14:23).'
        ],
        'mcq': {
            'question': 'What is a major cause of youth unemployment in Kenya today?',
            'options': [
                'A) Lack of biblical scriptures about working hard.',
                'B) Strong preference for white-collar office jobs and negative attitudes toward manual self-employment.',
                'C) The government banning all forms of agricultural work.',
                'D) A total lack of rain across the entire country.'
            ],
            'answer': 'B',
            'explanation': 'Many school leavers avoid practical vocational trades while waiting for scarce office jobs, creating an employment bottleneck.'
        }
    },

    # TOPIC 2: CHRISTIAN MORAL VALUES (SEXUAL PURITY)
    {
        'topic_order': 2,
        'topic_name': 'Christian Moral Values',
        'topic_desc': 'Christian ethics regarding human sexuality, sexual purity, traditional African comparisons, overcoming temptations, biological/psychological consequences, and sanctity of life.',
        'unit_order': 1,
        'unit_name': 'Human Sexuality as a Gift from God',
        'unit_desc': 'The biological, emotional, and psychological dimensions of human sexuality created in the image of God for companionship and complementarity.',
        'lesson_title': 'Human Sexuality as a Gift from God',
        'svg_fn': get_svg_t2_l1,
        'image': {
            'title': 'Creation of Humanity in the Image of God',
            'caption': 'Artistic representation of God creating male and female in equal dignity and holiness as described in Genesis 1.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg/800px-Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg',
            'author': 'Michelangelo (Sistine Chapel)',
            'licensing': 'Public Domain'
        },
        'youtube': {
            'title': 'BibleProject: Genesis 1-2 — Creation and Humanity',
            'description': 'How God created male and female in His image to share equal dignity, holy companionship, and mutual partnership.',
            'youtube_id': 'KOUV7mW4i4c'
        },
        'goals': [
            'Define human sexuality and identify its biological, emotional, and psychological dimensions',
            'Explain biblical teachings on why God created male and female (Genesis 1:27-28, Genesis 2:18-24)',
            'Develop personal values of self-respect and reverence for the body as a temple of God'
        ],
        'intro': 'As you grow from a child into a teenager, your body and emotions undergo natural changes. These changes are part of your human sexuality. God designed male and female with beauty, purpose, and dignity. How should we honor this divine gift?',
        'scripture': '### Genesis 1:27-28
> "So God created mankind in his own image, in the image of God he created them; male and female he created them. God blessed them and said, 'Be fruitful and increase in number; fill the earth and subdue it.'"

### Genesis 2:18
> "The Lord God said, 'It is not good for the man to be alone. I will make a helper suitable for him.'"

### Genesis 2:24
> "That is why a man leaves his father and mother and is united to his wife, and they become one flesh."',
        'theology': 'Human sexuality is not dirty or accidental; it is a sacred gift from God. Male and female share equal dignity as image-bearers of God. Sexuality involves the whole person—body, emotions, and mind—created for companionship, complementarity, and sacred covenant in marriage.',
        'deep_dive': '### Three Dimensions of Human Sexuality
- **Biological/Physiological:** Physical anatomy, reproductive organs, and puberty changes created by God.
- **Emotional:** Feelings, capacity to express love, care, tenderness, and attraction.
- **Mental/Psychological:** Self-awareness and understanding of one's gender identity.
- **Divine Purposes:** Companionship (preventing loneliness), Complementarity (mutual support), Procreation (raising godly families), and Sacred Union (covenant marriage).',
        'process': {
            'title': 'Framework: 4 Steps to Cultivating Self-Respect & Healthy Teenage Self-Image',
            'steps': [
                {'step': 1, 'title': 'Celebrate Your Uniqueness', 'description': 'Recognize that you are fearfully and wonderfully made by God (Psalm 139:14).'},
                {'step': 2, 'title': 'Practice Modesty & Decency', 'description': 'Dress decently and respect your body as a holy temple of the Holy Spirit.'},
                {'step': 3, 'title': 'Set Clear Personal Boundaries', 'description': 'Refuse inappropriate physical contact and protect your personal space.'},
                {'step': 4, 'title': 'Filter Media Influences', 'description': 'Reject social media messages that reduce human sexuality to mere physical lust.'}
            ]
        },
        'context': 'In Kenyan schools and communities, teenagers face peer pressure and suggestive social media trends. Christian unions and guidance counseling clubs help learners embrace positive self-esteem and respect for both genders.',
        'reflection': 'What does it mean to say your body is a "temple of the Holy Spirit"? How should this truth shape how you treat yourself and peers of the opposite sex?',
        'summary': [
            'Human sexuality is a sacred gift from God encompassing biological, emotional, and mental dimensions.',
            'Male and female are created in the image of God with equal dignity and complementary roles.',
            'God designed sexuality for holy companionship, mutual partnership, and sacred marriage covenant.',
            'Self-respect and modesty are essential Christian values in honoring our bodies as temples of God.'
        ],
        'mcq': {
            'question': 'Which of the following best defines "human sexuality" from a Christian perspective?',
            'options': [
                'A) A purely physical drive that humans cannot control.',
                'B) A sacred gift from God encompassing our biological, emotional, and mental make-up as male or female.',
                'C) Something shameful that should never be discussed.',
                'D) A cultural role that has nothing to do with God's creation.'
            ],
            'answer': 'B',
            'explanation': 'Christianity teaches that sexuality involves our whole being—body, mind, and emotions—created by God for holy companionship and mutual honor.'
        }
    },
    {
        'topic_order': 2,
        'topic_name': 'Christian Moral Values',
        'topic_desc': 'Christian ethics regarding human sexuality, sexual purity, traditional African comparisons, overcoming temptations, biological/psychological consequences, and sanctity of life.',
        'unit_order': 2,
        'unit_name': 'Traditional African vs. Christian Understandings of Sexuality',
        'unit_desc': 'Comparing traditional African practices on marriage, gender roles, and sex education with Christian biblical teachings.',
        'lesson_title': 'Traditional African vs. Christian Understandings of Sexuality',
        'svg_fn': get_svg_t2_l2,
        'image': {
            'title': 'Mijikenda Wedding Blessing Ceremony in Coastal Kenya',
            'caption': 'Elder community leaders blessing a wedding couple, showcasing traditional African marriage customs and communal moral guidance.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/African_wedding_ceremony.jpg/800px-African_wedding_ceremony.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC BY-SA 4.0'
        },
        'youtube': {
            'title': 'BibleProject: Agapé — Self-Giving Love',
            'description': 'Exploring how Christ's sacrificial love transforms marital relationships into lifelong partnerships of mutual honor and equality.',
            'youtube_id': 'slyevQ1LW7A'
        },
        'goals': [
            'Outline traditional African cultural practices regarding sexuality, gender roles, and initiation',
            'Describe Christian biblical teachings on marriage, equal dignity, and mutual submission',
            'Compare areas of harmony and contrast between traditional culture and biblical truth'
        ],
        'intro': 'Our African cultural heritage has rich traditions regarding marriage, initiation, and family honor. How do traditional African customs align with or differ from Jesus Christ's teachings on marriage and gender equality?',
        'scripture': '### Ephesians 5:21-25
> "Submit to one another out of reverence for Christ. Wives, submit yourselves to your own husbands as you do to the Lord... Husbands, love your wives, just as Christ loved the church and gave himself up for her."

### 1 Corinthians 7:3-4
> "The husband should fulfill his marital duty to his wife, and likewise the wife to her husband. The wife does not have authority over her own body but yields it to her husband. In the same way, the husband does not have authority over his own body but yields it to his wife."

### Genesis 1:28
> "God blessed them and said, 'Be fruitful and multiply.'"',
        'theology': 'In Christ, cultural patriarchal hierarchies are transformed into mutual respect and sacrificial love. Christian marriage is a permanent, monogamous covenant reflecting Christ's love for the Church, where husband and wife share equal spiritual dignity.',
        'deep_dive': '### Cultural Traditions vs. Biblical Truth
- **Purpose of Sex:** In African culture, procreation was the supreme goal; childlessness could justify divorce. In Christianity, companionship and mutual love are primary; marriage remains sacred even without children.
- **Marriage Structure:** Traditional culture practiced polygamy for wealth and labor; Christianity commands lifelong monogamy (one husband, one wife).
- **Gender Roles:** Culture was strictly patriarchal with female subordination; Christianity teaches mutual submission and sacrificial servant-leadership.
- **Sex Education:** Grandparents and initiation elders taught culture; the Christian home and Church teach holy biblical principles.',
        'process': {
            'title': 'Framework: 4 Principles for Promoting Gender Equality and Mutual Respect',
            'steps': [
                {'step': 1, 'title': 'Reject Gender Stereotypes', 'description': 'Affirm that boys and girls possess equal intelligence, dignity, and leadership potential.'},
                {'step': 2, 'title': 'Share Responsibilities Equally', 'description': 'Distribute household chores and school duties fairly without sexist bias.'},
                {'step': 3, 'title': 'Eliminate Harmful Practices', 'description': 'Oppose early forced child marriage, female genital mutilation (FGM), and domestic violence.'},
                {'step': 4, 'title': 'Practice Mutual Honor', 'description': 'Speak with respect and support the academic and spiritual growth of all peers.'}
            ]
        },
        'context': 'Article 27 of the Constitution of Kenya guarantees equality and freedom from discrimination based on sex. Christianity reinforces this by teaching that in Christ there is neither male nor female (Gal 3:28).',
        'reflection': 'Which traditional African practices regarding sexuality (e.g. valuing virginity, elder mentorship) should we preserve, and which (e.g. child marriage, female subordination) must be reformed?',
        'summary': [
            'Traditional African culture valued chastity and procreation within marriage.',
            'Christianity teaches that marriage is a sacred, permanent, and monogamous covenant (Genesis 2:24).',
            'Husbands and wives are called to mutual submission, honor, and sacrificial love (Ephesians 5:21-33).',
            'In Christ, men and women share equal dignity as co-heirs of God's grace.'
        ],
        'mcq': {
            'question': 'How does the Christian understanding of marriage differ fundamentally from traditional African cultural views on childlessness?',
            'options': [
                'A) Christianity permits marrying second wives when children are not born.',
                'B) Christian marriage is a complete and sacred union of companionship even if a couple cannot have children.',
                'C) Christianity dissolves childless marriages immediately.',
                'D) Traditional African culture did not care about having children.'
            ],
            'answer': 'B',
            'explanation': 'While children are a precious blessing, Christian marriage is founded upon companionship and mutual love, remaining sacred and complete even without biological children.'
        }
    },
    {
        'topic_order': 2,
        'topic_name': 'Christian Moral Values',
        'topic_desc': 'Christian ethics regarding human sexuality, sexual purity, traditional African comparisons, overcoming temptations, biological/psychological consequences, and sanctity of life.',
        'unit_order': 3,
        'unit_name': 'Responsible Sexual Behavior and Fostering Purity',
        'unit_desc': 'Christian moral values and practical life skills including assertiveness, decision-making, and self-control to maintain sexual purity.',
        'lesson_title': 'Responsible Sexual Behavior and Fostering Purity',
        'svg_fn': get_svg_t2_l3,
        'image': {
            'title': 'Christian Youth Mentorship and Fellowship',
            'caption': 'Youth engaging in positive peer fellowship, character development, and mentorship.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Youth_Group_Fellowship.jpg/800px-Youth_Group_Fellowship.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC BY-SA 4.0'
        },
        'youtube': {
            'title': 'BibleProject: 1 Corinthians — The Body as the Temple of the Spirit',
            'description': 'Understanding how the Holy Spirit empowers believers to flee sexual immorality and honor God with their bodies.',
            'youtube_id': 'yiSjX3q3hdc'
        },
        'goals': [
            'Define responsible sexual behavior and the practice of chastity (abstinence)',
            'List core Christian moral values needed to maintain sexual purity (respect, integrity, self-control)',
            'Apply defensive life skills (assertiveness, decision-making, self-awareness) to overcome negative peer pressure'
        ],
        'intro': 'Have you ever felt pressured by peers to compromise your moral standards or watch inappropriate media? Saying "No" with confidence requires moral courage, clear boundaries, and internal spiritual strength.',
        'scripture': '### 1 Corinthians 6:18-20
> "Flee from sexual immorality... Do you not know that your bodies are temples of the Holy Spirit, who is in you, whom you have received from God? You are not your own; you were bought at a price. Therefore honor God with your bodies."

### 1 Thessalonians 4:3-4
> "It is God's will that you should be sanctified: that you should avoid sexual immorality; that each of you should learn to control your own body in a way that is holy and honorable."

### Matthew 6:13
> "And lead us not into temptation, but deliver us from the evil one."',
        'theology': 'Our physical bodies are holy sanctuaries of the Holy Spirit. Sexual purity is an act of worship and obedience to God who redeemed us through Christ's sacrificial death.',
        'deep_dive': '### Values and Life Skills for Purity
- **Chastity (Abstinence):** Complete refraining from sexual activity before marriage.
- **Moral Values:** Respect for self and others, integrity (doing right when alone), and self-control.
- **Assertiveness:** Confidently communicating moral boundaries without being aggressive or succumbing to pressure.
- **Decision-Making:** Evaluating long-term spiritual, academic, and physical consequences before taking action.
- **Self-Awareness:** Recognizing personal vulnerabilities and avoiding high-risk environments.',
        'process': {
            'title': 'Framework: 4-Step Boundary Setting Guide for Teenage Friendships',
            'steps': [
                {'step': 1, 'title': 'Define Non-Negotiable Boundaries', 'description': 'Decide in advance never to compromise on physical purity or suggestive media.'},
                {'step': 2, 'title': 'Communicate Assertively', 'description': 'Clearly state your values to friends: "I choose to honor God and stay pure."'},
                {'step': 3, 'title': 'Avoid High-Risk Environments', 'description': 'Refuse unchaperoned isolated settings and unsupervised late-night parties.'},
                {'step': 4, 'title': 'Cultivate Positive Accountability', 'description': 'Surround yourself with like-minded friends, mentors, and church youth leaders.'}
            ]
        },
        'context': 'In Kenya, teenagers navigate social media and peer pressure. Practicing digital hygiene, unfollowing inappropriate pages, and participating in Christian Unions (CU) or youth mentorship clubs provide essential community support.',
        'reflection': 'Pray for the strength of the Holy Spirit to guard your heart and mind daily. How can setting proactive boundaries protect your future, health, and relationship with God?',
        'summary': [
            'Our bodies are holy temples of the Holy Spirit redeemed by Christ (1 Cor 6:19-20).',
            'Responsible sexual behavior for unmarried youth means practicing chastity and complete abstinence.',
            'Moral values like self-respect and self-control provide the spiritual foundation for purity.',
            'Life skills such as assertiveness and decision-making empower learners to resist negative peer pressure.'
        ],
        'mcq': {
            'question': 'What life skill enables a Grade 9 learner to firmly say "No" to negative peer pressure regarding sexual relationships without being rude?',
            'options': [
                'A) Aggressiveness',
                'B) Assertiveness',
                'C) Compliance',
                'D) Low self-esteem'
            ],
            'answer': 'B',
            'explanation': 'Assertiveness allows a person to confidently express moral convictions and set firm boundaries with respect and clarity.'
        }
    },
    {
        'topic_order': 2,
        'topic_name': 'Christian Moral Values',
        'topic_desc': 'Christian ethics regarding human sexuality, sexual purity, traditional African comparisons, overcoming temptations, biological/psychological consequences, and sanctity of life.',
        'unit_order': 4,
        'unit_name': 'Irresponsible Sexual Behaviors',
        'unit_desc': 'Biblical prohibitions and legal consequences of irresponsible behaviors such as incest, rape, fornication, adultery, prostitution, and defilement.',
        'lesson_title': 'Irresponsible Sexual Behaviors',
        'svg_fn': get_svg_t2_l4,
        'image': {
            'title': 'Scales of Justice and the Rule of Law',
            'caption': 'The scales of justice representing moral boundaries, human rights protection, and statutory penalties for sexual offenses in Kenya.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Lady_Justice_with_scales.jpg/800px-Lady_Justice_with_scales.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC BY-SA 4.0'
        },
        'youtube': {
            'title': 'BibleProject: Galatians — Works of the Flesh vs. Fruit of the Spirit',
            'description': 'Contrasting the destructive works of the flesh (sexual immorality, debauchery) with the life-giving fruit of the Spirit.',
            'youtube_id': 'baXU74vhof0'
        },
        'goals': [
            'Define and describe forbidden sexual practices: incest, rape/defilement, fornication, adultery, and prostitution',
            'Explain biblical condemnation of sexual immorality (Leviticus 18, Galatians 5:19-21, 1 Corinthians 6:13-18)',
            'Analyze legal penalties under Kenyan law (Sexual Offences Act 2006) and strategies to resist exploitation'
        ],
        'intro': 'Human sexuality was designed by God to exist exclusively within the covenant of marriage. When this boundary is breached through violence, exploitation, or lust, it causes severe spiritual, emotional, and legal destruction.',
        'scripture': '### Galatians 5:19-21
> "The acts of the flesh are obvious: sexual immorality, impurity and debauchery; idolatry and witchcraft; hatred, discord, jealousy... I warn you, as I did before, that those who live like this will not inherit the kingdom of God."

### 1 Corinthians 6:13-18
> "The body is not meant for sexual immorality, but for the Lord, and the Lord for the body... Flee from sexual immorality."

### Leviticus 18:6
> "No one is to approach any close relative to have sexual relations. I am the Lord."',
        'theology': 'God established marriage as the only sacred container for sexual union. Violations of this covenant defile the temple of God, violate human rights, and bring severe spiritual alienation and judgment.',
        'deep_dive': '### Analysis of Irresponsible Sexual Behaviors
- **Incest:** Sexual relations between blood relatives (Lev 18:6-8). Destroys family trust and violates natural order.
- **Rape & Defilement:** Non-consensual sexual violence or sexual acts with a minor. In Kenya, rape carries a minimum of 20 years to life imprisonment (Sexual Offences Act 2006).
- **Fornication:** Sexual relations between unmarried individuals, driven by peer pressure, curiosity, or lack of self-control.
- **Adultery:** Marital unfaithfulness breaking the covenant vow.
- **Prostitution:** Commercial trading of sex for money, driven by poverty, drug addiction, or exploitation.',
        'process': {
            'title': 'Framework: 4 Steps to Resisting 'Sponsor' Culture and Predatory Grooming',
            'steps': [
                {'step': 1, 'title': 'Recognize Predatory Red Flags', 'description': 'Beware of older individuals offering money, expensive gifts, or rides in exchange for favors.'},
                {'step': 2, 'title': 'Firm Immediate Refusal', 'description': 'State clearly that your dignity is not for sale and reject all gifts.'},
                {'step': 3, 'title': 'Confide in Trusted Adults', 'description': 'Report any predatory advances to parents, school counselors, or church leaders.'},
                {'step': 4, 'title': 'Practice Contentment', 'description': 'Be content with what your family provides and focus on academic excellence.'}
            ]
        },
        'context': 'In Kenya, the Sexual Offences Act (2006) strictly punishes rape, defilement, and sexual harassment. The Directorate of Criminal Investigations (DCI) and Childline 116 actively prosecute offenders.',
        'reflection': 'If offered expensive gifts or money by an older person in exchange for a relationship, how will you apply Christian integrity and assertiveness?',
        'summary': [
            'God designed sexual union to exist exclusively within holy marriage covenant.',
            'Irresponsible behaviors like fornication, adultery, incest, and rape violate God's law.',
            'Rape and defilement are serious criminal offenses in Kenya punishable by 20+ years imprisonment.',
            'Integrity, contentment, and assertiveness protect young people from predatory exploitation.'
        ],
        'mcq': {
            'question': 'What is the minimum legal prison penalty for the crime of rape under Kenyan law?',
            'options': [
                'A) A small community fine paid to the victim's family.',
                'B) A minimum of 20 years in prison.',
                'C) 6 months of probation.',
                'D) 5 years of community service.'
            ],
            'answer': 'B',
            'explanation': 'Under Kenya's Sexual Offences Act (2006), rape carries a severe minimum mandatory sentence of 20 years in prison to deter sexual violence.'
        }
    },
    {
        'topic_order': 2,
        'topic_name': 'Christian Moral Values',
        'topic_desc': 'Christian ethics regarding human sexuality, sexual purity, traditional African comparisons, overcoming temptations, biological/psychological consequences, and sanctity of life.',
        'unit_order': 5,
        'unit_name': 'Biological and Psychological Consequences of Sexual Immorality',
        'unit_desc': 'Medical pathology of STIs, HIV/AIDS opportunistic infections, psychological trauma, and the Christian duty of compassion.',
        'lesson_title': 'Biological and Psychological Consequences of Sexual Immorality',
        'svg_fn': get_svg_t2_l5,
        'image': {
            'title': 'Adolescent Healthcare and Compassionate Medical Counseling',
            'caption': 'Healthcare professional providing compassionate health education and testing support to youth in a community medical center.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Healthcare_worker_counseling.jpg/800px-Healthcare_worker_counseling.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC BY-SA 4.0'
        },
        'youtube': {
            'title': 'BibleProject: Compassion & The Good Samaritan',
            'description': 'How Christ calls believers to show unconditional love, care, and practical support to those suffering from chronic illnesses.',
            'youtube_id': '4T4r1c3oKkY'
        },
        'goals': [
            'List major Sexually Transmitted Infections (STIs) and describe their symptoms and medical consequences',
            'Explain the transmission, biological mechanism, and management of HIV/AIDS',
            'Analyze the psychological trauma of sexual immorality and demonstrate Christian compassion'
        ],
        'intro': 'Many youth are deceived into believing that irresponsible sexual behavior has no consequences. In reality, sexual immorality carries devastating biological diseases and crushing psychological trauma. How does Christian truth guide our health and compassion?',
        'scripture': '### 1 Corinthians 6:18
> "Flee from sexual immorality. All other sins a person commits are outside the body, but whoever sins sexually, sins against their own body."

### John 10:10
> "The thief comes only to steal and kill and destroy; I have come that they may have life, and have it to the full."

### Proverbs 5:11-12
> "At the end of your life you will groan, when your flesh and body are spent. You will say, 'How I hated discipline! How my heart spurned correction!'"',
        'theology': 'Sexual sin uniquely harms the physical body and human spirit. Christ came to offer abundant life, health, and peace. While Christians abstain to preserve health, they must show Christlike compassion and care to all affected by disease.',
        'deep_dive': '### Biological & Psychological Consequences
- **Gonorrhea:** Bacterial infection causing painful urination, thick discharge, and permanent infertility if untreated.
- **Syphilis:** Primary painless chancre sore disappears, but bacteria cause massive skin rashes, organ failure, and brain damage years later.
- **Hepatitis B:** Viral disease causing fatal liver damage, cirrhosis, and jaundice; vaccine preventable but incurable once chronic.
- **HIV/AIDS:** Destroys CD4 white blood cells, exposing the body to opportunistic infections (TB, pneumonia, chronic diarrhea).
- **Psychological Trauma:** Chronic anxiety, crushing guilt, depression, suicidal thoughts, and academic failure.',
        'process': {
            'title': 'Framework: 4 Pillars of Christian Care and Non-Discrimination for HIV/AIDS',
            'steps': [
                {'step': 1, 'title': 'Eliminate Stigma & Rejection', 'description': 'Treat infected persons with love, dignity, and acceptance, rejecting all gossip.'},
                {'step': 2, 'title': 'Provide Material & Nutritional Support', 'description': 'Share food, clothing, and school supplies with affected orphans and families.'},
                {'step': 3, 'title': 'Encourage Medical Adherence', 'description': 'Support patients in taking Antiretroviral therapy (ARVs) consistently.'},
                {'step': 4, 'title': 'Offer Spiritual Hope & Prayer', 'description': 'Share the comforting gospel of Jesus Christ and pray for healing and peace.'}
            ]
        },
        'context': 'Kenya has made massive strides in reducing HIV transmission through NASCOP, school education, and free ARVs. The Church operates hospices, clinics, and orphan support programs across the nation.',
        'reflection': 'How does sexual sin "sin against one's own body" in a unique biological and emotional way? How can you show love to classmates affected by chronic illness?',
        'summary': [
            'Sexual immorality leads to painful, debilitating STIs like Gonorrhea, Syphilis, and Hepatitis B.',
            'HIV destroys the body's immune system, making patients vulnerable to opportunistic infections.',
            'Psychological consequences include severe depression, guilt, low self-esteem, and academic decline.',
            'Christians practice abstinence for protection while extending radical love and support to the sick.'
        ],
        'mcq': {
            'question': 'Why is Hepatitis B considered a particularly dangerous sexually transmitted viral infection?',
            'options': [
                'A) It is transmitted only through contaminated drinking water.',
                'B) It attacks and destroys liver tissue, has no cure once contracted, and can lead to death.',
                'C) It causes immediate temporary hair loss.',
                'D) It is easily cured with standard headache tablets.'
            ],
            'answer': 'B',
            'explanation': 'Hepatitis B is a virulent viral infection that attacks the liver, potentially leading to fatal liver failure or cancer.'
        }
    },
    {
        'topic_order': 2,
        'topic_name': 'Christian Moral Values',
        'topic_desc': 'Christian ethics regarding human sexuality, sexual purity, traditional African comparisons, overcoming temptations, biological/psychological consequences, and sanctity of life.',
        'unit_order': 6,
        'unit_name': 'Abortion and Divorce: Irresponsible Social Behaviors',
        'unit_desc': 'Biblical teachings on the sanctity of human life, prohibition of abortion, permanence of marriage covenant, and family reconciliation.',
        'lesson_title': 'Abortion and Divorce: Irresponsible Social Behaviors',
        'svg_fn': get_svg_t2_l6,
        'image': {
            'title': 'Mother and Child: The Sacred Gift of Human Life',
            'caption': 'A mother holding her newborn infant, symbolizing the sacred gift of life in the womb and the protective covenant of family.',
            'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Mother_and_child_-_Africa.jpg/800px-Mother_and_child_-_Africa.jpg',
            'author': 'Wikimedia Commons',
            'licensing': 'CC BY-SA 4.0'
        },
        'youtube': {
            'title': 'BibleProject: Covenants — God's Unbreakable Partnerships',
            'description': 'Understanding how marriage is an indissoluble holy covenant reflecting God's steadfast love and faithfulness.',
            'youtube_id': '7_CGP-12AE0'
        },
        'goals': [
            'Define abortion (spontaneous vs. induced) and explain why Christians consider induced abortion a sin',
            'Analyze the causes, physical consequences, and emotional trauma of induced abortion',
            'Examine biblical teachings on the permanence of marriage and the destructive effects of divorce'
        ],
        'intro': 'Human life begins at conception and is sacred in God's sight. Likewise, marriage is designed to be an unbreakable lifelong partnership. When abortion terminates an unborn life or divorce tears a family apart, God's holy design is wounded.',
        'scripture': '### Exodus 20:13
> "You shall not murder."

### Matthew 19:4-6
> "'Haven't you read,' he replied, 'that at the beginning the Creator made them male and female, and said, "For this reason a man will leave his father and mother and be united to his wife, and the two will become one flesh"? So they are no longer two, but one flesh. Therefore what God has joined together, let no one separate.'"

### Malachi 2:16
> "'The man who hates and divorces his wife,' says the Lord, the God of Israel, 'does violence to the one he should protect.'"',
        'theology': 'God is the sole author and giver of human life. Unborn children bear God's image from conception (Psalm 139:13-16). Marriage is an indissoluble spiritual covenant joined by God, requiring unconditional love, patience, and mutual forgiveness.',
        'deep_dive': '### Abortion & Divorce
- **Spontaneous Abortion (Miscarriage):** Natural loss of pregnancy due to medical factors; requires pastoral comfort.
- **Induced Abortion:** Deliberate termination of pregnancy. Considered a violation of the 6th Commandment ("You shall not murder"). Physical risks include severe hemorrhage, uterine perforation, infertility, and death.
- **Causes of Abortion:** Fear of poverty, disruption of studies, social stigma, and pressure from partners.
- **Causes & Effects of Divorce:** Adultery, domestic violence, alcohol abuse, and selfishness. Results in emotional trauma for children, broken homes, and economic hardship.',
        'process': {
            'title': 'Framework: 4-Step Christian Crisis Support & Family Reconciliation Guide',
            'steps': [
                {'step': 1, 'title': 'Empathetic Crisis Counseling', 'description': 'Provide compassionate shelter and counseling for young women facing unplanned pregnancies.'},
                {'step': 2, 'title': 'Defend Unborn Life', 'description': 'Encourage carrying pregnancy to term with church and family support.'},
                {'step': 3, 'title': 'Pastoral Marriage Mediation', 'description': 'Help couples in conflict resolve grievances through professional biblical counseling.'},
                {'step': 4, 'title': 'Foster Christlike Forgiveness', 'description': 'Promote genuine repentance, healing, and commitment to family stability.'}
            ]
        },
        'context': 'Under Article 26(4) of the Constitution of Kenya, abortion is illegal unless permitted by a trained medical professional in an emergency. Kenya's Ministry of Education has a School Re-entry Policy to support teenage mothers.',
        'reflection': 'When a teenager becomes pregnant, she faces intense fear. How can the Church and family show Christ's grace and practical support without condoning immorality?',
        'summary': [
            'Human life begins at conception and is sacred; induced abortion violates the 6th Commandment.',
            'Induced abortion causes severe physical hazards including infertility, hemorrhage, and death.',
            'Marriage is a permanent divine covenant that must not be broken (Matthew 19:6).',
            'Christian communities provide crisis pregnancy care, counseling, and family reconciliation.'
        ],
        'mcq': {
            'question': 'Why do Christians consider induced abortion to be a serious moral sin?',
            'options': [
                'A) Because medical procedures are too costly.',
                'B) Because God is the sole giver of human life, and terminating a pregnancy violates the commandment "You shall not murder" (Exodus 20:13).',
                'C) Because children are not valued in the Bible.',
                'D) Because it encourages students to stay in school.'
            ],
            'answer': 'B',
            'explanation': 'Christianity teaches that human life begins at conception in God's image, making induced abortion the taking of innocent human life.'
        }
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# EXECUTE INGESTION TRANSACTION
# ─────────────────────────────────────────────────────────────────────────────

with transaction.atomic():
    total_lessons = 0
    total_blocks = 0
    total_assets = 0

    for cfg in LESSONS_CONFIG:
        topic_obj, _ = Topic.objects.get_or_create(
            subject=cre,
            order=cfg['topic_order'],
            defaults={'name': cfg['topic_name'], 'description': cfg['topic_desc']}
        )
        topic_obj.name = cfg['topic_name']
        topic_obj.description = cfg['topic_desc']
        topic_obj.save()

        unit_obj, _ = LearningUnit.objects.get_or_create(
            topic=topic_obj,
            order=cfg['unit_order'],
            defaults={'name': cfg['unit_name'], 'description': cfg['unit_desc']}
        )
        unit_obj.name = cfg['unit_name']
        unit_obj.description = cfg['unit_desc']
        unit_obj.save()

        # Delete existing lessons in this unit to re-ingest clean and idempotent
        unit_obj.lessons.all().delete()

        lesson = Lesson.objects.create(
            topic=topic_obj,
            learning_unit=unit_obj,
            title=cfg['lesson_title'],
            status='published',
            version=1,
            immutable_metadata={
                'grade': 'Grade 9',
                'subject': 'CRE',
                'topic_order': cfg['topic_order'],
                'topic_name': cfg['topic_name'],
                'unit_order': cfg['unit_order'],
                'author': 'VLearn CRE Ingestion Engine',
                'curriculum_framework': 'CBC Kenya',
                'enrichment_version': 'v3_pedagogical'
            }
        )
        total_lessons += 1

        # Assets
        img_info = cfg['image']
        img_asset = LessonAsset.objects.create(
            lesson=lesson, asset_type='image', source_type='external', storage_type='url', status='attached',
            title=img_info['title'], description=img_info['caption'], url=img_info['url'],
            metadata={'author': img_info['author'], 'licensing': img_info['licensing'], 'caption': img_info['caption']}
        )
        total_assets += 1

        svg_content = cfg['svg_fn']()
        svg_asset = LessonAsset.objects.create(
            lesson=lesson, asset_type='diagram', source_type='ai_generated', storage_type='url', status='attached',
            title=f"Diagram: {cfg['lesson_title']}",
            description=f"Responsive vector diagram illustrating {cfg['lesson_title']}.",
            url=f"https://vlearn.africa/assets/cre/t{cfg['topic_order']}_l{cfg['unit_order']}.svg",
            metadata={'svg_xml': svg_content, 'viewBox': '0 0 800 450', 'theme': '#0f172a'}
        )
        total_assets += 1

        yt_info = cfg['youtube']
        yt_asset = LessonAsset.objects.create(
            lesson=lesson, asset_type='youtube', source_type='external', storage_type='url', status='attached',
            title=yt_info['title'], description=yt_info['description'],
            url=f"https://www.youtube.com/watch?v={yt_info['youtube_id']}",
            metadata={'youtube_id': yt_info['youtube_id'], 'embed_url': f"https://www.youtube.com/embed/{yt_info['youtube_id']}"}
        )
        total_assets += 1

        # Card 1 (Page 1): Discovery & Objectives (3 blocks)
        b1 = LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title='Discovery & Objectives', order=10, component_order=1,
            block_type='suggested_image', component_type='suggested_image', title=img_info['title'],
            content={'title': img_info['title'], 'url': img_info['url'], 'caption': img_info['caption'], 'author': img_info['author'], 'licensing': img_info['licensing']}
        )
        b1.assets.add(img_asset)
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title='Discovery & Objectives', order=20, component_order=2,
            block_type='learning_goal', component_type='learning_goal', title='Lesson Objectives',
            content={'goals': cfg['goals']}
        )
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=1, page_title='Discovery & Objectives', order=30, component_order=3,
            block_type='concept_explanation', component_type='concept_explanation', title='Sharing Experiences & Familiar Connection',
            content={'markdown': cfg['intro']}
        )
        total_blocks += 1

        # Card 2 (Page 2): Scriptural Exegesis (2 blocks)
        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title='Scriptural Exegesis', order=40, component_order=1,
            block_type='concept_explanation', component_type='concept_explanation', title='Core Biblical Foundations',
            content={'markdown': cfg['scripture']}
        )
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=2, page_title='Scriptural Exegesis', order=45, component_order=2,
            block_type='concept_explanation', component_type='concept_explanation', title='Theological Foundations & Principles',
            content={'markdown': cfg['theology']}
        )
        total_blocks += 1

        # Card 3 (Page 3): Vector SVG Diagram & Deep Dive (2 blocks)
        b3 = LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title='Pedagogical Diagram', order=50, component_order=1,
            block_type='suggested_diagram', component_type='suggested_diagram', title=f"Visual Architecture: {cfg['lesson_title']}",
            content={'title': f"Visual Architecture: {cfg['lesson_title']}", 'svg': svg_content, 'svg_xml': svg_content}
        )
        b3.assets.add(svg_asset)
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=3, page_title='Pedagogical Diagram', order=60, component_order=2,
            block_type='concept_explanation', component_type='concept_explanation', title='Theological Deep Dive & Analysis',
            content={'markdown': cfg['deep_dive']}
        )
        total_blocks += 1

        # Card 4 (Page 4): Practical Application & Context (2 blocks)
        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title='Practical Application', order=70, component_order=1,
            block_type='step_process', component_type='step_process', title=cfg['process']['title'],
            content=cfg['process']
        )
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=4, page_title='Practical Application', order=75, component_order=2,
            block_type='concept_explanation', component_type='concept_explanation', title='Kenyan Real-World Context & Integration',
            content={'markdown': cfg['context']}
        )
        total_blocks += 1

        # Card 5 (Page 5): Multimedia & Reflection (2 blocks)
        b5 = LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title='Multimedia & Reflection', order=80, component_order=1,
            block_type='suggested_video', component_type='suggested_video', title=yt_info['title'],
            content={'title': yt_info['title'], 'url': f"https://www.youtube.com/watch?v={yt_info['youtube_id']}", 'youtube_id': yt_info['youtube_id'], 'description': yt_info['description']}
        )
        b5.assets.add(yt_asset)
        total_blocks += 1

        LessonBlock.objects.create(
            lesson=lesson, page_number=5, page_title='Multimedia & Reflection', order=90, component_order=2,
            block_type='concept_explanation', component_type='concept_explanation', title='Spiritual Reflection & Ethical Introspection',
            content={'markdown': cfg['reflection']}
        )
        total_blocks += 1

        # Card 6 (Page 6): Mastery Check & Summary (2 blocks)
        LessonBlock.objects.create(
            lesson=lesson, page_number=6, page_title='Mastery Check', order=100, component_order=1,
            block_type='summary', component_type='summary', title='Summary & Key Takeaways',
            content={'points': cfg['summary']}
        )
        total_blocks += 1

        mcq_data = cfg['mcq']
        LessonBlock.objects.create(
            lesson=lesson, page_number=6, page_title='Mastery Check', order=110, component_order=2,
            block_type='knowledge_check', component_type='knowledge_check', title='Formative Knowledge Check',
            content={
                'check_type': 'multiple_choice',
                'question': mcq_data['question'],
                'options': mcq_data['options'],
                'answer': mcq_data['answer'],
                'explanation': mcq_data['explanation']
            }
        )
        total_blocks += 1

        print(f"[✓] Ingested Topic {cfg['topic_order']} Unit {cfg['unit_order']}: {cfg['lesson_title']} (Lesson ID: {lesson.id})")

    print(f"
================================================================================")
    print(f"INGESTION COMPLETE: {total_lessons} Lessons, {total_blocks} Blocks, {total_assets} Assets created.")
    print(f"================================================================================")
