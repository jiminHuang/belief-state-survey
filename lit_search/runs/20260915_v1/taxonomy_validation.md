# Taxonomy validation after close-reading the 2026 shortlist (run 20260915_v1)

## Paper-collection numbers (for the survey's methodology paragraph)

| Stage | Count |
|---|---|
| Queries (5 sections × 4–5 keywords) | 23 |
| Source A: OpenAlex, all venues, 2025-01-01→, raw hits / unique | 1150 / 715 |
| Source B: OpenAlex restricted to arXiv, 2026-01-01→, raw hits / unique | 1150 / 1008 |
| Merged unique (by DOI/id) | 1685 |
| After title-level dedup (preprint + journal versions) | 1460 |
| Excluded: no/short abstract | 45 |
| Excluded I1: no LLM term in title+abstract | 160 |
| Excluded E1: off-domain application | 35 |
| Excluded I2: < 2 topic terms | 357 |
| Included after rule screening | 863 |
| Of which published 2026 | 656 |
| Manually full-text screened (top-70 by relevance score, 2026) | 27 read so far |

arXiv's own API returned persistent HTTP 429 from this machine; Source B is the OpenAlex mirror of arXiv,
which lags arXiv by a few days. Rerun `search_arxiv.py` from another network to fill the gap.

## What the close reading changed in the taxonomy

### 1. The "state-level row is nearly empty" claim is no longer true, and that is the survey's hook
Between 2026-04 and 2026-09 at least 12 papers put an explicit belief state into an LLM agent
(Belief-State Engine, Belief at Risk, POMDP validation framework, BLF, Agent-BRACE, CBM/BeliefTrack,
BeliefMem, BB-WM, BOND, plus BSPO). None of the five surveys published in the same window (Horizon Gap,
credit-assignment survey, memory-evolution survey, forecasting-agents survey, UQ-for-agents taxonomy) has a
belief-state category. Revised gap statement: *belief state appears as a component inside memory, planning,
training and evaluation surveys, but never as the organizing object; the 2026 cluster has no shared
formalism, no shared metrics, and no comparison.*

### 2. New axis for Section 3 (representation): who maintains the belief
Close reading splits the 2026 cluster cleanly into three columns, which the outline did not have:
- **External Bayesian filter, LLM as observation model** — Belief-State Engine, Belief at Risk, POMDP
  validation framework. Belief is a probability vector over latent regimes; LLM never writes it.
- **Model-written belief in text** — Agent-BRACE (claims + ordinal certainty), BLF (probability + evidence
  summary), BOND (posterior tags), CBM (predicted belief state), BSPO (temporal factor graph). This is the
  column BSPO belongs to; the distinguishing sub-axis is whether the written belief is *testable*
  (BSPO PREDICT, CBM symbolic verification) or only *calibrated* (Agent-BRACE, BLF).
- **Learned world-model belief exposed to the policy** — BB-WM, text world models, POMDP world models with
  LM priors.
Probabilistic memory (BeliefMem, Noisy-OR) sits between the first two.

### 3. Section 4 (revision) gets a validated failure-mode taxonomy
Adopt CBM's three failure modes as the spine: **failed stay / failed update / failed isolation**, and add
a fourth that CBM does not have but STOCKTAKE, Agent-BRACE and BSPO all document: **failed act**
(belief revised, action not). Sub-themes with 2026 evidence:
- staleness detection: STALE, When Stale Constraints Go Unchecked, When Memory Updates but Behavior Does Not
- contradiction resolution: TOKI (4 operator families), MemOps (update/forget ops)
- surprise-gated revision: D-MEM (reward prediction error routing), BSPO (cross-span SURPRISE)
- belief–action gap: STOCKTAKE (knowing-doing rate 34–43 %), BSPO (prediction ≈ oracle, action ≈ random)

### 4. Section 5 (learning signals): state-level training now has four instances
- RL with belief-state rewards: CBM (−71 % failures), Agent-BRACE (joint belief + policy RL), BSPO
  (operation-level advantages routed through SURPRISE).
- Distillation of a Bayesian teacher's posterior: BOND.
Keep the credit-assignment survey (69 papers) as the reference for step-level methods and cite ECPO /
GiGPO / HiPER / IAPO / Memory-R2 as the "denser credit" line; cite "Explore More, Drift Less" as the
counter-position (outcome-only can suffice). The survey's argument becomes: denser credit and state-level
credit are orthogonal axes, and 2026 evidence supports both.

### 5. Section 7 (evaluation): belief-level metrics exist and are fragmented
Collected from 2026 papers, none of which cite each other:
- calibration over a trajectory: TC-ECE (UQ taxonomy), belief calibration (Agent-BRACE, BSE)
- posterior entropy, belief drift (Belief at Risk)
- turn-level exact belief accuracy with symbolic verification (BeliefTrack)
- revision accuracy, drift coherence, contradiction resolution, evidence sensitivity (BeliefShift)
- state resolution, premise resistance, implicit policy adaptation (STALE)
- symptom detection lag, skill score vs Bayes-filter oracle, knowing-doing rate (STOCKTAKE)
- operation-level probes (MemOps)
- prediction accuracy, surprise alignment, revision latency, stale-factor persistence (BSPO)
Table 4 of the survey should be this list, grouped by construct (calibration / accuracy / revision /
belief–action). STOCKTAKE's "fair oracle" (exact Bayes filter per factor) is the same design as BSPO's
controlled environment and should be cited as convergent methodology.

### 6. Competing surveys to position against in Section 1 (all 2026)
| Survey | Scope | Organising axis | Belief category? |
|---|---|---|---|
| Horizon Gap (2608.06663) | 1547 papers | lifecycle × horizon | no |
| Credit assignment in RL for LLMs (2604.09459) | 69 papers | granularity × methodology | no |
| Memory evolution (2605.06716) | n/s | storage→reflection→experience | no |
| Forecasting agents (2608.23058) | n/s | architecture type | no |
| UQ for agents (2609.07395) | n/s | what / how / where | partial (uncertainty, not state) |

## Still to do
- Full-text screen the remaining ~40 of the top-70 2026 list and rows 70–200 by score.
- Rerun `search_arxiv.py` from a non-rate-limited network to close the arXiv coverage gap.
- Add queries for "theory of mind belief modelling" and "opponent modelling" (OmniToM, Agent-ToM, BOND
  suggest a neighbouring cluster that the current queries reach only by accident).
