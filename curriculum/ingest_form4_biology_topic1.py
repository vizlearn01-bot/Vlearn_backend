"""
VLearn Form 4 Biology — Topic 1: Genetics
High-Structure Production Ingestion Engine

Topic: Genetics (Topic Order: 1)
Subject: Biology (Subject ID: 13)
Grade: Form 4 (Grade ID: 4)
Curriculum: 844 (Curriculum ID: 4)

Decomposed into 6 Learning Units & 6 Published Lessons (80 Total Pages):
  1. Foundations of Genetics and Biological Variation (12 Pages)
  2. Chromosomes, DNA Structure, and Protein Synthesis (12 Pages)
  3. Mendelian Monohybrid Inheritance & Test Crosses (14 Pages)
  4. Non-Mendelian Inheritance, Blood Groups, and Sex Linkage (14 Pages)
  5. Mutations, Mutagens, and Inherited Genetic Disorders (14 Pages)
  6. Applications of Genetics, Worked KCSE Problems, and Topic Assessment (14 Pages)

Usage:
  ./venv/bin/python curriculum/ingest_form4_biology_topic1.py [--replace]
"""

import os
import sys
import re
import django
from django.db import transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nexus_backend.settings")
django.setup()

from curriculum.models import (
    Curriculum, Grade, Subject, Topic, LearningUnit, Lesson, LessonBlock
)

def clean_text(text: str) -> str:
    """Removes bracket citations [33], [74], [132] and cleans double spaces."""
    if not text:
        return ""
    text = re.sub(r'\[(?:\d+|image_\d+|S\d+.*?|[\d,\s]+)\]', '', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def clean_dict(data):
    """Recursively cleans all strings in dictionary/list data structures."""
    if isinstance(data, str):
        return clean_text(data)
    elif isinstance(data, dict):
        return {k: clean_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_dict(item) for item in data]
    return data

def build_topic1_curriculum():
    """Returns the comprehensive pedagogical page and block structure for Topic 1: Genetics."""
    return [
        # =====================================================================
        # LESSON 1: Foundations of Genetics and Biological Variation
        # =====================================================================
        {
            "unit_order": 1,
            "unit_name": "Foundations of Genetics and Biological Variation",
            "unit_description": "Scope of genetics, heredity, variation types (continuous vs discontinuous), and environmental vs genetic interactions.",
            "lesson_title": "Foundations of Genetics and Biological Variation",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Foundations & Variation",
                        "content": {
                            "title": "Learning Objectives: Foundations & Variation",
                            "goals": [
                                "Define genetics, heredity, variation, genotype, phenotype, gene, and alleles.",
                                "Activate prerequisite knowledge of cell nucleus, chromatin, meiosis, and haploid/diploid gametes.",
                                "Distinguish between continuous variation (bell curve) and discontinuous variation (discrete bar graph).",
                                "Investigate environmental influences on phenotypic expression vs strict genetic control."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Welcome to Form 4 Biology: Topic 1 Genetics",
                        "content": {
                            "title": "Welcome to Form 4 Biology: Topic 1 Genetics",
                            "text": "Genetics is the branch of biology that studies heredity and variation. Heredity is the transmission of biological traits from parents to offspring through genes carried in gametes, while variation accounts for the physical differences observed between individuals of the same species."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Core Genetic Terminology Taxonomy",
                        "content": {
                            "term": "Heredity & Variation Definitions",
                            "definition": "Genetics studies how hereditary instructions stored in DNA dictate phenotypic variation across generations.",
                            "key_points": [
                                "Gene: Basic unit of inheritance carried at a specific locus on a chromosome.",
                                "Alleles: Alternative forms of the same gene (e.g., T for tall, t for dwarf).",
                                "Genotype: Genetic constitution of an organism (e.g., TT, Tt, tt).",
                                "Phenotype: Physical observable characteristics resulting from genotype-environment interaction (e.g., Tall plant)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Homozygous vs Heterozygous States",
                        "content": {
                            "title": "Homozygous vs Heterozygous States",
                            "text": "An organism is homozygous when it possesses two identical alleles for a gene (e.g., TT or tt). It is heterozygous when it possesses two different alleles (e.g., Tt)."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Prerequisite Concept Activation Map: Cell Nucleus to Diploid Zygote",
                        "content": {
                            "title": "Prerequisite Concept Activation Map: Cell Nucleus to Diploid Zygote",
                            "caption": "Cellular Inheritance Pathway: Eukaryotic Nucleus → Chromatin Condensation → Meiotic Gametogenesis → Diploid Zygote",
                            "description": "Flowchart showing Diploid Somatic Cell (2n) -> Meiosis -> Haploid Sperm/Egg Gametes (n) -> Fertilization -> Diploid Zygote (2n)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Prerequisite Knowledge Activation",
                        "content": {
                            "title": "Prerequisite Knowledge Activation",
                            "text": "Before studying inheritance, recall lower form topics:\n\n• Nucleus: The cell control center containing chromatin thread material.\n• Chromosomes: Structures formed when chromatin condenses during division.\n• Meiosis: Reduction division reducing diploid (2n) chromosome numbers to haploid (n) in gametes (sperm and egg).\n• Fertilisation: Restores the diploid state (2n) in the zygote."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Continuous Variation & Normal Distribution",
                        "content": {
                            "title": "Continuous Variation & Normal Distribution",
                            "text": "Continuous variation displays a smooth spectrum of intermediate phenotypes between two extremes without clear categories. Examples include human height, weight, skin color, and leaf length.\n\n• Characteristics: 1. Controlled by multiple genes (polygenic inheritance); 2. Highly influenced by environmental factors (nutrition, sunlight); 3. Plots a symmetrical bell-shaped normal distribution curve."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Biological Rule: Polygenic & Environmental Influence",
                        "content": {
                            "type": "tip",
                            "title": "Biological Rule: Polygenic & Environmental Influence",
                            "text": "A person may inherit genes for tall height, but severe malnutrition during childhood prevents them from reaching their full potential height, demonstrating gene-environment interaction."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Human Continuous Skin Color Variation Histogram",
                        "content": {
                            "title": "Human Continuous Skin Color Variation Histogram",
                            "caption": "Normal bell-shaped distribution curve demonstrating polygenic continuous variation in human skin pigmentation.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Human_skin_colour_chart_%26_histogram.PNG",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Human_skin_colour_chart_%26_histogram.PNG"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Discontinuous Variation & Single-Gene Control",
                        "content": {
                            "title": "Discontinuous Variation & Single-Gene Control",
                            "text": "Discontinuous variation shows distinct, clear-cut phenotypic categories with no intermediate forms. Examples include ABO blood groups (A, B, AB, O), tongue rolling ability, fingerprint patterns, and presence of free vs attached earlobes.\n\n• Characteristics: 1. Controlled by a single gene (or pair of alleles); 2. Completely unaffected by environmental factors; 3. Plots a discrete bar chart."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "definition_card",
                        "title": "Continuous vs Discontinuous Variation Comparison",
                        "content": {
                            "term": "Continuous vs Discontinuous Variation",
                            "definition": "Continuous variation exhibits a range of quantitative intermediates (polygenic & environmental). Discontinuous variation exhibits qualitative, distinct non-overlapping categories (single gene & uninfluenced by environment).",
                            "key_points": [
                                "Continuous Examples: Height, weight, intelligence, skin color, milk yield in cows.",
                                "Discontinuous Examples: Blood groups (A, B, AB, O), tongue rolling, sickle-cell anaemia, albinism.",
                                "Graphing: Normal bell curve (continuous) vs Bar chart (discontinuous)."
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Continuous vs Discontinuous Variation Distribution Curves",
                        "content": {
                            "title": "Continuous vs Discontinuous Variation Distribution Curves",
                            "caption": "Graphical Comparison: Symmetrical Bell-Shaped Normal Curve (Continuous Height) vs Discrete Bar Chart (ABO Blood Groups)",
                            "description": "Dual chart contrasting continuous normal distribution curve with discontinuous discrete category bar chart."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison Matrix: Continuous vs Discontinuous Variation",
                        "content": {
                            "headers": ["Feature", "Continuous Variation", "Discontinuous Variation"],
                            "rows": [
                                ["Phenotypic Range", "Smooth gradient with quantitative intermediates", "Clear-cut, discrete non-overlapping categories"],
                                ["Genetic Control", "Polygenic (controlled by multiple genes)", "Monogenic (controlled by a single gene or pair)"],
                                ["Environmental Impact", "Strongly influenced by environmental factors", "Completely unaffected by environmental factors"],
                                ["Graphical Representation", "Symmetrical bell-shaped normal curve", "Discrete bar chart"],
                                ["Biological Examples", "Human height, weight, skin color, crop yield", "ABO blood groups, tongue rolling, albinism"]
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Practical Biology: Investigating Variation",
                        "content": {
                            "title": "Practical Biology: Investigating Variation",
                            "text": "Students measure height/wrist circumferences of 50 classmates (continuous data) and tally tongue rollers vs non-rollers (discontinuous data) to construct class frequency histograms."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "concept_explanation",
                        "title": "Causes of Genetic Variation",
                        "content": {
                            "title": "Causes of Genetic Variation",
                            "text": "Genetic variation arises through three key mechanisms:\n1. Crossing over during prophase I of meiosis;\n2. Independent assortment of homologous chromosomes during metaphase I;\n3. Random fertilisation of male and female gametes."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Exam Tip: Graphing Variation Data",
                        "content": {
                            "type": "tip",
                            "title": "Exam Tip: Graphing Variation Data",
                            "text": "In KCSE practical exams, continuous data (height) requires a line graph or histogram with touching bars, while discontinuous data (blood groups) requires separated bar chart columns."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Variation Classification Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Variation Classification Simulator",
                            "prompt": "Classify the following human traits: (1) ABO Blood Group (A, B, AB, O); (2) Human Body Height (140 cm to 195 cm).",
                            "options": [
                                "Option A: Blood group is Discontinuous (single gene, discrete categories); Height is Continuous (polygenic, bell curve).",
                                "Option B: Both traits are continuous and affected by diet.",
                                "Option C: Height is discontinuous because people are either short or tall."
                            ],
                            "correct_option": "Option A: Blood group is Discontinuous (single gene, discrete categories); Height is Continuous (polygenic, bell curve).",
                            "explanation": "Blood group has 4 distinct categories unaffected by diet (discontinuous). Height shows a smooth quantitative spectrum (continuous)."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Variation & Foundations",
                        "content": {
                            "question": "Which biological characteristic distinguishes discontinuous variation from continuous variation?",
                            "options": [
                                "Discontinuous variation is controlled by a single gene and is completely unaffected by environmental factors.",
                                "Discontinuous variation plots a smooth bell-shaped normal curve.",
                                "Continuous variation is only found in bacterial cells.",
                                "Discontinuous variation changes dramatically when a person changes their diet."
                            ],
                            "correct_answer": 0,
                            "explanation": "Discontinuous variation is monogenic and unaffected by environment, producing discrete categories."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Foundations of Genetics: Key Takeaways",
                        "content": {
                            "title": "Foundations of Genetics: Key Takeaways",
                            "summary_points": [
                                "Genetics studies heredity (passing traits via genes) and variation (differences between individuals).",
                                "Alleles are alternative forms of a gene occupying the same locus on homologous chromosomes.",
                                "Continuous variation shows quantitative intermediates (polygenic & environmental, bell curve).",
                                "Discontinuous variation shows discrete categories (monogenic & environment-resistant, bar chart).",
                                "Genetic variation is generated by crossing over, independent assortment, and random fertilisation."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 2: Chromosomes, DNA Structure, and Protein Synthesis
        # =====================================================================
        {
            "unit_order": 2,
            "unit_name": "Chromosomes, DNA Structure, and Protein Synthesis",
            "unit_description": "Chromosome architecture, Watson-Crick double helix DNA model, transcription and translation protein synthesis, and DNA vs RNA comparison.",
            "lesson_title": "Chromosomes, DNA Structure, and Protein Synthesis",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Chromosomes & Nucleic Acids",
                        "content": {
                            "title": "Learning Objectives: Chromosomes & Nucleic Acids",
                            "goals": [
                                "Describe chromosome structure (chromatids, centromere, histones, autosomes vs sex chromosomes).",
                                "Detail the Watson-Crick DNA double helix model and complementary base pairing rules.",
                                "Trace the molecular pathway of protein synthesis (transcription & translation).",
                                "Construct a structural and chemical comparison matrix between DNA and RNA."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Chemical Basis of Heredity",
                        "content": {
                            "title": "The Chemical Basis of Heredity",
                            "text": "Genes are not abstract concepts; they are specific sequences of Deoxyribonucleic Acid (DNA) packaged into microscopic thread-like structures called chromosomes inside the cell nucleus."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Chromosome Architecture: Chromatids, Centromere, and Histone Spools",
                        "content": {
                            "title": "Chromosome Architecture: Chromatids, Centromere, and Histone Spools",
                            "caption": "Structural Organization of a Replicated Chromosome Displaying Sister Chromatids, Centromere, and DNA Wrapped Around Histone Proteins",
                            "description": "Diagram illustrating replicated chromosome with sister chromatids held by a centromere, uncoiling to show DNA double helix wrapped around octamer histone proteins."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Chromosome Structure & Autosomes vs Sex Chromosomes",
                        "content": {
                            "title": "Chromosome Structure & Autosomes vs Sex Chromosomes",
                            "text": "Human body cells contain 46 chromosomes (23 homologous pairs):\n\n• Autosomes (44 chromosomes / 22 pairs): Control general somatic body characteristics.\n• Sex Chromosomes / Heterosomes (2 chromosomes / 1 pair): XX in females, XY in males, determining biological sex."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_image",
                        "title": "Human Chromosome Karyotype",
                        "content": {
                            "title": "Human Chromosome Karyotype",
                            "caption": "Karyogram of human male chromosomes arranged in 22 autosome pairs and 1 XY sex chromosome pair.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Human_karyotype_with_bands_and_sub-bands.png",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Human_karyotype_with_bands_and_sub-bands.png"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Watson-Crick DNA Double Helix Model",
                        "content": {
                            "title": "The Watson-Crick DNA Double Helix Model",
                            "text": "DNA is a double-stranded macromolecule wound into a right-handed double helix. Each strand is a polymer composed of repeating monomer units called nucleotides.\n\n• Nucleotide Components: 1. Deoxyribose sugar; 2. Phosphate group; 3. Nitrogenous base (Adenine, Thymine, Cytosine, Guanine).\n• Base Pairing Rules: Adenine pairs with Thymine (A=T via 2 hydrogen bonds); Cytosine pairs with Guanine (C≡G via 3 hydrogen bonds)."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Watson-Crick DNA Double Helix Structure & Nucleotide Base Pairing",
                        "content": {
                            "title": "Watson-Crick DNA Double Helix Structure & Nucleotide Base Pairing",
                            "caption": "Molecular Model Displaying Sugar-Phosphate Backbones, Antiparallel Strands (5' to 3'), and Complementary Hydrogen Base Pairing (A=T, C≡G)",
                            "description": "Chemical diagram showing antiparallel sugar-phosphate backbones connected by A=T double hydrogen bonds and C≡G triple hydrogen bonds."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Complementary Base Pairing Rule",
                        "content": {
                            "term": "Chargaff's Base Pairing Rule",
                            "definition": "In DNA, Purine bases (Adenine & Guanine) always pair with Pyrimidine bases (Thymine & Cytosine). Adenine pairs strictly with Thymine (A=T), and Cytosine pairs strictly with Guanine (C≡G).",
                            "key_points": [
                                "Purines: Adenine (A), Guanine (G) — double-ring nitrogen structures.",
                                "Pyrimidines: Thymine (T), Cytosine (C) — single-ring nitrogen structures.",
                                "Hydrogen Bonds: 2 bonds between A and T; 3 bonds between C and G."
                            ]
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_image",
                        "title": "Watson-Crick DNA Double Helix Model Visualization",
                        "content": {
                            "title": "Watson-Crick DNA Double Helix Model Visualization",
                            "caption": "3D ribbon visualization of the DNA double helix showing sugar-phosphate backbones and complementary nitrogenous base rungs.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/c/c4/DNA_double_helix_horizontal.png",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:DNA_double_helix_horizontal.png"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Central Dogma: Gene to Protein",
                        "content": {
                            "title": "The Central Dogma: Gene to Protein",
                            "text": "Genes dictate physical traits by controlling protein synthesis (enzymes, structural proteins) in a two-step molecular pathway:\n\n1. Transcription: Occurs in the nucleus. DNA unwinds and an RNA polymerase enzyme synthesizes a single-stranded messenger RNA (mRNA) copy using complementary base pairing (Uracil replaces Thymine).\n\n2. Translation: Occurs on ribosomes in the cytoplasm. Transfer RNA (tRNA) molecules read mRNA codons (triplets) and assemble specific amino acids into a polypeptide protein chain."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Central Dogma: Transcription & Translation Protein Synthesis Pathway",
                        "content": {
                            "title": "Central Dogma: Transcription & Translation Protein Synthesis Pathway",
                            "caption": "Molecular Flowchart: Nuclear DNA → mRNA Transcription → Cytoplasmic Ribosome Translation → tRNA Amino Acid Polypeptide Chain",
                            "description": "Diagram illustrating nuclear DNA unwinding, mRNA synthesis, nuclear pore exit, ribosome binding, tRNA anticodon pairing, and growing amino acid chain."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Transcription & Translation Mechanics",
                        "content": {
                            "title": "Transcription & Translation Mechanics",
                            "text": "• Codon: A triplet sequence of bases on mRNA coding for a specific amino acid (e.g., AUG = Methionine start codon).\n• Anticodon: Complementary triplet on tRNA that pairs with mRNA codon during translation on the ribosome."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Structural & Chemical Comparison Matrix: DNA vs RNA",
                        "content": {
                            "title": "Structural & Chemical Comparison Matrix: DNA vs RNA",
                            "caption": "Comparative Architecture: Double-Stranded DNA (Deoxyribose, Thymine) vs Single-Stranded RNA (Ribose, Uracil)",
                            "description": "Comparative matrix contrasting DNA (Double helix, Deoxyribose sugar, Thymine base, Permanent nuclear master copy) with RNA (Single strand, Ribose sugar, Uracil base, Mobile cytoplasmic messenger)."
                        }
                    },
                    {
                        "type": "comparison_table",
                        "title": "Comparison Matrix: DNA vs RNA",
                        "content": {
                            "headers": ["Feature", "Deoxyribonucleic Acid (DNA)", "Ribonucleic Acid (RNA)"],
                            "rows": [
                                ["Strand Structure", "Double-stranded twisted helix", "Single-stranded linear or cloverleaf chain"],
                                ["Pentose Sugar", "Deoxyribose (one less oxygen atom)", "Ribose sugar"],
                                ["Nitrogenous Bases", "Adenine, Thymine, Cytosine, Guanine", "Adenine, Uracil (replaces T), Cytosine, Guanine"],
                                ["Location in Cell", "Permanently locked inside cell nucleus", "Synthesized in nucleus, functions in cytoplasm"],
                                ["Biological Function", "Permanent master genetic repository", "Transfers genetic code to assemble proteins"]
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "concept_explanation",
                        "title": "Role of RNA in Protein Synthesis",
                        "content": {
                            "title": "Role of RNA in Protein Synthesis",
                            "text": "Three types of RNA collaborate in protein synthesis: Messenger RNA (mRNA) carries the genetic recipe from nucleus to ribosome; Ribosomal RNA (rRNA) forms the structural ribosome factory; Transfer RNA (tRNA) delivers amino acids to the growing chain."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Exam Trap: Base Pairing in RNA",
                        "content": {
                            "type": "warning",
                            "title": "Exam Trap: Base Pairing in RNA",
                            "text": "RNA contains NO Thymine! During transcription, Adenine on DNA pairs with Uracil (U) on mRNA."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive DNA Base Pairing & Translation Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive DNA Base Pairing & Translation Simulator",
                            "prompt": "Given a DNA template strand sequence: 3'-T-A-C-C-G-A-A-T-T-5', determine the complementary mRNA sequence synthesized during transcription.",
                            "options": [
                                "Option A: 5'-A-U-G-G-C-U-U-A-A-3' (Adenine pairs with Uracil on mRNA; Thymine pairs with Adenine).",
                                "Option B: 5'-A-T-G-G-C-T-T-A-A-3' (Incorrect: RNA contains no Thymine).",
                                "Option C: 5'-U-A-C-C-G-A-A-U-U-3' (Incorrect: Copying identical strand)."
                            ],
                            "correct_option": "Option A: 5'-A-U-G-G-C-U-U-A-A-3' (Adenine pairs with Uracil on mRNA; Thymine pairs with Adenine).",
                            "explanation": "During transcription, DNA Adenine pairs with mRNA Uracil (U), DNA Thymine pairs with mRNA Adenine (A), and Cytosine pairs with Guanine (G)."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Chromosomes, DNA, & Protein Synthesis",
                        "content": {
                            "question": "Which nitrogenous base is present in RNA molecules but completely absent in DNA molecules?",
                            "options": [
                                "Uracil",
                                "Thymine",
                                "Cytosine",
                                "Guanine"
                            ],
                            "correct_answer": 0,
                            "explanation": "Uracil replaces Thymine in all RNA molecules."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "summary",
                        "title": "Nucleic Acids & Chromosomes: Key Takeaways",
                        "content": {
                            "title": "Nucleic Acids & Chromosomes: Key Takeaways",
                            "summary_points": [
                                "Chromosomes consist of DNA double helix strands packaged around octamer histone spools.",
                                "DNA nucleotides consist of deoxyribose, phosphate, and bases: A=T (2 H-bonds) and C≡G (3 H-bonds).",
                                "Protein synthesis proceeds via Transcription (DNA -> mRNA in nucleus) and Translation (mRNA -> tRNA amino acid chain on ribosomes).",
                                "DNA is double-stranded with deoxyribose and Thymine; RNA is single-stranded with ribose and Uracil."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 3: Mendelian Monohybrid Inheritance & Test Crosses
        # =====================================================================
        {
            "unit_order": 3,
            "unit_name": "Mendelian Monohybrid Inheritance & Test Crosses",
            "unit_description": "Gregor Mendel's experiments, First Law of Segregation, monohybrid crosses, Punnett squares (3:1 and 1:2:1 ratios), and test cross genotype determination.",
            "lesson_title": "Mendelian Monohybrid Inheritance & Test Crosses",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Mendelian Inheritance",
                        "content": {
                            "title": "Learning Objectives: Mendelian Inheritance",
                            "goals": [
                                "Explain why Gregor Mendel selected the garden pea (Pisum sativum) for inheritance experiments.",
                                "State Mendel's First Law of Segregation using precise genetic terminology.",
                                "Construct Punnett squares for monohybrid crosses to derive F1 and F2 genotypic (1:2:1) and phenotypic (3:1) ratios.",
                                "Execute test cross (back cross) mechanics to determine the unknown genotype of a dominant phenotype."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Gregor Mendel: Father of Modern Genetics",
                        "content": {
                            "title": "Gregor Mendel: Father of Modern Genetics",
                            "text": "In the 1860s, Austrian monk Gregor Mendel discovered the fundamental laws of inheritance through breeding experiments on garden pea plants (*Pisum sativum*)."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_image",
                        "title": "Gregor Mendel's Garden Pea (Pisum sativum)",
                        "content": {
                            "title": "Gregor Mendel's Garden Pea (Pisum sativum)",
                            "caption": "Garden pea pods (Pisum sativum) exhibiting distinct contrasting physical traits studied by Gregor Mendel.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 4.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Pisum_sativum_var._macrocarpum_Ilowiecki_2017-04-14_6973.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Why Mendel Chose the Garden Pea",
                        "content": {
                            "title": "Why Mendel Chose the Garden Pea",
                            "text": "Mendel chose *Pisum sativum* for four key biological reasons:\n1. Possesses 7 distinct pairs of sharply contrasting binary traits (Tall vs Dwarf, Yellow vs Green seeds, Purple vs White flowers);\n2. Naturally self-pollinating, making true-breeding pure lines easy to isolate;\n3. Easily cross-pollinated artificially by removing stamens;\n4. Fast generation time producing large numbers of offspring per cross."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Mendelian Segregation Mechanics & 7 Garden Pea Traits",
                        "content": {
                            "title": "Mendelian Segregation Mechanics & 7 Garden Pea Traits",
                            "caption": "Visual Matrix of Mendel's 7 Contrasting Pea Plant Characteristics (Stem Height, Seed Shape, Seed Color, Pod Shape, Pod Color, Flower Color, Flower Position)",
                            "description": "Diagram listing 7 traits: Stem length (Tall/Dwarf), Seed shape (Round/Wrinkled), Seed color (Yellow/Green), Pod shape (Inflated/Constricted), Pod color (Green/Yellow), Flower color (Purple/White), Flower position (Axial/Terminal)."
                        }
                    },
                    {
                        "type": "definition_card",
                        "title": "Mendel's First Law: Law of Segregation",
                        "content": {
                            "term": "Mendel's Law of Segregation",
                            "definition": "The characteristics of an organism are controlled by factors (genes) occurring in pairs. During the formation of gametes, these paired alleles segregate so that each gamete receives only one allele from each pair.",
                            "key_points": [
                                "Parental Genotype: Tt (Heterozygous Tall).",
                                "Gamete Segregation: 50% carry allele T; 50% carry allele t.",
                                "Fertilisation: Random fusion of male and female gametes restores allele pairs in zygote."
                            ]
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Monohybrid Cross Mechanics",
                        "content": {
                            "title": "Monohybrid Cross Mechanics",
                            "text": "A monohybrid cross involves studying the inheritance of a single trait (e.g., stem height T vs t).\n\n• Pure Breeding Parents (P1): Homozygous Tall (TT) x Homozygous Dwarf (tt).\n• F1 Generation: All offspring are Heterozygous Tall (Tt) because Tall allele (T) is completely dominant over Dwarf allele (t).\n• F2 Generation (F1 x F1): Selfing Tt x Tt produces 3 Tall : 1 Dwarf phenotypic ratio, and 1 TT : 2 Tt : 1 tt genotypic ratio."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Monohybrid Cross Punnett Square (Tt x Tt) 3:1 Ratio",
                        "content": {
                            "title": "Monohybrid Cross Punnett Square (Tt x Tt) 3:1 Ratio",
                            "caption": "Punnett Square Grid Demonstrating F2 Offspring Segregation: 1 TT (Tall) : 2 Tt (Tall) : 1 tt (Dwarf)",
                            "description": "2x2 Punnett square grid with top gametes T, t and side gametes T, t yielding TT, Tt, Tt, tt."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Step-by-Step Monohybrid Cross Formatting",
                        "content": {
                            "question": "Construct a complete genetic cross between two heterozygous tall pea plants (Tt x Tt). State the genotypic and phenotypic ratios of the offspring.",
                            "strategy": "Follow standard KCSE format: Phenotypes -> Genotypes -> Gametes (circled) -> Punnett Square -> Ratios.",
                            "solution": [
                                "Parental Phenotypes: Tall  x  Tall",
                                "Parental Genotypes:  Tt    x  Tt",
                                "Gametes:            (T) (t)   (T) (t)",
                                "Punnett Square:\n      |   T   |   t   |\n  ----+-------+-------\n    T |  TT   |  Tt   |\n  ----+-------+-------\n    t |  Tt   |  tt   |\n",
                                "Genotypic Ratio: 1 TT : 2 Tt : 1 tt (1 Homozygous Tall : 2 Heterozygous Tall : 1 Homozygous Dwarf)",
                                "Phenotypic Ratio: 3 Tall : 1 Dwarf"
                            ]
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Dominance vs Recessiveness",
                        "content": {
                            "title": "Dominance vs Recessiveness",
                            "text": "A dominant allele (represented by uppercase T) masks the expression of a recessive allele (lowercase t) in the heterozygous state (Tt). Recessive traits are expressed physically ONLY in the homozygous recessive state (tt)."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Exam Rule: Always Circle Gametes!",
                        "content": {
                            "type": "tip",
                            "title": "Exam Rule: Always Circle Gametes!",
                            "text": "In KCSE genetics questions, failing to put circles around gamete letters during genetic cross diagrams will result in a loss of gamete marks."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Test Cross Mechanics: Determining Unknown Genotype (T_ x tt)",
                        "content": {
                            "title": "Test Cross Mechanics: Determining Unknown Genotype (T_ x tt)",
                            "caption": "Diagnostic Cross Model: Crossing Dominant Phenotype with Homozygous Recessive (tt) to Reveal Genotype",
                            "description": "Flowchart displaying Case A: If unknown is TT x tt -> 100% Tall offspring; Case B: If unknown is Tt x tt -> 1 Tall : 1 Dwarf (50% Dwarf) offspring."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "The Test Cross (or Back Cross)",
                        "content": {
                            "title": "The Test Cross (or Back Cross)",
                            "text": "A test cross is used to determine whether an organism displaying a dominant phenotype is homozygous dominant (TT) or heterozygous (Tt). The unknown plant is crossed with a homozygous recessive individual (tt).\n\n• Interpretation 1: If ALL offspring are Tall, the unknown parent was Homozygous Tall (TT).\n• Interpretation 2: If 50% offspring are Tall and 50% Dwarf (1:1 ratio), the unknown parent was Heterozygous Tall (Tt)."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "worked_example",
                        "title": "Worked Example: Monohybrid Cross in Maize",
                        "content": {
                            "question": "In maize, yellow grain color (Y) is dominant over white grain color (y). A yellow maize plant was crossed with a white maize plant. Half the resulting grains were yellow and half were white. Determine the genotype of the yellow parent.",
                            "strategy": "Analyze 1:1 ratio resulting from cross with recessive (yy).",
                            "solution": [
                                "Parental Phenotypes: Yellow Grain  x  White Grain",
                                "White Parent Genotype: yy (Homozygous Recessive)",
                                "Offspring Ratio: 50% Yellow (Yy) : 50% White (yy)",
                                "Conclusion: Since white grains (yy) appeared, the yellow parent must have contributed a recessive 'y' allele.",
                                "Yellow Parent Genotype: Yy (Heterozygous Yellow)."
                            ]
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Traps in Genetics Crosses",
                        "content": {
                            "mistake": "Using different letters for the same gene (e.g., T for Tall and D for Dwarf).",
                            "correction": "Always use uppercase and lowercase versions of the SAME letter for alleles of a gene (T for Tall, t for Dwarf).",
                            "reasoning": "Using different letters implies two separate unlinked genes rather than alleles at the same locus."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Punnett Square Monohybrid Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Punnett Square Monohybrid Simulator",
                            "prompt": "A black guinea pig (B) is crossed with a white guinea pig (b). All F1 offspring are black. Two F1 black guinea pigs are mated. What proportion of F2 offspring will be white?",
                            "options": [
                                "Option A: 25% (1/4) white (F2 ratio 3 Black : 1 White).",
                                "Option B: 50% (1/2) white.",
                                "Option C: 0% white."
                            ],
                            "correct_option": "Option A: 25% (1/4) white (F2 ratio 3 Black : 1 White).",
                            "explanation": "Selfing F1 Bb x Bb produces 1 BB : 2 Bb : 1 bb (25% homozygous recessive white)."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Mendelian Monohybrid Inheritance",
                        "content": {
                            "question": "What is the expected phenotypic ratio in the F2 generation of a classic Mendelian monohybrid cross with complete dominance?",
                            "options": [
                                "3 Dominant : 1 Recessive",
                                "1 Dominant : 2 Intermediate : 1 Recessive",
                                "1 Dominant : 1 Recessive",
                                "9 Dominant : 3 Recessive"
                            ],
                            "correct_answer": 0,
                            "explanation": "Selfing F1 heterozygous plants yields a 3:1 phenotypic ratio."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Mendelian Inheritance: Key Takeaways",
                        "content": {
                            "title": "Mendelian Inheritance: Key Takeaways",
                            "summary_points": [
                                "Mendel's First Law states that paired alleles segregate during gamete formation so each gamete carries one allele.",
                                "Monohybrid crosses with complete dominance yield F2 genotypic ratios of 1 TT : 2 Tt : 1 tt and phenotypic ratios of 3:1.",
                                "Test crosses determine unknown dominant genotypes by crossing with homozygous recessive (tt) individuals (100% vs 1:1 ratio)."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 4: Non-Mendelian Inheritance, Blood Groups, and Sex Linkage
        # =====================================================================
        {
            "unit_order": 4,
            "unit_name": "Non-Mendelian Inheritance, Blood Groups, and Sex Linkage",
            "unit_description": "Incomplete dominance, ABO multiple alleles, Rhesus factor, sex determination, sex-linked traits (haemophilia, color blindness), and pedigree analysis.",
            "lesson_title": "Non-Mendelian Inheritance, Blood Groups, and Sex Linkage",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Non-Mendelian & Sex Linkage",
                        "content": {
                            "title": "Learning Objectives: Non-Mendelian & Sex Linkage",
                            "goals": [
                                "Explain incomplete dominance and codominance with snapdragon and roan cattle examples.",
                                "Analyze multiple alleles in the human ABO blood group system and Rhesus factor incompatibility.",
                                "Describe human sex determination (XX vs XY) and sex linkage on the X chromosome.",
                                "Interpret pedigree charts tracing X-linked recessive disorders (haemophilia, color blindness)."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Complex Inheritance Patterns Beyond Mendel",
                        "content": {
                            "title": "Complex Inheritance Patterns Beyond Mendel",
                            "text": "Many biological traits do not conform strictly to Mendel's simple dominant-recessive rules. Incomplete dominance, codominance, multiple alleles, and sex linkage represent complex genetic extensions."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Incomplete Dominance & Co-Dominance Inheritance Patterns",
                        "content": {
                            "title": "Incomplete Dominance & Co-Dominance Inheritance Patterns",
                            "caption": "Comparative Cross Model: Snapdragon Pink Intermediate (RW) vs Roan Cattle (CR CW) Co-Dominant Red and White Hair Expression",
                            "description": "Flowchart contrasting Incomplete Dominance (Red RR x White WW -> 100% Pink RW) with Codominance (Red CRCR x White CWCW -> 100% Roan CRCW)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Incomplete Dominance vs Codominance",
                        "content": {
                            "title": "Incomplete Dominance vs Codominance",
                            "text": "• Incomplete Dominance: Neither allele is completely dominant. The heterozygous phenotype is an intermediate blend between both parents (e.g., Red RR x White WW snapdragons produce 100% Pink RW flowers; F2 ratio = 1 Red : 2 Pink : 1 White).\n\n• Codominance: Both alleles are expressed fully and simultaneously in the phenotype (e.g., Roan cattle carrying $C^R C^W$ alleles express both distinct red hairs and white hairs)."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "definition_card",
                        "title": "Multiple Alleles: Human ABO Blood Groups",
                        "content": {
                            "term": "ABO Blood Group Multiple Alleles",
                            "definition": "A gene possessing more than two alternative allele forms within a population. The ABO blood group gene has 3 alleles: IA, IB, and i.",
                            "key_points": [
                                "Allele IA: Synthesizes Antigen A on red blood cells.",
                                "Allele IB: Synthesizes Antigen B on red blood cells.",
                                "Allele i: Recessive allele; synthesizes no antigen.",
                                "Codominance: IA and IB are codominant (producing Blood Group AB: IA IB)."
                            ]
                        }
                    },
                    {
                        "type": "suggested_diagram",
                        "title": "ABO Blood Group Multiple Alleles & Co-Dominance Matrix",
                        "content": {
                            "title": "ABO Blood Group Multiple Alleles & Co-Dominance Matrix",
                            "caption": "Genotype-Phenotype Mapping Grid for ABO Blood System Displaying Antigens and Codominant Alleles",
                            "description": "Table listing Genotypes (IA IA, IA i -> Group A; IB IB, IB i -> Group B; IA IB -> Group AB; ii -> Group O)."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_image",
                        "title": "ABO Blood Group System Compatibility",
                        "content": {
                            "title": "ABO Blood Group System Compatibility",
                            "caption": "Compatibility flow chart demonstrating blood group donation paths between donor and recipient antigens.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/f/f6/ABO_donation_path.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:ABO_donation_path.jpg"
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Rhesus Factor & Erythroblastosis Fetalis",
                        "content": {
                            "title": "Rhesus Factor & Erythroblastosis Fetalis",
                            "text": "The Rhesus factor is an inherited blood protein ($Rh^+$ dominant over $Rh^-$).\n\n• Medical Hazard: If an $Rh^-$ mother carries an $Rh^+$ fetus, fetal blood leakage during childbirth causes the mother to produce anti-Rh antibodies. In a second $Rh^+$ pregnancy, maternal antibodies cross the placenta, destroying fetal red blood cells (Erythroblastosis Fetalis)."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Human Sex Determination (XX vs XY) & 50:50 Probability",
                        "content": {
                            "title": "Human Sex Determination (XX vs XY) & 50:50 Probability",
                            "caption": "Meiotic Sex Chromosome Segregation Diagram Demonstrating 50% Female (XX) and 50% Male (XY) Offspring Probability",
                            "description": "Genetic cross diagram showing Female (XX) x Male (XY), producing 50% XX daughters and 50% XY sons."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Human Sex Determination Mechanics",
                        "content": {
                            "title": "Human Sex Determination Mechanics",
                            "text": "Human sex is determined by sex chromosomes:\n• Females: Homomorphic XX (all eggs carry one X chromosome).\n• Males: Heteromorphic XY (50% sperm carry X; 50% sperm carry Y).\n• Result: Fertilisation by X-sperm produces a female (XX); fertilisation by Y-sperm produces a male (XY). The father's sperm determines the sex of the child."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "suggested_diagram",
                        "title": "X-Linked Recessive Sex Linkage: Haemophilia Carrier Inheritance",
                        "content": {
                            "title": "X-Linked Recessive Sex Linkage: Haemophilia Carrier Inheritance",
                            "caption": "Genetic Cross Chart Demonstrating Inheritance of Haemophilia (Xh) from Carrier Mother to Affected Son",
                            "description": "Cross diagram Mother (XH Xh) x Father (XH Y) yielding 25% XH XH (Normal female), 25% XH Xh (Carrier female), 25% XH Y (Normal male), 25% Xh Y (Haemophiliac male)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Sex Linkage & X-Linked Recessive Traits",
                        "content": {
                            "title": "Sex Linkage & X-Linked Recessive Traits",
                            "text": "Sex linkage refers to genes located on the sex chromosomes (usually the X chromosome).\n\n• Haemophilia & Red-Green Colour Blindness: Caused by recessive alleles carried on the X chromosome ($X^h$).\n• Male Susceptibility: Males ($X^h Y$) have only ONE X chromosome. A single recessive allele guarantees expression of the disorder because the Y chromosome carries no corresponding allele. Females ($X^H X^h$) are asymptomatic carriers."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Pedigree Chart Symbols & Inheritance Analysis Model",
                        "content": {
                            "title": "Pedigree Chart Symbols & Inheritance Analysis Model",
                            "caption": "Family Pedigree Tree Demonstrating Symbols (Squares = Males, Circles = Females, Shaded = Affected) Tracing Sex-Linked Haemophilia",
                            "description": "3-generation family tree diagram displaying pedigree symbols used to trace inherited disorders across generations."
                        }
                    },
                    {
                        "type": "worked_example",
                        "title": "Worked Example: ABO Blood Group Paternity Cross",
                        "content": {
                            "question": "A woman of blood group A gives birth to a child of blood group O. She claims a man of blood group AB is the father. Determine whether this claim is genetically possible.",
                            "strategy": "Analyze genotypes: Mother (Group A = IA IA or IA i); Child (Group O = ii); Alleged Father (Group AB = IA IB).",
                            "solution": [
                                "Child Genotype: ii (Must inherit one 'i' allele from mother and one 'i' allele from father).",
                                "Mother Genotype: Must be IA i (Heterozygous Group A).",
                                "Alleged Father Genotype: IA IB (Possesses NO 'i' allele to pass to child).",
                                "Conclusion: The alleged father (Group AB) CANNOT be the biological father because he cannot contribute an 'i' allele."
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Blood Group & Sex Linkage Cross Simulator",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Blood Group & Sex Linkage Cross Simulator",
                            "prompt": "A woman who is a carrier for haemophilia (XH Xh) marries a normal man (XH Y). What is the probability that their sons will have haemophilia?",
                            "options": [
                                "Option A: 50% of sons (1/2 of male children will be Xh Y).",
                                "Option B: 100% of sons.",
                                "Option C: 0% of sons."
                            ],
                            "correct_option": "Option A: 50% of sons (1/2 of male children will be Xh Y).",
                            "explanation": "Sons inherit their Y chromosome from father and either XH or Xh from carrier mother, giving 50% chance of haemophilia among sons."
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Non-Mendelian & Sex Linkage",
                        "content": {
                            "question": "Why are human males significantly more likely to express X-linked recessive conditions like haemophilia than females?",
                            "options": [
                                "Males possess only one X chromosome, so a single recessive allele on the X chromosome is expressed without a dominant allele on Y to mask it.",
                                "Males produce more red blood cells than females.",
                                "The Y chromosome carries two dominant haemophilia genes.",
                                "Females do not possess any X chromosomes."
                            ],
                            "correct_answer": 0,
                            "explanation": "Males are hemizygous (XY), so a single recessive X-linked allele is expressed immediately."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "summary",
                        "title": "Complex Inheritance: Key Takeaways",
                        "content": {
                            "title": "Complex Inheritance: Key Takeaways",
                            "summary_points": [
                                "Incomplete dominance produces intermediate F1 phenotypes; codominance expresses both parental alleles fully.",
                                "Human ABO blood group is controlled by 3 alleles (IA, IB codominant; i recessive).",
                                "Human sex is determined by XX (female) and XY (male); father's sperm determines child sex.",
                                "Sex-linked traits (haemophilia, colour blindness) are carried on X chromosome; males express X-linked recessive traits more frequently."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 5: Mutations, Mutagens, and Inherited Genetic Disorders
        # =====================================================================
        {
            "unit_order": 5,
            "unit_name": "Mutations, Mutagens, and Inherited Genetic Disorders",
            "unit_description": "Mutations, chemical/physical mutagens, chromosomal structural and number changes (Down's, Turner's, Klinefelter's), gene mutations (sickle-cell anaemia), and albinism.",
            "lesson_title": "Mutations, Mutagens, and Inherited Genetic Disorders",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Mutations & Genetic Disorders",
                        "content": {
                            "title": "Learning Objectives: Mutations & Genetic Disorders",
                            "goals": [
                                "Define mutation and distinguish between spontaneous mutations and induced mutagens.",
                                "Analyze four structural chromosomal mutations (deletion, duplication, inversion, translocation).",
                                "Explain chromosomal nondisjunction and clinical features of Down's, Turner's, and Klinefelter's syndromes.",
                                "Detail the point mutation causing Sickle-Cell Anaemia and explain the malaria heterozygote advantage."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Genetic Stability and Spontaneous Change",
                        "content": {
                            "title": "Genetic Stability and Spontaneous Change",
                            "text": "While DNA replication is remarkably precise, sudden permanent alterations in the genetic material do occur. These changes are called mutations, providing the raw material for biological evolution."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "definition_card",
                        "title": "Mutations and Mutagens Taxonomy",
                        "content": {
                            "term": "Mutation & Mutagen Definitions",
                            "definition": "A mutation is a sudden, permanent change in the structure, sequence, or quantity of genetic material (DNA or chromosomes) in an organism.",
                            "key_points": [
                                "Spontaneous Mutations: Occur naturally due to replication errors.",
                                "Mutagens: Environmental agents that increase mutation rates (UV light, X-rays, mustard gas, nitrous acid, asbestos).",
                                "Somatic Mutation: Affects body cells (not inherited; e.g., skin cancer).",
                                "Gene Mutation: Affects gamete-producing cells (passed to offspring)."
                            ]
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Four Types of Chromosomal Structural Mutations",
                        "content": {
                            "title": "Four Types of Chromosomal Structural Mutations",
                            "caption": "Structural Modification Diagrams: Deletion, Duplication, Inversion, and Translocation Chromosome Rearrangements",
                            "description": "Diagram illustrating 1. Deletion (loss of chromosome segment); 2. Duplication (repeating segment); 3. Inversion (180° rotation of segment); 4. Translocation (transfer of segment to non-homologous chromosome)."
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Chromosomal Mutations — Structural Changes",
                        "content": {
                            "title": "Chromosomal Mutations — Structural Changes",
                            "text": "Chromosomal structural mutations alter the arrangement of genes along a chromosome:\n1. Deletion: A piece breaks off and is lost.\n2. Duplication: A chromosome segment is repeated.\n3. Inversion: A chromosome segment breaks, rotates 180°, and reattaches in reverse order.\n4. Translocation: A broken chromosome segment attaches to a non-homologous chromosome."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "concept_explanation",
                        "title": "Chromosomal Number Mutations (Nondisjunction)",
                        "content": {
                            "title": "Chromosomal Number Mutations (Nondisjunction)",
                            "text": "Nondisjunction is the failure of homologous chromosomes (or sister chromatids) to separate during anaphase of meiosis. This produces gametes with extra or missing chromosomes."
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Meiotic Nondisjunction & Karyotype of Down's Syndrome (Trisomy 21)",
                        "content": {
                            "title": "Meiotic Nondisjunction & Karyotype of Down's Syndrome (Trisomy 21)",
                            "caption": "Nondisjunction Mechanism: Meiotic Failure of Chromosome 21 Separation Resulting in 47 Chromosomes (Trisomy 21)",
                            "description": "Flowchart showing nondisjunction of chromosome 21 in egg, fertilisation by normal sperm, resulting in 3 copies of chromosome 21 (47 total chromosomes)."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Trisomy 21 Down's Syndrome Chromosomal Karyotype",
                        "content": {
                            "title": "Trisomy 21 Down's Syndrome Chromosomal Karyotype",
                            "caption": "Human karyotype displaying 3 copies of chromosome 21 (Trisomy 21), characteristic of Down's Syndrome.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/ab/21_trisomy_-_Down_syndrome.png",
                            "author": "Wikimedia Commons",
                            "licensing": "CC BY-SA 3.0",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:21_trisomy_-_Down_syndrome.png"
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "concept_explanation",
                        "title": "Clinical Features of Down's, Turner's, & Klinefelter's Syndromes",
                        "content": {
                            "title": "Clinical Features of Down's, Turner's, & Klinefelter's Syndromes",
                            "text": "• Down's Syndrome (Trisomy 21 - 47 chromosomes): Slanted eyes, flat nasal bridge, short stature, mental retardation, heart defects.\n\n• Turner's Syndrome (Monosomy XO - 45 chromosomes): Female lacking one X chromosome. Short stature, webbed neck, sterile undeveloped ovaries.\n\n• Klinefelter's Syndrome (Trisomy XXY - 47 chromosomes): Male with extra X chromosome. Abnormally tall, enlarged breasts (gynecomastia), sterile underdeveloped testes."
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "concept_explanation",
                        "title": "Gene (Point) Mutations & Sickle-Cell Anaemia",
                        "content": {
                            "title": "Gene (Point) Mutations & Sickle-Cell Anaemia",
                            "text": "A gene mutation is a change in the nucleotide base sequence of a single gene.\n\n• Sickle-Cell Anaemia: A base substitution mutation where Adenine replaces Thymine (CTC -> CAC) in the gene coding for beta-haemoglobin. This substitutes Valine for Glutamic Acid, causing red blood cells to distort into sickle shapes under low oxygen tension, causing vessel blockages and severe anaemia."
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Sickle-Cell Anaemia Gene Mutation & Malaria Heterozygote Advantage",
                        "content": {
                            "title": "Sickle-Cell Anaemia Gene Mutation & Malaria Heterozygote Advantage",
                            "caption": "Balanced Polymorphism Model: Normal (HbA HbA), Sickle Anaemia (HbS HbS), and Heterozygous Carrier (HbA HbS) Malaria Protection",
                            "description": "Diagram illustrating point mutation CTC -> CAC, normal biconcave vs sickled red cells, and malaria parasite destruction in HbA HbS heterozygous carriers."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Microscopic Blood Smear of Sickle Red Blood Cells",
                        "content": {
                            "title": "Microscopic Blood Smear of Sickle Red Blood Cells",
                            "caption": "Scanning electron micrograph of sickled crescent-shaped red blood cells alongside normal biconcave erythrocytes.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Sickle_cell_anemia_smear.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Sickle_cell_anemia_smear.jpg"
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "concept_explanation",
                        "title": "Heterozygote Advantage in Malaria Belts",
                        "content": {
                            "title": "Heterozygote Advantage in Malaria Belts",
                            "text": "Heterozygous individuals ($Hb^A Hb^S$) possess the 'sickle-cell trait'. They do not suffer severe anaemia, and their sickled red blood cells rupture when invaded by *Plasmodium falciparum* malaria parasites, providing natural immunity against lethal malaria in tropical Africa."
                        }
                    },
                    {
                        "type": "callout",
                        "title": "Inherited Disorder: Albinism",
                        "content": {
                            "type": "tip",
                            "title": "Inherited Disorder: Albinism",
                            "text": "Albinism is an autosomal recessive condition ($aa$) caused by a gene mutation preventing tyrosinase enzyme synthesis, resulting in complete lack of melanin pigment in skin, hair, and eyes."
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Mutation Mechanism Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Mutation Mechanism Challenge",
                            "prompt": "Why has the sickle-cell allele (HbS) remained at high frequencies in East Africa despite being lethal in the homozygous state (HbS HbS)?",
                            "options": [
                                "Option A: Heterozygous carriers (HbA HbS) have a natural selective advantage because they are protected against severe Plasmodium falciparum malaria.",
                                "Option B: The sickle-cell allele is dominant and spreads automatically.",
                                "Option C: Sickle-cell anaemia is caused by eating unboiled milk."
                            ],
                            "correct_option": "Option A: Heterozygous carriers (HbA HbS) have a natural selective advantage because they are protected against severe Plasmodium falciparum malaria.",
                            "explanation": "Heterozygotes survive malaria outbreaks, passing the HbS allele to subsequent generations (balanced polymorphism)."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Mutations & Inherited Disorders",
                        "content": {
                            "question": "What is the genetic cause of Down's Syndrome in humans?",
                            "options": [
                                "Nondisjunction during meiosis resulting in an extra copy of chromosome 21 (Trisomy 21, total 47 chromosomes).",
                                "A point mutation in the insulin gene.",
                                "Loss of the Y chromosome in males.",
                                "Exposure to cold drinking water."
                            ],
                            "correct_answer": 0,
                            "explanation": "Down's syndrome is caused by nondisjunction of chromosome 21 resulting in Trisomy 21 (47 chromosomes)."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "summary",
                        "title": "Mutations & Disorders: Key Takeaways",
                        "content": {
                            "title": "Mutations & Disorders: Key Takeaways",
                            "summary_points": [
                                "Mutations are sudden permanent genetic changes, accelerated by mutagens (UV light, X-rays, chemicals).",
                                "Chromosomal structural mutations include Deletion, Duplication, Inversion, and Translocation.",
                                "Meiotic nondisjunction causes number changes: Down's (Trisomy 21), Turner's (XO), and Klinefelter's (XXY).",
                                "Sickle-cell anaemia is a point mutation in beta-haemoglobin; heterozygous carriers ($Hb^A Hb^S$) enjoy malaria resistance."
                            ]
                        }
                    }
                ]
            ]
        },

        # =====================================================================
        # LESSON 6: Applications of Genetics, Worked KCSE Problems, and Topic Assessment
        # =====================================================================
        {
            "unit_order": 6,
            "unit_name": "Applications of Genetics, Worked KCSE Problems, and Topic Assessment",
            "unit_description": "Practical applications (selective breeding, recombinant DNA insulin, gene therapy, genetic counselling), worked KCSE problems, and topic assessment.",
            "lesson_title": "Applications of Genetics, Worked KCSE Problems, and Topic Assessment",
            "pages": [
                # Page 1
                [
                    {
                        "type": "learning_goal",
                        "title": "Learning Objectives: Applied Genetics & KCSE Mastery",
                        "content": {
                            "title": "Learning Objectives: Applied Genetics & KCSE Mastery",
                            "goals": [
                                "Analyze practical applications of genetics in agriculture (selective breeding, hybrid vigor) and medicine.",
                                "Detail recombinant DNA technology in producing human insulin via transgenic bacteria.",
                                "Master KCSE genetics problem-solving for monohybrid crosses, blood groups, and pedigree charts.",
                                "Complete comprehensive end-of-topic revision assessment."
                            ]
                        }
                    },
                    {
                        "type": "concept_explanation",
                        "title": "Biotechnology & Applied Genetics",
                        "content": {
                            "title": "Biotechnology & Applied Genetics",
                            "text": "Understanding genetic principles enables humanity to manipulate DNA to improve crop yields, breed high-yielding livestock, produce lifesaving pharmaceuticals, and counsel families on hereditary risks."
                        }
                    }
                ],
                # Page 2
                [
                    {
                        "type": "concept_explanation",
                        "title": "Applications in Agriculture: Selective Breeding",
                        "content": {
                            "title": "Applications in Agriculture: Selective Breeding",
                            "text": "• Selective Breeding (Artificial Selection): Choosing parents with desirable traits (e.g., high milk yield, drought resistance) to breed over generations.\n• Hybrid Vigor (Heterosis): Crossing two genetically distinct inbred lines produces hybrid offspring (e.g., GH-4 hybrid maize) that out-perform both parents in vigor, growth rate, and disease resistance."
                        }
                    }
                ],
                # Page 3
                [
                    {
                        "type": "concept_explanation",
                        "title": "Applications in Medicine & Genetic Engineering",
                        "content": {
                            "title": "Applications in Medicine & Genetic Engineering",
                            "text": "• Recombinant DNA Technology: Inserting human genes into bacterial plasmids to manufacture human insulin, growth hormone, and vaccines.\n• Gene Therapy: Replacing defective mutant genes with functional normal genes using viral vectors to treat genetic diseases like cystic fibrosis.\n• DNA Fingerprinting: Analyzing variable VNTR DNA bands for forensic crime solving and paternity disputes."
                        }
                    }
                ],
                # Page 4
                [
                    {
                        "type": "suggested_diagram",
                        "title": "Recombinant DNA Technology & Bacterial Insulin Production",
                        "content": {
                            "title": "Recombinant DNA Technology & Bacterial Insulin Production",
                            "caption": "Genetic Engineering Flowchart: Human Insulin Gene Cut with Restriction Enzyme → Plasmid Vector Insertion → Bacterial Transformation → Industrial Fermentation",
                            "description": "Flowchart displaying 1. Isolation of human insulin gene; 2. Cutting bacterial plasmid with restriction endonuclease; 3. Joining with DNA ligase; 4. Insertion into E. coli; 5. Mass production of human insulin."
                        }
                    },
                    {
                        "type": "suggested_image",
                        "title": "Recombinant DNA Vector in Biotechnology Visualization",
                        "content": {
                            "title": "Recombinant DNA Vector in Biotechnology Visualization",
                            "caption": "Diagrammatic representation of a circular bacterial plasmid vector used in recombinant DNA technology.",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/d/da/Making_of_a_DNA_vaccine.jpg",
                            "author": "Public Domain, Wikimedia Commons",
                            "licensing": "Public domain",
                            "commons_page_url": "https://commons.wikimedia.org/wiki/File:Making_of_a_DNA_vaccine.jpg"
                        }
                    }
                ],
                # Page 5
                [
                    {
                        "type": "concept_explanation",
                        "title": "Genetic Counselling & Ethics",
                        "content": {
                            "title": "Genetic Counselling & Ethics",
                            "text": "Genetic counselling involves testing prospective parents and analyzing family pedigree trees to calculate risks of transmitting inherited disorders (sickle-cell, haemophilia) to future children, empowering informed reproductive choices."
                        }
                    }
                ],
                # Page 6
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 1: Monohybrid Cross Ratios",
                        "content": {
                            "question": "A pure breeding black bull was crossed with a pure breeding white cow. All F1 offspring were black. (a) Identify the dominant allele. (b) Calculate the percentage of white offspring in F2 if F1 individuals are interbred. (4 Marks)",
                            "strategy": "Identify complete dominance and standard 3:1 F2 phenotypic ratio.",
                            "solution": [
                                "(a) Dominant Allele: Black coat allele (B). (1 Mark)",
                                "(b) F2 Cross: Bb x Bb\n    Punnett Square: 1 BB : 2 Bb : 1 bb\n    Phenotypic Ratio: 3 Black : 1 White\n    Percentage of White Offspring (bb) = (1 / 4) x 100% = 25%. (3 Marks)"
                            ]
                        }
                    }
                ],
                # Page 7
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 2: Test Cross Mechanics",
                        "content": {
                            "question": "A farmer has a black ram of unknown genotype. Describe how the farmer can determine whether the ram is pure breeding (BB) or heterozygous (Bb). (4 Marks)",
                            "strategy": "Describe test cross procedure: cross with homozygous recessive white ewe (bb).",
                            "solution": [
                                "1. Procedure: Cross the black ram of unknown genotype with a white ewe of homozygous recessive genotype (bb). (1 Mark)",
                                "2. Result 1: If ALL offspring are black, the ram is pure breeding homozygous dominant (BB). (1.5 Marks)",
                                "3. Result 2: If 50% of offspring are black and 50% are white (1:1 ratio), the ram is heterozygous (Bb). (1.5 Marks)"
                            ]
                        }
                    }
                ],
                # Page 8
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 3: ABO Blood Group Paternity",
                        "content": {
                            "question": "A father of blood group B and a mother of blood group A have a child of blood group O. Construct a genetic cross to determine the genotypes of both parents and calculate the probability of them having another child of blood group AB. (5 Marks)",
                            "strategy": "Mother must be IA i; Father must be IB i to produce ii child.",
                            "solution": [
                                "Parental Phenotypes: Group A  x  Group B",
                                "Parental Genotypes:  IA i     x  IB i",
                                "Gametes:            (IA) (i)    (IB) (i)",
                                "Punnett Square:\n        |   IA   |   i    |\n    ----+--------+--------\n     IB | IA IB  |  IB i  |\n    ----+--------+--------\n      i |  IA i  |   ii   |\n",
                                "Offspring Phenotypes: 25% Group AB (IA IB), 25% Group B (IB i), 25% Group A (IA i), 25% Group O (ii).",
                                "Probability of Group AB = 25% (1/4)."
                            ]
                        }
                    }
                ],
                # Page 9
                [
                    {
                        "type": "worked_example",
                        "title": "Worked KCSE Question 4: Haemophilia Sex Linkage",
                        "content": {
                            "question": "Explain why haemophilia is rare in human females compared to males. (4 Marks)",
                            "strategy": "Explain X-linked recessive inheritance, homozygous requirement for females vs hemizygous in males.",
                            "solution": [
                                "1. Haemophilia is caused by a sex-linked recessive allele carried on the X chromosome (Xh). (1 Mark)",
                                "2. Males possess only one X chromosome (XY). A single recessive Xh allele causes haemophilia because there is no corresponding allele on Y to mask it. (1.5 Marks)",
                                "3. Females possess two X chromosomes (XX). A female expresses haemophilia ONLY if she inherits TWO recessive alleles (Xh Xh), requiring a haemophiliac father and carrier/haemophiliac mother. (1.5 Marks)"
                            ]
                        }
                    }
                ],
                # Page 10
                [
                    {
                        "type": "common_mistake",
                        "title": "Common Student Traps in Genetics Exams",
                        "content": {
                            "mistake": "Failing to put circles around gametes or confusing 'genotype' with 'phenotype'.",
                            "correction": "Always draw circles around gametes in genetic cross diagrams. Genotype is the letter combination (e.g., Tt); Phenotype is the physical appearance (e.g., Tall).",
                            "reasoning": "KCSE examiners award specific marks for gamete circles and correct ratio labeling."
                        }
                    }
                ],
                # Page 11
                [
                    {
                        "type": "mini_activity",
                        "title": "Interactive Applied Genetics & Pedigree Challenge",
                        "content": {
                            "activity_type": "scenario_decision",
                            "title": "Interactive Applied Genetics & Pedigree Challenge",
                            "prompt": "How does bacterial production of human insulin via recombinant DNA technology benefit diabetic patients over traditional pig insulin extraction?",
                            "options": [
                                "Option A: Produces exact human insulin in high volumes without allergic immune rejection associated with animal insulin.",
                                "Option B: Bacteria convert insulin into sugar.",
                                "Option C: Pig insulin is identical to human DNA."
                            ],
                            "correct_option": "Option A: Produces exact human insulin in high volumes without allergic immune rejection associated with animal insulin.",
                            "explanation": "Transgenic E. coli bacteria synthesize pure human insulin, avoiding immune side effects caused by animal pancreas extracts."
                        }
                    }
                ],
                # Page 12
                [
                    {
                        "type": "knowledge_check",
                        "title": "Knowledge Checkpoint: Applied Genetics & Review",
                        "content": {
                            "question": "What is the term for the superior performance, growth rate, and yield of hybrid offspring over both inbred parents?",
                            "options": [
                                "Hybrid Vigor (Heterosis)",
                                "Incomplete Dominance",
                                "Nondisjunction",
                                "Genetic Drift"
                            ],
                            "correct_answer": 0,
                            "explanation": "Hybrid vigor (heterosis) refers to the enhanced performance of cross-bred hybrid organisms."
                        }
                    }
                ],
                # Page 13
                [
                    {
                        "type": "summary",
                        "title": "Topic 1 Mastery Synthesis & Complete Review",
                        "content": {
                            "title": "Topic 1 Mastery Synthesis & Complete Review",
                            "summary_points": [
                                "Genetics studies heredity and variation (continuous bell curve vs discontinuous discrete bar graph).",
                                "DNA is a double helix (A=T, C≡G) that directs protein synthesis via Transcription and Translation.",
                                "Mendel's First Law governs monohybrid crosses (F2 3:1 phenotypic, 1:2:1 genotypic; test cross 1:1 ratio).",
                                "Complex inheritance includes codominance, ABO multiple alleles, Rh factor, XX/XY sex determination, and X-linked haemophilia.",
                                "Mutations (structural/number nondisjunction Down's/Turner's/Klinefelter's and point sickle-cell) provide evolutionary variation.",
                                "Applications include selective breeding, recombinant DNA insulin, gene therapy, and genetic counselling."
                            ]
                        }
                    }
                ]
            ]
        }
    ]

def ingest_form4_biology_topic1(replace=False):
    print("=" * 80)
    print("VLearn Form 4 Biology — Topic 1: Genetics")
    print("High-Structure Production Ingestion Engine")
    print("=" * 80)

    curriculum = Curriculum.objects.filter(name="844").first()
    if not curriculum:
        print("[!] Error: Curriculum '844' not found.")
        return

    grade = Grade.objects.filter(curriculum=curriculum, name="Form 4").first()
    if not grade:
        print("[!] Error: Grade 'Form 4' not found.")
        return

    subject = Subject.objects.filter(grade=grade, name="Biology").first()
    if not subject:
        print("[!] Error: Subject 'Biology' not found under Form 4.")
        return

    print(f"[*] Resolved Target: {curriculum.name} -> {grade.name} -> {subject.name} (ID: {subject.id})")

    topic_name = "Genetics"
    topic = Topic.objects.filter(subject=subject, name=topic_name).first()

    if topic and replace:
        print(f"[*] Found existing Topic '{topic_name}' (ID: {topic.id}). Removing for clean replace...")
        topic.delete()
        topic = None

    if not topic:
        topic = Topic.objects.create(
            subject=subject,
            name=topic_name,
            order=1,
            description="Comprehensive syllabus on genetics, variation, DNA/RNA molecular biology, Mendelian monohybrid crosses, non-Mendelian inheritance, blood groups, sex linkage, mutations, and biotechnology."
        )
        print(f"[+] Created Topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"[*] Using existing Topic: {topic.name} (ID: {topic.id})")

    curriculum_data = build_topic1_curriculum()
    total_lessons = 0
    total_pages = 0
    total_blocks = 0

    with transaction.atomic():
        for unit_data in curriculum_data:
            unit_order = unit_data["unit_order"]
            unit_name = unit_data["unit_name"]
            unit_desc = unit_data["unit_description"]
            lesson_title = unit_data["lesson_title"]
            pages_data = unit_data["pages"]

            learning_unit, _ = LearningUnit.objects.get_or_create(
                topic=topic,
                order=unit_order,
                defaults={"name": unit_name, "description": unit_desc}
            )

            lesson = Lesson.objects.filter(topic=topic, learning_unit=learning_unit).first()
            if lesson:
                lesson.blocks.all().delete()
            else:
                lesson = Lesson.objects.create(
                    topic=topic,
                    learning_unit=learning_unit,
                    title=lesson_title,
                    status="published",
                    version=1
                )
            print(f"  [+] Ingesting Lesson {unit_order}: {lesson.title} (ID: {lesson.id})")

            block_order = 10
            lesson_page_count = len(pages_data)

            for page_idx, page_blocks in enumerate(pages_data, 1):
                first_block_title = page_blocks[0].get("title", f"Page {page_idx}")
                for b_data in page_blocks:
                    b_type = b_data["type"]
                    b_title = b_data.get("title", first_block_title)
                    b_content = clean_dict(b_data.get("content", {}))

                    LessonBlock.objects.create(
                        lesson=lesson,
                        page_number=page_idx,
                        page_title=first_block_title,
                        title=b_title,
                        block_type=b_type,
                        component_type=b_type,
                        component_order=block_order,
                        order=block_order,
                        content=b_content,
                        metadata={}
                    )
                    block_order += 10
                    total_blocks += 1

            total_lessons += 1
            total_pages += lesson_page_count
            print(f"      [OK] Ingested {lesson_page_count} Pages for Lesson {unit_order}.")

    print("=" * 80)
    print("[SUCCESS] Form 4 Biology Topic 1 (Genetics) Ingestion Complete!")
    print(f"[*] Total Lessons Ingested: {total_lessons}")
    print(f"[*] Total Pages Ingested:   {total_pages}")
    print(f"[*] Total Blocks Ingested:  {total_blocks}")
    print("=" * 80)

if __name__ == "__main__":
    replace_flag = "--replace" in sys.argv
    ingest_form4_biology_topic1(replace=replace_flag)
