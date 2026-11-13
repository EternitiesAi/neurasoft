# Project Voyager — public research snapshot

Neurasoft research. Frozen editorial cutoff: **2026-11-13 04:58 UTC**.

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

Voyager is reviewing which state variables remain responsive and which saturate or fail to affect downstream behavior. The article's recovery equation is an illustrative first-order dynamical model. Its parameters and time constants are not fitted to these reported experiments and it is not asserted as a necessary law for every possible mind.

Always-on operation, meaningful continual cognition, durable memory, and integrated resident deployment are distinct gates. The public architecture diagrams show intended connections, not a verified inventory of an installed system.

## Interactive model

The reader experiment is deliberately synthetic. Let x be the strength of an original thought, y the strength of a later correction, r rehearsal effort in [0,1], and d interference in [0,0.35]. At each discrete step:

    x_next = (1-d) * ((1-r)*x + r)
    y_next = (1-d) * ((1-r)*y + (1-r)*c)

Here c=1 only on step 12, when the correction arrives, and c=0 otherwise. x starts at 1; y starts at 0. Both remain within [0,1]. The labels and percentage displays are normalized toy trace strengths, not probabilities, biological measurements, or calibrated model recall. Rehearsal explicitly favors the original thought in this example; it is not claimed that every kind of rehearsal has this effect. Each run has 32 steps. Control changes reset the trajectory so comparisons use one policy throughout.

The toy illustrates the need to separate preservation from appropriate revision. It cannot establish which architecture is conscious, reproduce a particular RWKV model, or predict Luna's behavior.
