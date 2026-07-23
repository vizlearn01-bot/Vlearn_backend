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

