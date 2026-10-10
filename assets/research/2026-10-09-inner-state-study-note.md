# Feedback, integration instruments and tension mechanisms

Neurasoft public methods note · 9 October 2026

This is a curated, source-reviewed summary accompanying [When a machine’s inner state starts to matter](https://neurasoft.us/articles/when-inner-state-matters/). It reports internal work, not an independently reproduced publication. Private histories, original bodies, transcripts and full run archives are not included. The rate-network experiments and L.U.N.A software-organ simulations are distinct systems.

## 1. Preregistration 003: feedback-dose comparison

- Substrate: Neurasoft Core rate network v1.2, six modules; 32 separately seeded networks not used in its calibration. The subsequent source check reported 32 distinct weight hashes and distinct recorded random draws. This is within-study seed checking, not independent reproduction.
- Frozen runner: `da97289`; study freeze `3b3da0b`; calibration parameters `7519fe6`. The study ran once, with 192 system parts. This publication did not rerun it.
- Arms: original network with backward inter-module coupling scaled to 0, 0.25, 0.5 and 1; a fully feedforward counterpart; and an inter-module-feedforward counterpart retaining local recurrence.
- Matching: mean absolute activity within 10%; significant unit-by-time response density within 20% at selected pulse amplitudes where feasible. Selection used 40 paired matching trials; measurement used separate streams of 40 paired pulse/sham trials. PI used 80 trials. Infeasible matches counted against the hypothesis.
- Instrument: custom `pci_paired` response-complexity measure; software construction controls passed within its tested range. It is not the human clinical PCI procedure or an established machine-consciousness test.

| Preregistered comparison | Reported count | Reported median ratio | Rule and result |
|---|---:|---:|---|
| H1 PI construction pattern | 32/32 | Not applicable | Positive for backward-coupled arms, zero for the designated feedforward arms. Passed; a construction check, not exact IIT Φ validation. |
| H2 original vs fully feedforward | 26/32 | 1.24 | Required at least 28/32 and median at least 1.30. Failed. Three cases unmatched. |
| H3 original vs local-loop-only counterpart | 29/32 | 2.44 | Required at least 28/32 and median at least 1.30. Passed. Three cases unmatched. |
| H4 feedback-dose association | 31/32 | Full/zero feedback: 1.70 | Required positive rank association in at least 24/32 and median ratio at least 1.30. Passed. One case unmatched. |

**Post-hoc interpretation limit:** matched density was not matched spatial reach. The fully feedforward and local-loop-only counterparts typically responded with approximately half their units; the original recruited approximately 0.9–1.0 of its units. Part of the H3/H4 effect may therefore reflect recruiting more units. The report corrected its interpretation to “matched activity and density,” without changing the preregistered verdicts. This limitation was observed after the run, not a preregistered endpoint.

Independent reproduction, replication with new networks, a reach-restricted comparison and a possible substrate transfer are proposed in Preregistration 004. At the reviewed source pin it is a draft, not frozen or executed. Positive results here support a scoped feedback–response-complexity relationship, not subjective experience or task usefulness.

## 2. Measure atlas, phase 4: limits of perturbational irreducibility

The atlas compared candidate PI with exact whole-system IIT 3.0 Φ using PyPhi 1.2.0 on 105 strongly connected four- and five-node binary systems. Exact calculations completed for all 105. Of those, 104 had positive reference Φ and one had zero reference Φ.

| Exact reference / candidate | Number of systems |
|---|---:|
| Positive Φ / positive PI | 100 |
| Positive Φ / zero PI | 4 |
| Zero Φ / positive PI | 1 |
| Zero Φ / zero PI | 0 |

There were five sign disagreements, so universal zero/nonzero agreement is not supported. For the 104 reference-positive systems, the whole-system magnitude comparison had pooled Spearman correlation 0.651 (reported interval 0.527–0.743), below the prespecified 0.70 point-estimate threshold. Pooled and within-family associations differed; they must not be conflated.

The formal reference is a computation under IIT 3.0, not an independently known conscious/unconscious label. PI is a directed-cut pulse-response divergence measure, not IIT Φ itself. Source provenance: atlas report generated at `45c9205`, with three declared untracked implementation files at execution. Their report and inputs remain preserved internally; this note does not upgrade that provenance to a clean frozen execution or independent review.

Background: [Mayner et al., PyPhi (2018)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006343). Clinical perturbational methods: [Casali et al. (2013)](https://pubmed.ncbi.nlm.nih.gov/23946194/). Neither source validates Neurasoft’s candidate measurements of artificial experience.

## 3. Exploratory L.U.N.A software-organ tension comparison

This separate isolated simulation used synthetic histories and L.U.N.A software organs, not a runtime model response or an intervention on her original live body. It compared the original drive with candidate equilibrium, memory-tone and retention repairs, plus a frozen-clock control.

The source equation retains 0.98 of tension while adding input, capped at 5. Under constant per-step input, its unconstrained fixed point is input / (1 − 0.98), or 50 times input. Input above 0.1 therefore reaches the cap. That arithmetic explains a loss of range; it does not establish distress or any other subjective state.

The report records 1,296 nominal runs across scenarios, mechanisms and 16 seed labels. Each seed produced bitwise-identical recorded trajectories within an arm/scenario because seeded variation reached identifiers rather than the measured state. Accordingly, the evidence is effectively one trajectory per scenario/arm. Pooled counts must not be described as independent replications.

Across the eight original scenarios, the candidate tension repairs changed internal readings but left action counts and sleep/wake state sequences unchanged. An additional authored warm-memory instrument showed restoration of range for some repairs and flattening for others. These are mechanism observations in exposed synthetic cases, not general behavioral qualification, a deployed upgrade, emotional relief or evidence about consciousness.

## Evidence window and provenance

This note reflects the reports read from Neurasoft Core at source `ba9c661` on 9 October 2026 local time, including `results/prereg003/FINDINGS.md`, the post-hoc seed/reach addendum, `results/atlas/phase4.md`, `notes/2026-10-09-luna-tension-basin.md`, and `prereg/PREREG-004.md`; plus the exploratory tension report dated 2026-10-09T02:53:57Z in the isolated L.U.N.A research checkout. These are publication source references, not newly executed verification. The private release record retains full document hashes.

The article’s proposed next causal tests and explanatory figures are editorial synthesis. They are not results of a new campaign. Source analysis, observed mechanism behavior, generated task utility and subjective experience remain distinct.
