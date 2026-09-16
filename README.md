# From Memory to Belief: A Survey of State Maintenance and Belief Revision in LLM Decision Agents

Paper list, screening records, and the rerunnable literature-search pipeline for the survey *From Memory to Belief* (Huang, Wang, Peng, Ananiadou, Tsujii; preprint 2026).

- `paper.pdf` — the preprint.
- `paper_tex/` — LaTeX sources (ACL template), including the 33-benchmark catalogue and the 120-row master table.
- `lit_search/` — search + screening scripts, `config.json` (queries, rules, curated titles), and the run directories with per-stage counts and full-text screening records.

Organising question: **which object receives credit** — the output, the trajectory, the interaction, or the belief state written before the action.

## Paper list (full-text screened, 179 papers)

Columns: system, year, who maintains the belief, credited object, evidence level (P = peer-reviewed, A = preprint). Entries are grouped by the survey section they support; the complete record with revision signal, metrics, and notes is `lit_search/runs/20260916_v3/manual_screen_all_v3.csv`.

### Belief representation (who maintains the belief)

| Paper | Year | Belief kept by | Credited | Ev. |
|---|---|---|---|---|
| [Teaching Models to Express Their Uncertainty in Words](https://arxiv.org/abs/2205.14334) | 2022 | model-written | output | P |
| [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221) | 2022 | model-written | output | A |
| [Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation](https://arxiv.org/abs/2302.09664) | 2023 | n/a | output | P |
| [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | 2023 | external memory | action/turn | P |
| [LLM+P: Empowering Large Language Models with Optimal Planning Proficiency](https://arxiv.org/abs/2304.11477) | 2023 | n/a | output | A |
| [MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) | 2023 | external memory | output | P |
| [RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text](https://arxiv.org/abs/2305.13304) | 2023 | model-written | output | A |
| [Large Language Models as Commonsense Knowledge for Large-Scale Task Planning](https://arxiv.org/abs/2305.14078) | 2023 | learned world model | step/trajectory | P |
| [Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992) | 2023 | learned world model | step/trajectory | P |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 2023 | external memory | step/trajectory | P |
| [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) | 2023 | external memory | step/trajectory | P |
| [TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance](https://arxiv.org/abs/2309.03736) | 2023 | external memory | action/turn | A |
| [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | 2023 | external memory | output | A |
| [FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743) | 2023 | external memory | action/turn | P |
| [A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist](https://arxiv.org/abs/2402.18485) | 2024 | external memory | action/turn | P |
| [FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making](https://arxiv.org/abs/2407.06567) | 2024 | external memory | belief state | P |
| [Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://arxiv.org/abs/2407.07086) | 2024 | model-written | belief state | A |
| [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) | 2024 | external memory | n/a | A |
| [QuBE: Question-based Belief Enhancement for Agentic LLM Reasoning](https://arxiv.org/abs/10.18653/v1/2024.emnlp-main.1193) | 2024 | model-written | belief state | P |
| [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) | 2025 | external memory | output | P |
| [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) | 2025 | external memory | n/a | A |
| [MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents](https://arxiv.org/abs/2506.15841) | 2025 | model-written | belief state | A |
| [MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent](https://arxiv.org/abs/2507.02259) | 2025 | model-written | belief state | P |
| [Memento: Fine-tuning LLM Agents without Fine-tuning LLMs](https://arxiv.org/abs/2508.16153) | 2025 | external memory | action/turn | A |
| [Controlling Long-Horizon Behavior in Language Model Agents with Explicit State Dynamics](https://arxiv.org/abs/2601.16087) | 2026 | external memory | n/a | A |
| [From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning for Embodied Agents](https://arxiv.org/abs/2602.04326) | 2026 | model-written | belief state | A |
| [Recursive Belief Vision Language Action Models](https://arxiv.org/abs/2602.20659) | 2026 | learned world model | belief state | A |
| [Graph of States: Solving Abductive Tasks with Large Language Models](https://arxiv.org/abs/2603.21250) | 2026 | external memory | n/a | A |
| [TAMTRL: Teacher-Aligned Reward Reshaping for Multi-Turn Reinforcement Learning in Long-Context Compression](https://arxiv.org/abs/2603.21663) | 2026 | model-written | step/trajectory | A |
| [From Topology to Trajectory: LLM-Driven World Models For Supply Chain Resilience](https://arxiv.org/abs/2604.11041) | 2026 | learned world model | step/trajectory | A |
| [Bayesian Linguistic Forecaster](https://arxiv.org/abs/2604.18576) | 2026 | model-written (numeric prob + text evidence summary) | none | A |
| [Belief Memory (BeliefMem)](https://arxiv.org/abs/2605.05583) | 2026 | external store with probabilities | none | A |
| [Agent-BRACE](https://arxiv.org/abs/2605.11436) | 2026 | model-written (atomic claims + ordinal certainty) | belief + policy jointly (RL) | A |
| [CHAL: Council of Hierarchical Agentic Language](https://arxiv.org/abs/2605.12718) | 2026 | model-written | belief state | A |
| [Learning POMDP World Models from Observations with Language-Model Priors](https://arxiv.org/abs/2605.13740) | 2026 | learned world model | belief state | A |
| [Belief Engine: Configurable and Inspectable Stance Dynamics in Multi-Agent LLM Deliberation](https://arxiv.org/abs/2605.15343) | 2026 | probabilistic memory | belief state | A |
| [GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations](https://arxiv.org/abs/2605.14498) | 2026 | external memory | n/a | A |
| [Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP](https://arxiv.org/abs/2605.16205) | 2026 | external memory | n/a | A |
| [Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents](https://arxiv.org/abs/2605.17641) | 2026 | external memory | belief state | A |
| [Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents](https://arxiv.org/abs/2605.21768) | 2026 | external memory | belief state | A |
| [MemGym: a Long-Horizon Memory Environment for LLM Agents](https://arxiv.org/abs/2605.20833) | 2026 | external memory | n/a | A |
| [Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents](https://arxiv.org/abs/2606.01886) | 2026 | external memory | n/a | A |
| [Text World Models (review)](https://arxiv.org/abs/2606.09032) | 2026 | learned/prompted transition model | n/a | A |
| [HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning](https://arxiv.org/abs/2606.10507) | 2026 | model-written | step/trajectory | A |
| [ProPlay: Procedural World Models for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.12780) | 2026 | learned world model | step/trajectory | A |
| [Belief at Risk](https://arxiv.org/abs/2606.15473) | 2026 | external Bayesian filter (LLM as observation model) | none | A |
| [When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense](https://arxiv.org/abs/2606.22030) | 2026 | probabilistic memory | belief state | A |
| [Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning](https://arxiv.org/abs/2606.27483) | 2026 | model-written | step/trajectory | A |
| [Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents](https://arxiv.org/abs/2606.27806) | 2026 | learned world model | belief state | A |
| [BayesEvolve: Explicit Belief States for Autonomous Scientific Discovery](https://arxiv.org/abs/2606.30335) | 2026 | external Bayesian filter | belief state | A |
| [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639) | 2026 | learned world model | belief state | A |
| [Auditing Belief-Conditioned LLM Agents in Hidden-Information Social Deduction Games](https://arxiv.org/abs/2607.10814) | 2026 | external memory | belief state | A |
| [Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correction for Autonomous Decision-Making](https://arxiv.org/abs/2607.17038) | 2026 | external memory | action/turn | A |
| [NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability](https://arxiv.org/abs/2607.28942) | 2026 | external memory | action/turn | A |
| [MADE: Belief-Driven Dual-Agent Coordination for Autonomous Model Deployment](https://arxiv.org/abs/2608.01189) | 2026 | external memory | action/turn | A |
| [EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.05446) | 2026 | external memory | action/turn | A |
| [Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents](https://arxiv.org/abs/2608.12476) | 2026 | external memory | n/a | A |
| [Belief-Based World Model](https://arxiv.org/abs/2609.00455) | 2026 | learned WM exposes belief to LLM | none (policy prompted) | A |
| [Belief-Calibrated Optimization: An Explicit World Model for Agentic Optimization](https://arxiv.org/abs/2609.01861) | 2026 | model-written | belief state | A |
| [EvoSCM: Scientific Belief Revision Through Causal Model Evolution and Experimentation](https://arxiv.org/abs/2609.01526) | 2026 | model-written | belief state | A |
| [CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents](https://arxiv.org/abs/2609.02265) | 2026 | learned world model | belief state | A |
| [Semantic Bayesian World Models](https://arxiv.org/abs/2609.03834) | 2026 | external Bayesian filter | belief state | A |
| [Belief-State Engine](https://arxiv.org/abs/2609.10036) | 2026 | external Bayesian filter | none (prompting) | A |

### Belief revision and failure modes

| Paper | Year | Belief kept by | Credited | Ev. |
|---|---|---|---|---|
| [Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/abs/2302.01560) | 2023 | context (free-form trace) | step/trajectory | P |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023 | external memory | step/trajectory | P |
| [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | 2023 | context (free-form trace) | output | P |
| [Language Models can Solve Computer Tasks](https://arxiv.org/abs/2303.17491) | 2023 | context (free-form trace) | action/turn | P |
| [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128) | 2023 | context (free-form trace) | output | P |
| [Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models](https://arxiv.org/abs/2310.04406) | 2023 | external memory | step/trajectory | P |
| [Reflect-RL: Two-Player Online RL Fine-Tuning for LMs](https://arxiv.org/abs/2402.12621) | 2024 | model-written | action/turn | P |
| [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.07199) | 2024 | external memory | step/trajectory | A |
| [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://arxiv.org/abs/2501.01702) | 2025 | context (free-form trace) | step/trajectory | P |
| [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/abs/2507.05257) | 2025 | evaluator-side oracle | n/a | A |
| [DenoiseFlow: Uncertainty-Aware Denoising for Reliable LLM Agentic Workflows](https://arxiv.org/abs/2603.00532) | 2026 | context (free-form trace) | step/trajectory | A |
| [D-MEM](https://arxiv.org/abs/2603.14597) | 2026 | external memory | n/a | A |
| [Dynamic Theory of Mind as a Temporal Memory Problem: Evidence from Large Language Models](https://arxiv.org/abs/2603.14646) | 2026 | context (free-form trace) | n/a | A |
| [BeliefShift](https://arxiv.org/abs/2603.23848) | 2026 | n/a (user beliefs) | n/a | A |
| [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](https://arxiv.org/abs/2604.01212) | 2026 | model-written | n/a | A |
| [DeltaLogic: Minimal Premise Edits Reveal Belief-Revision Failures in Logical Reasoning Models](https://arxiv.org/abs/2604.02733) | 2026 | context (free-form trace) | output | A |
| [Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing](https://arxiv.org/abs/2604.08401) | 2026 | context (free-form trace) | belief state | A |
| [Complete Cyclic Subtask Graphs for Tool-Using LLM Agents: Flexibility, Cost, and Bottlenecks in Long-Horizon Workflows](https://arxiv.org/abs/2604.22820) | 2026 | model-written | n/a | A |
| [MEDLEY-BENCH: Benchmarking Behavioural Metacognition and Belief Revision Under Social Pressure in Large Language Models](https://arxiv.org/abs/2604.16009) | 2026 | context (free-form trace) | n/a | A |
| [T²PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.02178) | 2026 | context (free-form trace) | action/turn | A |
| [STALE](https://arxiv.org/abs/2605.06527) | 2026 | external memory | n/a | A |
| [Why We Need World Models for AGI: Where LLMs Fail and How World Models May Outperform](https://arxiv.org/abs/2605.23972) | 2026 | context (free-form trace) | n/a | A |
| [Representation Signatures and Risk-Feedback Alignment in LLM Trading Agents](https://arxiv.org/abs/2605.28850) | 2026 | context (free-form trace) | output | A |
| [OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling](https://arxiv.org/abs/2605.26322) | 2026 | evaluator-side oracle | n/a | A |
| [Contextual Belief Management (BeliefTrack)](https://arxiv.org/abs/2605.30219) | 2026 | model-written predicted belief state | belief-state reward (RL) | A |
| [TOKI](https://arxiv.org/abs/2606.06240) | 2026 | external memory | n/a | A |
| [Repair the Amplifier, Not the Symptom: Stable World-Model Correction for Agent Rollouts](https://arxiv.org/abs/2607.01767) | 2026 | learned world model | step/trajectory | A |
| [MemOps](https://arxiv.org/abs/2607.12893) | 2026 | external memory | n/a | A |
| [STOCKTAKE](https://arxiv.org/abs/2607.13618) | 2026 | evaluator-side exact Bayes filter oracle | n/a | A |
| [Long-Horizon State Tracking in LLMs: Executing MD5 through a Deep Sequence of Dependent Tool Calls](https://arxiv.org/abs/2609.00012) | 2026 | context (free-form trace) | n/a | A |
| [When Memory Updates but Behavior Does Not](https://arxiv.org/abs/2608.01619) | 2026 | external memory | n/a | A |
| [When Stale Constraints Go Unchecked](https://arxiv.org/abs/2608.25553) | 2026 | inherited memory | n/a | A |
| [UQ for LLM Agents taxonomy](https://arxiv.org/abs/2609.07395) | 2026 | n/a | n/a | A |

### Learning signals by credited object

| Paper | Year | Belief kept by | Credited | Ev. |
|---|---|---|---|---|
| [Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610) | 2022 | n/a | output | P |
| [FireAct: Toward Language Agent Fine-tuning](https://arxiv.org/abs/2310.05915) | 2023 | context (free-form trace) | step/trajectory | A |
| [AgentTuning: Enabling Generalized Agent Abilities for LLMs](https://arxiv.org/abs/2310.12823) | 2023 | context (free-form trace) | step/trajectory | P |
| [ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL](https://arxiv.org/abs/2402.19446) | 2024 | n/a | action/turn | P |
| [SOTOPIA-pi: Interactive Learning of Socially Intelligent Language Agents](https://arxiv.org/abs/2403.08715) | 2024 | n/a | output | A |
| [AgentGym: Evolving Large Language Model-based Agents across Diverse Environments](https://arxiv.org/abs/2406.04151) | 2024 | context (free-form trace) | step/trajectory | A |
| [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337) | 2024 | n/a | output | P |
| [Reinforcement Learning for Long-Horizon Interactive LLM Agents](https://arxiv.org/abs/2502.01600) | 2025 | context (free-form trace) | step/trajectory | A |
| [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/abs/2503.09516) | 2025 | context (free-form trace) | output | A |
| [SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks](https://arxiv.org/abs/2503.15478) | 2025 | n/a | action/turn | A |
| [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](https://arxiv.org/abs/2503.19470) | 2025 | context (free-form trace) | output | P |
| [RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2504.20073) | 2025 | context (free-form trace) | step/trajectory | A |
| [Group-in-Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2505.10978) | 2025 | n/a | step/trajectory | P |
| [Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interaction](https://arxiv.org/abs/2506.07976) | 2025 | context (free-form trace) | step/trajectory | A |
| [Agentic Reinforced Policy Optimization](https://arxiv.org/abs/2507.19849) | 2025 | context (free-form trace) | step/trajectory | A |
| [Agent-R1: A Unified and Modular Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2511.14460) | 2025 | context (free-form trace) | step/trajectory | A |
| [Collaborative Multi-Agent Test-Time Reinforcement Learning for Reasoning](https://arxiv.org/abs/2601.09667) | 2026 | external memory | action/turn | A |
| [SuS: Strategy-aware Surprise for Intrinsic Exploration](https://arxiv.org/abs/2601.10349) | 2026 | context (free-form trace) | output | A |
| [HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents](https://arxiv.org/abs/2602.16165) | 2026 | context (free-form trace) | step/trajectory | A |
| [MICA: Multi-granularity Intertemporal Credit Assignment for Long-Horizon Emotional Support Dialogue](https://arxiv.org/abs/2603.06194) | 2026 | external memory | action/turn | A |
| [Hindsight Credit Assignment for Long-Horizon LLM Agents](https://arxiv.org/abs/2603.08754) | 2026 | context (free-form trace) | step/trajectory | A |
| [TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs](https://arxiv.org/abs/2603.22293) | 2026 | context (free-form trace) | action/turn | A |
| [SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training](https://arxiv.org/abs/2603.18079) | 2026 | external memory | step/trajectory | A |
| [Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration](https://arxiv.org/abs/2604.02869) | 2026 | context (free-form trace) | action/turn | A |
| [Co-Evolution of Policy and Internal Reward for Language Agents](https://arxiv.org/abs/2604.03098) | 2026 | model-written | step/trajectory | A |
| [CAPO: Critic-Guided Action-Aligned Policy Optimization for Advancing LLM Agent Capabilities](https://arxiv.org/abs/2604.18401) | 2026 | context (free-form trace) | action/turn | A |
| [AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.00425) | 2026 | context (free-form trace) | step/trajectory | A |
| [BOND (distilling Bayesian beliefs)](https://arxiv.org/abs/2605.04507) | 2026 | model-written posterior tags | belief distillation (SFT from Bayesian teacher) | A |
| [Not All Turns Matter: Credit Assignment for Multi-Turn Jailbreaking](https://arxiv.org/abs/2605.08778) | 2026 | context (free-form trace) | action/turn | A |
| [PiCA: Pivot-Based Credit Assignment for Search Agentic Reinforcement Learning](https://arxiv.org/abs/2605.09287) | 2026 | context (free-form trace) | step/trajectory | A |
| [What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents](https://arxiv.org/abs/2605.19447) | 2026 | context (free-form trace) | action/turn | A |
| [SKILLC: Learning Autonomous Skill Internalization in LLM Agents via Contrastive Credit Assignment](https://arxiv.org/abs/2605.27899) | 2026 | context (free-form trace) | step/trajectory | A |
| [ECPO](https://arxiv.org/abs/2606.05885) | 2026 | n/a | step (anchor-state advantages) | A |
| [Self-evolving LLM agents with in-distribution Optimization](https://arxiv.org/abs/2606.07367) | 2026 | context (free-form trace) | step/trajectory | A |
| [Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2606.22995) | 2026 | context (free-form trace) | step/trajectory | A |
| [STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2607.04963) | 2026 | context (free-form trace) | step/trajectory | A |
| [TCPO: Turn-Level Credit Policy Optimization](https://arxiv.org/abs/2608.01667) | 2026 | context (free-form trace) | action/turn | A |
| [Teach the Magnitude, Not the Direction: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents](https://arxiv.org/abs/2608.13179) | 2026 | context (free-form trace) | action/turn | A |
| [HiDiffTIR: Hierarchical Difficulty-Aware Policy Optimization for Multi-Turn Tool-Integrated Reasoning](https://arxiv.org/abs/2608.21863) | 2026 | context (free-form trace) | action/turn | A |
| [IAPO: Influence-Aware Policy Optimization for Credit Assignment in Multi-Turn Service Agents](https://arxiv.org/abs/2608.24588) | 2026 | context (free-form trace) | action/turn | A |
| [VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning](https://arxiv.org/abs/2608.28128) | 2026 | evaluator-side oracle | action/turn | A |
| [Explore More Drift Less](https://arxiv.org/abs/2609.01245) | 2026 | n/a | outcome only | A |
| [PGPO: Potential-Guided Policy Optimization for Multi-Turn Agentic Tasks](https://arxiv.org/abs/2609.02236) | 2026 | context (free-form trace) | action/turn | A |

### Belief-guided evidence acquisition

| Paper | Year | Belief kept by | Credited | Ev. |
|---|---|---|---|---|
| [Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent LLM Systems](https://arxiv.org/abs/2603.13256) | 2026 | probabilistic memory | action/turn | A |
| [RetailBench: Evaluating Long-Horizon Autonomous Decision-Making and Strategy Stability of LLM Agents in Realistic Retail Environments](https://arxiv.org/abs/2603.16453) | 2026 | context (free-form trace) | n/a | A |
| [Can LLM Agents Be CFOs? Benchmarking Long-Horizon Resource Allocation in an Uncertain Enterprise Environment](https://arxiv.org/abs/2603.23638) | 2026 | context (free-form trace) | n/a | A |
| [Context Gathering Decision Process](https://arxiv.org/abs/2605.07042) | 2026 | POMDP over search state | n/a | A |
| [MedExAgent: Training LLM Agents to Ask, Examine, and Diagnose in Noisy Clinical Environments](https://arxiv.org/abs/2605.07058) | 2026 | context (free-form trace) | output | A |
| [Bayesian-Agent](https://arxiv.org/abs/2606.08348) | 2026 | external posterior over skills | none | A |
| [Adaptive AI Delegation under Uncertainty: A Bayesian Governance Policy for Sequential Decision Authority](https://arxiv.org/abs/2606.29406) | 2026 | external Bayesian filter | n/a | A |

### Evaluation and benchmarks

| Paper | Year | Belief kept by | Credited | Ev. |
|---|---|---|---|---|
| [ALFWorld: Aligning Text and Embodied Environments for Interactive Learning](https://arxiv.org/abs/2010.03768) | 2020 | evaluator-side oracle | output | P |
| [PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change](https://arxiv.org/abs/2206.10498) | 2022 | evaluator-side oracle | output | P |
| [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) | 2023 | evaluator-side oracle | output | P |
| [SmartPlay: A Benchmark for LLMs as Intelligent Agents](https://arxiv.org/abs/2310.01557) | 2023 | evaluator-side oracle | output | P |
| [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649) | 2024 | evaluator-side oracle | output | P |
| [Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753) | 2024 | evaluator-side oracle | output | P |
| [tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) | 2024 | evaluator-side oracle | n/a | A |
| [tau2-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982) | 2025 | evaluator-side oracle | n/a | A |
| [Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning](https://arxiv.org/abs/2605.24216) | 2026 | evaluator-side oracle | step/trajectory | A |
| [MINDGAMES: A Live Arena for Evaluating Social and Strategic Reasoning in Multi-Agent LLMs](https://arxiv.org/abs/2605.29512) | 2026 | n/a | n/a | A |
| [POMDP validation framework](https://arxiv.org/abs/2606.17383) | 2026 | external Bayesian filter | none | A |
| [FinBench: Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting](https://arxiv.org/abs/2607.16229) | 2026 | n/a | output | A |
| [Business Arena: Benchmarking LLM Agents in a Realistic Marketplace](https://arxiv.org/abs/2608.08621) | 2026 | n/a | action/turn | A |

### Other

| Paper | Year | Belief kept by | Credited | Ev. |
|---|---|---|---|---|
| [Decision Transformer: Reinforcement Learning via Sequence Modeling](https://arxiv.org/abs/2106.01345) | 2021 | context (free-form trace) | action/turn | P |
| [Dialogue State Tracking with a Language Model using Schema-Driven Prompting](https://arxiv.org/abs/2109.07506) | 2021 | model-written | belief state | P |
| [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) | 2022 | context (free-form trace) | output | P |
| [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) | 2022 | n/a | output | P |
| [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) | 2022 | n/a | action/turn | P |
| [Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608) | 2022 | context (free-form trace) | action/turn | P |
| [Language Models as Agent Models](https://arxiv.org/abs/2212.01681) | 2022 | n/a | n/a | P |
| [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) | 2023 | learned world model | belief state | P |
| [Evaluating Large Language Models in Theory of Mind Tasks](https://arxiv.org/abs/2302.02083) | 2023 | n/a | output | P |
| [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) | 2023 | context (free-form trace) | step/trajectory | P |
| [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) | 2023 | external memory | n/a | P |
| [How FaR Are Large Language Models From Agents with Theory-of-Mind?](https://arxiv.org/abs/2310.03051) | 2023 | context (free-form trace) | action/turn | P |
| [Agents Thinking Fast and Slow: A Talker-Reasoner Architecture](https://arxiv.org/abs/2410.08328) | 2024 | model-written | belief state | A |
| [TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138) | 2024 | context (free-form trace) | output | A |
| [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547) | 2025 | n/a | n/a | P |
| [Agentic Reasoning for Large Language Models](https://arxiv.org/abs/2601.12538) | 2026 | n/a | n/a | A |
| [Credit Assignment in RL for LLMs (survey)](https://arxiv.org/abs/2604.09459) | 2026 | n/a | step/trajectory | A |
| [From Storage to Experience (memory survey)](https://arxiv.org/abs/2605.06716) | 2026 | external store | n/a | A |
| [The Horizon Gap (survey)](https://arxiv.org/abs/2608.06663) | 2026 | n/a | n/a | A |
| [LLM Agents for Forecasting (survey)](https://arxiv.org/abs/2608.23058) | 2026 | n/a | n/a | A |

## Rerunning the search

```bash
cd lit_search
echo YOUR_OPENALEX_KEY > .openalex_key   # not committed
python3 search.py && python3 search_openalex_arxiv.py && python3 screen.py
```

## Citation

```bibtex
@misc{huang2026frommemory,
  title={From Memory to Belief: A Survey of State Maintenance and Belief Revision in LLM Decision Agents},
  author={Huang, Jimin and Wang, Yuyan and Peng, Xueqing and Ananiadou, Sophia and Tsujii, Jun'ichi},
  year={2026},
  howpublished={\url{https://github.com/jiminHuang/belief-state-survey}},
  note={Preprint. Zenodo DOI: TBD}
}
```

License: code MIT; paper and screening records CC BY 4.0.