# Awesome Belief-State LLM Agents

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![papers](https://img.shields.io/badge/papers-518-blue) ![updated](https://img.shields.io/badge/updated-monthly-brightgreen)

A curated, monthly-updated list of papers on how language-model agents **construct, revise, and test what they believe** between decisions. It is the living companion of the survey

> **From Memory to Testable Belief: A Survey of LLM Agents**  
> Jimin Huang, Yuyan Wang, Xueqing Peng, Sophia Ananiadou, Jun'ichi Tsujii. Preprint, 2026. [[PDF]](paper.pdf)

A belief has three parts: a **state** (what is believed and how firmly), a **transition** (how it is carried across an action and revised), and a **likelihood** (how the next observation scores it). Every paper is placed by which of the three it supplies and where each comes from: written by the model, fixed by the designer, learned, or absent. Memory research gave agents a state, revision and post-training gave them a transition, and the likelihood is still mostly supplied from outside.

## Contents

- [Belief-level learning signals at a glance](#belief-level-learning-signals-at-a-glance)
- [Surveys](#surveys)
- [State term](#state-term)
- [Transition term](#transition-term)
- [Likelihood term as a learning signal](#likelihood-term-as-a-learning-signal)
- [Likelihood term as a choice of evidence](#likelihood-term-as-a-choice-of-evidence)
- [Likelihood term as a metric](#likelihood-term-as-a-metric)
- [Background](#background)
- [Updates](#updates)
- [How the list is maintained](#how-the-list-is-maintained)
- [Contributing](#contributing)
- [Citation](#citation)

## Belief-level learning signals at a glance

Systems whose training signal reaches the belief itself, by where that signal comes from. The last rows are the ones that take it from the agent's own observations.

| System | Signal comes from | Paper |
|---|---|---|
| CBM | symbolic verifier | [When Should Models Change Their Minds? Contextual Belief Management in Large Language Models](https://arxiv.org/abs/2605.30219) (2026) |
| Agent-BRACE | calibration target | [Agent-BRACE: Decoupling Beliefs from Actions in Long-Horizon Tasks via Verbalized State Uncertainty](https://arxiv.org/abs/2605.11436) (2026) |
| BOND | Bayesian teacher | [Distilling Bayesian Belief States into Language Models for Auditable Negotiation](https://arxiv.org/abs/2605.04507) (2026) |
| DEL-ToM | process belief model | [DEL-ToM: Inference-Time Scaling for Theory-of-Mind Reasoning via Dynamic Epistemic Logic](https://arxiv.org/abs/2505.17348) (2025) |
| VAGEN | simulator state | [VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents](https://arxiv.org/abs/2510.16907) (2025) |
| T3 | known hypothesis | [T3: Reducing Belief Deviation in Reinforcement Learning for Active Reasoning](https://arxiv.org/abs/2510.12264) (2025) |
| IGPO | known answer | [Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn Search Agents](https://arxiv.org/abs/2510.14967) (2025) |
| InfoPO | known answer | [InfoPO: Information-Driven Policy Optimization for User-Centric Agents](https://arxiv.org/abs/2603.00656) (2026) |
| MARBO | ground-truth roles | [MARBO: Relational Belief Grounding for LLM Agents in Social Deduction Games](https://arxiv.org/abs/2609.06563) (2026) |
| PABU | teacher labels | [PABU: Progress-Aware Belief Update for Efficient LLM Agents](https://arxiv.org/abs/2602.09138) (2026) |
| MMPO | own answer entropy (proxy) | [Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2605.30159) (2026) |
| ABBEL | reconstruction of the agent's past observations | [ABBEL: Learning Natural-Language Belief States for Memory-Efficient Interaction](https://arxiv.org/abs/2512.20111) (2025) |
| PaW | the agent's own next observation (prediction, not a claim) | [Policy and World Modeling Co-Training for Language Agents](https://arxiv.org/abs/2606.02388) (2026) |
| Dark Room | the agent's own next observation (negative result: collapses under GRPO) | [The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and The Channel, Not the Content, Decides What Works](https://arxiv.org/abs/2607.21273) (2026) |
| ReBel | **the agent's own next observation** | [Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents](https://arxiv.org/abs/2605.20061) (2026) |

## Surveys

Neighbouring surveys, each of which supplies one term of the belief (memory: state; uncertainty: confidence on the state; rewards and credit: transition and signal; world models: learned transition and likelihood).

- [Uncertainty Quantification for LLM Agents: A Taxonomy, an Evaluation Protocol, and an Empirical Study](https://arxiv.org/abs/2609.07395) (2026)
- Survey on Evaluation of LLM-based Agents (2026)
- **Theory of Agent (ToA)** — Theory of Agent: The Science of Internalization and Externalization for LLM-Based Agents (2026)
- **The Horizon Gap (survey)** — [The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.06663) (2026)
- **Text World Models (review)** — [Bridging the Agent-World Gap: Text World Models for LLM-based Agents](https://arxiv.org/abs/2606.09032) (2026)  `state: world model`
- **Proactive Service Agents survey** — [Proactive Service Agents: A Unified Decision Framework, Methods, and Evaluation](https://arxiv.org/abs/2609.03727) (2026)
- **LLM Agents for Forecasting (survey)** — [LLM-based Agents for Forecasting and Prediction: Methods, Training, Evaluation, and Applications](https://arxiv.org/abs/2608.23058) (2026)
- **Graph-based agent memory survey** — [Graph-based Agent Memory: Taxonomy, Techniques, and Applications](https://arxiv.org/abs/2602.05665) (2026)  `state: store`
- **From Storage to Experience (memory survey)** — [From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms](https://arxiv.org/abs/2605.06716) (2026)  `state: store`
- **Credit Assignment in RL for LLMs (survey)** — [From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models](https://arxiv.org/abs/2604.09459) (2026)  `credit: trajectory`
- **CPS statistical control survey** — [Complex Problem Solving in Large Language Models: A Statistical Control Survey and Diagnostic Framework](https://arxiv.org/abs/2609.20973) (2026)
- **Agentic Reasoning survey** — [Agentic Reasoning for Large Language Models](https://arxiv.org/abs/2601.12538) (2026)
- Sailing by the Stars: A Survey on Reward Models and Learning Strategies for Learning from Rewards (2025)
- Memory in the Age of AI Agents (2025)
- Large Language Model Agents in Finance: A Survey Bridging Research, Practice, and Real-World Deployment (2025)
- A Survey of Uncertainty Estimation Methods on Large Language Models (2025)
- A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models (2025)
- **Survey of self-evolving agents** — [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) (2025)
- **Cognitive Memory survey** — [Cognitive Memory in Large Language Models](https://arxiv.org/abs/2504.02441) (2025)  `state: store`
- **Agentic RL survey** — [The Landscape of Agentic Reinforcement Learning for LLMs: A Survey](https://arxiv.org/abs/2509.02547) (2025, TMLR)
- A Survey on the Memory Mechanism of Large Language Model based Agents (2024)

## State term

Where the belief lives and who writes it: context, external stores, probabilistic stores, external Bayesian filters, model-written beliefs, learned world models.


**2026**

- **Simple mechanism interfaces** — [Engineering Simplicity: Simple Mechanism Interfaces Steer LLM Agents](https://arxiv.org/abs/2609.36365) (2026)  `state: context`
- **Forecast-Dojo** — [Forecast-Dojo: Replayable Environments for Benchmarking and Training LLM Forecasting Agents](https://arxiv.org/abs/2609.28876) (2026)  `state: written` `credit: trajectory`
- **META** — [Agent Memory with Episodic Retrieval for Financial Decision-Making](https://arxiv.org/abs/2609.28771) (2026, AACL-IJCNLP 2026 Findings)  `state: store`
- **AEWM / EditAct** — [Agent-Editing World Model: Rethinking World Modeling for LLM Agents](https://arxiv.org/abs/2609.28416) (2026)  `state: world model` `credit: interaction`
- **Truth stance layer (expressed doubt + revision store)** — [Truth for Believable AI: Expressed Doubt, Provenance, and Belief Revision as an Engineerable Stance](https://arxiv.org/abs/2609.26035) (2026)  `state: probabilistic store`
- **ReAdapt** — [When LLM Agents Fail to Read the Room: ReAdapt for Relational Social Reasoning](https://arxiv.org/abs/2609.25284) (2026)  `state: written`
- **Few-shot in-context world representations** — [Few-Shot Demonstrations Elicit the Use of In-Context World Representations in LLMs](https://arxiv.org/abs/2609.24352) (2026)  `state: context`
- **Jev-Mem** — [Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents](https://arxiv.org/abs/2609.23986) (2026)  `state: store`
- **LLM explainer over Active Inference agent** — [Triggers and Diagnostics for LLM-Based Interpretability Failures in Active Inference Agents](https://arxiv.org/abs/2609.23215) (2026)  `state: external filter`
- **Bayesian Chronicle Agents (BCA)** — [Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents](https://arxiv.org/abs/2609.21997) (2026)  `state: external filter`
- **ENIGMA** — Executable Epistemic Contracts in Deterministic Agent Simulation: The ENIGMA Architecture (2026)  `state: probabilistic store`
- **CoLearn** — [CoLearn: An Agentic Tutor that Learns its Learner in a Human--AI Co-Learning Loop](https://arxiv.org/abs/2609.21154) (2026)  `state: probabilistic store`
- **GAVEL** — [GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning](https://arxiv.org/abs/2609.19315) (2026)  `state: external filter` `credit: state`
- **Infinite-Parameter LLM** — [Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data](https://arxiv.org/abs/2609.18842) (2026)  `state: external filter` `credit: state`
- **Clue possibility matrix** — [Clueing up LLMs with Tool-Augmented Deductive Reasoning](https://arxiv.org/abs/2609.18736) (2026)  `state: external filter`
- **RoVLaP** — [Bridging Learned Visual Perception and Symbolic Belief-Space Planning via Probabilistic Grounding](https://arxiv.org/abs/2609.16884) (2026, NeuS 2026)  `state: external filter`
- **CORE (+PERSIST)** — [Toward Robust Personalized Alignment for LLMs: Mitigating Persona Drift in Multi-Turn Dialogue](https://arxiv.org/abs/2609.12373) (2026, Findings of EMNLP 2026)  `state: probabilistic store` `credit: state`
- **Rank-Bounded Memory** — Rank-Bounded Memory: Self-Poisoning and Attribution Laundering in LLM Agents (2026)  `state: store`
- **Belief-State Engine** — [Belief-State Engine: Augmenting LLMs for Principled Planning Under Partial Observability](https://arxiv.org/abs/2609.10036) (2026)  `state: external filter`
- **AeroBelief** — [Dual-Layer Semantic-Spatial Belief Mapping for Aerial Object Goal Navigation](https://arxiv.org/abs/2609.08164) (2026)  `state: probabilistic store`
- **MoM / P-Mem** — [MoM: Memory of Memory](https://arxiv.org/abs/2609.25054) (2026)  `state: written`
- [Semantic Bayesian World Models](https://arxiv.org/abs/2609.03834) (2026)  `state: external filter` `credit: state`
- **CAPTURE: preference drift vs memory poisoning** — [CAPTURE: Disentangling Preference Drift from Memory Poisoning in Personalized LLM Agents](https://arxiv.org/abs/2609.02265) (2026)  `state: world model` `credit: state`
- **APEx** — [APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering](https://arxiv.org/abs/2609.02253) (2026)  `state: store` `credit: memory op`
- **BCO: belief-calibrated scaffold optimization** — [Belief-Calibrated Optimization: An Explicit World Model for Agentic Optimization](https://arxiv.org/abs/2609.01861) (2026)  `state: written` `credit: state`
- **EvoSCM causal belief revision** — [EvoSCM: Scientific Belief Revision Through Causal Model Evolution and Experimentation](https://arxiv.org/abs/2609.01526) (2026)  `state: written` `credit: state`
- **AC1 self-model loop replication** — A Controlled Replication of a Self-Model Loop for Language-Model Agents: Controls, Confounds, and Finite-Horizon Path Dependence (2026)  `state: external filter`
- **Belief-Based World Model** — [Towards a Belief-Based World Model for LLM Agents](https://arxiv.org/abs/2609.00455) (2026)  `state: world model`
- **Planted latent variable** — [Planting a Latent Variable in Natural-Looking Text: a More Realistic Test of Belief States in LLMs and Their Link to Concept Geometry](https://arxiv.org/abs/2608.26887) (2026)  `state: context`
- **GPM: governed persistent memory** — [Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents](https://arxiv.org/abs/2608.12476) (2026)  `state: store`
- **EvoHarness-RL learned harness state** — [EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.05446) (2026)  `state: store` `credit: interaction`
- **LongHorizon-Harness** — [LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks](https://arxiv.org/abs/2608.01964) (2026)  `state: store`
- **MADE: belief-driven dual-agent deployment** — [MADE: Belief-Driven Dual-Agent Coordination for Autonomous Model Deployment](https://arxiv.org/abs/2608.01189) (2026)  `state: store` `credit: interaction`
- **NeSyFS: neuro-symbolic fast-slow under partial observability** — [NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability](https://arxiv.org/abs/2607.28942) (2026)  `state: store` `credit: interaction`
- **Physics of long-horizon planning** — [The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation](https://arxiv.org/abs/2607.24720) (2026)  `state: world model` `credit: world-model loss`
- **RLAW: POMDP routing + self-correcting critique** — [Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correction for Autonomous Decision-Making](https://arxiv.org/abs/2607.17038) (2026)  `state: store` `credit: interaction`
- **Auditing belief-conditioned Werewolf agents** — [Auditing Belief-Conditioned LLM Agents in Hidden-Information Social Deduction Games](https://arxiv.org/abs/2607.10814) (2026)  `state: store` `credit: state`
- **Light-Omni** — [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](https://arxiv.org/abs/2607.05511) (2026)  `state: store`
- **WorldEvolver** — [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639) (2026)  `state: world model` `credit: state`
- **BayesEvolve: explicit belief for discovery** — [BayesEvolve: Explicit Belief States for Autonomous Scientific Discovery](https://arxiv.org/abs/2606.30335) (2026)  `state: external filter` `credit: state`
- **Hybrid-WM** — [Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents](https://arxiv.org/abs/2606.27806) (2026)  `state: world model` `credit: state`
- **Internalizing the Future** — [Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning](https://arxiv.org/abs/2606.27483) (2026)  `state: written` `credit: trajectory`
- **Qwen-AgentWorld** — [Qwen-AgentWorld: Language World Models for General Agents](https://arxiv.org/abs/2606.24597) (2026)  `state: world model` `credit: world-model loss`
- **Nous: when belief-based memory helps** — [When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense](https://arxiv.org/abs/2606.22030) (2026)  `state: probabilistic store` `credit: state`
- **Mind-Studio** — [Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games](https://arxiv.org/abs/2606.16070) (2026)  `state: world model`
- **Belief at Risk** — [Belief at Risk: Quantifying Agentic AI Model Risk with LLM-Inferred Bayesian State Filters](https://arxiv.org/abs/2606.15473) (2026)  `state: external filter`
- **ProPlay** — [ProPlay: Procedural World Models for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.12780) (2026)  `state: world model` `credit: trajectory`
- **HIPIF** — [HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning](https://arxiv.org/abs/2606.10507) (2026)  `state: written` `credit: trajectory`
- **InKH financial harness** — [Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents](https://arxiv.org/abs/2606.01886) (2026)  `state: store`
- **PatchWorld** — [PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments](https://arxiv.org/abs/2605.30880) (2026)  `state: world model` `credit: world-model loss`
- **PUMA user-state modeling** — [Know You Before You Speak: User-State Modeling for LLM Personalization in Multi-Turn Conversation](https://arxiv.org/abs/2605.24647) (2026)  `state: probabilistic store` `credit: world-model loss`
- **Memory-R2 / LoGo-GRPO** — [Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents](https://arxiv.org/abs/2605.21768) (2026)  `state: store` `credit: state`
- **MemGym** — [MemGym: a Long-Horizon Memory Environment for LLM Agents](https://arxiv.org/abs/2605.20833) (2026)  `state: store`
- **CMI** — [Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents](https://arxiv.org/abs/2605.17641) (2026)  `state: store` `credit: state`
- **CAGE-2 compound agent design** — [Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP](https://arxiv.org/abs/2605.16205) (2026)  `state: store`
- **Belief Engine stance dynamics** — [Belief Engine: Configurable and Inspectable Stance Dynamics in Multi-Agent LLM Deliberation](https://arxiv.org/abs/2605.15343) (2026)  `state: probabilistic store` `credit: state`
- **GroupMemBench multi-party memory** — [GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations](https://arxiv.org/abs/2605.14498) (2026)  `state: store`
- **Pinductor: LLM-prior POMDP world models** — [Learning POMDP World Models from Observations with Language-Model Priors](https://arxiv.org/abs/2605.13740) (2026)  `state: world model` `credit: state`
- [CHAL: Council of Hierarchical Agentic Language](https://arxiv.org/abs/2605.12718) (2026)  `state: written` `credit: state`
- **Agent-BRACE** — [Agent-BRACE: Decoupling Beliefs from Actions in Long-Horizon Tasks via Verbalized State Uncertainty](https://arxiv.org/abs/2605.11436) (2026)  `state: written` `credit: state`
- **Belief Memory (BeliefMem)** — [Belief Memory: Agent Memory Under Partial Observability](https://arxiv.org/abs/2605.05583) (2026)  `state: store`
- **Bayesian Linguistic Forecaster** — [Agentic Forecasting using Sequential Bayesian Updating of Linguistic Beliefs](https://arxiv.org/abs/2604.18576) (2026)  `state: written`
- **ReflectiChain world-model supply chain** — [From Topology to Trajectory: LLM-Driven World Models For Supply Chain Resilience](https://arxiv.org/abs/2604.11041) (2026)  `state: world model` `credit: trajectory`
- **LSE-MTP** — [Toward Consistent World Models with Multi-Token Prediction and Latent Semantic Enhancement](https://arxiv.org/abs/2604.06155) (2026, ACL 2026)  `state: context` `credit: world-model loss`
- **LOCARD structured belief state** — [LOCARD: An Agentic Framework for Blockchain Forensics](https://arxiv.org/abs/2604.04211) (2026, IEEE International Conference on Blockchain 2026)  `state: written`
- **Belief geometries via SAEs** — [Finding Belief Geometries with Sparse Autoencoders](https://arxiv.org/abs/2604.02685) (2026)  `state: context`
- **Meta-Harness** — [Meta-Harness: End-to-End Optimization of Model Harnesses](https://arxiv.org/abs/2603.28052) (2026)  `state: store` `credit: memory op`
- **TAMTRL** — [TAMTRL: Teacher-Aligned Reward Reshaping for Multi-Turn Reinforcement Learning in Long-Context Compression](https://arxiv.org/abs/2603.21663) (2026)  `state: written` `credit: trajectory`
- **Graph of States** — [Graph of States: Solving Abductive Tasks with Large Language Models](https://arxiv.org/abs/2603.21250) (2026)  `state: store`
- **Kumiho** — [Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures](https://arxiv.org/abs/2603.17244) (2026)  `state: store`
- **MM-Lifelong / ReMA** — [Towards Multimodal Lifelong Understanding: A Dataset and Agentic Baseline](https://arxiv.org/abs/2603.05484) (2026)  `state: store`
- **SSMG-Nav** — [SSMG-Nav: Enhancing Lifelong Object Navigation with Semantic Skeleton Memory Graph](https://arxiv.org/abs/2603.01813) (2026)  `state: store`
- **MMA-RAG^T** — [Adversarial Intent is a Latent Variable: Stateful Trust Inference for Securing Multimodal Agentic RAG](https://arxiv.org/abs/2602.21447) (2026)  `state: written`
- **RB-VLA: recursive belief VLA** — [Recursive Belief Vision Language Action Models](https://arxiv.org/abs/2602.20659) (2026)  `state: world model` `credit: state`
- **StarWM** — [World Models for Policy Refinement in StarCraft II](https://arxiv.org/abs/2602.14857) (2026)  `state: world model` `credit: world-model loss`
- **WebWorld** — [WebWorld: A Large-Scale World Model for Web Agent Training](https://arxiv.org/abs/2602.14721) (2026)  `state: world model` `credit: world-model loss`
- **INTENT** — [Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use](https://arxiv.org/abs/2602.11541) (2026)  `state: world model`
- **AutoHarness** — [AutoHarness: improving LLM agents by automatically synthesizing a code harness](https://arxiv.org/abs/2603.03329) (2026)  `state: external filter`
- **Code2World** — [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856) (2026)  `state: world model` `credit: world-model loss`
- **PABU** — [PABU: Progress-Aware Belief Update for Efficient LLM Agents](https://arxiv.org/abs/2602.09138) (2026)  `state: written` `credit: state`
- **SWIRL** — [Self-Improving World Modelling with Latent Actions](https://arxiv.org/abs/2602.06130) (2026)  `state: world model` `credit: world-model loss`
- **PCE** — [From Assumptions to Actions: Turning LLM Reasoning into Uncertainty-Aware Planning for Embodied Agents](https://arxiv.org/abs/2602.04326) (2026)  `state: written` `credit: state`
- **MemSkill** — [MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents](https://arxiv.org/abs/2602.02474) (2026)  `state: store` `credit: memory op`
- **EoG belief propagation** — [Think Locally, Explain Globally: Graph-Guided LLM Investigations via Local Reasoning and Belief Propagation](https://arxiv.org/abs/2601.17915) (2026)  `state: external filter`
- **External affective state dynamics** — [Controlling Long-Horizon Behavior in Language Model Agents with Explicit State Dynamics](https://arxiv.org/abs/2601.16087) (2026)  `state: store`
- **InfiAgent** — [InfiAgent: An Infinite-Horizon Framework for General-Purpose Autonomous Agents](https://arxiv.org/abs/2601.03204) (2026)  `state: written`
- **SimpleMem** — [SimpleMem: Efficient Lifelong Memory for LLM Agents](https://arxiv.org/abs/2601.02553) (2026)  `state: store`
- **Episodic-Semantic Memory** — [Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents](https://arxiv.org/abs/2605.17625) (2026)  `state: store` `credit: memory op`
- **HAGE** — [HAGE: Harnessing Agentic Memory via RL-Driven Weighted Graph Evolution](https://arxiv.org/abs/2605.09942) (2026)  `state: store` `credit: memory op`
- **Bayes-consistent orchestration** — [Position: agentic AI orchestration should be Bayes-consistent](https://arxiv.org/abs/2605.00742) (2026)  `state: external filter`
- **LLM + causal model POMDP planning** — Augmenting large language models with psychologically grounded models of causal reasoning for planning under uncertainty (2026, Frontiers in Artificial Intelligence)  `state: external filter`
- **CSSP** — Causal-Dependency State Space Prompting: bounded-memory long-horizon reasoning for streaming IT incidents (2026, Engineering Research Express)  `state: external filter` `credit: state`
- **Hindsight** — Hindsight: Structured Agent Memory that Retains, Recalls, and Reflects (2026, Annual Meeting of the Association for Computational Linguistics)  `state: store`
- **PRISM** — PRISM: Preference-Guided Semantic Reasoning with Vision-Language Models for Object Goal Navigation (2026, International Conference on Multimedia Retrieval)  `state: written`

**2025**

- **Agent2World** — [Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback](https://arxiv.org/abs/2512.22336) (2025)  `state: world model` `credit: trajectory`
- **ABBEL** — [ABBEL: Learning Natural-Language Belief States for Memory-Efficient Interaction](https://arxiv.org/abs/2512.20111) (2025)  `state: written` `credit: state`
- **Word to World** — [From Word to World: Can Large Language Models be Implicit Text-based World Models?](https://arxiv.org/abs/2512.18832) (2025, ACL 2026)  `state: world model` `credit: world-model loss`
- **Emergent World Beliefs** — [Emergent World Beliefs: Exploring Transformers in Stochastic Games](https://arxiv.org/abs/2512.23722) (2025)  `state: world model`
- **Hindsight** — [Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects](https://arxiv.org/abs/2512.12818) (2025)  `state: store`
- **NextLat belief-state latents** — [Next-Latent Prediction Transformers Learn Compact World Models](https://arxiv.org/abs/2511.05963) (2025)  `state: world model` `credit: world-model loss`
- **ContextFolding** — [Scaling Long-Horizon LLM Agent via Context-Folding](https://arxiv.org/abs/2510.11967) (2025)  `state: written` `credit: memory op`
- **Markovian Thinker** — [The Markovian Thinker: Architecture-Agnostic Linear Scaling of Reasoning](https://arxiv.org/abs/2510.06557) (2025)  `state: written` `credit: output`
- **CWM games** — [Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) (2025)  `state: world model`
- **ACON** — [ACON: Optimizing Context Compression for Long-horizon LLM Agents](https://arxiv.org/abs/2510.00615) (2025)  `state: written`
- **ID-RAG** — [ID-RAG: Identity Retrieval-Augmented Generation for Long-Horizon Persona Coherence in Generative Agents](https://arxiv.org/abs/2509.25299) (2025)  `state: store`
- **ReasoningBank** — [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140) (2025)  `state: store`
- **ReSum** — [ReSum: Unlocking Long-Horizon Search Intelligence via Context Summarization](https://arxiv.org/abs/2509.13313) (2025)  `state: written` `credit: trajectory`
- **Social World Models (S3AP)** — [Social World Models](https://arxiv.org/abs/2509.00559) (2025)  `state: written`
- **Memento** — [Memento: Fine-tuning LLM Agents without Fine-tuning LLMs](https://arxiv.org/abs/2508.16153) (2025)  `state: store` `credit: interaction`
- **M3-Agent** — [Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory](https://arxiv.org/abs/2508.09736) (2025)  `state: store` `credit: trajectory`
- **CoEx** — [CoEx -- Co-evolving World-model and Exploration](https://arxiv.org/abs/2507.22281) (2025, EMNLP 2025)  `state: world model`
- **PRIME** — [PRIME: Large Language Model Personalization with Cognitive Dual-Memory and Personalized Thought Process](https://arxiv.org/abs/2507.04607) (2025, Conference on Empirical Methods in Natural Language Processing)  `state: store`
- **MemOS** — [MemOS: A Memory OS for AI System](https://arxiv.org/abs/2507.03724) (2025)  `state: store`
- **MemAgent** — [MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent](https://arxiv.org/abs/2507.02259) (2025, ICLR 2026)  `state: written` `credit: state`
- **MEM1** — [MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents](https://arxiv.org/abs/2506.15841) (2025)  `state: written` `credit: state`
- **EvolvTrip** — [EvolvTrip: Enhancing Literary Character Understanding with Temporal Theory-of-Mind Graphs](https://arxiv.org/abs/2506.13641) (2025)  `state: written`
- **MemoryOS** — [Memory OS of AI Agent](https://arxiv.org/abs/2506.06326) (2025, Conference on Empirical Methods in Natural Language Processing)  `state: store`
- **ReflAct** — [ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection](https://arxiv.org/abs/2505.15182) (2025, EMNLP 2025)  `state: written`
- **Lookbacks belief tracking** — [Language Models use Lookbacks to Track Beliefs](https://arxiv.org/abs/2505.14685) (2025)  `state: context`
- **Mem0** — [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) (2025)  `state: store`
- **Dynamic Cheatsheet** — [Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory](https://arxiv.org/abs/2504.07952) (2025, Conference of the European Chapter of the Association for Computational Linguistics)  `state: store` `credit: memory op`
- **EnigmaToM** — [EnigmaToM: Improve LLMs' Theory-of-Mind Reasoning Capabilities with Neural Knowledge Base of Entity States](https://arxiv.org/abs/2503.03340) (2025, Annual Meeting of the Association for Computational Linguistics)  `state: written`
- **A-Mem** — [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) (2025, NeurIPS 2025)  `state: store` `credit: output`
- **LLaMAR** — [LLaMAR: Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://arxiv.org/abs/2407.10031) (2025)  `state: context`
- **Bayesian geometry of attention** — [The Bayesian Geometry of Transformer Attention](https://arxiv.org/abs/2512.22471) (2025)  `state: context`
- **R4** — [R4: Retrieval-Augmented Reasoning for Vision-Language Models in 4D Spatio-Temporal Space](https://arxiv.org/abs/2512.15940) (2025)  `state: world model`
- [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564) (2025)  `state: store`
- **Memory in LLMs: mechanisms/eval** — [Memory in Large Language Models: Mechanisms, Evaluation and Evolution](https://arxiv.org/abs/2509.18868) (2025)  `state: store`
- **Zep / Graphiti** — [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956) (2025)  `state: store`
- **LLM cooperative game simulation** — A Large Language Model-Enabled Framework for Simulating Multi-Agent Cooperative Game (2025, BigData Congress [Services Society])  `state: external filter`

**2024**

- **MindForge** — [MindForge: Empowering Embodied Agents with Theory of Mind for Lifelong Cultural Learning](https://arxiv.org/abs/2411.12977) (2024, NeurIPS 2025)  `state: written`
- **QuBE** — [QuBE: Question-based Belief Enhancement for Agentic LLM Reasoning](https://arxiv.org/abs/10.18653/v1/2024.emnlp-main.1193) (2024, EMNLP 2024)  `state: written` `credit: state`
- **WMA Web Agent** — [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://arxiv.org/abs/2410.13232) (2024, ICLR 2025)  `state: world model` `credit: world-model loss`
- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) (2024)  `state: store`
- **LaBToM** — [Understanding Epistemic Language with a Language-augmented Bayesian Theory of Mind](https://arxiv.org/abs/2408.12022) (2024, TACL 2024)  `state: external filter`
- **HiAgent** — [HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model](https://arxiv.org/abs/2408.09559) (2024, Annual Meeting of the Association for Computational Linguistics)  `state: written`
- **Hypothetical Minds** — [Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with Large Language Models](https://arxiv.org/abs/2407.07086) (2024)  `state: written` `credit: state`
- **FinCon** — [FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making](https://arxiv.org/abs/2407.06567) (2024, NeurIPS 2024)  `state: store` `credit: state`
- **PercepToM** — [Perceptions to Beliefs: Exploring Precursory Inferences for Theory of Mind in Large Language Models](https://arxiv.org/abs/2407.06004) (2024, EMNLP 2024)  `state: written`
- **TimeToM** — [TimeToM: Temporal Space is the Key to Unlocking the Door of Large Language Models' Theory-of-Mind](https://arxiv.org/abs/2407.01455) (2024, Annual Meeting of the Association for Computational Linguistics)  `state: written`
- **From Words to Actions** — [From Words to Actions: Unveiling the Theoretical Underpinnings of LLM-Driven Autonomous Systems](https://arxiv.org/abs/2405.19883) (2024, ICML 2024)  `state: context`
- **Latent state estimation for UI agents** — [Latent State Estimation Helps UI Agents to Reason](https://arxiv.org/abs/2405.11120) (2024)  `state: written`
- **FinAgent** — [A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist](https://arxiv.org/abs/2402.18485) (2024, KDD 2024)  `state: store` `credit: interaction`
- **ReadAgent** — [A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts](https://arxiv.org/abs/2402.09727) (2024, ICML 2024)  `state: store`
- **MEMORYLLM** — [MEMORYLLM: Towards Self-Updatable Large Language Models](https://arxiv.org/abs/2402.04624) (2024, International Conference on Machine Learning)  `state: probabilistic store` `credit: state`
- **Belief state geometry** — [Transformers represent belief state geometry in their residual stream](https://arxiv.org/abs/2405.15943) (2024, Neural Information Processing Systems)  `state: context`
- **GIF-MCTS code world models** — [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search](https://arxiv.org/abs/2405.15383) (2024, Neural Information Processing Systems)  `state: world model` `credit: world-model loss`
- **Beliefs of self and others** — [Language Models Represent Beliefs of Self and Others](https://arxiv.org/abs/2402.18496) (2024, International Conference on Machine Learning)  `state: context`

**2023**

- **Interactive planning POMDP** — [Interactive Planning Using Large Language Models for Partially Observable Robotics Tasks](https://arxiv.org/abs/2312.06876) (2023)  `state: context`
- **LAW** — [Language Models, Agent Models, and World Models: The LAW for Machine Reasoning and Planning](https://arxiv.org/abs/2312.05230) (2023)  `state: world model`
- **FinMem** — [FinMem: A Performance-Enhanced LLM Trading Agent with Layered Memory and Character Design](https://arxiv.org/abs/2311.13743) (2023, AAAI Spring Symposium 2024)  `state: store` `credit: interaction`
- **SimToM** — [Think Twice: Perspective-Taking Improves Large Language Models' Theory-of-Mind Capabilities](https://arxiv.org/abs/2311.10227) (2023, Annual Meeting of the Association for Computational Linguistics)  `state: context`
- **ToM Multi-Agent Collab** — [Theory of Mind for Multi-Agent Collaboration via Large Language Models](https://arxiv.org/abs/2310.10701) (2023, EMNLP 2023)  `state: written`
- **MemGPT** — [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) (2023)  `state: store` `credit: output`
- **RAFA** — [Reason for Future, Act for Now: A Principled Framework for Autonomous LLM Agents with Provable Sample Efficiency](https://arxiv.org/abs/2309.17382) (2023)  `state: context`
- **TradingGPT** — [TradingGPT: Multi-Agent System with Layered Memory and Distinct Characters for Enhanced Financial Trading Performance](https://arxiv.org/abs/2309.03736) (2023)  `state: store` `credit: interaction`
- **ExpeL** — [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) (2023, AAAI 2024)  `state: store` `credit: trajectory`
- **RecallM** — [RecallM: An Adaptable Memory Mechanism with Temporal Understanding for Large Language Models](https://arxiv.org/abs/2307.02738) (2023)  `state: store` `credit: memory op`
- **CoELA** — [Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485) (2023, International Conference on Learning Representations)  `state: store` `credit: trajectory`
- **SymbolicToM** — [Minding Language Models' (Lack of) Theory of Mind: A Plug-and-Play Multi-Character Belief Tracker](https://arxiv.org/abs/2306.00924) (2023, ACL 2023)  `state: external filter`
- **Voyager** — [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) (2023, TMLR 2024)  `state: store` `credit: trajectory`
- **RAP** — [Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992) (2023, EMNLP 2023)  `state: world model` `credit: trajectory`
- **RET-LLM** — [RET-LLM: Towards a General Read-Write Memory for Large Language Models](https://arxiv.org/abs/2305.14322) (2023)  `state: store`
- **LLM-MCTS** — [Large Language Models as Commonsense Knowledge for Large-Scale Task Planning](https://arxiv.org/abs/2305.14078) (2023, NeurIPS 2023)  `state: world model` `credit: trajectory`
- **RecurrentGPT** — [RecurrentGPT: Interactive Generation of (Arbitrarily) Long Text](https://arxiv.org/abs/2305.13304) (2023)  `state: written` `credit: output`
- **MemoryBank** — [MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) (2023, AAAI 2024)  `state: store` `credit: output`
- **LLM+P** — [LLM+P: Empowering Large Language Models with Optimal Planning Proficiency](https://arxiv.org/abs/2304.11477) (2023)  `credit: output`
- **Generative Agents** — [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) (2023, UIST 2023)  `state: store` `credit: interaction`
- **Semantic Entropy** — [Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation](https://arxiv.org/abs/2302.09664) (2023, ICLR 2023)  `credit: output`
- **Synapse** — [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863) (2023, ICLR 2024)  `state: store`

**2022**

- **ReAct** — [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) (2022, International Conference on Learning Representations)  `state: context`
- **LMs (Mostly) Know** — [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221) (2022)  `state: written` `credit: output`
- **Verbalized Uncertainty** — [Teaching Models to Express Their Uncertainty in Words](https://arxiv.org/abs/2205.14334) (2022, TMLR 2022)  `state: written` `credit: output`
- **HELM** — [History Compression via Language Models in Reinforcement Learning](https://arxiv.org/abs/2205.12258) (2022, ICML 2022)  `state: store` `credit: trajectory`

**2021**

- **Do LMs have beliefs** — [Do Language Models Have Beliefs? Methods for Detecting, Updating, and Visualizing Model Beliefs](https://arxiv.org/abs/2111.13654) (2021)  `credit: state`

**2020**

- **RAG** — [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) (2020, NeurIPS 2020)  `state: store` `credit: output`
- **GATA belief graphs** — [Learning Dynamic Belief Graphs to Generalize on Text-Based Games](https://arxiv.org/abs/2002.09127) (2020, Neural Information Processing Systems)  `state: world model` `credit: state`
- **Text games with common sense** — [Playing Text-Based Games with Common Sense](https://arxiv.org/abs/2012.02757) (2020)  `state: store` `credit: trajectory`

## Transition term

How the belief is carried across an action and revised: triggers, mechanisms, and the four failure modes (failed stay, update, isolation, act).


**2026**

- **UQ for LLM Agents taxonomy** — [Uncertainty Quantification for LLM Agents: A Taxonomy, an Evaluation Protocol, and an Empirical Study](https://arxiv.org/abs/2609.07395) (2026)
- **When Stale Constraints Go Unchecked** — [When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory](https://arxiv.org/abs/2608.25553) (2026)  `state: store`
- **Structured memory over-personalization** — [Mitigating Over-Personalization in LLMs via Structured Memory](https://arxiv.org/abs/2608.08300) (2026)  `state: store`
- **When Memory Updates but Behavior Does Not** — [When Memory Updates but Behavior Does Not: Repairing Implicit Stale Dependencies in Personalized Agent Responses](https://arxiv.org/abs/2608.01619) (2026)  `state: store`
- **MD5 state tracking** — [Long-Horizon State Tracking in LLMs: Executing MD5 through a Deep Sequence of Dependent Tool Calls](https://arxiv.org/abs/2609.00012) (2026)  `state: context`
- **STOCKTAKE** — [STOCKTAKE: Measuring the Gap Between Perception and Action in LLM Agents with a Fair Oracle](https://arxiv.org/abs/2607.13618) (2026)
- **MemOps** — [MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations](https://arxiv.org/abs/2607.12893) (2026)  `state: store`
- **WM-SAR** — [Repair the Amplifier, Not the Symptom: Stable World-Model Correction for Agent Rollouts](https://arxiv.org/abs/2607.01767) (2026)  `state: world model` `credit: trajectory`
- **InfoDelphi** — [Diverse Evidence, Better Forecasts: Multi-Agent Deliberation Under Information Asymmetry](https://arxiv.org/abs/2607.01661) (2026)  `state: context`
- **EVAF** — [Memory Depth, Not Memory Access: Selective Parametric Consolidation for Long-Running Language Agents](https://arxiv.org/abs/2606.26806) (2026)  `state: store` `credit: memory op`
- **Closing the Feedback Loop** — [Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning](https://arxiv.org/abs/2606.17591) (2026)  `state: store`
- **MIST** — [Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models](https://arxiv.org/abs/2606.10949) (2026)  `state: store`
- **TOKI** — [TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory](https://arxiv.org/abs/2606.06240) (2026)  `state: store`
- **Trivium** — [Trivium: Temporal Regret as a First-Class Objective for Causal-Memory Controllers](https://arxiv.org/abs/2606.04421) (2026)  `state: world model` `credit: world-model loss`
- **Contextual Belief Management (BeliefTrack)** — [When Should Models Change Their Minds? Contextual Belief Management in Large Language Models](https://arxiv.org/abs/2605.30219) (2026)  `state: written` `credit: state`
- **OmniToM explicit belief modeling** — [OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling](https://arxiv.org/abs/2605.26322) (2026)
- **Representation signatures in trading agents** — [Representation Signatures and Risk-Feedback Alignment in LLM Trading Agents](https://arxiv.org/abs/2605.28850) (2026)  `state: context` `credit: output`
- **Why world models: LLM state-tracking failures (Flux)** — [Why We Need World Models for AGI: Where LLMs Fail and How World Models May Outperform](https://arxiv.org/abs/2605.23972) (2026)  `state: context`
- **EquiMem** — [EquiMem: Calibrating Shared Memory in Multi-Agent Debate via Game-Theoretic Equilibrium](https://arxiv.org/abs/2605.09278) (2026)  `state: store`
- **STALE** — [STALE: Can LLM Agents Know When Their Memories Are No Longer Valid?](https://arxiv.org/abs/2605.06527) (2026)  `state: store`
- **T2PO** — [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.02178) (2026)  `state: context` `credit: interaction`
- **AI Scientists Reasoning** — [AI scientists produce results without reasoning scientifically](https://arxiv.org/abs/2604.18805) (2026)  `state: context`
- **Cyclic subtask graphs** — [Complete Cyclic Subtask Graphs for Tool-Using LLM Agents: Flexibility, Cost, and Bottlenecks in Long-Horizon Workflows](https://arxiv.org/abs/2604.22820) (2026)  `state: written`
- **MEDLEY-BENCH** — [MEDLEY-BENCH: Benchmarking Behavioural Metacognition and Belief Revision Under Social Pressure in Large Language Models](https://arxiv.org/abs/2604.16009) (2026)  `state: context`
- **SAVeR: self-audited verified reasoning** — [Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing](https://arxiv.org/abs/2604.08401) (2026)  `state: context` `credit: state`
- **DeltaLogic minimal-edit revision** — [DeltaLogic: Minimal Premise Edits Reveal Belief-Revision Failures in Logical Reasoning Models](https://arxiv.org/abs/2604.02733) (2026)  `state: context` `credit: output`
- **YC-Bench** — [YC-Bench: Benchmarking AI Agents for Long-Term Planning and Consistent Execution](https://arxiv.org/abs/2604.01212) (2026)  `state: written`
- **BeliefShift** — [BeliefShift: Benchmarking Temporal Belief Consistency and Opinion Drift in LLM Agents](https://arxiv.org/abs/2603.23848) (2026)
- **RPMS** — [RPMS: Enhancing LLM-Based Embodied Planning through Rule-Augmented Memory Synergy](https://arxiv.org/abs/2603.17831) (2026)  `state: written`
- **DToM-Track: dynamic ToM as temporal memory** — [Dynamic Theory of Mind as a Temporal Memory Problem: Evidence from Large Language Models](https://arxiv.org/abs/2603.14646) (2026)  `state: context`
- **D-MEM** — [D-MEM: Dopamine-Gated Agentic Memory via Reward Prediction Error Routing](https://arxiv.org/abs/2603.14597) (2026)  `state: store`
- **Reasoning Theater** — [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/abs/2603.05488) (2026)  `state: context` `credit: output`
- **DenoiseFlow** — [DenoiseFlow: Uncertainty-Aware Denoising for Reliable LLM Agentic Workflows](https://arxiv.org/abs/2603.00532) (2026)  `state: context` `credit: trajectory`
- **Persuasion Propagation** — [Understanding Persuasion in Long-Running Agents](https://arxiv.org/abs/2602.00851) (2026)  `state: context`
- **HiMem** — [HiMem: Hierarchical Long-Term Memory for LLM Long-Horizon Agents](https://arxiv.org/abs/2601.06377) (2026)  `state: store`
- **TRACE** — [TRACE: An Operational Reasoning Schema for Auditable Agentic Commitments](https://arxiv.org/abs/2607.12480) (2026)  `state: written`
- **MemStrata temporal validity** — [Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge](https://arxiv.org/abs/2606.26511) (2026)  `state: store`
- [Debugging code world models](https://arxiv.org/abs/2602.07672) (2026)  `state: world model` `credit: world-model loss`
- **ReflectiChain** — ReflectiChain: Mitigating Semantic-Execution Drift in Long-Horizon LLM Agents via Retrospective Reflection and Double-Loop Policy Adaptation (2026, Electronics)  `state: world model`

**2025**

- **LLMs as discounted Bayesian filters** — [Large Language Models as Discounted Bayesian Filters](https://arxiv.org/abs/2512.18489) (2025)  `state: context`
- **AccumulatingContext** — [Accumulating Context Changes the Beliefs of Language Models](https://arxiv.org/abs/2511.01805) (2025)  `state: context`
- **Active Confusion Expression** — [Active Confusion Expression in Large Language Models: Leveraging World Models toward Better Social Reasoning](https://arxiv.org/abs/2510.07974) (2025)  `state: written` `credit: output`
- **ACE** — [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) (2025)  `state: written`
- **Debate or Vote** — [Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?](https://arxiv.org/abs/2508.17536) (2025, Neural Information Processing Systems)  `state: context` `credit: output`
- **BASIL** — [BASIL: Bayesian Assessment of Sycophancy in LLMs](https://arxiv.org/abs/2508.16846) (2025, Conference on Fairness, Accountability and Transparency)  `state: context` `credit: output`
- **Sycophancy under Pressure** — [Sycophancy under Pressure: Evaluating and Mitigating Sycophantic Bias via Adversarial Dialogues in Scientific QA](https://arxiv.org/abs/2508.13743) (2025)  `state: context` `credit: output`
- **Bayesian Coherence Coefficient** — [Are LLM Belief Updates Consistent with Bayes' Theorem?](https://arxiv.org/abs/2507.17951) (2025)  `state: context`
- **MemoryAgentBench** — [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/abs/2507.05257) (2025)
- **Overcoming Multi-step Complexity in Multimodal Theory-of-Min** — [Overcoming Multi-step Complexity in Multimodal Theory-of-Mind Reasoning: A Scalable Bayesian Planner](https://arxiv.org/abs/2506.01301) (2025, International Conference on Machine Learning)  `state: external filter` `credit: output`
- **Measuring Sycophancy of Language Models in Multi-turn Dialog** — [Measuring Sycophancy of Language Models in Multi-turn Dialogues](https://arxiv.org/abs/2505.23840) (2025, Conference on Empirical Methods in Natural Language Processing)  `state: context`
- **LLM Debate Overconfidence** — [When Two LLMs Debate, Both Think They'll Win](https://arxiv.org/abs/2505.19184) (2025)  `state: context`
- **Experience-following memory study** — [How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior](https://arxiv.org/abs/2505.16067) (2025, Annual Meeting of the Association for Computational Linguistics)  `state: store` `credit: memory op`
- **LLMs get lost multi-turn** — [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120) (2025)  `state: context`
- **ToM-agent counterfactual reflection** — [Large Language Models as Theory of Mind Aware Generative Agents with Counterfactual Reflection](https://arxiv.org/abs/2501.15355) (2025)  `state: written`
- **AgentRefine** — [AgentRefine: Enhancing Agent Generalization through Refinement Tuning](https://arxiv.org/abs/2501.01702) (2025, ICLR 2025)  `state: context` `credit: trajectory`
- **WMNav** — [WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation](https://arxiv.org/abs/2503.02247) (2025, IEEE/RJS International Conference on Intelligent RObots and Systems)  `state: world model`

**2024**

- **Agent Q** — [Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.07199) (2024)  `state: store` `credit: trajectory`
- **Coherence norms** — [Are language models rational? The case of coherence norms and belief revision](https://arxiv.org/abs/2406.03442) (2024)
- **Reflect-RL** — [Reflect-RL: Two-Player Online RL Fine-Tuning for LMs](https://arxiv.org/abs/2402.12621) (2024, ACL 2024)  `state: written` `credit: interaction`
- **self-verification limits** — [On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks](https://arxiv.org/abs/2402.08115) (2024, International Conference on Learning Representations)  `state: context`
- **Rational belief revision in model editing** — [Fundamental Problems With Model Editing: How Should Rational Belief Revision Work in LLMs?](https://arxiv.org/abs/2406.19354) (2024, TMLR)

**2023**

- **Sycophancy** — [Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548) (2023, International Conference on Learning Representations)  `state: context` `credit: output`
- **LATS** — [Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models](https://arxiv.org/abs/2310.04406) (2023, ICML 2024)  `state: store` `credit: trajectory`
- **ProAgent** — [ProAgent: Building Proactive Cooperative Agents with Large Language Models](https://arxiv.org/abs/2308.11339) (2023, AAAI 2024)  `state: written`
- **MQuAKE / MeLLo** — [MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions](https://arxiv.org/abs/2305.14795) (2023, Conference on Empirical Methods in Natural Language Processing)  `state: store`
- **Self-Debug** — [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128) (2023, ICLR 2024)  `state: context` `credit: output`
- **Self-Refine** — [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) (2023, NeurIPS 2023)  `state: context` `credit: output`
- **RCI** — [Language Models can Solve Computer Tasks](https://arxiv.org/abs/2303.17491) (2023, NeurIPS 2023)  `state: context` `credit: interaction`
- **Reflexion** — [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) (2023, NeurIPS 2023)  `state: store` `credit: trajectory`
- **DEPS** — [Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/abs/2302.01560) (2023, NeurIPS 2023)  `state: context` `credit: trajectory`
- **NLMs as epistemic agents** — Probabilistic coherence, logical consistency, and Bayesian learning: Neural language models as epistemic agents (2023, PLoS ONE)

**2022**

- **Towards Teachable Reasoning Systems** — [Towards Teachable Reasoning Systems: Using a Dynamic Memory of User Feedback for Continual System Improvement](https://arxiv.org/abs/2204.13074) (2022, Conference on Empirical Methods in Natural Language Processing)  `state: store`

**2021**

- **BeliefBank** — [BeliefBank: Adding Memory to a Pre-Trained Language Model for a Systematic Notion of Belief](https://arxiv.org/abs/2109.14723) (2021, Conference on Empirical Methods in Natural Language Processing)  `state: store`

## Likelihood term as a learning signal

Who scores what the agent produced, and which object the gradient reaches: output, trajectory, interaction, world-model loss, or the belief itself.


**2026**

- **Mind2Dialogue** — [Mind2Dialogue: Training Human-Aware Language Models by Simulating User Mental States](https://arxiv.org/abs/2609.15972) (2026)  `state: written` `credit: output`
- **MARBO** — [MARBO: Relational Belief Grounding for LLM Agents in Social Deduction Games](https://arxiv.org/abs/2609.06563) (2026, EMNLP 2026)  `state: written` `credit: state`
- **PGPO** — [PGPO: Potential-Guided Policy Optimization for Multi-Turn Agentic Tasks](https://arxiv.org/abs/2609.02236) (2026)  `state: context` `credit: interaction`
- **Explore More Drift Less** — [Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents](https://arxiv.org/abs/2609.01245) (2026)  `credit: output`
- **Hindsight Memory-PRM** — [Hindsight Memory-PRM: Supervising Memory Management with Auditable Hindsight Credit](https://arxiv.org/abs/2608.29605) (2026)  `state: store` `credit: memory op`
- **ContextPilot** — [ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained RL](https://arxiv.org/abs/2608.28476) (2026, EMNLP 2026)  `state: context` `credit: memory op`
- **VICT** — [VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning](https://arxiv.org/abs/2608.28128) (2026)  `credit: interaction`
- **IAPO: influence-aware credit for service agents** — [IAPO: Influence-Aware Policy Optimization for Credit Assignment in Multi-Turn Service Agents](https://arxiv.org/abs/2608.24588) (2026)  `state: context` `credit: interaction`
- **HiDiffTIR** — [HiDiffTIR: Hierarchical Difficulty-Aware Policy Optimization for Multi-Turn Tool-Integrated Reasoning](https://arxiv.org/abs/2608.21863) (2026)  `state: context` `credit: interaction`
- **RTPO** — [RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training](https://arxiv.org/abs/2608.18682) (2026)  `credit: interaction`
- **CrEST** — [Teach the Magnitude, Not the Direction: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents](https://arxiv.org/abs/2608.13179) (2026)  `state: context` `credit: interaction`
- **VerMem** — [Verifiable Memory: Learning Unified Memory Management with Local and Global Verifiers for Large Language Model Agents](https://arxiv.org/abs/2608.03137) (2026)  `state: store` `credit: memory op`
- **TCPO turn-level credit** — [TCPO: Turn-Level Credit Policy Optimization](https://arxiv.org/abs/2608.01667) (2026)  `state: context` `credit: interaction`
- **Dark Room** — [The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and The Channel, Not the Content, Decides What Works](https://arxiv.org/abs/2607.21273) (2026)  `state: written` `credit: state`
- **MSCE** — [From Memory to Skills: Evidence-Grounded Co-Evolution Governance for Long-Horizon LLM Agents](https://arxiv.org/abs/2607.16621) (2026)  `state: store` `credit: trajectory`
- **STAPO trajectory-neglect steps** — [STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2607.04963) (2026)  `state: context` `credit: trajectory`
- **PivoARL** — [Agent Reinforcement Learning via Pivotal-Aware Self-Feedback Retry](https://arxiv.org/abs/2607.03702) (2026)  `state: context` `credit: interaction`
- **G2PO** — [Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2606.22995) (2026)  `state: context` `credit: trajectory`
- **Q-Evolve** — [Self-evolving LLM agents with in-distribution Optimization](https://arxiv.org/abs/2606.07367) (2026)  `state: context` `credit: trajectory`
- **ECPO** — [When Denser Credit Is Not Enough: Evidence-Calibrated Policy Optimization for Long-Horizon LLM Agent Training](https://arxiv.org/abs/2606.05885) (2026)  `credit: trajectory`
- **PCCC / CVT-RL** — [Policy-Conditioned Counterfactual Credit for Verifiable Reinforcement Learning of Long-Horizon Language Agents](https://arxiv.org/abs/2606.05263) (2026)  `state: written` `credit: state`
- **PaW** — [Policy and World Modeling Co-Training for Language Agents](https://arxiv.org/abs/2606.02388) (2026, EMNLP 2026)  `state: world model` `credit: world-model loss`
- **SPADER** — [SPADER: Step-wise Peer Advantage with Diversity-Aware Exploration Rewards for Multi-Answer Question Answering](https://arxiv.org/abs/2606.00593) (2026)  `state: context` `credit: interaction`
- **MMPO** — [Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2605.30159) (2026)  `state: written` `credit: state`
- **SkillC** — [SKILLC: Learning Autonomous Skill Internalization in LLM Agents via Contrastive Credit Assignment](https://arxiv.org/abs/2605.27899) (2026)  `state: context` `credit: trajectory`
- **ReBel** — [Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents](https://arxiv.org/abs/2605.20061) (2026)  `state: written` `credit: state`
- **SERL selective hindsight distillation** — [What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents](https://arxiv.org/abs/2605.19447) (2026)  `state: context` `credit: interaction`
- **CAVE** — [CAVE: A Structured Credit Assignment Approach for Fragmented Visual Evidence Reasoning](https://arxiv.org/abs/2605.16416) (2026)  `state: context` `credit: interaction`
- **PiCA pivot-based credit** — [PiCA: Pivot-Based Credit Assignment for Search Agentic Reinforcement Learning](https://arxiv.org/abs/2605.09287) (2026)  `state: context` `credit: trajectory`
- **TRACE turn credit for jailbreaking** — [Not All Turns Matter: Credit Assignment for Multi-Turn Jailbreaking](https://arxiv.org/abs/2605.08778) (2026)  `state: context` `credit: interaction`
- **MDLM text world models** — [Masked Diffusion Language Models are Strong and Steerable Text-Based World Models for Agentic RL](https://arxiv.org/abs/2607.16204) (2026)  `state: world model` `credit: world-model loss`
- **TreeMem** — [Tree-based Credit Assignment for Multi-Agent Memory System](https://arxiv.org/abs/2605.04811) (2026)  `state: store` `credit: memory op`
- **BOND (distilling Bayesian beliefs)** — [Distilling Bayesian Belief States into Language Models for Auditable Negotiation](https://arxiv.org/abs/2605.04507) (2026)  `state: written` `credit: state`
- **AEM adaptive entropy modulation** — [AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning](https://arxiv.org/abs/2605.00425) (2026)  `state: context` `credit: trajectory`
- **CAPO: critic-guided action-aligned PO** — [CAPO: Critic-Guided Action-Aligned Policy Optimization for Advancing LLM Agent Capabilities](https://arxiv.org/abs/2604.18401) (2026)  `state: context` `credit: interaction`
- **UI-Copilot** — [UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization](https://arxiv.org/abs/2604.13822) (2026, ACL 2026)  `state: store` `credit: interaction`
- **ToMAgent lookahead ToM** — [Infusing Theory of Mind into Socially Intelligent LLM Agents](https://arxiv.org/abs/2509.22887) (2026, Annual Meeting of the Association for Computational Linguistics)  `state: written` `credit: state`
- **OASES** — [OASES: Outcome-Aligned Search-Evaluation Co-Training for Agentic Search](https://arxiv.org/abs/2604.03675) (2026)  `state: context` `credit: state`
- **Self-Guide internal reward co-evolution** — [Co-Evolution of Policy and Internal Reward for Language Agents](https://arxiv.org/abs/2604.03098) (2026)  `state: written` `credit: trajectory`
- **MT-GRPO Iterative Reward Calibration** — [Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration](https://arxiv.org/abs/2604.02869) (2026)  `state: context` `credit: interaction`
- **HISR** — [HISR: Hindsight Information Modulated Segmental Process Rewards For Multi-turn Agentic Reinforcement Learning](https://arxiv.org/abs/2603.18683) (2026)  `state: context` `credit: interaction`
- **SLEA-RL: step-level experience augmentation** — [SLEA-RL: Step-Level Experience Augmented Reinforcement Learning for Multi-Turn Agentic Training](https://arxiv.org/abs/2603.18079) (2026)  `state: store` `credit: trajectory`
- **CoMAM** — [Joint Optimization of Multi-agent Memory System](https://arxiv.org/abs/2603.12631) (2026)  `state: store` `credit: memory op`
- **TIPS** — [TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs](https://arxiv.org/abs/2603.22293) (2026)  `state: context` `credit: interaction`
- **HCAPO hindsight critic** — [Hindsight Credit Assignment for Long-Horizon LLM Agents](https://arxiv.org/abs/2603.08754) (2026)  `state: context` `credit: trajectory`
- **MICA: intertemporal credit for emotional support** — [MICA: Multi-granularity Intertemporal Credit Assignment for Long-Horizon Emotional Support Dialogue](https://arxiv.org/abs/2603.06194) (2026)  `state: store` `credit: interaction`
- **EvoTool** — [EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection](https://arxiv.org/abs/2603.04900) (2026, Annual Meeting of the Association for Computational Linguistics)  `state: context` `credit: interaction`
- **HiPER: hierarchical RL with explicit credit assignment** — [HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents](https://arxiv.org/abs/2602.16165) (2026)  `state: context` `credit: trajectory`
- **ELPO** — [Learning from the Irrecoverable: Error-Localized Policy Optimization for Tool-Integrated LLM Reasoning](https://arxiv.org/abs/2602.09598) (2026, Annual Meeting of the Association for Computational Linguistics)  `credit: interaction`
- **HumanLM state alignment** — [HumanLM: Simulating Users with State Alignment Beats Response Imitation](https://arxiv.org/abs/2603.03303) (2026)  `state: written` `credit: state`
- **world models as intermediary** — [World Models as an Intermediary between Agents and the Real World](https://arxiv.org/abs/2602.00785) (2026)  `state: world model` `credit: world-model loss`
- **SDPO** — [Reinforcement Learning via Self-Distillation](https://arxiv.org/abs/2601.20802) (2026)  `state: context` `credit: output`
- **MatchTIR** — [MatchTIR: Fine-Grained Supervision for Tool-Integrated Reasoning via Bipartite Matching](https://arxiv.org/abs/2601.10712) (2026, ACL 2026)  `state: context` `credit: interaction`
- **SuS strategy-aware surprise** — [SuS: Strategy-aware Surprise for Intrinsic Exploration](https://arxiv.org/abs/2601.10349) (2026)  `state: context` `credit: output`
- **MATTRL test-time multi-agent RL** — [Collaborative Multi-Agent Test-Time Reinforcement Learning for Reasoning](https://arxiv.org/abs/2601.09667) (2026)  `state: store` `credit: interaction`
- **Fine-Mem** — [Fine-Mem: Fine-Grained Feedback Alignment for Long-Horizon Memory Management](https://arxiv.org/abs/2601.08435) (2026)  `state: store` `credit: memory op`
- **SCRIBE** — [SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models](https://arxiv.org/abs/2601.03555) (2026)  `state: context` `credit: interaction`
- **AgeMem** — [Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents](https://arxiv.org/abs/2601.01885) (2026, ACL 2026)  `state: store` `credit: memory op`
- **ToolVerse** — [ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.15660) (2026)  `state: context` `credit: interaction`
- **BRAID** — [Bridging Interleaved Multi-Modal Reasoning as a Unified Decision Process](https://arxiv.org/abs/2607.03748) (2026)  `credit: interaction`
- **SGCD sibling-guided credit** — [Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2606.12634) (2026)  `credit: output`
- **APPO** — [APPO: Agentic Procedural Policy Optimization](https://arxiv.org/abs/2606.12384) (2026)  `credit: output`
- **SkillOS** — [SkillOS: Learning Skill Curation for Self-Evolving Agents](https://arxiv.org/abs/2605.06614) (2026)  `state: store` `credit: memory op`
- **RL recipe long-horizon tool agents** — [Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe](https://arxiv.org/abs/2603.21972) (2026)  `state: context` `credit: trajectory`
- **SE-Search** — [SE-Search: Self-Evolving Search Agent via Memory and Dense Reward](https://arxiv.org/abs/2603.03293) (2026)  `state: store` `credit: memory op`
- **HGPO** — [Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks](https://arxiv.org/abs/2602.22817) (2026)  `credit: interaction`
- **SkillRL** — [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](https://arxiv.org/abs/2602.08234) (2026)  `state: store` `credit: trajectory`
- **BranPO** — [BranPO: Scalable Contrastive Branch Sampling for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2602.03719) (2026)  `credit: interaction`
- **SHADOW** — SHADOW: Dynamic-Aware Credit Assignment Against Long-Horizon Tasks (2026, AAAI 2026)  `state: context` `credit: interaction`

**2025**

- **GenEnv** — [GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators](https://arxiv.org/abs/2512.19682) (2025)  `state: world model` `credit: trajectory`
- **Turn-PPO** — [Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs](https://arxiv.org/abs/2512.17008) (2025, EACL 2026)  `state: context` `credit: interaction`
- **WMAct** — [Thinking by Doing: Building Efficient World Model Reasoning in LLMs via Multi-turn Interaction](https://arxiv.org/abs/2511.23476) (2025)  `state: context` `credit: output`
- **MindPower** — [MindPower: Enabling Theory-of-Mind Reasoning in VLM-based Embodied Agents](https://arxiv.org/abs/2511.23055) (2025, CVPR 2026)  `state: written` `credit: output`
- **SORL** — [Stabilizing Off-Policy Training for Long-Horizon LLM Agent via Turn-Level Importance Sampling and Clipping-Triggered Normalization](https://arxiv.org/abs/2511.20718) (2025)  `state: context` `credit: interaction`
- **Agent-R1** — [Agent-R1: A Unified and Modular Framework for Agentic Reinforcement Learning](https://arxiv.org/abs/2511.14460) (2025)  `state: context` `credit: trajectory`
- **AgentPRM** — [AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress](https://arxiv.org/abs/2511.08325) (2025, The Web Conference)  `state: context` `credit: interaction`
- **DeepAgent** — [DeepAgent: A General Reasoning Agent with Scalable Toolsets](https://arxiv.org/abs/2510.21618) (2025, WWW 2026)  `state: store` `credit: interaction`
- **VAGEN** — [VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents](https://arxiv.org/abs/2510.16907) (2025)  `state: written` `credit: state`
- **MARSHAL** — [MARSHAL: Incentivizing Multi-Agent Reasoning via Self-Play with Strategic LLMs](https://arxiv.org/abs/2510.15414) (2025)  `credit: interaction`
- **SPA** — [Why Do LLM Agents Fail in Exploring New Environments? A World-Modeling Perspective](https://arxiv.org/abs/2510.15047) (2025)  `state: world model` `credit: world-model loss`
- **IGPO** — [Information Gain-based Policy Optimization: A Simple and Effective Approach for Multi-Turn Search Agents](https://arxiv.org/abs/2510.14967) (2025)  `state: context` `credit: interaction`
- **T3** — [T3: Reducing Belief Deviation in Reinforcement Learning for Active Reasoning](https://arxiv.org/abs/2510.12264) (2025, ICLR 2026)  `state: probabilistic store` `credit: trajectory`
- **Demystifying agentic RL** — [Demystifying Reinforcement Learning in Agentic Reasoning](https://arxiv.org/abs/2510.11701) (2025)  `state: context` `credit: trajectory`
- **AgentFlow** — [In-the-Flow Agentic System Optimization for Effective Planning and Tool Use](https://arxiv.org/abs/2510.05592) (2025)  `state: store` `credit: trajectory`
- **MATPO** — [Multi-Agent Tool-Integrated Policy Optimization](https://arxiv.org/abs/2510.04678) (2025)  `credit: trajectory`
- **PPR** — [Hybrid Reward Normalization for Process-supervised Non-verifiable Agentic Tasks](https://arxiv.org/abs/2509.25598) (2025)  `state: context` `credit: trajectory`
- **GUI-Shepherd** — [GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks](https://arxiv.org/abs/2509.23738) (2025)  `credit: interaction`
- **iStar** — [Agentic Reinforcement Learning with Implicit Step Rewards](https://arxiv.org/abs/2509.19199) (2025)  `state: context` `credit: interaction`
- **TARL** — [Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents](https://arxiv.org/abs/2509.14480) (2025)  `state: context` `credit: interaction`
- **EMPG** — [Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents](https://arxiv.org/abs/2509.09265) (2025)  `state: context` `credit: interaction`
- **Memory-R1** — [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828) (2025, ACL 2025)  `state: store` `credit: memory op`
- **Agent Lightning** — [Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://arxiv.org/abs/2508.03680) (2025)  `state: context` `credit: interaction`
- **FLAG-TRADER** — [FLAG-TRADER: Fusion LLM-Agent with Gradient-based Reinforcement Learning for Financial Trading](https://arxiv.org/abs/2502.11433) (2025, Findings of ACL 2025)  `state: context` `credit: interaction`
- **ARPO** — [Agentic Reinforced Policy Optimization](https://arxiv.org/abs/2507.19849) (2025)  `state: context` `credit: trajectory`
- **ECON** — [From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian Nash Equilibrium](https://arxiv.org/abs/2506.08292) (2025, International Conference on Machine Learning)  `state: external filter` `credit: trajectory`
- **TTI (Thinking vs Doing)** — [Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interaction](https://arxiv.org/abs/2506.07976) (2025)  `state: context` `credit: trajectory`
- **Dyna-Think** — [Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents](https://arxiv.org/abs/2506.00320) (2025)  `state: world model` `credit: world-model loss`
- **Beyond Markovian** — [Beyond Markovian: Reflective Exploration via Bayes-Adaptive RL for LLM Reasoning](https://arxiv.org/abs/2505.20561) (2025)  `state: context` `credit: trajectory`
- **DEL-ToM** — [DEL-ToM: Inference-Time Scaling for Theory-of-Mind Reasoning via Dynamic Epistemic Logic](https://arxiv.org/abs/2505.17348) (2025, Conference on Empirical Methods in Natural Language Processing)  `state: written` `credit: state`
- **WebAgent-R1** — [WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2505.16421) (2025, EMNLP 2025)  `state: context` `credit: trajectory`
- **ARPO** — [ARPO:End-to-End Policy Optimization for GUI Agents with Experience Replay](https://arxiv.org/abs/2505.16282) (2025)  `state: context` `credit: trajectory`
- **SearchRLStudy** — [An Empirical Study on Reinforcement Learning for Reasoning-Search Interleaved LLM Agents](https://arxiv.org/abs/2505.15117) (2025)  `state: context` `credit: trajectory`
- **StepSearch** — [StepSearch: Igniting LLMs Search Ability via Step-Wise Proximal Policy Optimization](https://arxiv.org/abs/2505.15107) (2025, EMNLP 2025)  `state: context` `credit: interaction`
- **RLVR-World** — [RLVR-World: Training World Models with Reinforcement Learning](https://arxiv.org/abs/2505.13934) (2025, Neural Information Processing Systems)  `state: world model` `credit: world-model loss`
- **Fine-Grained Reward Credit** — [Reinforcing Multi-Turn Reasoning in LLM Agents via Fine-Grained Reward Structure and Credit Assignment](https://arxiv.org/abs/2505.11821) (2025)  `state: context` `credit: interaction`
- **GiGPO** — [Group-in-Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2505.10978) (2025, NeurIPS 2025)  `credit: trajectory`
- **ZeroSearch** — [ZeroSearch: Incentivize the Search Capability of LLMs without Searching](https://arxiv.org/abs/2505.04588) (2025)  `state: context` `credit: trajectory`
- **RAGEN / StarPO** — [RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2504.20073) (2025)  `state: context` `credit: trajectory`
- **ToolRL** — [ToolRL: Reward is All Tool Learning Needs](https://arxiv.org/abs/2504.13958) (2025, NeurIPS 2025)  `state: context` `credit: output`
- **ReTool** — [ReTool: Reinforcement Learning for Strategic Tool Use in LLMs](https://arxiv.org/abs/2504.11536) (2025)  `state: context` `credit: trajectory`
- **ReSearch** — [ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning](https://arxiv.org/abs/2503.19470) (2025, NeurIPS 2025)  `state: context` `credit: output`
- **Bayesian teaching** — [Bayesian Teaching Enables Probabilistic Reasoning in Large Language Models](https://arxiv.org/abs/2503.17523) (2025, Nature Communications)  `state: written` `credit: state`
- **SWEET-RL** — [SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks](https://arxiv.org/abs/2503.15478) (2025)  `credit: interaction`
- **Search-R1** — [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/abs/2503.09516) (2025)  `state: context` `credit: output`
- **LOOP** — [Reinforcement Learning for Long-Horizon Interactive LLM Agents](https://arxiv.org/abs/2502.01600) (2025)  `state: context` `credit: trajectory`
- **CollabLLM** — [CollabLLM: From Passive Responders to Active Collaborators](https://arxiv.org/abs/2502.00640) (2025, International Conference on Machine Learning)  `state: context` `credit: interaction`
- **Memento 2 stateful reflective memory** — [Memento 2: Learning by Stateful Reflective Memory](https://arxiv.org/abs/2512.22716) (2025)  `state: store` `credit: memory op`
- **GTR-Turbo** — [GTR-Turbo: Merged Checkpoint is Secretly a Free Teacher for Agentic VLM Training](https://arxiv.org/abs/2512.13043) (2025)  `credit: trajectory`
- **STARE-VLA** — [STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models](https://arxiv.org/abs/2512.05107) (2025)  `credit: interaction`
- **CriticSearch** — [CriticSearch: Fine-Grained Credit Assignment for Search Agents via a Retrospective Critic](https://arxiv.org/abs/2511.12159) (2025, ACL 2026)  `credit: interaction`
- **SALT** — [SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph](https://arxiv.org/abs/2510.20022) (2025, EACL 2026)  `credit: interaction`
- **SPA-RL** — [SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution](https://arxiv.org/abs/2505.20732) (2025)  `credit: interaction`
- **ReasonRAG** — [Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning](https://arxiv.org/abs/2505.14069) (2025, Neural Information Processing Systems)  `state: context` `credit: interaction`

**2024**

- **WebRL** — [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337) (2024, ICLR 2025)  `credit: output`
- **DistRL** — [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://arxiv.org/abs/2410.14803) (2024, International Conference on Learning Representations)  `state: context` `credit: trajectory`
- **SCoRe** — [Training Language Models to Self-Correct via Reinforcement Learning](https://arxiv.org/abs/2409.12917) (2024, ICLR 2025)  `state: context` `credit: interaction`
- **DigiRL** — [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://arxiv.org/abs/2406.11896) (2024, NeurIPS 2024)  `state: context` `credit: interaction`
- **AgentGym** — [AgentGym: Evolving Large Language Model-based Agents across Diverse Environments](https://arxiv.org/abs/2406.04151) (2024)  `state: context` `credit: trajectory`
- **r to Q*** — [From $r$ to $Q^*$: Your Language Model is Secretly a Q-Function](https://arxiv.org/abs/2404.12358) (2024)  `credit: output`
- **Agent-FLAN** — [Agent-FLAN: Designing Data and Methods of Effective Agent Tuning for Large Language Models](https://arxiv.org/abs/2403.12881) (2024, Annual Meeting of the Association for Computational Linguistics)  `state: context` `credit: trajectory`
- **SOTOPIA-pi** — [SOTOPIA-pi: Interactive Learning of Socially Intelligent Language Agents](https://arxiv.org/abs/2403.08715) (2024)  `credit: output`
- **ArCHer** — [ArCHer: Training Language Model Agents via Hierarchical Multi-Turn RL](https://arxiv.org/abs/2402.19446) (2024, ICML 2024)  `credit: interaction`
- **POAD** — Reinforcing LLM Agents via Policy Optimization with Action Decomposition (2024, NeurIPS 2024)  `state: context` `credit: interaction`

**2023**

- **Math-Shepherd** — [Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations](https://arxiv.org/abs/2312.08935) (2023, Annual Meeting of the Association for Computational Linguistics)  `credit: output`
- **LLaRP** — [Large Language Models as Generalizable Policies for Embodied Tasks](https://arxiv.org/abs/2310.17722) (2023, International Conference on Learning Representations)  `state: context` `credit: trajectory`
- **AgentTuning** — [AgentTuning: Enabling Generalized Agent Abilities for LLMs](https://arxiv.org/abs/2310.12823) (2023, ACL 2024 Findings)  `state: context` `credit: trajectory`
- **FireAct** — [FireAct: Toward Language Agent Fine-tuning](https://arxiv.org/abs/2310.05915) (2023)  `state: context` `credit: trajectory`
- [Let's verify step by step](https://arxiv.org/abs/2305.20050) (2023, International Conference on Learning Representations)  `credit: output`
- **DPO** — [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) (2023, Neural Information Processing Systems)  `credit: output`

**2022**

- **LLMs Can Self-Improve** — [Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610) (2022, EMNLP 2023)  `credit: output`
- **ILQL** — [Offline RL for Natural Language Generation with Implicit Language Q Learning](https://arxiv.org/abs/2206.11871) (2022, International Conference on Learning Representations)  `state: context` `credit: trajectory`

**2021**

- **WebGPT** — [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332) (2021)  `state: context` `credit: trajectory`

## Likelihood term as a choice of evidence

Systems whose belief decides what to observe next.


**2026**

- **REFLEX (Jev)** — [REFLEX with Jev for Efficient Selective Control in LLM Agents](https://arxiv.org/abs/2609.26532) (2026)  `state: context`
- **FinalityBench** — [FinalityBench: An Effect-Level Benchmark for Agent Decisions Under Delayed and Conflicting Financial Finality](https://arxiv.org/abs/2609.04706) (2026)  `state: context`
- **LENS** — [LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents](https://arxiv.org/abs/2608.16185) (2026)  `state: probabilistic store`
- **EnvACE world rehearsal** — [EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.06197) (2026)  `state: world model` `credit: trajectory`
- **KbSD** — [KbSD: Knowledge Boundary aware Self-Distillation for Behavioral Calibration in Agentic Search](https://arxiv.org/abs/2606.29863) (2026)  `state: context` `credit: output`
- **Governance-aware POMDP for AI delegation** — [Adaptive AI Delegation under Uncertainty: A Bayesian Governance Policy for Sequential Decision Authority](https://arxiv.org/abs/2606.29406) (2026)  `state: external filter`
- **Bayesian-Agent** — [Bayesian-Agent: Posterior-Guided Skill Evolution Across LLM Agent Harnesses](https://arxiv.org/abs/2606.08348) (2026)  `state: external filter`
- **CA-BED** — [CA-BED: Conversation-Aware Bayesian Experimental Design](https://arxiv.org/abs/2606.01182) (2026)  `state: probabilistic store`
- **BAG** — [Clarify, Abstain or Answer? Strategising in Conversation with Belief-Augmented Generation](https://arxiv.org/abs/2605.25831) (2026)  `state: context`
- **MedExAgent** — [MedExAgent: Training LLM Agents to Ask, Examine, and Diagnose in Noisy Clinical Environments](https://arxiv.org/abs/2605.07058) (2026)  `state: context` `credit: output`
- **Context Gathering Decision Process** — [The Context Gathering Decision Process: A POMDP Framework for Agentic Search](https://arxiv.org/abs/2605.07042) (2026)  `state: external filter`
- **Oblivion** — [Oblivion: Self-Adaptive Agentic Memory Control through Decay-Driven Activation](https://arxiv.org/abs/2604.00131) (2026)  `state: store` `credit: memory op`
- **EnterpriseArena** — [Can LLM Agents Be CFOs? Benchmarking Long-Horizon Resource Allocation in an Uncertain Enterprise Environment](https://arxiv.org/abs/2603.23638) (2026)  `state: context`
- **RetailBench long-horizon retail POMDP** — [RetailBench: Evaluating Long-Horizon Autonomous Decision-Making and Strategy Stability of LLM Agents in Realistic Retail Environments](https://arxiv.org/abs/2603.16453) (2026)  `state: context`
- **REDEREF: training-free probabilistic multi-agent control** — [Training-Free Agentic AI: Probabilistic Control and Coordination in Multi-Agent LLM Systems](https://arxiv.org/abs/2603.13256) (2026)  `state: probabilistic store` `credit: interaction`
- **Agents fail to use world models** — [Current Agents Fail to Leverage World Model as Tool for Foresight](https://arxiv.org/abs/2601.03905) (2026, Annual Meeting of the Association for Computational Linguistics)  `state: world model`
- **Bayesian orchestration** — [Bayesian Orchestration of Multi-LLM Agents for Cost-Aware Sequential Decision-Making](https://arxiv.org/abs/2601.01522) (2026)  `state: external filter` `credit: state`
- **InfoPO** — [InfoPO: Information-Driven Policy Optimization for User-Centric Agents](https://arxiv.org/abs/2603.00656) (2026)  `state: context` `credit: interaction`
- **FOREAGENT predict-before-execute** — [Can We Predict Before Executing Machine Learning Agents?](https://arxiv.org/abs/2601.05930) (2026, Annual Meeting of the Association for Computational Linguistics)  `state: world model`

**2025**

- **Align While Search** — [Align While Search: Belief-Guided Exploratory Inference for World-Grounded Embodied Agents](https://arxiv.org/abs/2512.24461) (2025)  `state: external filter`
- **R-WoM** — [R-WoM: Retrieval-augmented World Model For Computer-use Agents](https://arxiv.org/abs/2510.11892) (2025)  `state: world model`
- **Language and Experience** — [Language and Experience: A Computational Model of Social Learning in Complex Tasks](https://arxiv.org/abs/2509.00074) (2025)  `state: world model`
- **MindGames** — [Do Large Language Models Have a Planning Theory of Mind? Evidence from MindGames: a Multi-Step Persuasion Task](https://arxiv.org/abs/2507.16196) (2025, COLM 2025)
- **DeepResearcher** — [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://arxiv.org/abs/2504.03160) (2025, EMNLP 2025)  `state: context` `credit: trajectory`
- **R1-Searcher** — [R1-Searcher: Incentivizing the Search Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2503.05592) (2025)  `state: context` `credit: trajectory`
- **Ark / MedArk** — Ask and Retrieve Knowledge: Towards Proactive Asking with Imperfect Information in Medical Multi-turn Dialogues (2025, Annual International ACM SIGIR Conference on Research and Development in Information Retrieval)  `state: context` `credit: trajectory`

**2024**

- **InferAct** — [Preemptive Detection and Correction of Misaligned Actions in LLM Agents](https://arxiv.org/abs/2407.11843) (2024, Conference on Empirical Methods in Natural Language Processing)  `state: written` `credit: interaction`

**2023**

- **Self-RAG** — [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511) (2023, International Conference on Learning Representations)  `state: context` `credit: output`
- **DECKARD** — [Do Embodied Agents Dream of Pixelated Sheep?: Embodied Decision Making using Language Guided World Modelling](https://arxiv.org/abs/2301.12050) (2023, International Conference on Machine Learning)  `state: world model` `credit: world-model loss`

## Likelihood term as a metric

Belief-level evaluation and benchmarks: calibration, accuracy and revision, memory validity, Bayesian coherence, belief-action gap.


**2026**

- **EnterpriseBench** — [EnterpriseBench: Benchmarking LLM Agents on Enterprise-Level Strategic Reasoning and Decision-Making](https://arxiv.org/abs/2609.37658) (2026)  `state: context`
- **memory-bench construction** — Constructing a Benchmark When Every Component Is a Language Model (2026)  `state: store`
- **Regent Chess replication** — [Replication Without Persistence in Hosted LLMs: Measurement Sensitivity in Action-Time Belief Evaluation](https://arxiv.org/abs/2609.22478) (2026)  `state: written`
- **REE diagnostic for ICL in games** — [Recursive Reasoning or Statistical Extrapolation? In-Context Learning in Multi-Agent Interdependent Decision-Making](https://arxiv.org/abs/2609.18591) (2026)  `state: context`
- **Werewolf accusation belief-shift** — [Do LLMs Trust the Accuser or the Accusation? Measuring Belief Shifts in Werewolf](https://arxiv.org/abs/2609.12446) (2026)  `state: written`
- **ECCBench** — [Good Memory Has ECC: Evaluating the Memory of Vision-Language Models Beyond Accuracy](https://arxiv.org/abs/2609.00103) (2026)
- **Business Arena marketplace benchmark** — [Business Arena: Benchmarking LLM Agents in a Realistic Marketplace](https://arxiv.org/abs/2608.08621) (2026)  `credit: interaction`
- **Can LLM Agents Price Competitively? A Dynamic Multi-Attribut** — [Can LLM Agents Price Competitively? A Dynamic Multi-Attribute Auction Benchmark for Agentic Commerce](https://arxiv.org/abs/2608.00102) (2026)  `state: context`
- **Critic Experience Bank** — [Critic Experience Bank: Self-Evolving Step-Level Confidence Estimation for LLM Agents](https://arxiv.org/abs/2607.12397) (2026)  `state: store`
- **Conv-FinRe** — Conv-FinRe: A Conversational and Longitudinal Benchmark for Utility-Grounded Financial Recommendation (2026, SIGIR 2026)
- **BayesBench** — [BayesBench: Evaluating LLM Belief Trajectories Under Multi-Turn Evidence Accumulation](https://arxiv.org/abs/2606.30850) (2026)  `state: context`
- **FinBench calibration benchmark** — [FinBench: Time-Gated Calibration and Uncertainty Benchmarking for Agentic Financial Forecasting](https://arxiv.org/abs/2607.16229) (2026)  `credit: output`
- **POMDP validation framework** — [Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation](https://arxiv.org/abs/2606.17383) (2026)  `state: external filter`
- **Thinking-RFT for ToM** — [From Shortcuts to Reasoning: Robust Post-Training of Theory of Mind with Reinforcement Learning](https://arxiv.org/abs/2606.09092) (2026, ICML 2026)  `credit: output`
- **MINDGAMES live arena** — [MINDGAMES: A Live Arena for Evaluating Social and Strategic Reasoning in Multi-Agent LLMs](https://arxiv.org/abs/2605.29512) (2026)
- **WorldMemArena** — [WorldMemArena: Evaluating Multimodal Agent Memory Through Action-World Interaction](https://arxiv.org/abs/2605.29341) (2026)  `state: store`
- **Agent-ToM: learning to monitor agents via ToM** — [Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning](https://arxiv.org/abs/2605.24216) (2026)  `credit: trajectory`
- **MINTEval** — [MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems](https://arxiv.org/abs/2605.18565) (2026)
- **Does Theory of Mind Improvement Really Benefit Human-AI Inte** — [Does Theory of Mind Improvement Really Benefit Human-AI Interactions? Empirical Findings from Interactive Evaluations](https://arxiv.org/abs/2605.15205) (2026, Annual Meeting of the Association for Computational Linguistics)  `state: context`
- **Memora** — [From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents](https://arxiv.org/abs/2604.20006) (2026, Annual Meeting of the Association for Computational Linguistics)  `state: store`
- **LifeSim** — [LifeSim: Long-Horizon User Life Simulator for Personalized Assistant Evaluation](https://arxiv.org/abs/2603.12152) (2026, Annual Meeting of the Association for Computational Linguistics)  `state: context`
- **Theory of Space** — [Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration?](https://arxiv.org/abs/2602.07055) (2026)  `state: written`
- **STAGE** — [STAGE: A Full-Screenplay Benchmark for Reasoning over Evolving Stories](https://arxiv.org/abs/2601.08510) (2026)  `state: written` `credit: state`
- **CubeBench** — [CubeBench: Diagnosing Interactive, Long-Horizon Spatial Reasoning Under Partial Observations](https://arxiv.org/abs/2512.23328) (2026)
- **Parallel WebBench** — [When Web Agents Finish but Still Fail: Reproducible Triggers and Trace Diagnostics for Parallel Web Exploration](https://arxiv.org/abs/2606.20724) (2026)  `state: context` `credit: trajectory`
- **WMF-AM working memory probe** — [WMF-AM: Probing LLM Working Memory via Depth-Parameterized Cumulative State Tracking](https://arxiv.org/abs/2603.27343) (2026)  `state: context`

**2025**

- **Martingale Score** — [Martingale Score: An Unsupervised Metric for Bayesian Rationality in LLM Reasoning](https://arxiv.org/abs/2512.02914) (2025, Neural Information Processing Systems)  `state: context`
- **RecToM** — [RecToM: A Benchmark for Evaluating Machine Theory of Mind in LLM-based Conversational Recommender Systems](https://arxiv.org/abs/2511.22275) (2025, AAAI 2026)
- **ENACT** — [ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction](https://arxiv.org/abs/2511.20937) (2025)  `state: world model`
- **Evo-Memory** — [Evo-Memory: Benchmarking LLM Agent Test-time Learning with Self-Evolving Memory](https://arxiv.org/abs/2511.20857) (2025)  `state: store`
- **HaluMem** — [HaluMem: Evaluating Hallucinations in Memory Systems of Agents](https://arxiv.org/abs/2511.03506) (2025)  `state: store`
- **MemoryBench** — [MemoryBench: A Benchmark for Memory and Continual Learning in LLM Systems](https://arxiv.org/abs/2510.17281) (2025)  `state: store`
- **EvolveCast** — [Do Language Models Update their Forecasts with New Information?](https://arxiv.org/abs/2509.23936) (2025)  `state: context`
- **SoMi-ToM** — [SoMi-ToM: Evaluating Multi-Perspective Theory of Mind in Embodied Social Interactions](https://arxiv.org/abs/2506.23046) (2025, Neural Information Processing Systems)  `state: context`
- **MemBench** — [MemBench: Towards More Comprehensive Evaluation on the Memory of LLM-based Agents](https://arxiv.org/abs/2506.21605) (2025, Annual Meeting of the Association for Computational Linguistics)  `state: store`
- **tau2-bench** — [tau2-Bench: Evaluating Conversational Agents in a Dual-Control Environment](https://arxiv.org/abs/2506.07982) (2025)
- **DIAMONDs** — [$\textttDIAMONDs$: A Dataset for $\mathbbD$ynamic $\mathbbI$nformation $\mathbbA$nd $\mathbbM$ental modeling $\mathbbO$f $\mathbbN$umeric $\mathbbD$iscussions](https://arxiv.org/abs/2505.12651) (2025)
- **LifelongAgentBench** — [LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners](https://arxiv.org/abs/2505.11942) (2025)  `state: store`
- **PersuasiveToM** — [PersuasiveToM: A Benchmark for Evaluating Machine Theory of Mind in Persuasive Dialogues](https://arxiv.org/abs/2502.21017) (2025)
- **Vending-Bench** — [Vending-Bench: A Benchmark for Long-Term Coherence of Autonomous Agents](https://arxiv.org/abs/2502.15840) (2025)  `state: store`
- **Text2World** — [Text2World: Benchmarking Large Language Models for Symbolic World Model Generation](https://arxiv.org/abs/2502.13092) (2025, Annual Meeting of the Association for Computational Linguistics)  `state: world model` `credit: output`
- **PrefEval** — [Do LLMs Recognize Your Preferences? Evaluating Personalized Preference Following in LLMs](https://arxiv.org/abs/2502.09597) (2025, International Conference on Learning Representations)  `state: context`
- **ToMATO** — [ToMATO: Verbalizing the Mental States of Role-Playing LLMs for Benchmarking Theory of Mind](https://arxiv.org/abs/2501.08838) (2025, AAAI Conference on Artificial Intelligence)  `state: context`
- **UltraHorizon** — [UltraHorizon: Benchmarking Agent Capabilities in Ultra Long-Horizon Scenarios](https://arxiv.org/abs/2509.21766) (2025)  `state: context`

**2024**

- **SimpleToM** — [SimpleToM: Exposing the Gap between Explicit ToM Inference and Implicit ToM Application in LLMs](https://arxiv.org/abs/2410.13648) (2024, ICLR 2026)
- **LongMemEval** — [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813) (2024, ICLR 2025)  `state: store`
- **Embodied Agent Interface** — [Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making](https://arxiv.org/abs/2410.07166) (2024, Neural Information Processing Systems)  `state: world model`
- **MuMA-ToM** — [MuMA-ToM: Multi-modal Multi-Agent Theory of Mind](https://arxiv.org/abs/2408.12574) (2024, AAAI Conference on Artificial Intelligence)  `state: world model`
- **AppWorld** — [AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents](https://arxiv.org/abs/2407.18901) (2024, ACL 2024)  `state: context`
- **Belief-R** — [Belief Revision: The Adaptability of Large Language Models Reasoning](https://arxiv.org/abs/2406.19764) (2024, EMNLP 2024)  `state: context`
- **tau-bench** — [tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045) (2024)
- **NegotiationToM** — [NegotiationToM: A Benchmark for Stress-testing Machine Theory of Mind on Negotiation Surrounding](https://arxiv.org/abs/2404.13627) (2024, Conference on Empirical Methods in Natural Language Processing)
- **LoCoMo** — [Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753) (2024, ACL 2024)  `credit: output`
- **ToMBench** — [ToMBench: Benchmarking Theory of Mind in Large Language Models](https://arxiv.org/abs/2402.15052) (2024, Annual Meeting of the Association for Computational Linguistics)
- **FortUne Dial** — [Deal, or no deal (or who knows)? Forecasting Uncertainty in Conversations using Large Language Models](https://arxiv.org/abs/2402.03284) (2024, ACL 2024)  `state: context` `credit: output`
- **VisualWebArena** — [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://arxiv.org/abs/2401.13649) (2024, ACL 2024)  `credit: output`
- **MMToM-QA** — [MMToM-QA: Multimodal Theory of Mind Question Answering](https://arxiv.org/abs/2401.08743) (2024, Annual Meeting of the Association for Computational Linguistics)  `state: probabilistic store`
- **MemSim** — [MemSim: A Bayesian Simulator for Evaluating Memory of LLM-based Personal Assistants](https://arxiv.org/abs/2409.20163) (2024, Neural Information Processing Systems)  `state: store`
- **Common-ToM** — [Views Are My Own, But Also Yours: Benchmarking Theory of Mind using Common Ground](https://arxiv.org/abs/2403.02451) (2024, Annual Meeting of the Association for Computational Linguistics)  `state: written`

**2023**

- **FANToM** — [FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions](https://arxiv.org/abs/2310.15421) (2023, Conference on Empirical Methods in Natural Language Processing)  `state: context`
- **SmartPlay** — [SmartPlay: A Benchmark for LLMs as Intelligent Agents](https://arxiv.org/abs/2310.01557) (2023, ICLR 2024)  `credit: output`
- **AgentBench** — [AgentBench: Evaluating LLMs as Agents](https://arxiv.org/abs/2308.03688) (2023, ICLR 2024)  `credit: output`
- **Clever Hans N-ToM** — [Clever Hans or Neural Theory of Mind? Stress Testing Social Reasoning in Large Language Models](https://arxiv.org/abs/2305.14763) (2023, Conference of the European Chapter of the Association for Computational Linguistics)  `state: context`
- **HI-TOM** — [HI-TOM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in Large Language Models](https://arxiv.org/abs/2310.16755) (2023, Findings of EMNLP 2023)  `state: context`
- **WebArena** — [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) (2023, ICLR 2024)  `state: context`

**2022**

- **WebShop** — [WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents](https://arxiv.org/abs/2207.01206) (2022, NeurIPS 2022)  `state: context`
- **PlanBench** — [PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change](https://arxiv.org/abs/2206.10498) (2022, NeurIPS 2023 Datasets and Benchmarks)  `credit: output`

**2020**

- **ALFWorld** — [ALFWorld: Aligning Text and Embodied Environments for Interactive Learning](https://arxiv.org/abs/2010.03768) (2020, ICLR 2021)  `credit: output`

## Background

- **ToM and decision science typology** — Theory of mind and decision science: Towards a typology of tasks and computational models. (2020, Neuropsychologia)

## Updates

- **2026-09 (monthly update)** — 29 papers added from the September 2026 window (434 rule-screened candidates, 47 read in full; papers already in the survey corpus skipped). Belief-credited additions: CORE (probabilistic persona belief, PPO reward scores it against gold slot values), GAVEL and Infinite-Parameter LLMs (known answer). Also MoM/P-Mem, Forecast-Dojo, Bayesian Chronicle Agents, Rank-Bounded Memory and others. No survey claim affected.
- **2026-09** — initial release with the survey preprint: 485 papers (2020 to September 2026), five keyword and citation-tree rounds plus a targeted round around belief-level self-supervision (ReBel, ABBEL, PaW, Dark Room).

## How the list is maintained

The list is generated from a screening record, not edited by hand: `lit_search/runs/20260916_v3/manual_screen_all_v*.csv` (518 included papers, 181 peer-reviewed) holds one row per paper with who maintains the belief, the credited object, the revision signal, whether a belief-level metric is reported, and notes. Each month `lit_search/monthly_update.py` runs the keyword queries on OpenAlex and a phrase search on Hugging Face Papers for the new month, applies the same rule screen, and removes everything already seen; the survivors are read in full, coded, merged with `merge_update.py`, and this README is regenerated with `make_readme.py`. The procedure is in [`UPDATE.md`](UPDATE.md); the search protocol behind the survey is in Appendix A of the paper.

```bash
cd lit_search
echo YOUR_OPENALEX_KEY > .openalex_key      # not committed
python3 monthly_update.py 2026-10            # candidates for one month
python3 merge_update.py 2026-10              # after full-text screening
python3 make_readme.py ../README.md
```

## Contributing

Missing a paper? Open an issue or a pull request with the arXiv link and one line saying which term of the belief it supplies (state, transition, or likelihood) and where that term comes from. Papers are included if they concern a language-model agent and construct, revise, test, learn, or evaluate an explicit state carried between decisions, or document a failure of such a state.

## Citation

```bibtex
@misc{huang2026frommemory,
  title={From Memory to Testable Belief: A Survey of LLM Agents},
  author={Huang, Jimin and Wang, Yuyan and Peng, Xueqing and Ananiadou, Sophia and Tsujii, Jun'ichi},
  year={2026},
  howpublished={\url{https://github.com/jiminHuang/belief-state-survey}},
  note={SSRN preprint 7493158}
  doi={10.2139/ssrn.7493158}
}
```
