# LinkedIn copy for the SSRN preprint

Paste the SSRN link in the first comment rather than the post body (LinkedIn shows link-free posts to more people). Replace [SSRN] and [REPO] before posting.

---

## A. Main post (~200 words)

Language-model agents fail less often because they cannot reason than because they cannot keep track. The agent loses what it learned three steps ago, keeps acting on evidence that has since been contradicted, or revises what it believes and then does the same thing anyway.

Our new survey, *From Memory to Belief*, takes the object those failures are about — the belief an agent carries between decisions — and asks a simple question of 485 papers.

A belief has three parts: a **state** (what is believed, and how firmly), a **transition** (how it is carried across an action), and a **likelihood** (how the next observation scores it). Every system is placed by which parts it has and where each comes from: written by the model, fixed by the designer, learned, or absent.

The picture that comes out: memory research gave agents a state. Revision and post-training gave them a transition. The likelihood is still supplied from outside — by an oracle, a simulator, or a teacher. The first systems to score a written belief against the agent's own observations arrived this year, and their beliefs are binary, isolated, and fragile: one negative result shows that dense prediction rewards can collapse a GRPO-trained agent entirely.

Paper on SSRN, and the full paper list is a monthly-updated repository: [REPO]

With Yuyan Wang, Xueqing Peng, Sophia Ananiadou and Jun'ichi Tsujii. Thanks to The Fin AI community, and to the NVIDIA Academic Grant Program for the compute.

#LLM #AIAgents #NLP #MachineLearning #ReinforcementLearning

---

## B. Short version (for reposts or X)

Agents fail at state, not at reasoning.

New survey: a belief has a state, a transition, and a likelihood. We sorted 485 papers by which of the three a system has and where each comes from.

Memory gave agents the state. Post-training gave them the transition. The likelihood — the part that lets an agent's own observations correct what it believes — still comes from an oracle or a teacher almost everywhere.

Preprint: [SSRN] · Living paper list: [REPO]

---

## C. First comment (links)

Preprint: [SSRN]
Paper list, screening record and search pipeline (updated monthly): [REPO]
Happy to add anything we missed — issues and pull requests welcome.

---

## Notes before posting

- Push the public repository first; the awesome-list README and the v5 PDF are still local.
- Send the SSRN DOI so the README citation block and the repository footnote in the preprint carry it.
- Tag the co-authors and The Fin AI page; ask them to repost within the first hour.
