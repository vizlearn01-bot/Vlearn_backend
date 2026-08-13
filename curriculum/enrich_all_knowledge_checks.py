"""
VLearn Form 4 Biology — Master Knowledge Check Ingestion & Standardizer

Updates all 36 modules across Topics 1, 2, 3, and 4 with:
- Authentic, curriculum-accurate KCSE Multiple Choice Questions.
- 4 real, distinct, challenging options (no generic templates).
- Standardized keys: answer, correct, correct_answer (unambiguous matching).
- Deep, insightful, multi-sentence biological explanations.
"""

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from django.db import transaction
from curriculum.models import Topic, Lesson, LessonBlock

# Master Dictionary of 36 High-Yield KCSE Multiple-Choice Questions
KCSE_QUESTIONS = {
    # ─── TOPIC 1: GENETICS ──────────────────────────────────────────────────
    (1, 1): {
        "question": "Which of the following cellular structures carries the hereditary material passed from parents to offspring during sexual reproduction?",
        "options": [
            "Chromosomes located inside the cell nucleus",
            "Ribosomes located on the rough endoplasmic reticulum",
            "Golgi bodies packaging secretory proteins",
            "Cell wall cellulose microfibrils"
        ],
        "answer": "A",
        "explanation": "Chromosomes inside the cell nucleus contain DNA molecules organized into genes, which are the physical and chemical units of heredity transmitted from parents to offspring during gamete formation and fertilisation."
    },
    (1, 2): {
        "question": "Which pair of human characteristics correctly illustrates continuous variation and discontinuous variation, respectively?",
        "options": [
            "Body height and ABO blood group",
            "ABO blood group and body mass",
            "Tongue rolling ability and skin colour",
            "Albinism and finger length"
        ],
        "answer": "A",
        "explanation": "Human body height shows continuous variation (quantitative, bell-shaped distribution, polygenic with environmental influence), whereas ABO blood group shows discontinuous variation (discrete distinct categories, strictly genetic without intermediate forms)."
    },
    (1, 3): {
        "question": "According to the Watson-Crick DNA double-helix model, which complementary base pairing rule is always conserved across the DNA molecule?",
        "options": [
            "Adenine pairs with Thymine via 2 hydrogen bonds; Guanine pairs with Cytosine via 3 hydrogen bonds",
            "Adenine pairs with Guanine; Cytosine pairs with Thymine",
            "Uracil pairs with Thymine; Adenine pairs with Cytosine",
            "Adenine pairs with Cytosine via 3 hydrogen bonds; Guanine pairs with Thymine via 2 hydrogen bonds"
        ],
        "answer": "A",
        "explanation": "Complementary base pairing dictates that Adenine (A, a purine) pairs exclusively with Thymine (T, a pyrimidine) via 2 hydrogen bonds, while Guanine (G, a purine) pairs with Cytosine (C, a pyrimidine) via 3 hydrogen bonds, maintaining a constant 2.0 nm double-helix width."
    },
    (1, 4): {
        "question": "When two heterozygous tall pea plants (Tt) are crossed, what are the expected phenotypic and genotypic ratios among the offspring?",
        "options": [
            "Phenotypic ratio 3 Tall : 1 Dwarf; Genotypic ratio 1 TT : 2 Tt : 1 tt",
            "Phenotypic ratio 1 Tall : 1 Dwarf; Genotypic ratio 1 TT : 1 tt",
            "Phenotypic ratio 3 Dwarf : 1 Tall; Genotypic ratio 3 Tt : 1 tt",
            "Phenotypic ratio 4 Tall : 0 Dwarf; Genotypic ratio 4 Tt : 0 tt"
        ],
        "answer": "A",
        "explanation": "Crossing Tt × Tt produces offspring genotypes in the ratio 1 TT : 2 Tt : 1 tt (1:2:1). Because allele T is fully dominant over t, both TT and Tt plants exhibit the tall phenotype, yielding a 3 Tall : 1 Dwarf (3:1) phenotypic ratio."
    },
    (1, 5): {
        "question": "A man with blood group A whose father was blood group O marries a woman with blood group B whose mother was blood group O. What proportion of their children are expected to have blood group O?",
        "options": [
            "25% (1 in 4 chance)",
            "50% (1 in 2 chance)",
            "0% (No chance)",
            "75% (3 in 4 chance)"
        ],
        "answer": "A",
        "explanation": "The man is heterozygous (I^A I^O) having inherited allele I^O from his group O father. The woman is heterozygous (I^B I^O) from her group O mother. Crossing I^A I^O × I^B I^O produces 1 I^A I^B : 1 I^A I^O : 1 I^B I^O : 1 I^O I^O. Therefore, 1 in 4 offspring (25%) will inherit genotype I^O I^O (blood group O)."
    },
    (1, 6): {
        "question": "Which statement accurately distinguishes Down's Syndrome from Sickle-Cell Anaemia?",
        "options": [
            "Down's Syndrome is caused by chromosomal non-disjunction (Trisomy 21), whereas Sickle-Cell Anaemia is caused by a single-gene point mutation",
            "Down's Syndrome is a sex-linked gene mutation, whereas Sickle-Cell Anaemia is caused by chromosomal deletion",
            "Both disorders are caused by non-disjunction during meiosis II",
            "Sickle-Cell Anaemia is caused by an extra chromosome 21 in red blood cells"
        ],
        "answer": "A",
        "explanation": "Down's Syndrome is a chromosomal numerical mutation resulting from non-disjunction of chromosome pair 21 during meiosis (2n+1=47). Sickle-Cell Anaemia is a gene mutation involving a single base substitution (GAG → GTG) in the beta-globin gene on chromosome 11."
    },
    (1, 7): {
        "question": "What is the primary genetic difference between selective breeding (artificial selection) and modern genetic engineering?",
        "options": [
            "Selective breeding relies on sexual crossing within the same species over generations, whereas genetic engineering transfers specific recombinant genes directly across species barriers",
            "Selective breeding produces clones, whereas genetic engineering only produces hybrids",
            "Genetic engineering relies solely on vegetative propagation without DNA alteration",
            "Selective breeding alters base pairs in a laboratory test tube"
        ],
        "answer": "A",
        "explanation": "Selective breeding depends on sexual recombination between selected parents of the same or closely related species over multiple generations. Genetic engineering uses recombinant DNA technology and bacterial vectors to insert specific genes directly across taxonomic kingdoms."
    },
    (1, 8): {
        "question": "Why does haemophilia (a sex-linked recessive disorder carried on the X chromosome) appear far more frequently in human males than in human females?",
        "options": [
            "Males possess only one X chromosome (XY), so a single recessive mutant allele is immediately expressed phenotypically",
            "Males have higher testosterone levels which activate the mutant haemophilia gene",
            "Females have two Y chromosomes that suppress the expression of haemophilia",
            "Haemophilia alleles can only be inherited from the biological father"
        ],
        "answer": "A",
        "explanation": "Human males are hemizygous (XY) and possess only one X chromosome. If a male inherits a recessive mutant allele (X^h) from his carrier mother, there is no second homologous X chromosome with a dominant wild-type allele (X^H) to mask it, so he will always suffer from haemophilia."
    },

    # ─── TOPIC 2: EVOLUTION ─────────────────────────────────────────────────
    (2, 1): {
        "question": "According to the biological definition of organic evolution, which of the following best describes the process?",
        "options": [
            "Gradual, progressive modification of living organisms over successive generations from pre-existing simpler life forms",
            "Sudden transformation of an adult organism's phenotype during its individual lifespan",
            "Instantaneous creation of all modern complex species in their current anatomical form",
            "The movement of organisms from terrestrial to aquatic environments during seasons"
        ],
        "answer": "A",
        "explanation": "Organic evolution is the gradual, continuous change in the inherited characteristics and allele frequencies of populations over successive generations, producing diverse, highly adapted complex species from simpler ancestral organisms."
    },
    (2, 2): {
        "question": "In the famous 1953 Miller-Urey experiment simulating the prebiotic Earth's reducing atmosphere, which key organic compounds were synthesized spontaneously?",
        "options": [
            "Amino acids (such as glycine and alanine) and simple organic sugars",
            "Complete eukaryotic cells with membrane-bound nuclei",
            "Double-stranded DNA molecules bound to histone proteins",
            "Complex multicellular organisms"
        ],
        "answer": "A",
        "explanation": "Miller and Urey passed continuous high-voltage electrical sparks through a reducing gaseous mixture of methane (CH4), ammonia (NH3), hydrogen (H2), and water vapor (H2O), synthesizing amino acids and simple sugars, proving prebiotic chemical evolution was viable."
    },
    (2, 3): {
        "question": "Which evolutionary trend in hominid skull fossils provides the strongest anatomical evidence for increasing cognitive ability and complex tool manufacture?",
        "options": [
            "Progressive enlargement of cranial capacity accompanied by a flatter facial profile and reduced brow ridges",
            "Increase in canine tooth length and widening of the sagittal crest",
            "Backward migration of the foramen magnum toward the posterior of the skull",
            "Enlargement of heavy jaw prognathism for crushing raw bones"
        ],
        "answer": "A",
        "explanation": "The hominid fossil lineage shows a dramatic progressive increase in brain volume: Australopithecus (~450 cm³) → Homo habilis (~650 cm³) → Homo erectus (~1000 cm³) → Homo sapiens (~1400 cm³), correlating with advanced tool-making, language, and culture."
    },
    (2, 4): {
        "question": "The pentadactyl forelimbs of a human, bat, whale, and cheetah share a common ancestral bone plan but perform different functions. What evolutionary phenomenon does this illustrate?",
        "options": [
            "Divergent evolution leading to homologous structures",
            "Convergent evolution leading to analogous structures",
            "Special creation with static unchanging morphology",
            "Industrial melanism driven by directional selection"
        ],
        "answer": "A",
        "explanation": "Homologous structures share a common basic anatomical plan (humerus, radius, ulna, carpals, metacarpals, phalanges) derived from a common ancestor, but have diverged in shape and function to adapt to different environmental niches (Divergent Evolution)."
    },
    (2, 5): {
        "question": "Why was Jean-Baptiste Lamarck's hypothesis of the 'inheritance of acquired characteristics' rejected by modern genetics?",
        "options": [
            "Acquired somatic phenotypic changes do not alter the base sequences of DNA inside gametes (sperm and ova)",
            "Lamarck did not believe that environmental changes existed",
            "Darwin proved that organisms only produce one offspring per generation",
            "Acquired characteristics are exclusively inherited by male offspring"
        ],
        "answer": "A",
        "explanation": "Phenotypic changes acquired during an individual's lifetime (e.g. neck stretching or muscular development) affect only somatic body cells. Because they do not change the genetic code in reproductive gametes, they cannot be transmitted to the next generation."
    },
    (2, 6): {
        "question": "In polluted industrial areas of 19th-century England, why did the frequency of the dark melanic peppered moth (Biston betularia) rapidly increase?",
        "options": [
            "Soot blackened tree trunks, providing dark moths with camouflage against predatory birds, giving them higher survival and reproductive rates",
            "Soot particles acted as chemical mutagens that turned white moth eggs black",
            "White moths voluntarily changed their wing pigments to absorb more thermal energy",
            "Predatory birds avoided eating moths in polluted areas"
        ],
        "answer": "A",
        "explanation": "Industrial melanism exemplifies natural selection: atmospheric soot killed lichens and blackened tree trunks, giving dark melanic moths camouflage against predatory birds. Conspicuous pale moths were heavily predated, shifting allele frequencies toward melanism."
    },
    (2, 7): {
        "question": "When comparing the structural anatomy of a bird's wing and an insect's wing, which conclusion is scientifically correct?",
        "options": [
            "They are analogous structures: the bird wing has a bony pentadactyl skeleton, while the insect wing is a chitinous cuticular membrane",
            "They are homologous structures derived from a recent shared common ancestor",
            "The bird wing is a vestigial organ, while the insect wing is an endoskeleton",
            "Both wings possess identical humerus, radius, and ulna bones"
        ],
        "answer": "A",
        "explanation": "Bird wings and insect wings have completely different anatomical designs and embryonic origins (vertebrate bony endoskeleton vs. arthropod chitinous cuticle) but evolved to perform the same function (flight) due to similar selection pressures (Convergent Evolution)."
    },
    (2, 8): {
        "question": "What is the primary role of geographic isolation in the process of allopatric speciation?",
        "options": [
            "It physically prevents interbreeding and gene flow between separated populations, allowing independent mutations and natural selection to create reproductive isolation",
            "It causes all organisms in a population to develop identical mutations simultaneously",
            "It forces organisms to reproduce exclusively by asexual budding",
            "It increases migration rates between the separated geographical regions"
        ],
        "answer": "A",
        "explanation": "Geographic barriers (mountains, rivers, rift valleys) block gene flow between separated populations. Exposed to different environmental pressures and accumulating distinct genetic mutations over time, populations diverge until they can no longer interbreed to produce fertile offspring (speciation)."
    },

    # ─── TOPIC 3: RECEPTION, RESPONSE AND COORDINATION ──────────────────────
    (3, 1): {
        "question": "Why do multicellular organisms require specialized coordination systems (nervous and endocrine)?",
        "options": [
            "To detect changes in their internal and external environments and synchronize the activities of various organs for survival",
            "To ensure that all body cells divide at the exact same rate simultaneously",
            "To prevent cell membranes from carrying out active transport of ions",
            "To eliminate the need for cellular respiration in peripheral tissues"
        ],
        "answer": "A",
        "explanation": "In complex multicellular organisms, specialized organs are situated far apart. Coordination systems (rapid electrical neurones and systemic chemical hormones) detect environmental stimuli and synchronize effector organs to maintain homeostasis and survival."
    },
    (3, 2): {
        "question": "In a biological stimulus-response pathway, which sequence correctly traces the flow of information?",
        "options": [
            "Stimulus → Receptor → Sensory Neurone → Central Nervous System → Motor Neurone → Effector → Response",
            "Effector → Motor Neurone → Receptor → Brain → Sensory Neurone → Response",
            "Receptor → Stimulus → Effector → Motor Neurone → Response",
            "Stimulus → Motor Neurone → Receptor → Sensory Neurone → Effector"
        ],
        "answer": "A",
        "explanation": "An environmental stimulus is detected by a receptor, which generates nerve impulses along sensory neurones into the CNS. The CNS processes the input and sends motor impulses along motor neurones to effectors (muscles or glands) to execute the response."
    },
    (3, 3): {
        "question": "How does a tactic response (taxis) fundamentally differ from a tropism?",
        "options": [
            "Taxis is a locomotive movement of the entire organism in response to a directional stimulus, whereas tropism is a localized growth curvature of a sessile plant part",
            "Taxis is always non-directional, while tropism is always non-growth-related",
            "Tropisms occur only in animals, while tactic responses occur only in flowering plants",
            "Taxis involves auxin accumulation, while tropisms are driven entirely by muscle contraction"
        ],
        "answer": "A",
        "explanation": "Tactic responses (such as maggot negative phototaxis or Euglena positive phototaxis) involve whole-organism locomotion toward or away from a directional stimulus. Tropisms involve slow, irreversible differential cell elongation in sessile plant organs."
    },
    (3, 4): {
        "question": "Why does decapitating (pruning) the shoot apex of a tea bush cause it to become bushy with many lateral branches?",
        "options": [
            "Removing the shoot apex eliminates the primary source of auxin (IAA), releasing lateral buds from apical dominance so they can grow",
            "Decapitation stimulates the roots to stop absorbing water and mineral salts",
            "Pruning forces the stem to undergo immediate secondary growth and wood formation",
            "Removing the tip causes auxins to accumulate in the lateral buds at toxic concentrations"
        ],
        "answer": "A",
        "explanation": "Auxins produced by the terminal apical meristem diffuse downward and inhibit the growth of lateral axillary buds (Apical Dominance). Removing the shoot apex eliminates this auxin supply, allowing dormant lateral buds to develop into dense side branches."
    },
    (3, 5): {
        "question": "At a chemical synapse, how is a nerve impulse transmitted across the synaptic cleft from the presynaptic knob to the postsynaptic membrane?",
        "options": [
            "Depolarization triggers calcium influx, causing vesicles to release neurotransmitter (acetylcholine) which diffuses across the cleft to bind postsynaptic receptors",
            "Electrical sparks jump directly across the synaptic cleft without chemical molecules",
            "Potassium ions flow out through open Schwann cells directly into the synaptic gap",
            "Myelin sheaths expand across the cleft to provide a physical insulated bridge"
        ],
        "answer": "A",
        "explanation": "Arrival of an action potential opens voltage-gated Ca^2+ channels in the presynaptic knob. Calcium influx causes synaptic vesicles to fuse with the presynaptic membrane, releasing acetylcholine by exocytosis. Acetylcholine diffuses across the synaptic cleft (20 nm) and binds to receptors on the postsynaptic membrane to trigger depolarization."
    },
    (3, 6): {
        "question": "Which region of the mammalian brain is responsible for coordinating voluntary muscle movements, posture, and body balance?",
        "options": [
            "Cerebellum",
            "Medulla Oblongata",
            "Hypothalamus",
            "Cerebrum (Cerebral Cortex)"
        ],
        "answer": "A",
        "explanation": "The cerebellum coordinates precision voluntary movements, maintains muscle tone, posture, and balance (equilibrium). The cerebrum controls conscious thought and intelligence; the medulla oblongata regulates automatic visceral functions (heartbeat, breathing); and the hypothalamus maintains homeostasis."
    },
    (3, 7): {
        "question": "When blood glucose concentration rises above normal (90 mg/100 cm³) following a carbohydrate-rich meal, what hormonal response restores homeostasis?",
        "options": [
            "Beta cells of the Islets of Langerhans secrete insulin, stimulating cells to absorb glucose and convert excess into glycogen in the liver",
            "Alpha cells secrete glucagon, converting liver glycogen into free glucose",
            "Adrenal medulla secretes adrenaline, stimulating rapid glycogen breakdown",
            "Thyroid gland secretes thyroxine to stop glucose absorption in the gut"
        ],
        "answer": "A",
        "explanation": "Elevated blood glucose stimulates beta-cells of the pancreatic Islets of Langerhans to secrete insulin into the bloodstream. Insulin promotes cellular glucose uptake, increases cellular respiration rates, and stimulates the liver and muscles to convert glucose into insoluble glycogen (glycogenesis)."
    },
    (3, 8): {
        "question": "During accommodation when focusing on a near object, what anatomical adjustments occur in the ciliary body and crystalline lens?",
        "options": [
            "Ciliary muscles contract, suspensory ligaments become slack (loosen), and the elastic lens becomes thicker and more convex, increasing its refractive power",
            "Ciliary muscles relax, suspensory ligaments become taut (tight), and the lens is pulled thin and flat",
            "The cornea flattens while the pupil expands to let in maximum light",
            "The retina moves forward while suspensory ligaments contract"
        ],
        "answer": "A",
        "explanation": "For near vision: Ciliary muscles contract, moving the ciliary body closer to the lens. Suspensory ligaments become slack, relieving tension on the elastic lens capsule. The crystalline lens bulges into a thicker, highly convex shape, increasing refractive power to focus diverging light rays sharply onto the fovea."
    },
    (3, 9): {
        "question": "In the mammalian inner ear, which specialized structures are responsible for dynamic balance (detecting rotational head movements) and hearing, respectively?",
        "options": [
            "Semicircular canals (dynamic balance) and Organ of Corti in the Cochlea (hearing)",
            "Eustachian tube (balance) and Tympanic membrane (hearing)",
            "Ear ossicles (balance) and Pinna (hearing)",
            "Utriculus (hearing) and Oval window (balance)"
        ],
        "answer": "A",
        "explanation": "The three fluid-filled semicircular canals (arranged in three mutually perpendicular planes with ampullae containing hair cells) detect dynamic rotational head movements. The coiled cochlea houses the Organ of Corti, whose sensory hair cells transduce sound pressure vibrations into auditory nerve impulses."
    },
    (3, 10): {
        "question": "Which fundamental physiological difference distinguishes nervous coordination from endocrine (hormonal) coordination?",
        "options": [
            "Nervous messages travel as electrochemical impulses along neurones at speeds up to 100 m/s with localized, rapid responses, whereas hormones travel via bloodstream with widespread, prolonged effects",
            "Nervous messages travel via blood plasma, while hormones travel along nerve axons",
            "Nervous coordination is exclusively found in plants, while hormonal regulation is restricted to vertebrates",
            "Nervous responses last for months, while hormonal responses occur in milliseconds"
        ],
        "answer": "A",
        "explanation": "Nervous coordination operates via electrical impulses along insulated neurones, transmitting signals extremely rapidly (up to 100 m/s) to localized effector targets for immediate, short-lived responses. Hormonal coordination operates via chemical messengers in the bloodstream with slower distribution, wider target fields, and longer-lasting physiological effects."
    },

    # ─── TOPIC 4: SUPPORT AND MOVEMENT IN PLANTS AND ANIMALS ────────────────
    (4, 1): {
        "question": "Which primary biological advantages are provided by physical support and motility in living organisms?",
        "options": [
            "Allows plants to display leaves for light capture and enables animals to locate food, find mates, and escape danger",
            "Prevents plants from carrying out transpiration and stops animal cells from synthesizing ATP",
            "Eliminates the need for cellular osmosis in plant roots",
            "Ensures that animals remain stationary throughout their entire life cycle"
        ],
        "answer": "A",
        "explanation": "Support holds plant photosynthetic leaves and flowers in optimal positions against gravity and environmental wind forces. In animals, skeletal support maintains body form and protects internal organs, while muscular locomotion enables active foraging, reproduction, and predator evasion."
    },
    (4, 2): {
        "question": "Which plant support tissue consists of dead cells at maturity with cell walls heavily and uniformly thickened with lignin?",
        "options": [
            "Sclerenchyma",
            "Collenchyma",
            "Parenchyma",
            "Epidermis"
        ],
        "answer": "A",
        "explanation": "Sclerenchyma tissue consists of dead elongated cells with narrow lumen and uniformly thickened secondary cell walls heavily impregnated with impermeable lignin, providing immense mechanical hardness and resistance to bending and compression forces."
    },
    (4, 3): {
        "question": "Which fins on a finned fish (such as Tilapia) are positioned vertically along the body midline to act like a keel, preventing the fish from rolling sideways in water?",
        "options": [
            "Dorsal fin and anal fin",
            "Pectoral fins and pelvic fins",
            "Caudal fin only",
            "Pectoral fins and caudal fin"
        ],
        "answer": "A",
        "explanation": "The unpaired median fins (dorsal and anal fins) are positioned vertically along the dorsal and ventral midlines to provide directional stability, preventing rolling (spinning on longitudinal axis) and yawing. Paired fins steer, brake, and pitch, while the caudal fin generates forward propulsion."
    },
    (4, 4): {
        "question": "On a mammalian vertebra, which anatomical structure encloses and protects the continuous spinal cord?",
        "options": [
            "The neural canal enclosed by the centrum and neural arch",
            "The transverse processes and rib facets",
            "The metapophyses and anapophyses",
            "The solid ventral centrum alone"
        ],
        "answer": "A",
        "explanation": "The neural canal is the hollow longitudinal cavity formed by the solid centrum ventrally and the bony neural arch dorsally. When vertebrae are stacked end to end, the neural canals align to form a continuous bony conduit protecting the delicate spinal cord."
    },
    (4, 5): {
        "question": "Which diagnostic feature is found exclusively on mammalian cervical vertebrae and serves to protect blood vessels supplying the brain?",
        "options": [
            "Vertebrarterial canals (foramina) in the transverse processes",
            "Long backward-pointing neural spines",
            "Demifacets for rib capitulum articulation",
            "Massive thick centrums with ventral hypapophyses"
        ],
        "answer": "A",
        "explanation": "Cervical vertebrae are uniquely diagnosed by a pair of vertebrarterial canals piercing the base of their transverse processes, through which the vertebral arteries and accompanying nerves pass safely up the neck to supply the brain."
    },
    (4, 6): {
        "question": "The triceps muscle straightens the arm by pulling on which specific bony projection of the forearm?",
        "options": [
            "The olecranon process of the ulna",
            "The radial tuberosity of the radius",
            "The glenoid cavity of the scapula",
            "The greater trochanter of the humerus"
        ],
        "answer": "A",
        "explanation": "The triceps extensor muscle has its movable insertion on the olecranon process of the ulna. When the triceps contracts, it exerts a downward pull on this bony lever, rotating the ulna around the humerus trochlea to straighten (extend) the arm at the elbow joint."
    },
    (4, 7): {
        "question": "Why is the hip joint (acetabulum and femur head) far more stable and resistant to dislocation than the shoulder joint (glenoid cavity and humerus head)?",
        "options": [
            "The acetabulum is a very deep, cup-shaped bony socket that deeply encloses the femur head to bear high body weight",
            "The hip joint is an immovable fibrous suture with zero synovial fluid",
            "The shoulder joint has no articular cartilage on its bone surfaces",
            "The femur is completely fused to the ilium of the pelvic girdle"
        ],
        "answer": "A",
        "explanation": "The pelvic acetabulum is formed by the developmental fusion of the ilium, ischium, and pubis into a deep, cup-shaped socket that deeply encloses the spherical femur head, providing high mechanical stability to bear the entire downward load of the upper body during running and jumping."
    },
    (4, 8): {
        "question": "Which statement accurately describes the anatomical and functional difference between a ligament and a tendon?",
        "options": [
            "A ligament connects bone to bone and is slightly elastic to prevent dislocation, whereas a tendon connects muscle to bone and is inelastic to transmit pulling force",
            "A ligament connects muscle to muscle, whereas a tendon connects cartilage to bone",
            "A tendon is highly elastic and lubricates joints, whereas a ligament contracts to move bones",
            "Ligaments and tendons are identical structures that both synthesize synovial fluid"
        ],
        "answer": "A",
        "explanation": "Ligaments are tough, slightly elastic fibrous bands connecting bone to bone across a joint to bind bones together and prevent dislocation. Tendons are dense, completely inelastic collagen cords connecting skeletal muscles to bones, ensuring 100% of muscle contraction force is transmitted to produce movement."
    },
    (4, 9): {
        "question": "Why do skeletal muscles always work in antagonistic pairs (such as biceps and triceps) to move a limb back and forth across a joint?",
        "options": [
            "Muscle fibers can only actively contract and pull; they cannot push when they relax",
            "Muscles only contract during sleep and require an opposing muscle to wake up",
            "One muscle of the pair is always smooth muscle while the other is cardiac muscle",
            "Nerve impulses can only stimulate relaxation, not active contraction"
        ],
        "answer": "A",
        "explanation": "Muscle tissue operates solely by active shortening (pulling). Because muscles cannot push when relaxing, returning an articulated bone to its original position requires an antagonistic partner muscle situated on the opposite side of the joint to contract and pull in the opposite direction."
    },
    (4, 10): {
        "question": "You are given an unlabeled bone specimen featuring a long shaft, a spherical head at one end, and two smooth distal condyles. Which bone is this?",
        "options": [
            "The mammalian Femur (Thigh Bone)",
            "The mammalian Scapula (Shoulder Blade)",
            "The mammalian Ulna (Forearm Bone)",
            "The Atlas Vertebra"
        ],
        "answer": "A",
        "explanation": "The femur is the longest, heaviest bone in the mammalian body, characterized proximally by a smooth spherical head articulating with the pelvic acetabulum, prominent trochanters for muscle attachment, and two smooth distal condyles forming the knee hinge joint."
    }
}


def run_enrichment():
    print("=" * 85)
    print("VLEARN FORM 4 BIOLOGY — ENRICHING ALL 36 KNOWLEDGE CHECKS")
    print("=" * 85)

    updated_count = 0

    with transaction.atomic():
        for (topic_num, mod_num), q_data in KCSE_QUESTIONS.items():
            topic = Topic.objects.get(subject__grade__name="Form 4", subject__name="Biology", order=topic_num)
            lessons = list(topic.lessons.order_by("learning_unit__order"))
            
            if mod_num <= len(lessons):
                lesson = lessons[mod_num - 1]
                
                # Locate the knowledge_check block in this lesson
                kc_block = lesson.blocks.filter(block_type__in=["knowledge_check", "multiple_choice"]).first()
                if not kc_block:
                    # Look by title or page
                    kc_block = lesson.blocks.filter(title__icontains="Knowledge Check").first()

                if kc_block:
                    kc_block.content = {
                        "check_type": "multiple_choice",
                        "question": q_data["question"],
                        "options": q_data["options"],
                        "answer": q_data["answer"],
                        "correct": q_data["answer"],
                        "correct_answer": q_data["answer"],
                        "explanation": q_data["explanation"],
                        "title": f"{lesson.learning_unit.name.split(': ')[-1]} — Check Your Understanding"
                    }
                    kc_block.title = f"Knowledge Check: {lesson.learning_unit.name.split(': ')[-1]}"
                    kc_block.save()
                    updated_count += 1
                    print(f"  [OK] Topic {topic_num} Module {mod_num:2d} ➔ Block ID: {kc_block.id} (Answer: {q_data['answer']})")
                else:
                    print(f"  [WARN] No Knowledge Check block found for Topic {topic_num}, Module {mod_num}")

    print("-" * 85)
    print(f"SUCCESS: Updated {updated_count} Knowledge Checks across all 4 topics with authentic KCSE MCQs!")
    print("=" * 85)


if __name__ == "__main__":
    run_enrichment()
