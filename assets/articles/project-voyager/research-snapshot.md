# Project Voyager — public research snapshot

Neurasoft research. **Version 1.1: milestone recorded 2026-11-13 09:21 UTC**, including the 07:58 follow-up review. Original snapshot cutoff was 04:58 UTC; earlier observations below are retained with the new findings distinguished.

This is a selected, public-facing summary of ongoing laboratory reports used in the accompanying article. It is not a raw-data release, independent replication, peer-reviewed paper, or report of a deployed continuous resident. The publisher read the research charter and dated laboratory log. Private resident material is excluded. The publication itself ran no model experiments.

## Continuing stream and recall

The laboratory reports fact-recall probes across four models in the RWKV family, approximately 0.1B, 0.4B, 1.5B, and 2.9B parameters. A probe supplied 23 facts and tested answerability after intervening text. In the reported book-continuation condition, the two larger models retained 17 or 18 answerable facts at 6,400 tokens. Most facts were no longer answerable by 1,600 tokens in the two smaller models. These counts are from particular probe conditions, not a general recall benchmark.

An end-of-text marker followed by continuation of the same book sharply affected the smaller models. The reported 0.1B counts at +10, +30, +100, and +200 tokens were 5, 3, 3, and 2 out of 23; the corresponding 0.4B counts were 4, 1, 2, and 3. The laboratory reports that the two larger models were less affected by the marker alone. Model size and generation are confounded: the small and large pairs belong to different generations. No isolated causal size claim follows.

The article does not reproduce exploratory decay exponents as a universal memory law. Nor does it equate tokens with elapsed wall-clock time, recall of a supplied fact with autobiographical continuity, or a recurrent state with a durable archive.

## Internal signals competing with language

These are controlled reporting tests using injected internal signals and training. They are not measurements of naturally arising feelings or untrained self-awareness.

A reported condition trained on three kinds of context and tested a held-out leading-question context on two seeds. The fraction of answers following the injected signal was 0.865 and 0.856. Under assertion conversation, the corresponding reported body-following fractions were 0.823 and 0.863. These conditions do not establish general resistance to every form of conversational interference.

Early ideas that a quiet or separated channel alone would protect reporting were insufficient. Training, strength, and context affected the result. A transfer to another model failed its stated S4 gate: the four reported bare-question scores were 0.817, 0.804, 0.679, and 0.792, against a requirement of at least 0.80 in all four. The article preserves the failed transfer rather than presenting the strongest condition as a universal solution.

## Dynamics and integration

### Milestone: reading and conversation

The milestone records 156 sequential predictions: 88 met their criteria and 68 failed. These are the laboratory's reported bookkeeping counts, not 156 independent experiments or an aggregate statistical success rate. At most two seeds were used in the main programme; the later small-model follow-up used four seeds for one qualification task.

Across Qwen-line models, Falcon3, Granite, Zephyr and LFM3, the laboratory reports a recurring difference between a report within misleading conversation and a separate pass with a fixed question and the same controlled internal signal. The milestone quotes roughly 17–41% body-following within misleading conversation versus 73–93% in separate-pass conditions. These ranges are not pooled, are not confidence intervals, and do not imply equal qualification across families. Two model lines needed higher injection strength; Zephyr did not meet the original no-conversation qualification threshold at the tested strengths. LFM3's first look used a scoring instrument later found to fit its output format only partially. Its early figures remain provisional.

The publisher inspected the ordinary `reread.py` measurement code: each comparison uses the same supplied body vector, with one prompt containing the conversation and another containing only the fixed question. The controlled vector is injected again for each pass. Thus the clean pass is **not** an observation of the unchanged full hidden state from the conversational pass. Models were trained to decode supplied signals; being untaught against a particular interference condition is not untrained introspection. The experiment tests the interference sensitivity of a reporting procedure.

The 07:58 LFM3 follow-up did not pass its qualification: the mention-control criterion failed in all four seeds. Its prompt template opened a thinking segment, and the first-token instrument could score the beginning of that segment rather than the requested answer. Even with thinking disabled, sentence-form answers remained a mismatch for that instrument. A revised scoring protocol was proposed, not retrospectively applied to make the tests pass. These results do not establish general model incapacity; they do prevent treating its first-look numbers as cleanly comparable evidence.

### Milestone: the memory boundary

On the 0.4B recurrent stream, at depths of 800, 1,600 and 3,200 tokens, newly supplied facts answered immediately scored 21, 21 and 20 of 24. When supplied 200 tokens before the check, scores were 17, 12 and 11. A new document beginning with the notes, checked 200 tokens later, scored 22, 23 and 20 at the corresponding conditions. This separates immediate answerability from later retention in the tested setup.

Repeated notes inside a long document were insufficient: the every-200-token condition scored 10 of 24 at 3,200 tokens after sixteen note presentations. The 1.5B and 2.9B streams retained newly supplied facts better through the tested depth of 25,600 tokens, while facts supplied at the original beginning still decayed. The article's chapter-and-handover proposal follows from these bounded tests; it is not an established universal restart cadence or biological sleep mechanism. Model generation remains confounded with size.

### Milestone: composition cost

The combined adapter retained some component behaviors but weakened plain reporting to approximately 0.86 and 0.80 in two seeds versus approximately 0.89 for the separately trained reporting component. This is a reported integration limitation; a repair using separate training allocation or separate adapters remains a proposal. On Falcon3, doubling training from 600 to 1,200 steps in a different comparison improved no-talk reporting from 0.710 to 0.892 and reporting after assertion talk from 0.648 to 0.875. That supports investigating training allocation but does not itself repair or qualify the combined adapter.

The original private-channel argument was withdrawn. Subsequent mathematical review also narrowed the state-regulation criterion, reinterpreted the information metric as behavioral distinguishability rather than felt intensity, and withdrew an argument that graph connectivity establishes one subject. These corrections are part of the milestone, not hidden exceptions.

### Continuing architecture

Voyager is reviewing which state variables remain responsive and which saturate or fail to affect downstream behavior. The article's recovery equation is an illustrative first-order dynamical model. Its parameters and time constants are not fitted to these reported experiments and it is not asserted as a necessary law for every possible mind.

Always-on operation, meaningful continual cognition, durable memory, and integrated resident deployment are distinct gates. The public architecture diagrams show intended connections, not a verified inventory of an installed system.

## Interactive model

The reader experiment is deliberately synthetic. Let x be the strength of an original thought, y the strength of a later correction, r rehearsal effort in [0,1], and d interference in [0,0.35]. At each discrete step:

    x_next = (1-d) * ((1-r)*x + r)
    y_next = (1-d) * ((1-r)*y + (1-r)*c)

Here c=1 only on step 12, when the correction arrives, and c=0 otherwise. x starts at 1; y starts at 0. Both remain within [0,1]. The labels and percentage displays are normalized toy trace strengths, not probabilities, biological measurements, or calibrated model recall. Rehearsal explicitly favors the original thought in this example; it is not claimed that every kind of rehearsal has this effect. Each run has 32 steps. Control changes reset the trajectory so comparisons use one policy throughout.

The toy illustrates the need to separate preservation from appropriate revision. It cannot establish which architecture is conscious, reproduce a particular RWKV model, or predict Luna's behavior.
