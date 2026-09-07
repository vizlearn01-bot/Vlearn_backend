from django.core.management.base import BaseCommand
from django.db import connection, transaction
from curriculum.models import Simulation, SubjectDomain, SimulationStatus


class Command(BaseCommand):
    help = "Seeds the initial 7 registered interactive simulations across Chemistry and Physics."

    def handle(self, *args, **options):
        self.stdout.write("Hydrating Simulation Registry data...")

        # Ensure table exists if migration wasn't run via CLI
        with connection.schema_editor() as editor:
            tables = connection.introspection.table_names()
            if Simulation._meta.db_table not in tables:
                self.stdout.write(f"Creating table {Simulation._meta.db_table}...")
                editor.create_model(Simulation)

        simulations_data = [
            # Chemistry Active
            {
                "key": "charles_law",
                "title": "Charles's Law",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Gas Laws",
                "status": SimulationStatus.ACTIVE,
                "description": "Interactive gas law simulation demonstrating volume-temperature proportionality at constant pressure.",
                "archetype": "charles_law",
                "config": {
                    "initial_temperature_k": 273,
                    "min_temperature_k": 173,
                    "max_temperature_k": 373,
                    "particle_count": 20,
                    "formula": "V1 / T1 = V2 / T2",
                    "telemetry_events": ["TEMPERATURE_CHANGED", "VOLUME_CALCULATED"],
                    "context_spec": {
                        "overview": "Explores the direct relationship between absolute temperature (Kelvin) and volume of a gas at constant pressure.",
                        "how_to_use": [
                            "Step 1: Adjust the Temperature slider from 173 K to 373 K.",
                            "Step 2: Observe how particle velocity increases with higher temperature.",
                            "Step 3: Watch the container boundary expand or contract to maintain constant pressure."
                        ],
                        "expected_results": [
                            {
                                "action": "Increasing Temperature",
                                "expected_outcome": "Volume expands linearly (V ∝ T).",
                                "key_takeaway": "Direct proportional relationship at constant pressure (V1/T1 = V2/T2)."
                            },
                            {
                                "action": "Decreasing Temperature",
                                "expected_outcome": "Particle kinetic motion slows and volume contracts.",
                                "key_takeaway": "Gas volume approaches zero theoretical limit as temperature approaches Absolute Zero (0 K)."
                            }
                        ]
                    }
                },
            },
            {
                "key": "reaction_rate",
                "title": "Reaction Rate",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Reaction Rates and Reversible Reactions",
                "status": SimulationStatus.ACTIVE,
                "description": "Investigate collision theory and how concentration, temperature, and catalysts affect reaction speed.",
                "archetype": "reaction_rate",
                "config": {
                    "initial_concentration_m": 1.0,
                    "initial_temperature_c": 25,
                    "has_catalyst": False,
                    "telemetry_events": ["REACTION_STARTED", "REACTION_COMPLETED", "CATALYST_TOGGLED"],
                    "context_spec": {
                        "overview": "Demonstrates Collision Theory by showing how temperature and kinetic energy influence reaction rates and precipitate formation.",
                        "how_to_use": [
                            "Step 1: Set the initial temperature slider (10°C to 60°C).",
                            "Step 2: Click 'Start Reaction' to begin timer and collision monitoring.",
                            "Step 3: Observe the solution opacity and time required to form full sulfur precipitate."
                        ],
                        "expected_results": [
                            {
                                "action": "Increasing Temperature",
                                "expected_outcome": "Reaction time decreases rapidly, doubling speed for every ~10°C increase.",
                                "key_takeaway": "Higher kinetic energy leads to more frequent and successful particle collisions exceeding activation energy."
                            }
                        ]
                    }
                },
            },
            {
                "key": "electrolysis",
                "title": "Electrolysis",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Electrochemistry",
                "status": SimulationStatus.ACTIVE,
                "description": "Simulate ionic migration, cathode/anode reactions, and gas production during aqueous electrolysis.",
                "archetype": "electrolysis",
                "config": {
                    "electrolyte": "CuSO4",
                    "voltage_volts": 6.0,
                    "anode_type": "Copper",
                    "cathode_type": "Copper",
                    "telemetry_events": ["POWER_TOGGLED", "ION_DEPOSITION_UPDATED"],
                    "context_spec": {
                        "overview": "Demonstrates quantitative electrochemistry, showing how electrical current drives non-spontaneous redox reactions at the electrodes.",
                        "how_to_use": [
                            "Step 1: Adjust circuit voltage (2 V to 12 V).",
                            "Step 2: Click 'Start Electrolysis' to energize the copper sulfate cell.",
                            "Step 3: Track real-time mass changes on the copper anode and cathode."
                        ],
                        "expected_results": [
                            {
                                "action": "Increasing Voltage / Current",
                                "expected_outcome": "Mass changes at anode and cathode accelerate proportionally.",
                                "key_takeaway": "Mass of element deposited or dissolved is directly proportional to total electrical charge transferred (Q = I × t)."
                            },
                            {
                                "action": "Anode vs Cathode Reaction",
                                "expected_outcome": "Copper dissolves at anode (Cu → Cu²⁺ + 2e⁻) and deposits at cathode (Cu²⁺ + 2e⁻ → Cu).",
                                "key_takeaway": "Total mass of copper in system remains conserved."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_electrode_potential_explorer",
                "title": "Standard Electrode Potential Explorer",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Electrochemistry",
                "status": SimulationStatus.ACTIVE,
                "description": "Compare different metals against the Standard Hydrogen Electrode to understand why some metals lose electrons more easily.",
                "archetype": "electrode_potential_explorer",
                "config": {
                    "context_spec": {
                        "overview": "Standard electrode potentials predict the direction of electron flow. Electrons always flow from the half-cell with the lower reduction potential toward the half-cell with the higher reduction potential.",
                        "how_to_use": [
                            "Step 1: Select a metal from the dropdown.",
                            "Step 2: Predict which way electrons will flow.",
                            "Step 3: Observe the voltmeter reading and electron flow direction.",
                            "Step 4: Explore both positive and negative potentials."
                        ],
                        "expected_results": [
                            {
                                "action": "Positive E° (e.g. Copper +0.34V)",
                                "expected_outcome": "Electrons flow from Hydrogen to the Metal.",
                                "key_takeaway": "Higher reduction potential means greater tendency to gain electrons (stronger oxidizing agent)."
                            },
                            {
                                "action": "Negative E° (e.g. Magnesium -2.37V)",
                                "expected_outcome": "Electrons flow from the Metal to Hydrogen.",
                                "key_takeaway": "Lower reduction potential means greater tendency to lose electrons (stronger reducing agent)."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_preferential_discharge",
                "title": "Preferential Discharge of Ions",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Electrochemistry",
                "status": SimulationStatus.ACTIVE,
                "description": "Watch ions compete at the electrodes and discover why concentration, electrochemical position, and electrode material determine the winner.",
                "archetype": "preferential_discharge",
                "config": {
                    "context_spec": {
                        "overview": "When several ions are present, the ion discharged depends on its position in the electrochemical series, concentration, and the electrode involved.",
                        "how_to_use": [
                            "Step 1: Choose an electrolyte.",
                            "Step 2: Start Electrolysis.",
                            "Step 3: Watch the ions compete at the electrodes.",
                            "Step 4: Read the observation panel to understand why the winning ion was chosen."
                        ],
                        "expected_results": [
                            {
                                "action": "Dilute vs Concentrated NaCl",
                                "expected_outcome": "Dilute favors OH⁻, Concentrated favors Cl⁻ at the anode.",
                                "key_takeaway": "High concentration can override position in the electrochemical series."
                            },
                            {
                                "action": "Inert vs Active Copper Electrode",
                                "expected_outcome": "Active copper dissolves instead of discharging an anion.",
                                "key_takeaway": "The nature of the electrode itself can participate in the reaction."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_electroplating",
                "title": "Electroplating & Faraday's Laws",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Electrochemistry",
                "status": SimulationStatus.ACTIVE,
                "description": "A deterministic simulation demonstrating electroplating as the practical application of electrolysis while proving Faraday's Laws.",
                "archetype": "chem_electroplating",
                "config": {
                    "context_spec": {
                        "overview": "How does electric current deposit metal onto an object? Watch the simultaneous movement of ions and mass transfer to see electroplating in action and prove Faraday's First Law mathematically.",
                        "how_to_use": [
                            "Step 1: Choose an object to plate.",
                            "Step 2: Choose a coating metal.",
                            "Step 3: Adjust the current (Amperage).",
                            "Step 4: Start plating and observe mass transfer."
                        ],
                        "expected_results": [
                            {
                                "action": "Increasing Current",
                                "expected_outcome": "Faster metal deposition and anode depletion.",
                                "key_takeaway": "Mass deposited is directly proportional to current (Faraday's First Law)."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_acid_base_dissociation",
                "title": "Acid-Base Strength & Ionization Dynamics",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Acids, Bases and Salts",
                "status": SimulationStatus.ACTIVE,
                "description": "Explore how acid strength (ionization constant Ka) and concentration dictate free H3O+ ion counts, pH, and electrical conductivity.",
                "archetype": "acid_base_dissociation",
                "config": {
                    "initial_acid_type": "weak_acid",
                    "initial_concentration": 0.1,
                    "min_concentration": 0.001,
                    "max_concentration": 1.0,
                    "step": 0.005,
                    "weak_acid_ka": 0.000018,
                    "context_spec": {
                        "overview": "Explore how acid strength (ionization constant Ka) and concentration dictate free [H3O+] ion counts, pH, and electrical conductivity.",
                        "how_to_use": [
                            "Step 1: Toggle between Strong Acid (HA → 100% ionized) and Weak Acid (HA ⇌ partial).",
                            "Step 2: Drag the Concentration slider from 0.001 M to 1.0 M.",
                            "Step 3: Select measurement probes: Digital pH Meter, Conductivity Light Bulb, or Particle View."
                        ],
                        "expected_results": [
                            {
                                "action": "Comparing 0.1 M Strong vs 0.1 M Weak Acid",
                                "expected_outcome": "Strong acid yields pH 1.0 & bright bulb; Weak acid yields pH 2.87 & dim bulb.",
                                "key_takeaway": "Strong acids ionize completely; weak acids ionize partially."
                            },
                            {
                                "action": "Diluting Strong Acid to 0.001 M",
                                "expected_outcome": "pH rises to 3.0, matching the pH of a higher-concentration weak acid.",
                                "key_takeaway": "pH measures free H3O+ concentration, not total added acid."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_salts_solubility_precipitation",
                "title": "Salt Solubility & Precipitation Equilibrium",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Acids, Bases and Salts",
                "status": SimulationStatus.ACTIVE,
                "description": "See the difference between a soluble salt (NaCl) that disappears into solution and an insoluble salt (AgCl) that forms a solid precipitate at the bottom of the beaker.",
                "archetype": "salt_solubility_precipitation",
                "config": {
                    "salts": {
                        "nacl": {
                            "name": "Table Salt (NaCl)",
                            "max_solubility_g_per_100ml": 36.0,
                            "label": "Soluble"
                        },
                        "agcl": {
                            "name": "Silver Chloride (AgCl)",
                            "max_solubility_g_per_100ml": 0.0002,
                            "label": "Insoluble"
                        }
                    },
                    "max_mass_g": 10,
                    "context_spec": {
                        "overview": "Explore the concept of solubility by comparing a highly soluble salt (NaCl) that dissolves completely into ions versus a practically insoluble salt (AgCl) that forms a solid white precipitate at the bottom of the solution vessel.",
                        "how_to_use": [
                            "Step 1: Select a salt type — Table Salt (NaCl - Soluble) or Silver Chloride (AgCl - Insoluble).",
                            "Step 2: Click 'Add Spoonful (+1 g)' or drag the salt amount slider to add mass.",
                            "Step 3: Observe whether the beaker stays clear (dissolved) or forms a solid pile at the bottom (precipitate).",
                            "Step 4: Try adjusting the temperature slider to see how heating affects solubility."
                        ],
                        "expected_results": [
                            {
                                "action": "Adding NaCl to water",
                                "expected_outcome": "Salt dissolves completely. Water stays clear with free Na+ and Cl- ions.",
                                "key_takeaway": "NaCl is highly soluble (36 g per 100 mL). Adding small amounts produces no precipitate."
                            },
                            {
                                "action": "Adding AgCl to water",
                                "expected_outcome": "Salt immediately forms a white solid precipitate at the bottom. Virtually none dissolves.",
                                "key_takeaway": "AgCl is practically insoluble (0.0002 g per 100 mL). The dissolved amount is negligible."
                            },
                            {
                                "action": "Increasing temperature with NaCl",
                                "expected_outcome": "Slightly more NaCl dissolves as temperature increases.",
                                "key_takeaway": "For most ionic solids, solubility increases with temperature (endothermic dissolution)."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_hess_law_pathways",
                "title": "Hess's Law & Reaction Pathways",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Energy Changes in Chemical and Physical Processes",
                "status": SimulationStatus.ACTIVE,
                "description": "Visually discover Hess's Law by comparing a direct reaction with a two-step reaction pathway.",
                "archetype": "hess_law_pathways",
                "config": {
                    "context_spec": {
                        "overview": "Different reaction pathways can have different intermediate energy changes, but the total enthalpy change is always the same.",
                        "how_to_use": [
                            "Step 1: Click 'Route 1' and 'Run Simulation' to observe the direct energy and temperature change.",
                            "Step 2: Reset the simulation.",
                            "Step 3: Click 'Route 2' and 'Run Simulation' to observe the two-step pathway.",
                            "Step 4: Compare the final total energy and final temperature."
                        ],
                        "expected_results": [
                            {
                                "action": "Running both reaction pathways",
                                "expected_outcome": "Both pathways result in exactly the same total enthalpy change (-100 kJ/mol) and final temperature (44.0°C).",
                                "key_takeaway": "The total enthalpy change of a reaction is independent of the pathway taken."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_heat_of_solution_pack",
                "title": "Heat of Solution (Hot Pack vs Cold Pack)",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Energy Changes in Chemical and Physical Processes",
                "status": SimulationStatus.ACTIVE,
                "description": "Compare an exothermic dissolution (Hot Pack) with an endothermic dissolution (Cold Pack) to visualize energy flow.",
                "archetype": "heat_of_solution_pack",
                "config": {
                    "context_spec": {
                        "overview": "When dissolving a substance, energy is used to separate ions (Lattice Energy) and energy is released when water surrounds those ions (Hydration Energy).",
                        "how_to_use": [
                            "Step 1: Click 'Hot Pack' and 'Dissolve Salt' to observe an exothermic reaction.",
                            "Step 2: Note the energy flow direction and temperature change.",
                            "Step 3: Reset the simulation.",
                            "Step 4: Click 'Cold Pack' and 'Dissolve Salt' to observe an endothermic reaction."
                        ],
                        "expected_results": [
                            {
                                "action": "Hot Pack (Exothermic)",
                                "expected_outcome": "Temperature increases. Energy flows out. Hydration Energy > Lattice Energy.",
                                "key_takeaway": "More energy was released than absorbed."
                            },
                            {
                                "action": "Cold Pack (Endothermic)",
                                "expected_outcome": "Temperature decreases. Energy flows in. Lattice Energy > Hydration Energy.",
                                "key_takeaway": "More energy was absorbed than released."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_collision_theory_kinetics",
                "title": "Collision Theory & Activation Energy",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Reaction Rates and Reversible Reactions",
                "status": SimulationStatus.ACTIVE,
                "description": "Adjust collision conditions and discover what is required for a successful chemical reaction.",
                "archetype": "collision_theory_kinetics",
                "config": {
                    "activation_energy": 50,
                    "context_spec": {
                        "overview": "Chemical reactions only occur when particles collide with enough energy and in the correct orientation.",
                        "how_to_use": [
                            "Step 1: Adjust the launch speed.",
                            "Step 2: Choose a collision orientation.",
                            "Step 3: Run the collision.",
                            "Step 4: Observe the outcome.",
                            "Step 5: Discover why reactions succeed or fail."
                        ],
                        "expected_results": [
                            {
                                "action": "Low Energy Collision",
                                "expected_outcome": "Particles bounce apart.",
                                "key_takeaway": "Low energy prevents reactions."
                            },
                            {
                                "action": "High Energy, Wrong Orientation",
                                "expected_outcome": "Particles glance off each other.",
                                "key_takeaway": "Wrong orientation prevents reactions."
                            },
                            {
                                "action": "High Energy, Correct Orientation",
                                "expected_outcome": "Successful reaction! New bonds formed.",
                                "key_takeaway": "Both conditions together produce a successful reaction."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_haber_process_optimizer",
                "title": "Industrial Optimization: The Haber Process",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Reaction Rates and Reversible Reactions",
                "status": SimulationStatus.ACTIVE,
                "description": "Adjust the reactor conditions and discover why industry chooses compromise conditions instead of maximizing a single variable.",
                "archetype": "chem_haber_process_optimizer",
                "config": {
                    "context_spec": {
                        "overview": "The Haber Process produces ammonia by balancing reaction rate and equilibrium yield. Industry chooses operating conditions that provide a practical compromise rather than maximizing a single factor.",
                        "how_to_use": [
                            "Step 1: Adjust temperature.",
                            "Step 2: Adjust pressure.",
                            "Step 3: Observe reaction speed.",
                            "Step 4: Observe ammonia yield.",
                            "Step 5: Discover the compromise used in industry."
                        ],
                        "expected_results": [
                            {
                                "action": "Increasing Temperature",
                                "expected_outcome": "Increases reaction speed but reduces equilibrium yield.",
                                "key_takeaway": "Industry must compromise to get product fast enough."
                            },
                            {
                                "action": "Increasing Pressure",
                                "expected_outcome": "Favours ammonia formation.",
                                "key_takeaway": "Higher pressure increases yield but has practical limits."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_voltaic_cell_flow",
                "title": "Voltaic Cell & Salt Bridge",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Electrochemistry",
                "status": SimulationStatus.ACTIVE,
                "description": "Observe the complete operation of a Daniel Cell including electron flow, oxidation, reduction, and salt bridge function.",
                "archetype": "chem_voltaic_cell_flow",
                "config": {
                    "context_spec": {
                        "overview": "How does a voltaic cell produce electricity? Watch the simultaneous movement of electrons and ions to see chemistry in action.",
                        "how_to_use": [
                            "Step 1: Start the cell.",
                            "Step 2: Observe electron flow.",
                            "Step 3: Observe oxidation and reduction at the electrodes.",
                            "Step 4: Observe ion movement in the salt bridge."
                        ],
                        "expected_results": [
                            {
                                "action": "Starting the cell",
                                "expected_outcome": "Electrons flow from anode to cathode.",
                                "key_takeaway": "Zinc releases electrons more readily than Copper."
                            },
                            {
                                "action": "Continuous operation",
                                "expected_outcome": "Ions flow through the salt bridge.",
                                "key_takeaway": "The salt bridge maintains electrical neutrality, allowing the current to continue flowing."
                            }
                        ]
                    }
                },
            },
            {
                "key": "chem_activity_series_displacement",
                "title": "Metal Reactivity & Activity Series",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Metals",
                "status": SimulationStatus.ACTIVE,
                "description": "A lightweight React simulation demonstrating how the activity (reactivity) series determines whether a displacement reaction occurs.",
                "archetype": "chem_activity_series_displacement",
                "config": {
                    "context_spec": {
                        "overview": "Visually determine whether a metal will replace another metal dissolved in solution based on their positions in the activity series.",
                        "how_to_use": [
                            "Step 1: Select a metal strip.",
                            "Step 2: Select a metal salt solution.",
                            "Step 3: Check their relative reactivity in the Activity Series panel.",
                            "Step 4: Run the experiment and observe if a displacement reaction occurs."
                        ],
                        "expected_results": [
                            {
                                "action": "More reactive metal in less reactive solution (e.g. Zinc in Copper Sulfate)",
                                "expected_outcome": "The metal strip is coated and the solution color fades. A reaction occurs.",
                                "key_takeaway": "More reactive metals displace less reactive metals from their solutions."
                            },
                            {
                                "action": "Less reactive metal in more reactive solution (e.g. Copper in Zinc Sulfate)",
                                "expected_outcome": "No change occurs.",
                                "key_takeaway": "Less reactive metals cannot displace more reactive ones."
                            }
                        ]
                    }
                }
            },
            {
                "key": "chem_soap_micelle_action",
                "title": "Soap Micelle Formation",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Organic Chemistry II",
                "status": SimulationStatus.ACTIVE,
                "description": "Help soap remove grease by forming micelles. Observe how soap molecules reorganize around oil in soft water vs reacting with Ca2+ in hard water.",
                "archetype": "chem_soap_micelle_action",
                "config": {
                    "initial_soap_amount": 2,
                    "initial_water_type": "soft",
                    "context_spec": {
                        "overview": "Explore micelle formation during soap cleaning action and discover how hard water Ca2+ ions cause scum precipitation.",
                        "how_to_use": [
                            "Step 1: Select Soap Amount (Low, Medium, High).",
                            "Step 2: Choose Water Type (Soft Water vs Hard Water).",
                            "Step 3: Click 'Run Simulation' to observe molecular reorganization.",
                            "Step 4: Analyze cleaning efficiency and scum formation in the observation panel."
                        ],
                        "expected_results": [
                            {
                                "action": "Running in Soft Water",
                                "expected_outcome": "Soap tails embed in grease while heads face water, forming micelles that lift oil away (85-98% cleaning efficiency).",
                                "key_takeaway": "Hydrophobic tails attract grease; hydrophilic heads attract water."
                            },
                            {
                                "action": "Running in Hard Water",
                                "expected_outcome": "Ca²⁺ ions react with carboxylate heads, forming grey scum flakes (RCOO)₂Ca↓ and leaving grease trapped.",
                                "key_takeaway": "Hard water ions consume soap by precipitation."
                            }
                        ]
                    }
                }
            },
            {
                "key": "chem_functional_group_tests",
                "title": "Functional Groups & Chemical Tests",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Organic Chemistry II",
                "status": SimulationStatus.ACTIVE,
                "description": "Identify unknown organic compounds using chemical tests. Observe reactions and determine whether alcohols or carboxylic acids are present.",
                "archetype": "chem_functional_group_tests",
                "config": {
                    "context_spec": {
                        "overview": "Identify the unknown compound using chemical tests. Observe each reaction and determine which functional group is present.",
                        "how_to_use": [
                            "Step 1: Select an Unknown Sample (Ethanol, Ethanoic Acid, Propanol, or Butanoic Acid).",
                            "Step 2: Choose a Chemical Test (Sodium Metal Test, Sodium Hydrogen Carbonate Test, or Ceric Ammonium Nitrate Test).",
                            "Step 3: Click 'Run Test' to observe the reaction and identify the functional group."
                        ],
                        "expected_results": [
                            {
                                "action": "Alcohols + CAN Test",
                                "expected_outcome": "Solution turns from pale yellow to deep Red/Amber alkoxycerium complex.",
                                "key_takeaway": "Ceric Ammonium Nitrate specifically identifies alcoholic hydroxyl (-OH) groups."
                            },
                            {
                                "action": "Carboxylic Acids + NaHCO₃ Test",
                                "expected_outcome": "Rapid CO₂ effervescence and vigorous gas evolution.",
                                "key_takeaway": "Carboxylic acids liberate CO₂ gas from sodium bicarbonate due to higher acidity."
                            }
                        ]
                    }
                }
            },
            {
                "key": "chem_radioactive_decay_half_life",
                "title": "Radioactive Decay & Half-Life",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Radioactivity",
                "status": SimulationStatus.ACTIVE,
                "description": "Observe radioactive sample decay kinetics over time and discover why population half-life is predictable while individual atom decay is random.",
                "archetype": "chem_radioactive_decay_half_life",
                "config": {
                    "context_spec": {
                        "overview": "Observe a radioactive sample over time. Can you discover why scientists can predict the decay of a population but never the decay of one individual atom?",
                        "how_to_use": [
                            "Step 1: Select Initial Sample Size (50 to 1000 atoms).",
                            "Step 2: Click 'Run Simulation' to watch random atom decay and the live population graph.",
                            "Step 3: Note the half-life milestone pause when 50% of the sample remains."
                        ],
                        "expected_results": [
                            {
                                "action": "Sample Decay Run",
                                "expected_outcome": "Population follows a predictable exponential decay curve while individual atom decay occurs randomly.",
                                "key_takeaway": "Half-life measures when 50% of the population remains, not when a specific atom decays."
                            }
                        ]
                    }
                }
            },
            {
                "key": "chem_nuclear_fission_chain_reaction",
                "title": "Nuclear Fission & Chain Reactions",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Radioactivity",
                "status": SimulationStatus.ACTIVE,
                "description": "Trigger nuclear fission in U-235 nuclei and adjust control rod positions to regulate neutron absorption and prevent thermal runaway.",
                "archetype": "chem_nuclear_fission_chain_reaction",
                "config": {
                    "context_spec": {
                        "overview": "Trigger a nuclear chain reaction. Can you produce energy safely, or will the reaction become uncontrollable?",
                        "how_to_use": [
                            "Step 1: Choose Fuel Density (Low, Medium, High).",
                            "Step 2: Set Control Rod Position (Fully Inserted, Half Inserted, Fully Removed).",
                            "Step 3: Click 'Fire Initial Neutron' to initiate fission and observe neutron multiplication."
                        ],
                        "expected_results": [
                            {
                                "action": "Control Rods Fully Removed + High Density",
                                "expected_outcome": "Uncontrolled chain reaction with rapid neutron multiplication and thermal runaway warning.",
                                "key_takeaway": "Control rods absorb neutrons to prevent uncontrolled exponential fission."
                            },
                            {
                                "action": "Control Rods Half Inserted",
                                "expected_outcome": "Controlled critical fission with steady energy output.",
                                "key_takeaway": "Steady state fission balances neutron generation and absorption."
                            }
                        ]
                    }
                }
            },
            {
                "key": "chem_titration_volumetric_analysis",
                "title": "Titration Lab — Volumetric Analysis",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "The Mole: Formulae and Chemical Equations",
                "status": SimulationStatus.ACTIVE,
                "description": "Virtual volumetric analysis lab simulating direct acid-base, back titration, and redox titrations with real-time burette dropwise manipulation, stoichiometry, and equivalence detection.",
                "archetype": "chem_titration_volumetric_analysis",
                "config": {
                    "modes": ["direct", "back", "redox"],
                    "telemetry_events": ["SIMULATION_CHECKPOINT_VERIFIED", "TITRE_RECORDED"],
                    "context_spec": {
                        "overview": "Master quantitative volumetric analysis including direct strong acid-strong base neutralisation, back titration of insoluble carbonates, and self-indicating redox titrations with potassium manganate(VII).",
                        "how_to_use": [
                            "Step 1: Select Titration Mode (Direct, Back Titration, or Redox).",
                            "Step 2: Read the initial analyte label and standard titrant specifications.",
                            "Step 3: Manipulate the burette stopcock using +0.1 cm³, +1.0 cm³, or Fast Add to deliver titrant drop-wise into the conical flask.",
                            "Step 4: Watch for the exact end point colour change (e.g., pink to colourless for direct, colourless to faint pink for back/redox).",
                            "Step 5: Record concordant titre readings and test your understanding with the Predict and Challenge tabs."
                        ],
                        "expected_results": [
                            {
                                "action": "Direct Titration (NaOH + HCl)",
                                "expected_outcome": "Solution turns from pink to permanently colourless at exactly 25.0 cm³.",
                                "key_takeaway": "At equivalence point, moles of H⁺ from HCl equal moles of OH⁻ from NaOH (1:1 stoichiometry)."
                            },
                            {
                                "action": "Back Titration (MCO₃ + excess HCl + NaOH)",
                                "expected_outcome": "Solution turns from colourless to permanently faint pink at exactly 5.0 cm³.",
                                "key_takeaway": "Moles of acid reacted with carbonate = Total initial moles HCl − Moles NaOH used to neutralise residual acid."
                            },
                            {
                                "action": "Redox Titration (Fe²⁺ + KMnO₄)",
                                "expected_outcome": "Each drop decolourises until one drop gives a persistent faint pink/violet tinge at 22.5 cm³.",
                                "key_takeaway": "KMnO₄ is self-indicating; 1 mol of MnO₄⁻ oxidises 5 mol of Fe²⁺ in acidic conditions."
                            }
                        ]
                    }
                }
            },

            # Chemistry Placeholder
            {
                "key": "chemical_equilibrium",
                "title": "Chemical Equilibrium",
                "subject": SubjectDomain.CHEMISTRY,
                "topic": "Reaction Rates and Reversible Reactions",
                "status": SimulationStatus.PLACEHOLDER,
                "description": "Explore dynamic equilibrium shifts and Le Chatelier's principle under concentration and thermal pressure changes.",
                "archetype": "chemical_equilibrium",
                "config": {
                    "planned_features": ["Le Chatelier Shift Slider", "Equilibrium Constant Calculation", "Reaction Quotient Q vs K"],
                    "context_spec": {
                        "overview": "Illustrates Le Chatelier's Principle by showing how dynamic chemical systems respond to temperature, pressure, and concentration stress.",
                        "how_to_use": [
                            "Step 1: Select dynamic reaction parameters (temperature, reactant concentrations).",
                            "Step 2: Apply a concentration or thermal stress to the system.",
                            "Step 3: Observe the reaction quotient (Qc) shift relative to equilibrium constant (Kc)."
                        ],
                        "expected_results": [
                            {
                                "action": "Applying Stress",
                                "expected_outcome": "System shifts position of equilibrium in direction that offsets applied stress.",
                                "key_takeaway": "Dynamic equilibrium is restored when Qc = Kc."
                            }
                        ]
                    }
                },
            },

            # Physics Placeholders
            {
                "key": "freefall",
                "title": "Freefall Acceleration",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Gravity & Kinematics",
                "status": SimulationStatus.PLACEHOLDER,
                "description": "Analyze uniform acceleration and velocity-time graphs for objects falling under gravity.",
                "archetype": "freefall",
                "config": {
                    "planned_features": ["Gravity Selector (Earth/Moon/Mars)", "Air Resistance Toggle", "Velocity-Time Plotter"],
                    "context_spec": {
                        "overview": "Analyzes uniform gravitational acceleration and velocity-time kinematics for falling objects.",
                        "how_to_use": [
                            "Step 1: Select drop height and environmental gravity constant.",
                            "Step 2: Release object and record time-of-flight.",
                            "Step 3: Compare velocity-time curves with and without air resistance."
                        ],
                        "expected_results": [
                            {
                                "action": "Freefall in Vacuum",
                                "expected_outcome": "Constant downward acceleration (g = 9.8 m/s²).",
                                "key_takeaway": "All objects fall with identical acceleration regardless of mass when air resistance is absent."
                            }
                        ]
                    }
                },
            },
            {
                "key": "circuit",
                "title": "Circuit Builder",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Direct Current Circuits",
                "status": SimulationStatus.PLACEHOLDER,
                "description": "Interactive circuit schematic builder to test Ohm's law, resistors in series/parallel, and voltage drops.",
                "archetype": "circuit",
                "config": {
                    "planned_features": ["Resistor Grid", "Ammeter & Voltmeter Probes", "Switch & Battery Controls"],
                    "context_spec": {
                        "overview": "Interactive direct current circuit environment to explore Ohm's Law and series/parallel resistor combinations.",
                        "how_to_use": [
                            "Step 1: Adjust DC power source voltage.",
                            "Step 2: Configure resistor grid in series or parallel alignment.",
                            "Step 3: Probe branch currents and voltage drops with multimeters."
                        ],
                        "expected_results": [
                            {
                                "action": "Increasing Resistance",
                                "expected_outcome": "Total circuit current decreases (I = V / R).",
                                "key_takeaway": "Ohm's Law governs linear current response in ohmic conductors."
                            }
                        ]
                    }
                },
            },
            {
                "key": "optics",
                "title": "Ray Optics & Lenses",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Geometric Optics",
                "status": SimulationStatus.PLACEHOLDER,
                "description": "Trace focal rays through convex and concave lenses to visualize real vs. virtual image formation.",
                "archetype": "optics",
                "config": {
                    "planned_features": ["Focal Length Adjustment", "Focal Ray Tracing", "Real/Virtual Image Indicator"],
                    "context_spec": {
                        "overview": "Traces principal light rays through convex and concave spherical lenses to visualize real vs. virtual image formation.",
                        "how_to_use": [
                            "Step 1: Adjust object distance relative to focal length (f).",
                            "Step 2: Toggle principal rays (parallel, focal, central).",
                            "Step 3: Observe image magnification, inversion, and orientation."
                        ],
                        "expected_results": [
                            {
                                "action": "Object beyond 2f",
                                "expected_outcome": "Real, inverted, diminished image formed between f and 2f.",
                                "key_takeaway": "Thin lens equation (1/f = 1/do + 1/di) accurately predicts real image focal location."
                            }
                        ]
                    }
                },
            },
            {
                "key": "convex_lens_image_formation",
                "title": "Convex Lens: Principal Ray Diagrams & Image Formation",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Thin Lenses & Optical Instruments",
                "status": SimulationStatus.ACTIVE,
                "description": "Interactive ray tracer for convex lenses with live construction of parallel, optical centre, and focal rays across 5 standard KCSE object distances.",
                "archetype": "convex_lens_image_formation",
                "config": {
                    "context_spec": {
                        "overview": "Principal ray tracing for converging convex lenses showing real and virtual image formation.",
                        "how_to_use": [
                            "Step 1: Select object position (beyond 2F, at 2F, F to 2F, at F, or inside F).",
                            "Step 2: Trace principal rays.",
                            "Step 3: Analyze real-time values for image distance (v), magnification (m), and nature."
                        ],
                        "expected_results": [
                            {
                                "action": "Object beyond 2F",
                                "expected_outcome": "Real, inverted, and diminished image formed between F and 2F.",
                                "key_takeaway": "Emulates optical camera mechanics."
                            }
                        ]
                    }
                },
            },
            {
                "key": "lens_formula_calculator",
                "title": "Verification of the Lens Formula (1/f = 1/u + 1/v)",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Thin Lenses & Optical Instruments",
                "status": SimulationStatus.ACTIVE,
                "description": "Step-by-step algebraic substitution of the thin lens formula alongside dynamic 1/v against 1/u linear graph plotting.",
                "archetype": "lens_formula_calculator",
                "config": {
                    "context_spec": {
                        "overview": "Algebraic and graphical verification of the thin lens formula 1/f = 1/u + 1/v.",
                        "how_to_use": [
                            "Step 1: Choose object distance u.",
                            "Step 2: Follow algebraic substitution steps.",
                            "Step 3: Observe experimental coordinate point on the 1/v vs 1/u line."
                        ],
                        "expected_results": [
                            {
                                "action": "Plotting 1/v vs 1/u",
                                "expected_outcome": "Straight line of slope -1 with intercept 1/f.",
                                "key_takeaway": "Graph axes intercepts directly provide focal power and focal length."
                            }
                        ]
                    }
                },
            },
            {
                "key": "eye_defects_simulator",
                "title": "Eye Defects: Ray Diagnosis & Spectacle Lens Correction",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Thin Lenses & Optical Instruments",
                "status": SimulationStatus.ACTIVE,
                "description": "Dual-eye anatomical ray tracing comparing uncorrected vision vs spectacle-corrected sight for Myopia, Hypermetropia, and Presbyopia.",
                "archetype": "eye_defects_simulator",
                "config": {
                    "context_spec": {
                        "overview": "Ray diagnosis of human eye defects and corrective spectacle lens simulation.",
                        "how_to_use": [
                            "Step 1: Select eye condition (Normal, Myopia, Hypermetropia, Presbyopia).",
                            "Step 2: Observe uncorrected focal point relative to the retina.",
                            "Step 3: Apply corrective spectacle lens to restore sharp 20/20 vision on the retina."
                        ],
                        "expected_results": [
                            {
                                "action": "Myopia Correction",
                                "expected_outcome": "Diverging concave lens shifts premature focus back onto the retina.",
                                "key_takeaway": "Short-sightedness requires concave lenses to diverge incoming rays."
                            }
                        ]
                    }
                },
            },
            {
                "key": "lens_power_diopters",
                "title": "Lens Power in Diopters (P = 1/f)",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Thin Lenses & Optical Instruments",
                "status": SimulationStatus.ACTIVE,
                "description": "Calculates optical power in dioptres P = 1/f with dynamic ray refraction bending angles and continuous focal power spectrum.",
                "archetype": "lens_power_diopters",
                "config": {
                    "context_spec": {
                        "overview": "Exploration of optical lens power in dioptres (P = 1/f in metres).",
                        "how_to_use": [
                            "Step 1: Choose an optical lens preset.",
                            "Step 2: Simulate refraction and observe ray deviation angle.",
                            "Step 3: Track lens position along the continuous dioptre spectrum."
                        ],
                        "expected_results": [
                            {
                                "action": "Shorter focal length",
                                "expected_outcome": "Greater ray bending and higher numerical dioptre power.",
                                "key_takeaway": "Lens power P in dioptres is inversely proportional to focal length in metres."
                            }
                        ]
                    }
                },
            },
            {
                "key": "diverging_lens_simulator",
                "title": "Diverging Lens: The Virtual Invariant Law",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Thin Lenses & Optical Instruments",
                "status": SimulationStatus.ACTIVE,
                "description": "Concave lens ray tracer demonstrating the invariant formation of virtual, upright, and diminished images regardless of object position.",
                "archetype": "diverging_lens_simulator",
                "config": {
                    "context_spec": {
                        "overview": "Demonstrates why diverging concave lenses always form virtual, upright, and diminished images.",
                        "how_to_use": [
                            "Step 1: Adjust object distance u across near, middle, and far positions.",
                            "Step 2: Trace diverging rays and their virtual focal extensions.",
                            "Step 3: Verify that magnification remains between 0 and 1."
                        ],
                        "expected_results": [
                            {
                                "action": "Varying object position",
                                "expected_outcome": "Image is always formed between the lens and virtual focus F.",
                                "key_takeaway": "Concave lenses cannot project real images; ideal for door peepholes and myopia."
                            }
                        ]
                    }
                },
            },
            {
                "key": "circular_motion_angular_quantities",
                "title": "Circular Motion & Angular Quantities (T, f, ω, v)",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Uniform Circular Motion",
                "status": SimulationStatus.ACTIVE,
                "description": "Interactive rotational mechanics exploring period, frequency, angular velocity, and the linear speed differential v = ωr across different radii.",
                "archetype": "circular_motion_angular_quantities",
                "config": {
                    "context_spec": {
                        "overview": "Examine how angular velocity ω remains constant across an entire rotating body while tangential speed v scales directly with radius.",
                        "how_to_use": [
                            "Step 1: Select a rotating scenario (Ferris Wheel, Bicycle Wheel, Ceiling Fan, or Drill).",
                            "Step 2: Compare Point A on the rim against Point B at half-radius.",
                            "Step 3: Track revolutions, angular sweep in radians, and calculate T, f, ω, and v."
                        ],
                        "expected_results": [
                            {
                                "action": "Measuring speeds at different radii",
                                "expected_outcome": "Both points share identical period T and angular velocity ω, but outer rim speed is double.",
                                "key_takeaway": "Tangential linear speed v is proportional to radius: v = ωr."
                            }
                        ]
                    }
                },
            },
            {
                "key": "centripetal_acceleration",
                "title": "Centripetal Acceleration: Direction Vector & Inward Law",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Uniform Circular Motion",
                "status": SimulationStatus.ACTIVE,
                "description": "Visualizes why constant speed in a circular path still generates acceleration due to continuous velocity vector direction change toward the center.",
                "archetype": "centripetal_acceleration",
                "config": {
                    "context_spec": {
                        "overview": "Demonstrates the paradox of circular motion: constant scalar speed with non-zero inward acceleration a = v²/r.",
                        "how_to_use": [
                            "Step 1: Select a cornering scenario (Car on bend, Track athlete, Rotor, or Jet).",
                            "Step 2: Watch the speedometer needle remain stationary while the compass needle continuously rotates.",
                            "Step 3: Observe the inward acceleration vector ac = v²/r and compute required force F = ma."
                        ],
                        "expected_results": [
                            {
                                "action": "Analyzing dual dashboard gauges",
                                "expected_outcome": "Speedometer stays constant; compass needle spins through 360 degrees.",
                                "key_takeaway": "Acceleration is vector rate of change. Changing direction requires inward acceleration a = v²/r."
                            }
                        ]
                    }
                },
            },
            {
                "key": "centripetal_force_sources",
                "title": "Sources of Centripetal Force & Tangential Inertia",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Uniform Circular Motion",
                "status": SimulationStatus.ACTIVE,
                "description": "Explores the real physical forces providing centripetal acceleration (Friction, Tension, Gravity) and demonstrates Newton's 1st Law tangential escape.",
                "archetype": "centripetal_force_sources",
                "config": {
                    "context_spec": {
                        "overview": "Clarifies that centripetal force is not a standalone force, but a label for the real physical force pulling an object inward.",
                        "how_to_use": [
                            "Step 1: Select a scenario (Car on road = Friction, String = Tension, Moon = Gravity).",
                            "Step 2: Inspect the inward real force vector and calculated magnitude F = mv²/r.",
                            "Step 3: Click 'Cut Force / Icy Road' to observe instantaneous tangential escape in a straight line."
                        ],
                        "expected_results": [
                            {
                                "action": "Removing the inward force mid-motion",
                                "expected_outcome": "The object instantly abandons the circular path and flies off along the tangent.",
                                "key_takeaway": "Without an inward centripetal force, inertia carries the body in a straight line (Newton's 1st Law)."
                            }
                        ]
                    }
                },
            },
            {
                "key": "banked_track_dynamics",
                "title": "Banked Track & Vehicle Cornering Mechanics",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Uniform Circular Motion",
                "status": SimulationStatus.ACTIVE,
                "description": "Explore civil and mechanical engineering design of banked roadways and tracks, eliminating reliance on tyre friction at ideal design speed.",
                "archetype": "banked_track_dynamics",
                "config": {
                    "context_spec": {
                        "overview": "Explore civil and mechanical engineering design of banked roadways and tracks. Understand how normal reaction force components eliminate reliance on tyre friction at design speed, and determine safe speed windows before skidding occurs.",
                        "how_to_use": [
                            "Step 1: Select an engineering scenario (Standard Highway Curve, NASCAR/Velodrome, Icy Mountain Bend, or Flat Curve).",
                            "Step 2: Adjust road banking angle theta, turn radius r, and vehicle speed v to view real-time vector resolution of weight (mg), normal reaction (N), and lateral friction (f).",
                            "Step 3: Tune speed to ideal design speed v0 = sqrt(r*g*tan(theta)) to achieve zero lateral friction wear, or push past maximum safe speed vmax to observe outward skidding."
                        ],
                        "expected_results": [
                            {
                                "action": "Operating at ideal banking speed v_0",
                                "expected_outcome": "Horizontal component of normal force N*sin(theta) completely provides centripetal acceleration; lateral tyre friction f drops to 0 N.",
                                "key_takeaway": "Banked curves allow safe turns even under zero-friction conditions (e.g. ice)."
                            }
                        ]
                    }
                },
            },
            {
                "key": "archimedes_principle_buoyancy",
                "title": "Archimedes' Principle & Buoyancy Balance",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Floating and Sinking",
                "status": SimulationStatus.ACTIVE,
                "description": "Virtual Eureka can displacement lab verifying that buoyant upthrust equals the weight of displaced fluid (U = rho * V * g).",
                "archetype": "archimedes_principle_buoyancy",
                "config": {
                    "context_spec": {
                        "overview": "Virtual Eureka can displacement lab verifying that buoyant upthrust equals the weight of displaced fluid (U = rho * V * g).",
                        "how_to_use": [
                            "Step 1: Choose solid material (wood, aluminium, iron, lead) and liquid (pure water, sea water, kerosene, glycerin, mercury).",
                            "Step 2: Submerge solid and record displaced liquid volume in measuring cylinder.",
                            "Step 3: Compare spring balance apparent loss of weight with displaced liquid weight."
                        ],
                        "expected_results": [
                            {
                                "action": "Submerging solid block into liquid",
                                "expected_outcome": "Displaced liquid volume matches submerged solid volume; upthrust equals weight of displaced liquid.",
                                "key_takeaway": "Archimedes' Principle: Apparent weight loss = Upthrust = rho_liquid * V_sub * g."
                            }
                        ]
                    }
                },
            },
            {
                "key": "law_of_floatation_equilibrium",
                "title": "Law of Floatation & Plimsoll Line",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Floating and Sinking",
                "status": SimulationStatus.ACTIVE,
                "description": "Investigate equilibrium of floating bodies, ship draft depth, reserve buoyancy, and international Plimsoll line marks across varying water densities.",
                "archetype": "law_of_floatation_equilibrium",
                "config": {
                    "context_spec": {
                        "overview": "Investigate equilibrium of floating bodies, ship draft depth, reserve buoyancy, and international Plimsoll line marks across varying water densities.",
                        "how_to_use": [
                            "Step 1: Select water environment (Fresh Water, Summer Sea, Winter Sea, Tropical Sea, Dead Sea).",
                            "Step 2: Adjust cargo load to observe ship draft and waterplane displacement.",
                            "Step 3: Ensure water level does not submerge the legal Plimsoll line mark for the active sea zone."
                        ],
                        "expected_results": [
                            {
                                "action": "Moving from fresh water to dense sea water",
                                "expected_outcome": "Ship rises higher in the water; draft decreases due to higher liquid density.",
                                "key_takeaway": "A floating vessel displaces its own weight of fluid (Law of Floatation: W_ship = rho_liquid * V_disp * g)."
                            }
                        ]
                    }
                },
            },
            {
                "key": "hydrometer_calibration_density",
                "title": "Hydrometer Calibration & Relative Density",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Floating and Sinking",
                "status": SimulationStatus.ACTIVE,
                "description": "Interactive glass hydrometer exploring stem sensitivity, bulb ballast, inverse density scale gradation, and commercial milk/battery testing.",
                "archetype": "hydrometer_calibration_density",
                "config": {
                    "context_spec": {
                        "overview": "Interactive glass hydrometer exploring stem sensitivity, bulb ballast, inverse density scale gradation, and commercial milk/battery testing.",
                        "how_to_use": [
                            "Step 1: Immerse hydrometer into test liquids (pure water, kerosene, milk, battery acid, concentrated acid).",
                            "Step 2: Use magnified loupe to read the liquid meniscus against the stem scale.",
                            "Step 3: Compare narrow vs wide stem geometries to analyze instrument sensitivity."
                        ],
                        "expected_results": [
                            {
                                "action": "Testing liquids of increasing density",
                                "expected_outcome": "Hydrometer floats higher; stem emerges further above the liquid surface.",
                                "key_takeaway": "Hydrometer stem scale is non-linear and inverted: lower density marks at top, higher density marks at bottom."
                            }
                        ]
                    }
                },
            },
            {
                "key": "balloons_and_submarines_buoyancy",
                "title": "Submarine & Weather Balloon Aerostatic Buoyancy",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Floating and Sinking",
                "status": SimulationStatus.ACTIVE,
                "description": "Dual hydro-aerostatic simulator contrasting variable-mass submarine ballast trim against variable-volume weather balloon stratospheric ascent.",
                "archetype": "balloons_and_submarines_buoyancy",
                "config": {
                    "context_spec": {
                        "overview": "Dual hydro-aerostatic simulator contrasting variable-mass submarine ballast trim against variable-volume weather balloon stratospheric ascent.",
                        "how_to_use": [
                            "Step 1: Submarine mode: flood Kingston ballast valves to dive, blow compressed air to surface, achieve neutral depth hover.",
                            "Step 2: Balloon mode: launch helium/hydrogen radiosonde and monitor exponential air density drop with altitude.",
                            "Step 3: Observe balloon volume expansion up to burst diameter threshold."
                        ],
                        "expected_results": [
                            {
                                "action": "Submarine ballast tank flooding",
                                "expected_outcome": "Overall density exceeds sea water; downward weight overcomes upthrust to initiate dive.",
                                "key_takeaway": "Submarines regulate buoyancy by changing mass at constant volume; balloons expand volume in decreasing air density."
                            }
                        ]
                    }
                },
            },
            {
                "key": "em_wave_orthogonal_fields",
                "title": "Orthogonal EM Wave Fields & Wave Equation",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Electromagnetic Spectrum",
                "status": SimulationStatus.ACTIVE,
                "description": "Transverse electromagnetic wave propagation: mutually perpendicular electric (E) and magnetic (B) field oscillations, Poynting energy flux vector (S), speed of light across optical media (v = c / n), and photon energetics.",
                "archetype": "em_wave_orthogonal_fields",
                "config": {
                    "context_spec": {
                        "overview": "Investigate transverse electromagnetic wave propagation: mutually perpendicular electric (E) and magnetic (B) field oscillations, Poynting energy flux vector (S = (1/μ₀)(E × B)), speed of light across optical media (v = c / n), and photon quantum energetics (E = hf).",
                        "how_to_use": [
                            "Step 1: Select propagation medium (Vacuum, Air, Water, Crown Glass, Diamond) to observe how refractive index n reduces wave speed v = c/n and wavelength lambda = v/f while frequency remains constant.",
                            "Step 2: Adjust Frequency (f) from 100 MHz to 1000 MHz (1 GHz) or Wavelength slider to verify inverse proportionality.",
                            "Step 3: Toggle Field Vectors, Wave Ribbon, and Poynting Energy Flux (S) to confirm vector perpendicularity E ⟂ B ⟂ k.",
                            "Step 4: Solve the KCSE examination challenges with step-by-step solutions."
                        ],
                        "expected_results": [
                            {
                                "action": "Transitioning into Optically Denser Medium (n > 1)",
                                "expected_outcome": "Wave speed slows down (v = c / n) and wavelength compresses proportionally (λ = v / f), while frequency stays constant.",
                                "key_takeaway": "Wave frequency is determined solely by the source transmitter; medium determines speed and wavelength."
                            },
                            {
                                "action": "Verifying Vector Perpendicularity (E ⟂ B ⟂ k)",
                                "expected_outcome": "E-field in vertical y-axis and B-field in horizontal x-axis propagate along +z with zero dot product (E · B = 0).",
                                "key_takeaway": "EM waves are purely transverse waves with mutually perpendicular electric and magnetic vectors."
                            }
                        ]
                    },
                    "telemetry_events": ["sim_interaction", "practice_correct", "practice_incorrect", "set_camera_preset", "reset_simulation"]
                },
            },
            {
                "key": "speed_of_light_experiments",
                "title": "Speed of Light Historical Laboratory",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Electromagnetic Spectrum",
                "status": SimulationStatus.ACTIVE,
                "description": "Historical recreation of Hippolyte Fizeau's toothed wheel (1849) and Ole Rømer's Jupiter Io eclipse delay (1676) to determine the finite speed of light.",
                "archetype": "speed_of_light_experiments",
                "config": {
                    "context_spec": {
                        "overview": "Historical recreation of Hippolyte Fizeau's toothed wheel (1849) and Ole Rømer's Jupiter Io eclipse delay (1676) to determine the finite speed of light.",
                        "how_to_use": [
                            "Step 1: In Fizeau tab, adjust wheel RPM to ~724 RPM to observe the first extinction/eclipse where c = 4 D N f.",
                            "Step 2: In Rømer tab, scrub Earth orbital month from January to July to observe the +16.6 minute eclipse delay across Earth's orbital diameter.",
                            "Step 3: Solve historical KCSE practice calculation challenges."
                        ],
                        "expected_results": [
                            {
                                "action": "Setting wheel speed to first eclipse frequency",
                                "expected_outcome": "Reflected light beam from distant mirror is eclipsed by the adjacent moving tooth.",
                                "key_takeaway": "Light transit time over distance 2D equals wheel tooth-to-gap transit time (c = 4 D N f)."
                            }
                        ]
                    }
                },
            },
            {
                "key": "em_spectrum_analyzer_bands",
                "title": "Interactive EM Spectrum Bands & Wavelength Analyzer",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Electromagnetic Spectrum",
                "status": SimulationStatus.ACTIVE,
                "description": "Master continuous spectrum analyzer covering all 7 major bands from 10^-14 m to 10^4 m, Wien's law, ionizing boundaries, and ROYGBIV visible sub-bands.",
                "archetype": "em_spectrum_analyzer_bands",
                "config": {
                    "context_spec": {
                        "overview": "Explore the continuous electromagnetic spectrum across all 7 major bands. Manipulate wavelength on a 24-order-of-magnitude logarithmic slider, compare scales to real-world objects, verify wave equations, and inspect ionizing safety limits.",
                        "how_to_use": [
                            "Step 1: Drag the logarithmic slider to span wavelengths from 10⁻¹⁴ m to 10⁴ m.",
                            "Step 2: Jump between all 7 major spectral regions using the quick band buttons.",
                            "Step 3: Analyze the expanded ROYGBIV color breakdown and exact nanometer swatch in the visible band.",
                            "Step 4: Solve KCSE exam calculation problems with immediate feedback."
                        ],
                        "expected_results": [
                            {
                                "action": "Decreasing Wavelength (λ ↓)",
                                "expected_outcome": "Frequency (f ↑) and photon energy (E ↑) increase inversely.",
                                "key_takeaway": "Wave speed in vacuum c = 3.0×10⁸ m/s remains constant for all EM radiation (c = fλ)."
                            }
                        ]
                    }
                },
            },
            {
                "key": "em_radiation_attenuation_hazards",
                "title": "Radiation Attenuation, Penetration & Shielding Simulator",
                "subject": SubjectDomain.PHYSICS,
                "topic": "Electromagnetic Spectrum",
                "status": SimulationStatus.ACTIVE,
                "description": "Investigate exponential Beer-Lambert attenuation I(x) = I0 * exp(-mu * x), Half-Value Layers (HVL), absorber shields, and non-ionizing vs ionizing damage mechanisms.",
                "archetype": "em_radiation_attenuation_hazards",
                "config": {
                    "context_spec": {
                        "overview": "Demonstrates how electromagnetic radiation attenuates exponentially through matter according to the Beer-Lambert law I(x) = I0 * exp(-mu * x), and contrasts non-ionizing vs ionizing biological damage.",
                        "how_to_use": [
                            "Step 1: Select radiation beam (Radio, Microwave, IR, Visible, UV, X-Ray, Gamma).",
                            "Step 2: Choose shielding absorber material (Air, Paper, Soft Tissue, Aluminum, Concrete, Dense Lead).",
                            "Step 3: Adjust shield thickness slider and observe real-time exponential attenuation.",
                            "Step 4: Explore Cellular Damage tab to observe thermal vs DNA strand damage."
                        ],
                        "expected_results": [
                            {
                                "action": "Varying shield thickness across Half-Value Layers (HVLs)",
                                "expected_outcome": "Transmitted intensity meter follows (1/2)^n exponential drop.",
                                "key_takeaway": "Each HVL cuts transmitted flux by 50%. A lead shield of 4 HVLs leaves only 6.25% of the beam."
                            }
                        ]
                    }
                },
            },
        ]

        with transaction.atomic():
            for item in simulations_data:
                existing_sim = Simulation.objects.filter(key=item["key"]).first()
                if existing_sim:
                    existing_config = existing_sim.config or {}
                    merged_config = item["config"]
                    existing_config.update(merged_config)
                    item["config"] = existing_config

                sim, created = Simulation.objects.update_or_create(
                    key=item["key"],
                    defaults=item,
                )
                action_str = "Created" if created else "Updated (Merged)"
                self.stdout.write(self.style.SUCCESS(f"  [{action_str}] {sim}"))

        self.stdout.write(self.style.SUCCESS("Simulation registry seed complete."))

