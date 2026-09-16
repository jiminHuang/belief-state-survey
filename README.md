# From Memory to Belief: A Survey of State Maintenance and Belief Revision in LLM Decision Agents

Paper list, screening records, and the rerunnable literature-search pipeline for the survey *From Memory to Belief* (Huang, Wang, Peng, Ananiadou, Tsujii; preprint 2026).

- `paper.pdf` — the preprint.
- `paper_tex/` — LaTeX sources (ACL template), including the 33-benchmark catalogue and the 462-row master table.
- `lit_search/` — search + screening scripts, `config.json` (queries, rules, curated titles), and the run directories with per-stage counts and full-text screening records.

Organising question: **which object receives credit** — the output, the trajectory, the interaction, or the belief state written before the action.

## Paper list (full-text screened, 462 papers)

Columns: paper, year, who maintains the belief, credited object, evidence level (P = peer-reviewed, A = preprint), source (K = keyword search, S1--S4 = citation-tree round). 173 papers are peer-reviewed. Entries are grouped by the survey section they support; the complete record with revision signal, metrics, and notes is `lit_search/runs/20260916_v3/manual_screen_all_v8.csv`.

### Belief representation (who maintains the belief)

| Paper | Year | Belief kept by | Credited | Ev. | Src |
|---|---|---|---|---|---|
| [Learning Dynamic Belief Graphs to Generalize on Text-Based Games](https://arxiv.org/abs/2002.09127) | 2020 | world model | state | P | S1 |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | 2020 | external memory | output | P | S1 |
| [Playing Text-Based Games with Common Sense](https://arxiv.org/abs/2012.02757) | 2020 | external memory | trajectory | A | S2 |
| [Do Language Models Have Beliefs? Methods for Detecting, Updating, and Visualizing Model Beliefs](https://arxiv.org/abs/2111.13654) | 2021 | n/a | state | A | S1 |
| [History Compression via Language Models in Reinforcement Learning](https://arxiv.org/abs/2205.12258) | 2022 | external memory | trajectory | P | S1 |
| [Teaching Models to Express Their Uncertainty in Words](https://arxiv.org/abs/2205.14334) | 2022 | written | output | P | K |
| [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221) | 2022 | written | output | A | K |
| [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | 2022 | context | none | P | S1 |
| [Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation](https://arxiv.org/abs/2302.09664) | 2023 | n/a | output | P | K |
| [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | 2023 | external memory | interaction (action) | P | K |
| [LLM+P: Empowering Large Language Models with Optimal Planning Proficiency](https://arxiv.org/abs/2304.11477) | 2023 | n/a | output | A | K |
| [MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) | 2023 | external memory | output | P | K |
| [RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text](https://arxiv.org/abs/2305.13304) | 2023 | written | output | A | K |
| [Large Language Models as Commonsense Knowledge for Large-Scale Task Planning](https://arxiv.org/abs/2305.14078) | 2023 | world model | trajectory | P | K |
| [RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322) | 2023 | external memory | none | A | S1 |
| [Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992) | 2023 | world model | trajectory | P | K |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 2023 | external memory | trajectory | P | K |
| [Minding Language Models' (Lack of) Theory of Mind: A Plug-and-Play Multi-Character Belief Tracker](https://arxiv.org/abs/2306.00924) | 2023 | ext. filter | none | P | S1 |
| [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863) | 2023 | external memory | none | P | S1 |
| [Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485) | 2023 | external memory | trajectory | P | S1 |
| [RecallM: An Adaptable Memory Mechanism with Temporal Understanding for Large Language Models](https://arxiv.org/abs/2307.02738) | 2023 | external memory | interaction (memory op) | A | S2 |
| [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) | 2023 | external memory | trajectory | P | K |
| [TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance](https://arxiv.org/abs/2309.03736) | 2023 | external memory | interaction (action) | A | K |
| [Reason for Future, Act for Now: A Principled Framework for Autonomous LLM Agents with Provable Sample Efficiency](https://arxiv.org/abs/2309.17382) | 2023 | context | none | A | S1 |
| [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) | 2023 | external memory | output | A | K |
| [Theory of Mind for Multi-Agent Collaboration via Large Language Models](https://arxiv.org/abs/2310.10701) | 2023 | written | none | P | S1 |
| [Think Twice: Perspective-Taking Improves Large Language Models' Theory-of-Mind Capabilities](https://arxiv.org/abs/2311.10227) | 2023 | context | none | P | S1 |
| [FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743) | 2023 | external memory | interaction (action) | P | K |
| [Language Models, Agent Models, and World Models: The LAW for Machine Reasoning and Planning](https://arxiv.org/abs/2312.05230) | 2023 | world model | none | A | S1 |
| [QuBE: Question-based Belief Enhancement for Agentic LLM Reasoning](https://arxiv.org/abs/10.18653/v1/2024.emnlp-main.1193) | 2024 | written | state | P | K |
| [MEMORYLLM: Towards Self-Updatable Large Language Models](https://arxiv.org/abs/2402.04624) | 2024 | prob. memory | state | P | S1 |
| [A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts](https://arxiv.org/abs/2402.09727) | 2024 | external memory | none | P | S1 |
| [A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist](https://arxiv.org/abs/2402.18485) | 2024 | external memory | interaction (action) | P | K |
| [Language Models Represent Beliefs of Self and Others](https://arxiv.org/abs/2402.18496) | 2024 | context | none | P | S2 |
| [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://arxiv.org/abs/2405.15383) | 2024 | world model | world-model loss | P | S2 |
| [Transformers represent belief state geometry in their residual stream](https://arxiv.org/abs/2405.15943) | 2024 | context | none | P | S2 |
| [From Words to Actions: Unveiling the Theoretical Underpinnings of LLM-Driven Autonomous Systems](https://arxiv.org/abs/2405.19883) | 2024 | context | none | P | S1 |
| [TimeToM: Temporal Space is the Key to Unlocking the Door of Large Language Models' Theory-of-Mind](https://arxiv.org/abs/2407.01455) | 2024 | written | none | P | S2 |
| [Perceptions to Beliefs: Exploring Precursory Inferences for Theory of Mind in Large Language Models](https://arxiv.org/abs/2407.06004) | 2024 | written | none | P | S1 |
| [FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making](https://arxiv.org/abs/2407.06567) | 2024 | external memory | state | P | K |
| [Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://arxiv.org/abs/2407.07086) | 2024 | written | state | A | K |
| [HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model](https://arxiv.org/abs/2408.09559) | 2024 | written | none | P | S1 |
| [Understanding Epistemic Language with a Language-augmented Bayesian Theory of Mind](https://arxiv.org/abs/2408.12022) | 2024 | ext. filter | none | P | S3 |
| [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) | 2024 | external memory | none | A | K |
| [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://arxiv.org/abs/2410.13232) | 2024 | world model | world-model loss | P | S1 |
| [MindForge: Empowering Embodied Agents with Theory of Mind for Lifelong Cultural Learning](https://arxiv.org/abs/2411.12977) | 2024 | written | none | P | S3 |
| A Large Language Model-Enabled Framework for Simulating Multi-Agent Cooperative Game | 2025 | ext. filter | none | P | S1 |
| [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) | 2025 | external memory | none | A | S1 |
| [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) | 2025 | external memory | output | P | K |
| [EnigmaToM: Improve LLMs' Theory-of-Mind Reasoning Capabilities with Neural Knowledge Base of Entity States](https://arxiv.org/abs/2503.03340) | 2025 | written | none | P | S3 |
| [Cognitive Memory in Large Language Models](https://arxiv.org/abs/2504.02441) | 2025 | external memory | none | A | S2 |
| [Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory](https://arxiv.org/abs/2504.07952) | 2025 | external memory | interaction (memory op) | P | S1 |
| [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) | 2025 | external memory | none | A | K |
| [Language Models use Lookbacks to Track Beliefs](https://arxiv.org/abs/2505.14685) | 2025 | context | none | A | S1 |
| [ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection](https://arxiv.org/abs/2505.15182) | 2025 | written | none | P | S1 |
| [Memory OS of AI Agent](https://arxiv.org/abs/2506.06326) | 2025 | external memory | none | P | S1 |
| [EvolvTrip: Enhancing Literary Character Understanding with Temporal Theory-of-Mind Graphs](https://arxiv.org/abs/2506.13641) | 2025 | written | none | A | S3 |
| [MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents](https://arxiv.org/abs/2506.15841) | 2025 | written | state | A | K |
| [MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent](https://arxiv.org/abs/2507.02259) | 2025 | written | state | P | K |
| [MemOS: A Memory OS for AI System](https://arxiv.org/abs/2507.03724) | 2025 | external memory | none | A | S1 |
| [PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://arxiv.org/abs/2507.04607) | 2025 | external memory | none | P | S3 |
| [CoEx - Co-evolving World-model and Exploration](https://arxiv.org/abs/2507.22281) | 2025 | world model | none | P | S1 |
| [Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736) | 2025 | external memory | trajectory | A | S2 |
| [Memento: Fine-tuning LLM Agents without Fine-tuning LLMs](https://arxiv.org/abs/2508.16153) | 2025 | external memory | interaction (action) | A | K |
| [Social World Models](https://arxiv.org/abs/2509.00559) | 2025 | written | none | A | S3 |
| [ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization](https://arxiv.org/abs/2509.13313) | 2025 | written | trajectory | A | S2 |
| [Memory in Large Language Models: Mechanisms, Evaluation and Evolution](https://arxiv.org/abs/2509.18868) | 2025 | external memory | none | A | S2 |
| [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140) | 2025 | external memory | none | A | S1 |
| [ID-RAG: Identity Retrieval-Augmented Generation for Long-Horizon Persona Coherence in Generative Agents](https://arxiv.org/abs/2509.25299) | 2025 | external memory | none | P | S2 |
| [ACON: Optimizing Context Compression for Long-horizon LLM Agents](https://arxiv.org/abs/2510.00615) | 2025 | written | none | A | S1 |
| [Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) | 2025 | world model | none | A | S2 |
| [Scaling Long-Horizon LLM Agent via Context-Folding](https://arxiv.org/abs/2510.11967) | 2025 | written | interaction (memory op) | A | S1 |
| [Next-Latent Prediction Transformers Learn Compact World Models](https://arxiv.org/abs/2511.05963) | 2025 | world model | world-model loss | A | S4 |
| [Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects](https://arxiv.org/abs/2512.12818) | 2025 | external memory | none | A | S1 |
| [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564) | 2025 | external memory | none | A | S1 |
| [R4: Retrieval-Augmented Reasoning for Vision-Language Models in 4D Spatio-Temporal Space](https://arxiv.org/abs/2512.15940) | 2025 | world model | none | A | S2 |
| [From Word to World: Can Large Language Models be Implicit Text-based World Models?](https://arxiv.org/abs/2512.18832) | 2025 | world model | world-model loss | P | S1 |
| [Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback](https://arxiv.org/abs/2512.22336) | 2025 | world model | trajectory | A | S1 |
| [The Bayesian Geometry of Transformer Attention](https://arxiv.org/abs/2512.22471) | 2025 | context | none | A | S2 |
| [Emergent World Beliefs: Exploring Transformers in Stochastic Games](https://arxiv.org/abs/2512.23722) | 2025 | world model | none | A | S1 |
| Augmenting large language models with psychologically grounded models of causal reasoning for planning under uncertainty | 2026 | ext. filter | none | P | S1 |
| Causal-Dependency State Space Prompting: bounded-memory long-horizon reasoning for streaming IT incidents | 2026 | ext. filter | state | P | S2 |
| Hindsight: Structured Agent Memory that Retains, Recalls, and Reflects | 2026 | external memory | none | P | S3 |
| PRISM: Preference-Guided Semantic Reasoning with Vision-Language Models for Object Goal Navigation | 2026 | written | none | P | S3 |
| [SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553) | 2026 | external memory | none | A | S1 |
| [Controlling Long-Horizon Behavior in Language Model Agents with Explicit State Dynamics](https://arxiv.org/abs/2601.16087) | 2026 | external memory | none | A | K |
| [Think Locally, Explain Globally: Graph-Guided LLM Investigations via Local Reasoning and Belief Propagation](https://arxiv.org/abs/2601.17915) | 2026 | ext. filter | none | A | S1 |
| [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474) | 2026 | external memory | interaction (memory op) | A | S1 |
| [From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning for Embodied Agents](https://arxiv.org/abs/2602.04326) | 2026 | written | state | A | K |
| [Graph-based Agent Memory: Taxonomy, Techniques, and Applications](https://arxiv.org/abs/2602.05665) | 2026 | external memory | none | A | S1 |
| [Self-Improving World Modelling with Latent Actions](https://arxiv.org/abs/2602.06130) | 2026 | world model | world-model loss | A | S1 |
| [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856) | 2026 | world model | world-model loss | A | S1 |
| [Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use](https://arxiv.org/abs/2602.11541) | 2026 | world model | none | A | S1 |
| [WebWorld: A Large-Scale World Model for Web Agent Training](https://arxiv.org/abs/2602.14721) | 2026 | world model | world-model loss | A | S1 |
| [Recursive Belief Vision Language Action Models](https://arxiv.org/abs/2602.20659) | 2026 | world model | state | A | K |
| [Adversarial Intent is a Latent Variable: Stateful Trust Inference for Securing Multimodal Agentic RAG](https://arxiv.org/abs/2602.21447) | 2026 | written | none | A | S2 |
| [SSMG-Nav: Enhancing Lifelong Object Navigation with Semantic Skeleton Memory Graph](https://arxiv.org/abs/2603.01813) | 2026 | external memory | none | A | S1 |
| [AutoHarness: improving LLM agents by automatically synthesizing a code harness](https://arxiv.org/abs/2603.03329) | 2026 | ext. filter | none | A | S1 |
| [Towards Multimodal Lifelong Understanding: A Dataset and Agentic Baseline](https://arxiv.org/abs/2603.05484) | 2026 | external memory | none | A | S1 |
| [Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures](https://arxiv.org/abs/2603.17244) | 2026 | external memory | none | A | S1 |
| [Graph of States: Solving Abductive Tasks with Large Language Models](https://arxiv.org/abs/2603.21250) | 2026 | external memory | none | A | K |
| [TAMTRL: Teacher-Aligned Reward Reshaping for Multi-Turn Reinforcement Learning in Long-Context Compression](https://arxiv.org/abs/2603.21663) | 2026 | written | trajectory | A | K |
| [Meta-Harness: End-to-End Optimization of Model Harnesses](https://arxiv.org/abs/2603.28052) | 2026 | external memory | interaction (memory op) | A | S1 |
| [Finding Belief Geometries with Sparse Autoencoders](https://arxiv.org/abs/2604.02685) | 2026 | context | none | A | S3 |
| [LOCARD: An Agentic Framework for Blockchain Forensics](https://arxiv.org/abs/2604.04211) | 2026 | written | none | P | S1 |
| [Toward Consistent World Models with Multi-Token Prediction and Latent Semantic Enhancement](https://arxiv.org/abs/2604.06155) | 2026 | context | world-model loss | P | S3 |
| [From Topology to Trajectory: LLM-Driven World Models For Supply Chain Resilience](https://arxiv.org/abs/2604.11041) | 2026 | world model | trajectory | A | K |
| [Bayesian Linguistic Forecaster](https://arxiv.org/abs/2604.18576) | 2026 | written | none | A | K |
| [Position: agentic AI orchestration should be Bayes-consistent](https://arxiv.org/abs/2605.00742) | 2026 | ext. filter | none | A | S1 |
| [Belief Memory (BeliefMem)](https://arxiv.org/abs/2605.05583) | 2026 | external memory | none | A | K |
| [HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution](https://arxiv.org/abs/2605.09942) | 2026 | external memory | interaction (memory op) | A | S2 |
| [Agent-BRACE](https://arxiv.org/abs/2605.11436) | 2026 | written | state | A | K |
| [CHAL: Council of Hierarchical Agentic Language](https://arxiv.org/abs/2605.12718) | 2026 | written | state | A | K |
| [Learning POMDP World Models from Observations with Language-Model Priors](https://arxiv.org/abs/2605.13740) | 2026 | world model | state | A | K |
| [GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations](https://arxiv.org/abs/2605.14498) | 2026 | external memory | none | A | K |
| [Belief Engine: Configurable and Inspectable Stance Dynamics in Multi-Agent LLM Deliberation](https://arxiv.org/abs/2605.15343) | 2026 | prob. memory | state | A | K |
| [Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP](https://arxiv.org/abs/2605.16205) | 2026 | external memory | none | A | K |
| [Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents](https://arxiv.org/abs/2605.17625) | 2026 | external memory | interaction (memory op) | A | S1 |
| [Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents](https://arxiv.org/abs/2605.17641) | 2026 | external memory | state | A | K |
| [MemGym: a Long-Horizon Memory Environment for LLM Agents](https://arxiv.org/abs/2605.20833) | 2026 | external memory | none | A | K |
| [Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents](https://arxiv.org/abs/2605.21768) | 2026 | external memory | state | A | K |
| [Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation](https://arxiv.org/abs/2605.24647) | 2026 | prob. memory | world-model loss | A | S4 |
| [PatchWorld: Gradient-Free Optimization of Executable World Models](https://arxiv.org/abs/2605.30880) | 2026 | world model | world-model loss | A | S3 |
| [Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents](https://arxiv.org/abs/2606.01886) | 2026 | external memory | none | A | K |
| [Text World Models (review)](https://arxiv.org/abs/2606.09032) | 2026 | world model | none | A | K |
| [HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning](https://arxiv.org/abs/2606.10507) | 2026 | written | trajectory | A | K |
| [ProPlay: Procedural World Models for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.12780) | 2026 | world model | trajectory | A | K |
| [Belief at Risk](https://arxiv.org/abs/2606.15473) | 2026 | ext. filter | none | A | K |
| [Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games](https://arxiv.org/abs/2606.16070) | 2026 | world model | none | A | S3 |
| [When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense](https://arxiv.org/abs/2606.22030) | 2026 | prob. memory | state | A | K |
| [Qwen-AgentWorld: Language World Models for General Agents](https://arxiv.org/abs/2606.24597) | 2026 | world model | world-model loss | A | S3 |
| [Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning](https://arxiv.org/abs/2606.27483) | 2026 | written | trajectory | A | K |
| [Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents](https://arxiv.org/abs/2606.27806) | 2026 | world model | state | A | K |
| [BayesEvolve: Explicit Belief States for Autonomous Scientific Discovery](https://arxiv.org/abs/2606.30335) | 2026 | ext. filter | state | A | K |
| [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639) | 2026 | world model | state | A | K |
| [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](https://arxiv.org/abs/2607.05511) | 2026 | external memory | none | A | S3 |
| [Auditing Belief-Conditioned LLM Agents in Hidden-Information Social Deduction Games](https://arxiv.org/abs/2607.10814) | 2026 | external memory | state | A | K |
| [Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correction for Autonomous Decision-Making](https://arxiv.org/abs/2607.17038) | 2026 | external memory | interaction (action) | A | K |
| [NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability](https://arxiv.org/abs/2607.28942) | 2026 | external memory | interaction (action) | A | K |
| [MADE: Belief-Driven Dual-Agent Coordination for Autonomous Model Deployment](https://arxiv.org/abs/2608.01189) | 2026 | external memory | interaction (action) | A | K |
| [EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.05446) | 2026 | external memory | interaction (action) | A | K |
| [Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents](https://arxiv.org/abs/2608.12476) | 2026 | external memory | none | A | K |
| [Planting a Latent Variable in Natural-Looking Text: a More Realistic Test of Belief States in LLMs and Their Link to Concept Geometry](https://arxiv.org/abs/2608.26887) | 2026 | context | none | A | S3 |
| [Belief-Based World Model](https://arxiv.org/abs/2609.00455) | 2026 | world model | none | A | K |
| [EvoSCM: Scientific Belief Revision Through Causal Model Evolution and Experimentation](https://arxiv.org/abs/2609.01526) | 2026 | written | state | A | K |
| [Belief-Calibrated Optimization: An Explicit World Model for Agentic Optimization](https://arxiv.org/abs/2609.01861) | 2026 | written | state | A | K |
| [APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering](https://arxiv.org/abs/2609.02253) | 2026 | external memory | interaction (memory op) | A | S2 |
| [CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents](https://arxiv.org/abs/2609.02265) | 2026 | world model | state | A | K |
| [Semantic Bayesian World Models](https://arxiv.org/abs/2609.03834) | 2026 | ext. filter | state | A | K |
| [Belief-State Engine](https://arxiv.org/abs/2609.10036) | 2026 | ext. filter | none | A | K |

### Belief revision and failure modes

| Paper | Year | Belief kept by | Credited | Ev. | Src |
|---|---|---|---|---|---|
| [BeliefBank: Adding Memory to a Pre-Trained Language Model for a Systematic Notion of Belief](https://arxiv.org/abs/2109.14723) | 2021 | external memory | none | P | S2 |
| [Towards Teachable Reasoning Systems: Using a Dynamic Memory of User Feedback for Continual System Improvement](https://arxiv.org/abs/2204.13074) | 2022 | external memory | none | P | S3 |
| Probabilistic coherence, logical consistency, and Bayesian learning: Neural language models as epistemic agents | 2023 | n/a | none | P | S2 |
| [Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/abs/2302.01560) | 2023 | context | trajectory | P | K |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023 | external memory | trajectory | P | K |
| [Language Models can Solve Computer Tasks](https://arxiv.org/abs/2303.17491) | 2023 | context | interaction (action) | P | K |
| [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | 2023 | context | output | P | K |
| [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128) | 2023 | context | output | P | K |
| [MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions](https://arxiv.org/abs/2305.14795) | 2023 | external memory | none | P | S1 |
| [ProAgent: Building Proactive Cooperative Agents with Large Language Models](https://arxiv.org/abs/2308.11339) | 2023 | written | none | P | S1 |
| [Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models](https://arxiv.org/abs/2310.04406) | 2023 | external memory | trajectory | P | K |
| [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) | 2023 | context | output | P | S1 |
| [On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks](https://arxiv.org/abs/2402.08115) | 2024 | context | none | P | S4 |
| [Reflect-RL: Two-Player Online RL Fine-Tuning for LMs](https://arxiv.org/abs/2402.12621) | 2024 | written | interaction (action) | P | K |
| [Are language models rational? The case of coherence norms and belief revision](https://arxiv.org/abs/2406.03442) | 2024 | n/a | none | A | S2 |
| [Fundamental Problems With Model Editing: How Should Rational Belief Revision Work in LLMs?](https://arxiv.org/abs/2406.19354) | 2024 | n/a | none | P | S1 |
| [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.07199) | 2024 | external memory | trajectory | A | K |
| [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://arxiv.org/abs/2501.01702) | 2025 | context | trajectory | P | K |
| [Large Language Models as Theory of Mind Aware Generative Agents with Counterfactual Reflection](https://arxiv.org/abs/2501.15355) | 2025 | written | none | A | S4 |
| [WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation](https://arxiv.org/abs/2503.02247) | 2025 | world model | none | P | S2 |
| [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120) | 2025 | context | none | A | S1 |
| [How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior](https://arxiv.org/abs/2505.16067) | 2025 | external memory | interaction (memory op) | P | S1 |
| [When Two LLMs Debate, Both Think They'll Win](https://arxiv.org/abs/2505.19184) | 2025 | context | none | A | S1 |
| [Measuring Sycophancy of Language Models in Multi-turn Dialogues](https://arxiv.org/abs/2505.23840) | 2025 | context | none | P | S3 |
| [Overcoming Multi-step Complexity in Multimodal Theory-of-Mind Reasoning: A Scalable Bayesian Planner](https://arxiv.org/abs/2506.01301) | 2025 | ext. filter | output | P | S3 |
| [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/abs/2507.05257) | 2025 | n/a | none | A | K |
| [Are LLM Belief Updates Consistent with Bayes' Theorem?](https://arxiv.org/abs/2507.17951) | 2025 | context | none | P | S1 |
| [Sycophancy under Pressure: Evaluating and Mitigating Sycophantic Bias via Adversarial Dialogues in Scientific QA](https://arxiv.org/abs/2508.13743) | 2025 | context | output | A | S3 |
| [BASIL: Bayesian Assessment of Sycophancy in LLMs](https://arxiv.org/abs/2508.16846) | 2025 | context | output | P | S2 |
| [Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?](https://arxiv.org/abs/2508.17536) | 2025 | context | output | P | S1 |
| [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) | 2025 | written | none | A | S1 |
| [Active Confusion Expression in Large Language Models: Leveraging World Models toward Better Social Reasoning](https://arxiv.org/abs/2510.07974) | 2025 | written | output | A | S3 |
| [Accumulating Context Changes the Beliefs of Language Models](https://arxiv.org/abs/2511.01805) | 2025 | context | none | A | S1 |
| [Large Language Models as Discounted Bayesian Filters](https://arxiv.org/abs/2512.18489) | 2025 | context | none | A | S1 |
| ReflectiChain: Mitigating Semantic-Execution Drift in Long-Horizon LLM Agents via Retrospective Reflection and Double-Loop Policy Adaptation | 2026 | world model | none | P | S1 |
| [HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents](https://arxiv.org/abs/2601.06377) | 2026 | external memory | none | A | S3 |
| [Debugging code world models](https://arxiv.org/abs/2602.07672) | 2026 | world model | world-model loss | A | S1 |
| [DenoiseFlow: Uncertainty-Aware Denoising for Reliable LLM Agentic Workflows](https://arxiv.org/abs/2603.00532) | 2026 | context | trajectory | A | K |
| [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488) | 2026 | context | output | A | S1 |
| [D-MEM](https://arxiv.org/abs/2603.14597) | 2026 | external memory | none | A | K |
| [Dynamic Theory of Mind as a Temporal Memory Problem: Evidence from Large Language Models](https://arxiv.org/abs/2603.14646) | 2026 | context | none | A | K |
| [RPMS: Enhancing LLM-Based Embodied Planning through Rule-Augmented Memory Synergy](https://arxiv.org/abs/2603.17831) | 2026 | written | none | A | S1 |
| [BeliefShift](https://arxiv.org/abs/2603.23848) | 2026 | n/a | none | A | K |
| [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](https://arxiv.org/abs/2604.01212) | 2026 | written | none | A | K |
| [DeltaLogic: Minimal Premise Edits Reveal Belief-Revision Failures in Logical Reasoning Models](https://arxiv.org/abs/2604.02733) | 2026 | context | output | A | K |
| [Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing](https://arxiv.org/abs/2604.08401) | 2026 | context | state | A | K |
| [MEDLEY-BENCH: Benchmarking Behavioural Metacognition and Belief Revision Under Social Pressure in Large Language Models](https://arxiv.org/abs/2604.16009) | 2026 | context | none | A | K |
| [AI scientists produce results without reasoning scientifically](https://arxiv.org/abs/2604.18805) | 2026 | context | none | A | S1 |
| [Complete Cyclic Subtask Graphs for Tool-Using LLM Agents: Flexibility, Cost, and Bottlenecks in Long-Horizon Workflows](https://arxiv.org/abs/2604.22820) | 2026 | written | none | A | K |
| [T²PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.02178) | 2026 | context | interaction (action) | A | K |
| [STALE](https://arxiv.org/abs/2605.06527) | 2026 | external memory | none | A | K |
| [EquiMem: Calibrating Shared Memory in Multi-Agent Debate via Game-Theoretic Equilibrium](https://arxiv.org/abs/2605.09278) | 2026 | external memory | none | A | S2 |
| [Why We Need World Models for AGI: Where LLMs Fail and How World Models May Outperform](https://arxiv.org/abs/2605.23972) | 2026 | context | none | A | K |
| [OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling](https://arxiv.org/abs/2605.26322) | 2026 | n/a | none | A | K |
| [Representation Signatures and Risk-Feedback Alignment in LLM Trading Agents](https://arxiv.org/abs/2605.28850) | 2026 | context | output | A | K |
| [Contextual Belief Management (BeliefTrack)](https://arxiv.org/abs/2605.30219) | 2026 | written | state | A | K |
| [Trivium: Temporal Regret as a First-Class Objective for Causal-Memory Controllers](https://arxiv.org/abs/2606.04421) | 2026 | world model | world-model loss | P | S2 |
| [TOKI](https://arxiv.org/abs/2606.06240) | 2026 | external memory | none | A | K |
| [Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models](https://arxiv.org/abs/2606.10949) | 2026 | external memory | none | A | S2 |
| [Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge](https://arxiv.org/abs/2606.26511) | 2026 | external memory | none | A | S1 |
| [Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents](https://arxiv.org/abs/2606.26806) | 2026 | external memory | interaction (memory op) | A | S2 |
| [Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information Asymmetry](https://arxiv.org/abs/2607.01661) | 2026 | context | none | A | S2 |
| [Repair the Amplifier, Not the Symptom: Stable World-Model Correction for Agent Rollouts](https://arxiv.org/abs/2607.01767) | 2026 | world model | trajectory | A | K |
| [TRACE: An Operational Reasoning Schema for Auditable Agentic Commitments](https://arxiv.org/abs/2607.12480) | 2026 | written | none | A | S1 |
| [MemOps](https://arxiv.org/abs/2607.12893) | 2026 | external memory | none | A | K |
| [STOCKTAKE](https://arxiv.org/abs/2607.13618) | 2026 | n/a | none | A | K |
| [When Memory Updates but Behavior Does Not](https://arxiv.org/abs/2608.01619) | 2026 | external memory | none | A | K |
| [Mitigating Over-Personalization in LLMs via Structured Memory](https://arxiv.org/abs/2608.08300) | 2026 | external memory | none | A | S2 |
| [When Stale Constraints Go Unchecked](https://arxiv.org/abs/2608.25553) | 2026 | external memory | none | A | K |
| [Long-Horizon State Tracking in LLMs: Executing MD5 through a Deep Sequence of Dependent Tool Calls](https://arxiv.org/abs/2609.00012) | 2026 | context | none | A | K |
| [UQ for LLM Agents taxonomy](https://arxiv.org/abs/2609.07395) | 2026 | n/a | none | A | K |

### Learning signals by credited object

| Paper | Year | Belief kept by | Credited | Ev. | Src |
|---|---|---|---|---|---|
| [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332) | 2021 | context | trajectory | A | S1 |
| [Offline RL for Natural Language Generation with Implicit Language Q Learning](https://arxiv.org/abs/2206.11871) | 2022 | context | trajectory | P | S1 |
| [Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610) | 2022 | n/a | output | P | K |
| [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) | 2023 | n/a | output | P | S1 |
| [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | 2023 | n/a | output | P | S1 |
| [FireAct: Toward Language Agent Fine-tuning](https://arxiv.org/abs/2310.05915) | 2023 | context | trajectory | A | K |
| [AgentTuning: Enabling Generalized Agent Abilities for LLMs](https://arxiv.org/abs/2310.12823) | 2023 | context | trajectory | P | K |
| [Large Language Models as Generalizable Policies for Embodied Tasks](https://arxiv.org/abs/2310.17722) | 2023 | context | trajectory | P | S1 |
| [Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations](https://arxiv.org/abs/2312.08935) | 2023 | n/a | output | P | S1 |
| Reinforcing LLM Agents via Policy Optimization with Action Decomposition | 2024 | context | interaction (action) | P | S1 |
| [ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL](https://arxiv.org/abs/2402.19446) | 2024 | n/a | interaction (action) | P | K |
| [SOTOPIA-pi: Interactive Learning of Socially Intelligent Language Agents](https://arxiv.org/abs/2403.08715) | 2024 | n/a | output | A | K |
| [Agent-FLAN: Designing Data and Methods of Effective Agent Tuning for Large Language Models](https://arxiv.org/abs/2403.12881) | 2024 | context | trajectory | P | S1 |
| [From $r$ to $Q^*$: Your Language Model is Secretly a Q-Function](https://arxiv.org/abs/2404.12358) | 2024 | n/a | output | A | S1 |
| [AgentGym: Evolving Large Language Model-based Agents across Diverse Environments](https://arxiv.org/abs/2406.04151) | 2024 | context | trajectory | A | K |
| [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://arxiv.org/abs/2406.11896) | 2024 | context | interaction (action) | P | S1 |
| [Training Language Models to Self-Correct via Reinforcement Learning](https://arxiv.org/abs/2409.12917) | 2024 | context | interaction (action) | P | S1 |
| [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://arxiv.org/abs/2410.14803) | 2024 | context | trajectory | P | S1 |
| [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337) | 2024 | n/a | output | P | K |
| [CollabLLM: From Passive Responders to Active Collaborators](https://arxiv.org/abs/2502.00640) | 2025 | context | interaction (action) | P | S2 |
| [Reinforcement Learning for Long-Horizon Interactive LLM Agents](https://arxiv.org/abs/2502.01600) | 2025 | context | trajectory | A | K |
| [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/abs/2503.09516) | 2025 | context | output | A | K |
| [SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks](https://arxiv.org/abs/2503.15478) | 2025 | n/a | interaction (action) | A | K |
| [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](https://arxiv.org/abs/2503.19470) | 2025 | context | output | P | K |
| [ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536) | 2025 | context | trajectory | A | S1 |
| [ToolRL: Reward is All Tool Learning Needs](https://arxiv.org/abs/2504.13958) | 2025 | context | output | P | S1 |
| [RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2504.20073) | 2025 | context | trajectory | A | K |
| [ZeroSearch: Incentivize the Search Capability of LLMs without Searching](https://arxiv.org/abs/2505.04588) | 2025 | context | trajectory | A | S1 |
| [Group-in-Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2505.10978) | 2025 | n/a | trajectory | P | K |
| [Reinforcing Multi-Turn Reasoning in LLM Agents via Fine-Grained Reward Structure and Credit Assignment](https://arxiv.org/abs/2505.11821) | 2025 | context | interaction (action) | A | S1 |
| [RLVR-World: Training World Models with Reinforcement Learning](https://arxiv.org/abs/2505.13934) | 2025 | world model | world-model loss | P | S2 |
| [Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning](https://arxiv.org/abs/2505.14069) | 2025 | context | interaction (action) | P | S2 |
| [StepSearch: Igniting LLMs Search Ability via Step-Wise Proximal Policy Optimization](https://arxiv.org/abs/2505.15107) | 2025 | context | interaction (action) | P | S1 |
| [An Empirical Study on Reinforcement Learning for Reasoning-Search Interleaved LLM Agents](https://arxiv.org/abs/2505.15117) | 2025 | context | trajectory | A | S1 |
| [ARPO:End-to-End Policy Optimization for GUI Agents with Experience Replay](https://arxiv.org/abs/2505.16282) | 2025 | context | trajectory | A | S2 |
| [WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2505.16421) | 2025 | context | trajectory | P | S1 |
| [DEL-ToM: Inference-Time Scaling for Theory-of-Mind Reasoning via Dynamic Epistemic Logic](https://arxiv.org/abs/2505.17348) | 2025 | written | state | P | S3 |
| [Beyond Markovian: Reflective Exploration via Bayes-Adaptive RL for LLM Reasoning](https://arxiv.org/abs/2505.20561) | 2025 | context | trajectory | A | S3 |
| [SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution](https://arxiv.org/abs/2505.20732) | 2025 | n/a | interaction (action) | A | S1 |
| [Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents](https://arxiv.org/abs/2506.00320) | 2025 | world model | world-model loss | A | S1 |
| [Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interaction](https://arxiv.org/abs/2506.07976) | 2025 | context | trajectory | A | K |
| [From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium](https://arxiv.org/abs/2506.08292) | 2025 | ext. filter | trajectory | P | S1 |
| [Agentic Reinforced Policy Optimization](https://arxiv.org/abs/2507.19849) | 2025 | context | trajectory | A | K |
| [Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://arxiv.org/abs/2508.03680) | 2025 | context | interaction (action) | A | S1 |
| [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828) | 2025 | external memory | interaction (memory op) | P | S1 |
| [Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents](https://arxiv.org/abs/2509.09265) | 2025 | context | interaction (action) | A | S1 |
| [Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents](https://arxiv.org/abs/2509.14480) | 2025 | context | interaction (action) | A | S1 |
| [Agentic Reinforcement Learning with Implicit Step Rewards](https://arxiv.org/abs/2509.19199) | 2025 | context | interaction (action) | A | S1 |
| [GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks](https://arxiv.org/abs/2509.23738) | 2025 | n/a | interaction (action) | A | S3 |
| [Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks](https://arxiv.org/abs/2509.25598) | 2025 | context | trajectory | A | S2 |
| [Multi-Agent Tool-Integrated Policy Optimization](https://arxiv.org/abs/2510.04678) | 2025 | n/a | trajectory | A | S3 |
| [In-the-Flow Agentic System Optimization for Effective Planning and Tool Use](https://arxiv.org/abs/2510.05592) | 2025 | external memory | trajectory | P | S2 |
| [Demystifying Reinforcement Learning in Agentic Reasoning](https://arxiv.org/abs/2510.11701) | 2025 | context | trajectory | A | S2 |
| [T3: Reducing Belief Deviation in Reinforcement Learning for Active Reasoning](https://arxiv.org/abs/2510.12264) | 2025 | prob. memory | trajectory | P | S1 |
| [Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn Search Agents](https://arxiv.org/abs/2510.14967) | 2025 | context | interaction (action) | A | S1 |
| [Why Do LLM Agents Fail in Exploring New Environments? A World-Modeling Perspective](https://arxiv.org/abs/2510.15047) | 2025 | world model | world-model loss | A | S1 |
| [MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs](https://arxiv.org/abs/2510.15414) | 2025 | n/a | interaction (action) | A | S3 |
| [VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents](https://arxiv.org/abs/2510.16907) | 2025 | written | state | A | S1 |
| [SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph](https://arxiv.org/abs/2510.20022) | 2025 | n/a | interaction (action) | P | S1 |
| [DeepAgent: A General Reasoning Agent with Scalable Toolsets](https://arxiv.org/abs/2510.21618) | 2025 | external memory | interaction (action) | P | S1 |
| [AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress](https://arxiv.org/abs/2511.08325) | 2025 | context | interaction (action) | P | S1 |
| [CriticSearch: Fine-Grained Credit Assignment for Search Agents via a Retrospective Critic](https://arxiv.org/abs/2511.12159) | 2025 | n/a | interaction (action) | P | S1 |
| [Agent-R1: A Unified and Modular Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2511.14460) | 2025 | context | trajectory | A | K |
| [Stabilizing Off-Policy Training for Long-Horizon LLM Agent via Turn-Level Importance Sampling and Clipping-Triggered Normalization](https://arxiv.org/abs/2511.20718) | 2025 | context | interaction (action) | A | S1 |
| [MindPower: Enabling Theory-of-Mind Reasoning in VLM-based Embodied Agents](https://arxiv.org/abs/2511.23055) | 2025 | written | output | P | S3 |
| [STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models](https://arxiv.org/abs/2512.05107) | 2025 | n/a | interaction (action) | A | S1 |
| [GTR-Turbo: Merged Checkpoint is Secretly a Free Teacher for Agentic VLM Training](https://arxiv.org/abs/2512.13043) | 2025 | n/a | trajectory | A | S1 |
| [Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs](https://arxiv.org/abs/2512.17008) | 2025 | context | interaction (action) | P | S1 |
| [GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators](https://arxiv.org/abs/2512.19682) | 2025 | world model | trajectory | A | S1 |
| [Memento 2: Learning by Stateful Reflective Memory](https://arxiv.org/abs/2512.22716) | 2025 | external memory | interaction (memory op) | A | S1 |
| SHADOW: Dynamic-Aware Credit Assignment Against Long-Horizon Tasks | 2026 | context | interaction (action) | P | S1 |
| [Infusing Theory of Mind into Socially Intelligent LLM Agents](https://arxiv.org/abs/2509.22887) | 2026 | written | state | P | S4 |
| [Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885) | 2026 | external memory | interaction (memory op) | P | S1 |
| [SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models](https://arxiv.org/abs/2601.03555) | 2026 | context | interaction (action) | A | S1 |
| [Collaborative Multi-Agent Test-Time Reinforcement Learning for Reasoning](https://arxiv.org/abs/2601.09667) | 2026 | external memory | interaction (action) | A | K |
| [SuS: Strategy-aware Surprise for Intrinsic Exploration](https://arxiv.org/abs/2601.10349) | 2026 | context | output | A | K |
| [MatchTIR: Fine-Grained Supervision for Tool-Integrated Reasoning via Bipartite Matching](https://arxiv.org/abs/2601.10712) | 2026 | context | interaction (action) | P | S1 |
| [Reinforcement Learning via Self-Distillation](https://arxiv.org/abs/2601.20802) | 2026 | context | output | A | S1 |
| [World Models as an Intermediary between Agents and the Real World](https://arxiv.org/abs/2602.00785) | 2026 | world model | world-model loss | A | S4 |
| [BranPO: Scalable Contrastive Branch Sampling for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2602.03719) | 2026 | n/a | interaction (action) | A | S1 |
| [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](https://arxiv.org/abs/2602.08234) | 2026 | external memory | trajectory | A | S1 |
| [Learning from the Irrecoverable: Error-Localized Policy Optimization for Tool-Integrated LLM Reasoning](https://arxiv.org/abs/2602.09598) | 2026 | n/a | interaction (action) | P | S3 |
| [HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents](https://arxiv.org/abs/2602.16165) | 2026 | context | trajectory | A | K |
| [Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2602.22817) | 2026 | n/a | interaction (action) | A | S1 |
| [SE-Search: Self-Evolving Search Agent via Memory and Dense Reward](https://arxiv.org/abs/2603.03293) | 2026 | external memory | interaction (memory op) | A | S2 |
| [HumanLM: Simulating Users with State Alignment Beats Response Imitation](https://arxiv.org/abs/2603.03303) | 2026 | written | state | A | S1 |
| [EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection](https://arxiv.org/abs/2603.04900) | 2026 | context | interaction (action) | P | S2 |
| [MICA: Multi-granularity Intertemporal Credit Assignment for Long-Horizon Emotional Support Dialogue](https://arxiv.org/abs/2603.06194) | 2026 | external memory | interaction (action) | A | K |
| [Hindsight Credit Assignment for Long-Horizon LLM Agents](https://arxiv.org/abs/2603.08754) | 2026 | context | trajectory | A | K |
| [Joint Optimization of Multi-agent Memory System](https://arxiv.org/abs/2603.12631) | 2026 | external memory | interaction (memory op) | A | S2 |
| [SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training](https://arxiv.org/abs/2603.18079) | 2026 | external memory | trajectory | A | K |
| [HISR: Hindsight Information Modulated Segmental Process Rewards For Multi-turn Agentic Reinforcement Learning](https://arxiv.org/abs/2603.18683) | 2026 | context | interaction (action) | A | S1 |
| [Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe](https://arxiv.org/abs/2603.21972) | 2026 | context | trajectory | A | S1 |
| [TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs](https://arxiv.org/abs/2603.22293) | 2026 | context | interaction (action) | A | K |
| [Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration](https://arxiv.org/abs/2604.02869) | 2026 | context | interaction (action) | A | K |
| [Co-Evolution of Policy and Internal Reward for Language Agents](https://arxiv.org/abs/2604.03098) | 2026 | written | trajectory | A | K |
| [OASES: Outcome-Aligned Search-Evaluation Co-Training for Agentic Search](https://arxiv.org/abs/2604.03675) | 2026 | context | state | A | S2 |
| [UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization](https://arxiv.org/abs/2604.13822) | 2026 | external memory | interaction (action) | P | S3 |
| [CAPO: Critic-Guided Action-Aligned Policy Optimization for Advancing LLM Agent Capabilities](https://arxiv.org/abs/2604.18401) | 2026 | context | interaction (action) | A | K |
| [AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.00425) | 2026 | context | trajectory | A | K |
| [BOND (distilling Bayesian beliefs)](https://arxiv.org/abs/2605.04507) | 2026 | written | state | A | K |
| [Tree-based Credit Assignment for Multi-Agent Memory System](https://arxiv.org/abs/2605.04811) | 2026 | external memory | interaction (memory op) | A | S2 |
| [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/abs/2605.06614) | 2026 | external memory | interaction (memory op) | A | S1 |
| [Not All Turns Matter: Credit Assignment for Multi-Turn Jailbreaking](https://arxiv.org/abs/2605.08778) | 2026 | context | interaction (action) | A | K |
| [PiCA: Pivot-Based Credit Assignment for Search Agentic Reinforcement Learning](https://arxiv.org/abs/2605.09287) | 2026 | context | trajectory | A | K |
| [CAVE: A Structured Credit Assignment Approach for Fragmented Visual Evidence Reasoning](https://arxiv.org/abs/2605.16416) | 2026 | context | interaction (action) | A | S1 |
| [What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents](https://arxiv.org/abs/2605.19447) | 2026 | context | interaction (action) | A | K |
| [SKILLC: Learning Autonomous Skill Internalization in LLM Agents via Contrastive Credit Assignment](https://arxiv.org/abs/2605.27899) | 2026 | context | trajectory | A | K |
| [SPADER: Step-wise Peer Advantage with Diversity-Aware Exploration Rewards for Multi-Answer Question Answering](https://arxiv.org/abs/2606.00593) | 2026 | context | interaction (action) | A | S2 |
| [ECPO](https://arxiv.org/abs/2606.05885) | 2026 | n/a | trajectory | A | K |
| [Self-evolving LLM agents with in-distribution Optimization](https://arxiv.org/abs/2606.07367) | 2026 | context | trajectory | A | K |
| [APPO: Agentic Procedural Policy Optimization](https://arxiv.org/abs/2606.12384) | 2026 | n/a | output | A | S1 |
| [Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2606.12634) | 2026 | n/a | output | A | S1 |
| [Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2606.22995) | 2026 | context | trajectory | A | K |
| [Agent Reinforcement Learning via Pivotal-Aware Self-Feedback Retry](https://arxiv.org/abs/2607.03702) | 2026 | context | interaction (action) | A | S1 |
| [Bridging Interleaved Multi-Modal Reasoning as a Unified Decision Process](https://arxiv.org/abs/2607.03748) | 2026 | n/a | interaction (action) | A | S1 |
| [STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2607.04963) | 2026 | context | trajectory | A | K |
| [ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.15660) | 2026 | context | interaction (action) | A | S1 |
| [Masked Diffusion Language Models are Strong and Steerable Text-Based World Models for Agentic RL](https://arxiv.org/abs/2607.16204) | 2026 | world model | world-model loss | A | S1 |
| [From Memory to Skills: Evidence-Grounded Co-Evolution Governance for Long-Horizon LLM Agents](https://arxiv.org/abs/2607.16621) | 2026 | external memory | trajectory | A | S3 |
| [TCPO: Turn-Level Credit Policy Optimization](https://arxiv.org/abs/2608.01667) | 2026 | context | interaction (action) | A | K |
| [Verifiable Memory: Learning Unified Memory Management with Local and Global Verifiers for Large Language Model Agents](https://arxiv.org/abs/2608.03137) | 2026 | external memory | interaction (memory op) | A | S3 |
| [Teach the Magnitude, Not the Direction: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents](https://arxiv.org/abs/2608.13179) | 2026 | context | interaction (action) | A | K |
| [RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training](https://arxiv.org/abs/2608.18682) | 2026 | n/a | interaction (action) | A | S3 |
| [HiDiffTIR: Hierarchical Difficulty-Aware Policy Optimization for Multi-Turn Tool-Integrated Reasoning](https://arxiv.org/abs/2608.21863) | 2026 | context | interaction (action) | A | K |
| [IAPO: Influence-Aware Policy Optimization for Credit Assignment in Multi-Turn Service Agents](https://arxiv.org/abs/2608.24588) | 2026 | context | interaction (action) | A | K |
| [VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning](https://arxiv.org/abs/2608.28128) | 2026 | n/a | interaction (action) | A | K |
| [ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL](https://arxiv.org/abs/2608.28476) | 2026 | context | interaction (memory op) | P | S3 |
| [Hindsight Memory-PRM: Supervising Memory Management with Auditable Hindsight Credit](https://arxiv.org/abs/2608.29605) | 2026 | external memory | interaction (memory op) | A | S2 |
| [Explore More Drift Less](https://arxiv.org/abs/2609.01245) | 2026 | n/a | output | A | K |
| [PGPO: Potential-Guided Policy Optimization for Multi-Turn Agentic Tasks](https://arxiv.org/abs/2609.02236) | 2026 | context | interaction (action) | A | K |
| [Mind2Dialogue: Training Human-Aware Language Models by Simulating User Mental States](https://arxiv.org/abs/2609.15972) | 2026 | written | output | A | S3 |

### Belief-guided evidence acquisition

| Paper | Year | Belief kept by | Credited | Ev. | Src |
|---|---|---|---|---|---|
| [Do Embodied Agents Dream of Pixelated Sheep?: Embodied Decision Making using Language Guided World Modelling](https://arxiv.org/abs/2301.12050) | 2023 | world model | world-model loss | P | S1 |
| [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511) | 2023 | context | output | P | S1 |
| [Preemptive Detection and Correction of Misaligned Actions in LLM Agents](https://arxiv.org/abs/2407.11843) | 2024 | written | interaction (action) | P | S1 |
| Ask and Retrieve Knowledge: Towards Proactive Asking with Imperfect Information in Medical Multi-turn Dialogues | 2025 | context | trajectory | P | S2 |
| [R1-Searcher: Incentivizing the Search Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2503.05592) | 2025 | context | trajectory | A | S1 |
| [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://arxiv.org/abs/2504.03160) | 2025 | context | trajectory | P | S1 |
| [Do Large Language Models Have a Planning Theory of Mind? Evidence from MindGames: a Multi-Step Persuasion Task](https://arxiv.org/abs/2507.16196) | 2025 | n/a | none | P | S3 |
| [Language and Experience: A Computational Model of Social Learning in Complex Tasks](https://arxiv.org/abs/2509.00074) | 2025 | world model | none | A | S3 |
| [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/abs/2510.11892) | 2025 | world model | none | A | S1 |
| [Align While Search: Belief-Guided Exploratory Inference for World-Grounded Embodied Agents](https://arxiv.org/abs/2512.24461) | 2025 | ext. filter | none | A | S2 |
| [Bayesian Orchestration of Multi-LLM Agents for Cost-Aware Sequential Decision-Making](https://arxiv.org/abs/2601.01522) | 2026 | ext. filter | state | A | S2 |
| [Current Agents Fail to Leverage World Model as Tool for Foresight](https://arxiv.org/abs/2601.03905) | 2026 | world model | none | P | S1 |
| [Can We Predict Before Executing Machine Learning Agents?](https://arxiv.org/abs/2601.05930) | 2026 | world model | none | P | S1 |
| [InfoPO: Information-Driven Policy Optimization for User-Centric Agents](https://arxiv.org/abs/2603.00656) | 2026 | context | interaction (action) | A | S1 |
| [Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent LLM Systems](https://arxiv.org/abs/2603.13256) | 2026 | prob. memory | interaction (action) | A | K |
| [RetailBench: Evaluating Long-Horizon Autonomous Decision-Making and Strategy Stability of LLM Agents in Realistic Retail Environments](https://arxiv.org/abs/2603.16453) | 2026 | context | none | A | K |
| [Can LLM Agents Be CFOs? Benchmarking Long-Horizon Resource Allocation in an Uncertain Enterprise Environment](https://arxiv.org/abs/2603.23638) | 2026 | context | none | A | K |
| [Oblivion: Self-Adaptive Agentic Memory Control through Decay-Driven Activation](https://arxiv.org/abs/2604.00131) | 2026 | external memory | interaction (memory op) | A | S2 |
| [Context Gathering Decision Process](https://arxiv.org/abs/2605.07042) | 2026 | ext. filter | none | A | K |
| [MedExAgent: Training LLM Agents to Ask, Examine, and Diagnose in Noisy Clinical Environments](https://arxiv.org/abs/2605.07058) | 2026 | context | output | A | K |
| [Clarify, Abstain or Answer? Strategising in Conversation with Belief-Augmented Generation](https://arxiv.org/abs/2605.25831) | 2026 | context | none | P | S2 |
| [CA-BED: Conversation-Aware Bayesian Experimental Design](https://arxiv.org/abs/2606.01182) | 2026 | prob. memory | none | A | S3 |
| [Bayesian-Agent](https://arxiv.org/abs/2606.08348) | 2026 | ext. filter | none | A | K |
| [Adaptive AI Delegation under Uncertainty: A Bayesian Governance Policy for Sequential Decision Authority](https://arxiv.org/abs/2606.29406) | 2026 | ext. filter | none | A | K |
| [KbSD: Knowledge Boundary aware Self-Distillation for Behavioral Calibration in Agentic Search](https://arxiv.org/abs/2606.29863) | 2026 | context | output | A | S2 |
| [EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.06197) | 2026 | world model | trajectory | A | S4 |
| [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](https://arxiv.org/abs/2608.16185) | 2026 | prob. memory | none | A | S2 |

### Evaluation and benchmarks

| Paper | Year | Belief kept by | Credited | Ev. | Src |
|---|---|---|---|---|---|
| [ALFWorld: Aligning Text and Embodied Environments for Interactive Learning](https://arxiv.org/abs/2010.03768) | 2020 | n/a | output | P | K |
| [PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change](https://arxiv.org/abs/2206.10498) | 2022 | n/a | output | P | K |
| [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206) | 2022 | context | none | P | S1 |
| [Clever Hans or Neural Theory of Mind? Stress Testing Social Reasoning in Large Language Models](https://arxiv.org/abs/2305.14763) | 2023 | context | none | P | S1 |
| [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) | 2023 | context | none | P | S1 |
| [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) | 2023 | n/a | output | P | K |
| [SmartPlay: A Benchmark for LLMs as Intelligent Agents](https://arxiv.org/abs/2310.01557) | 2023 | n/a | output | P | K |
| [FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions](https://arxiv.org/abs/2310.15421) | 2023 | context | none | P | S1 |
| [HI-TOM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in Large Language Models](https://arxiv.org/abs/2310.16755) | 2023 | context | none | P | S1 |
| [MMToM-QA: Multimodal Theory of Mind Question Answering](https://arxiv.org/abs/2401.08743) | 2024 | prob. memory | none | P | S2 |
| [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649) | 2024 | n/a | output | P | K |
| [Deal, or no deal (or who knows)? Forecasting Uncertainty in Conversations using Large Language Models](https://arxiv.org/abs/2402.03284) | 2024 | context | output | P | S3 |
| [ToMBench: Benchmarking Theory of Mind in Large Language Models](https://arxiv.org/abs/2402.15052) | 2024 | n/a | none | P | S1 |
| [Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753) | 2024 | n/a | output | P | K |
| [Views Are My Own, But Also Yours: Benchmarking Theory of Mind using Common Ground](https://arxiv.org/abs/2403.02451) | 2024 | written | none | P | S2 |
| [NegotiationToM: A Benchmark for Stress-testing Machine Theory of Mind on Negotiation Surrounding](https://arxiv.org/abs/2404.13627) | 2024 | n/a | none | P | S2 |
| [tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) | 2024 | n/a | none | A | K |
| [Belief Revision: The Adaptability of Large Language Models Reasoning](https://arxiv.org/abs/2406.19764) | 2024 | context | none | P | S1 |
| [AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901) | 2024 | context | none | P | S1 |
| [MuMA-ToM: Multi-modal Multi-Agent Theory of Mind](https://arxiv.org/abs/2408.12574) | 2024 | world model | none | P | S1 |
| [MemSim: A Bayesian Simulator for Evaluating Memory of LLM-based Personal Assistants](https://arxiv.org/abs/2409.20163) | 2024 | external memory | none | P | S2 |
| [Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making](https://arxiv.org/abs/2410.07166) | 2024 | world model | none | P | S1 |
| [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813) | 2024 | external memory | none | P | S1 |
| [SimpleToM: Exposing the Gap between Explicit ToM Inference and Implicit ToM Application in LLMs](https://arxiv.org/abs/2410.13648) | 2024 | n/a | none | P | S3 |
| [ToMATO: Verbalizing the Mental States of Role-Playing LLMs for Benchmarking Theory of Mind](https://arxiv.org/abs/2501.08838) | 2025 | context | none | P | S1 |
| [Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://arxiv.org/abs/2502.09597) | 2025 | context | none | P | S1 |
| [Text2World: Benchmarking Large Language Models for Symbolic World Model Generation](https://arxiv.org/abs/2502.13092) | 2025 | world model | output | P | S2 |
| [Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](https://arxiv.org/abs/2502.15840) | 2025 | external memory | none | A | S1 |
| [PersuasiveToM: A Benchmark for Evaluating Machine Theory of Mind in Persuasive Dialogues](https://arxiv.org/abs/2502.21017) | 2025 | n/a | none | A | S3 |
| [LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners](https://arxiv.org/abs/2505.11942) | 2025 | external memory | none | A | S1 |
| [DIAMONDs: A Dataset for Dynamic Information And Mental modeling Of Numeric Discussions](https://arxiv.org/abs/2505.12651) | 2025 | n/a | none | A | S3 |
| [tau2-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982) | 2025 | n/a | none | A | K |
| [MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents](https://arxiv.org/abs/2506.21605) | 2025 | external memory | none | P | S1 |
| [SoMi-ToM: Evaluating Multi-Perspective Theory of Mind in Embodied Social Interactions](https://arxiv.org/abs/2506.23046) | 2025 | context | none | P | S3 |
| [UltraHorizon: Benchmarking Agent Capabilities in Ultra Long-Horizon Scenarios](https://arxiv.org/abs/2509.21766) | 2025 | context | none | A | S1 |
| [Do Language Models Update their Forecasts with New Information?](https://arxiv.org/abs/2509.23936) | 2025 | context | none | A | S1 |
| [MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems](https://arxiv.org/abs/2510.17281) | 2025 | external memory | none | A | S1 |
| [HaluMem: Evaluating Hallucinations in Memory Systems of Agents](https://arxiv.org/abs/2511.03506) | 2025 | external memory | none | A | S1 |
| [Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory](https://arxiv.org/abs/2511.20857) | 2025 | external memory | none | A | S1 |
| [ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction](https://arxiv.org/abs/2511.20937) | 2025 | world model | none | A | S1 |
| [RecToM: A Benchmark for Evaluating Machine Theory of Mind in LLM-based Conversational Recommender Systems](https://arxiv.org/abs/2511.22275) | 2025 | n/a | none | P | S3 |
| [Martingale Score: An Unsupervised Metric for Bayesian Rationality in LLM Reasoning](https://arxiv.org/abs/2512.02914) | 2025 | context | none | P | S1 |
| [STAGE: A Full-Screenplay Benchmark for Reasoning over Evolving Stories](https://arxiv.org/abs/2601.08510) | 2026 | written | state | A | S2 |
| [Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration?](https://arxiv.org/abs/2602.07055) | 2026 | written | none | A | S1 |
| [LifeSim: Long-Horizon User Life Simulator for Personalized Assistant Evaluation](https://arxiv.org/abs/2603.12152) | 2026 | context | none | P | S1 |
| [WMF-AM: Probing LLM Working Memory via Depth-Parameterized Cumulative State Tracking](https://arxiv.org/abs/2603.27343) | 2026 | context | none | A | S1 |
| [From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents](https://arxiv.org/abs/2604.20006) | 2026 | external memory | none | P | S1 |
| [Does Theory of Mind Improvement Really Benefit Human-AI Interactions? Empirical Findings from Interactive Evaluations](https://arxiv.org/abs/2605.15205) | 2026 | context | none | P | S3 |
| [MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems](https://arxiv.org/abs/2605.18565) | 2026 | n/a | none | A | S1 |
| [Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning](https://arxiv.org/abs/2605.24216) | 2026 | n/a | trajectory | A | K |
| [WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction](https://arxiv.org/abs/2605.29341) | 2026 | external memory | none | A | S3 |
| [MINDGAMES: A Live Arena for Evaluating Social and Strategic Reasoning in Multi-Agent LLMs](https://arxiv.org/abs/2605.29512) | 2026 | n/a | none | A | K |
| [From Shortcuts to Reasoning: Robust Post-Training of Theory of Mind with Reinforcement Learning](https://arxiv.org/abs/2606.09092) | 2026 | n/a | output | P | S3 |
| [POMDP validation framework](https://arxiv.org/abs/2606.17383) | 2026 | ext. filter | none | A | K |
| [When Web Agents Finish but Still Fail: Reproducible Triggers and Trace Diagnostics for Parallel Web Exploration](https://arxiv.org/abs/2606.20724) | 2026 | context | trajectory | A | S2 |
| [BayesBench: Evaluating LLM Belief Trajectories Under Multi-Turn Evidence Accumulation](https://arxiv.org/abs/2606.30850) | 2026 | context | none | A | S1 |
| [FinBench: Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting](https://arxiv.org/abs/2607.16229) | 2026 | n/a | output | A | K |
| [Can LLM Agents Price Competitively? A Dynamic Multi-Attribute Auction Benchmark for Agentic Commerce](https://arxiv.org/abs/2608.00102) | 2026 | context | none | A | S3 |
| [Business Arena: Benchmarking LLM Agents in a Realistic Marketplace](https://arxiv.org/abs/2608.08621) | 2026 | n/a | interaction (action) | A | K |
| [Good Memory Has ECC: Evaluating the Memory of Vision-Language Models Beyond Accuracy](https://arxiv.org/abs/2609.00103) | 2026 | n/a | none | A | S2 |

### Other

| Paper | Year | Belief kept by | Credited | Ev. | Src |
|---|---|---|---|---|---|
| Theory of mind and decision science: Towards a typology of tasks and computational models. | 2020 | n/a | none | P | S1 |
| [Decision Transformer: Reinforcement Learning via Sequence Modeling](https://arxiv.org/abs/2106.01345) | 2021 | context | interaction (action) | P | K |
| [Dialogue State Tracking with a Language Model using Schema-Driven Prompting](https://arxiv.org/abs/2109.07506) | 2021 | written | state | P | K |
| [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) | 2022 | context | output | P | K |
| [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171) | 2022 | n/a | output | P | K |
| [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) | 2022 | n/a | interaction (action) | P | K |
| [Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608) | 2022 | context | interaction (action) | P | K |
| [Language Models as Agent Models](https://arxiv.org/abs/2212.01681) | 2022 | n/a | none | P | K |
| [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) | 2023 | world model | state | P | K |
| [Evaluating Large Language Models in Theory of Mind Tasks](https://arxiv.org/abs/2302.02083) | 2023 | n/a | output | P | K |
| [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) | 2023 | context | trajectory | P | K |
| [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) | 2023 | external memory | none | P | K |
| [How FaR Are Large Language Models From Agents with Theory-of-Mind?](https://arxiv.org/abs/2310.03051) | 2023 | context | interaction (action) | P | K |
| [Agents Thinking Fast and Slow: A Talker-Reasoner Architecture](https://arxiv.org/abs/2410.08328) | 2024 | written | state | A | K |
| [TradingAgents: Multi-Agents LLM Financial Trading Framework](https://arxiv.org/abs/2412.20138) | 2024 | context | output | A | K |
| [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) | 2025 | n/a | none | A | S1 |
| [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547) | 2025 | n/a | none | P | K |
| [Agentic Reasoning for Large Language Models](https://arxiv.org/abs/2601.12538) | 2026 | n/a | none | A | K |
| [Credit Assignment in RL for LLMs (survey)](https://arxiv.org/abs/2604.09459) | 2026 | n/a | trajectory | A | K |
| [From Storage to Experience (memory survey)](https://arxiv.org/abs/2605.06716) | 2026 | external memory | none | A | K |
| [The Horizon Gap (survey)](https://arxiv.org/abs/2608.06663) | 2026 | n/a | none | A | K |
| [LLM Agents for Forecasting (survey)](https://arxiv.org/abs/2608.23058) | 2026 | n/a | none | A | K |

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