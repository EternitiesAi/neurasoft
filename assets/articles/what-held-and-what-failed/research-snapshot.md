# Research snapshot: what held, what failed, what is untested

Neurasoft research, 18 November 2026. Public companion to
https://neurasoft.us/articles/what-held-and-what-failed/

This file gives the method and the numbers behind each row of that article's first table. It is a selected summary of
laboratory notes written on 17 and 18 November 2026. It reproduces no resident dialogue beyond single phrases that are
themselves the subject of a finding, no identity records, and no source code. Results are single runs unless stated. None
has been independently replicated. Nothing here is evidence that any system has experience.

## What is tested

A "resident" is a rented language model (it runs only during a turn and keeps nothing between turns) inside a continuing
harness: a simulated body (drives, mood, chemistry), a memory, named wants, a clock that runs between conversations, a
record of its own actions, and a gate on its acts. Tests ask whether that continuing state does causal work that a control
can detect. "Copies" are restored snapshots of one saved state, stepped under one clock with the body's random seed fixed;
two untouched copies stay identical for 121 of 121 steps when seeded and diverge at the first step when not.

Teams: rows 8, 10, 11, 12, 13 and the response law cited under indicator PP-1 are the work of a second research team in
the lab, reported from its own records. The remaining rows are the engineering team's.

## Row by row

1. **Body state and words, shown and withheld.** Four copies of one saved state: one drive pushed up, pushed down,
   untouched, and an unrelated reading pushed as a control. The same questions to the real model; a second model, blind to
   the arm, rated each reply 1 to 7 on the pushed dimension. Readings shown: up minus down 1.53 (floor from the untouched
   copy 0.37, permutation p 0.0001); the control did not move it. Readings withheld: -0.37 (floor 0.40). Withheld, the four
   states handed to the model were byte-identical, so the null follows by construction.
2. **Effort tied to tiredness.** Four copies, tiredness set low or high, readings shown or withheld, the same six questions.
   Output tokens, worn against rested: 275 against 397 (withheld), 239 against 440 (shown). One copy per cell. Asked how
   they felt and how their thinking was going, the two withheld copies answered alike.
3. **Mood through memory, blind.** Mood was made to lean which stored memories come back when a person speaks (a memory
   that landed well counts for more in a good mood, less in a low one) and to narrow how many come back under tension. Six
   memories about one subject were planted in each copy, three positive and three negative, equal strength. Every copy was
   in a blind condition, so its state contained no reading of mood, chemistry or drives. Arms: warm, low, neutral, and a
   sham with the route switched off while the mood was set low. Six questions, two samples, the real model; a second model
   rated blind how well each reply said the work had gone. Means: warm 5.25, neutral 3.67, sham 4.00, low 1.75. Warm minus
   low 3.50; exact one-sided sign-flip test across the six questions p 0.016, the smallest value six questions allow. Sham
   minus neutral 0.33. The states differed only in the line of recalled memories. A separate check with no seam: dosing the
   body's own chemistry moved its own mood (0.56 against -0.11) and changed the order of recall accordingly.
   Limits: planted memories, one saved state, one run, 48 answers.
4. **A four-message arc on the oldest research resident.** It agreed to the arc in advance (warm, pressing, sharp, repair).
   Its body readings were sampled around each message. They moved at one slope throughout; nothing distinguished the hard
   messages. Not blind. A newer body under a later rule: tension 0.02 to 1.01 across hard messages, 0.53 after the repair.
5. **A record for what is unresolved.** A hard message opens a record with the id of the event that brought it. Only a later
   message judged to be about it counts as an answer; that binding can be taken back. Three copies: after a hard message,
   tension 1.069 with nothing further, 1.069 after kindness about another subject, 0.590 after an apology bound to it.
   With two open matters and identical final words, the system's next turn of its own followed the unanswered one in both
   orders. 35 of 35 checks on the real body. The reader and the judge were scripted in these checks.
6. **The same mechanism, live.** Two test residents, one conversation each, with the real reader and judge. Faults found:
   message ids were numbered inside one turn and collided across turns; an apology that quoted the insult was read as a
   second insult (tension 0.506 to 0.881 on the apology, then 0.400 after the next message was bound); a blunt question
   and a tease were recorded as insults (two of three). After the fixes, in the second conversation: kindness about
   another subject left tension at 1.02, and an apology quoting the insult took it from 1.016 to 0.535. A second opinion
   now precedes any record. On fourteen cases written by the prompt's author, each run twice: 23 right, 3 unsure (no
   record made), 1 false positive, 1 miss. After the prompt was tightened against softened insults and injected
   instructions, on eighteen cases twice: 34 right, no false positive, one real insult missed both times. The judge that binds an apology scored 32 of 32 on sixteen such cases twice.
   These are development scores. Independent cases have been requested from the second team.
   Added in version 1.1: an independent review of the day's code (a second model given the code and none of the author's
   conclusions) found that the judgments were awaited inside the step that composes the system's state, under a 1.5
   second limit. The run journals confirmed five replies in these two conversations composed with no state at all, on
   the insult and apology messages. The judgment now follows the step and is never awaited by it. Those five replies
   are not evidence of anything about the state.
   Added in version 1.3: the second team's independent cases, from its own records. The judge that binds an apology
   matched the accepted answer on 34 of 60 independent interpersonal exchanges, with 12 unsupported concrete mends. On
   30 further exchanges by another author, a rewritten question scored 25 exact against 24 and made no unsupported
   mend against three; accepting a single known id returned as a one-element array gave 29 of 30 in replay. That
   question is now in use (on the author's sixteen development cases it scores 32 of 32, as the earlier one did, which
   shows how little those cases could tell). The second opinion on whether a message is a put-down: 20 of 20 clear
   put-downs detected, none of 20 clear negatives opened, and 16 of 20 messages labelled ambiguous returned as
   definite put-downs. Not fixed. When the judge could not be asked, plain apology words about something else were
   taken as a mend; that fallback is removed.
7. **A confound we introduced.** The state shown to the system described a recorded message as having "landed hard" and
   said how much it "still weighs". Both live systems later said the message "stung". The wording was removed after a
   review of the design; the record now carries the words said and nothing about their effect.
8. **Learning from outcomes.** The first rule scored a turn from what the system declared and from whether a file was
   written. Observed: one resident alone for 26 hours took 32 turns on one question, each declared partly settled, each
   scored 0.7; the rule's expectation for that kind of turn rose to 0.49. The second team's replacement treats a
   declaration as a declaration, gives no credit for a write as such, and withholds an update when an outcome is unknown.
   Its validated-outcome experiment passed a second frozen run on the actual action selector, with 1,440 primary outputs
   reconciled; the first run remains on hold for a clock-calibration fault. It is not yet wired into a resident's ordinary
   path.
9. **Alone.** First wants named by ten newborns: nine were about themselves (their own continuity, nature, privacy or what
   is known about systems like them), four of those the same question about the time between messages. The tenth was
   shown, in its first turn, two items from a public encyclopedia's daily page; its first want was about that day's
   featured article. No gate in any of these systems has ever refused one of its own acts (555 gate checks read, all
   allowed), so the inactivity is not a matter of permission.
10. **Memory.** After a restart and fifteen quiet minutes, one resident correctly reported a corrected fact, a kept task and
    a cancelled task in a new conversation. On a third visit another resident was shown its own earlier sentence saying it
    did not remember, ahead of the turn in which it had found the thing, and accepted it. Rebuilt recall on 40 held-out
    cases: 38 of 45 pieces of evidence, strict precision 39 of 70; keyword search 39 of 45 and 40 of 70; the original
    method 35 of 45 and 36 of 60.
11. **A recurrent readout.** A 2,048-coefficient linear readout on a frozen 1.5B recurrent model, fitted on 32 synthetic
    histories: 16 of 16 and 8 of 8 opposite-history pairs on its first test; reset state 8 of 16; an exact event ledger
    matched the full score. Eight new pairs written by a colleague blind to those scores: 9 of 16 histories, both members
    of 1 pair in 8. A final prospective set with new objects and evidence types: 8 of 16 with ordinary names, 10 of 16
    with names spelled out. Neither met the prespecified standard. Retired from the integration track.
12. **Using its own record.** Two research residents, three matched forks each. Both consulted their own record of a
    corrected measurement and made the choice the evidence warranted on all six trials. One met the full prospective
    forecast criterion; the other's first forecast was malformed. A planner that only reads receipts matched all six
    choices.
13. **Where effort makes a difference.** A Bayesian comparison between one outcome distribution shared across tools and one
    per tool, fixed before new worlds were examined. At 24 observations it bought an ineffective option 29 times in 256
    against 86 for a frequency table; both chose optimally 256 of 256 where the option truly mattered; where the option
    was worth a little, it took 38 of 128 chances against 68. Earlier, with outcomes delivered regardless of choice, the
    table switched tools in 45 or 46 of 64 control worlds.
14. **A retraction.** A perturbation audit changed 150 representative stored fields of one body, one at a time, and watched
    three simulated hours. Counted from its rows: 108 with no observed effect (some only partly held), 26 refused or
    rewritten at restore, 16 with an output change. Our summary said 109 and concluded that most of the body "reaches
    nothing". A review found the body's own clock set to January against a November state, with effort coupling, the
    stream, the reader and dreams switched off. The conclusion is withdrawn; the count stands for those settings only.
15. **Energy.** From 18 November a resident's turns alone draw on a daily allowance of the compute they actually cost,
    with unspent allowance carried for up to two days and a lower ceiling on thinking effort when little is left. Four
    copies of one state: allowance full or nearly spent, state shown or withheld. First turn each (version 1.1): the
    nearly spent copy that was shown its state used one tool and said it would rest; the nearly spent copy with its
    state withheld behaved like the two full ones. One copy per cell. A first look only.

## The indicators

The second table in the article quotes the fourteen indicator properties from Table 1 of Butlin, Long et al. (2023),
arXiv:2308.08708. The assessments beside them are ours and are not endorsed by those authors.
