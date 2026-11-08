# Privacy-preserving evaluation package

Companion release for *Emotion Classification in Kazakh Social Media: What Limits Performance
in a Low-Resource Setting?* (ICTACS-2026).

This package lets anyone **verify the numbers in the paper without receiving a single line of
the original post text**. The posts are public but searchable, so distributing them verbatim
would let a reader trace an anonymous confession back to its author. What is distributed
instead is, for each post, a SHA-256 hash of its normalised text together with its label and
a few derived attributes.

The package is public and unrestricted. The post text itself is available separately, under
the access terms described at the end of this file.

## What the hashes are and are not

They are a **verification** mechanism, not an anonymisation guarantee. They let two parties
confirm that they hold the same corpus and that no item moved between splits, and they reveal
nothing on their own. They do not withstand a dictionary attack: anyone holding an archive of
the same channels can hash their own copy the same way and match it. The package is released
on the understanding that the underlying posts are already public; what it avoids is
republishing them as a convenient, labelled, permanently archived dataset row.

## Files

| File | Rows | What it holds |
|---|---|---|
| `evaluation_set_metadata.csv` | 413 | the evaluation set |
| `training_pool_metadata.csv` | 2,054 | the authentic training pool (synthetic posts excluded) |
| `taxonomy.json` | — | the twelve Level-2 classes, their Level-1 parents, the shame marker roots, and the counts |
| `annotation_guidelines_en.md` | — | the annotation guidelines, English rendering |
| `annotation_guidelines_ru.md` | — | the same guidelines in Russian, the working language of the annotators |

## Columns

| Column | Meaning |
|---|---|
| `item_id` | stable identifier within the split |
| `text_sha256` | SHA-256 of the text, lower-cased, with punctuation and repeated whitespace removed |
| `n_words`, `n_chars` | length of the raw text, so length-based analyses are reproducible |
| `label_l2` | one of the twelve affective states |
| `label_l1` | its Level-1 parent (eight base classes) |
| `source_family` | `telegram_confession`, `telegram_other`, `threads_general`, `threads_targeted` |
| `has_shame_marker` | 1 if the text contains an explicit shame root (ұя-, стыд, позор, неловк, стесня, кринж) |
| `near_duplicate_across_splits` | 1 if the item has a counterpart in the other split at Jaccard ≥ 0.7 (see below) |

## Known defect: five near-duplicates across the split boundary

The near-duplicate filter used during corpus construction tokenised on whitespace **without
stripping punctuation first**, so a pair differing only by a comma scored Jaccard 0.56 instead
of 1.00 and passed the 0.7 threshold. Re-running the check correctly for this release finds
five evaluation posts (1.2 % of 413) that have a near-duplicate in the training pool. Two
pairs are textually identical; one of those carries a different label on each side
(`Disgust` in training, `Frustration` in the evaluation set).

They are flagged by `near_duplicate_across_splits = 1` in both files, so the effect on any
metric can be bounded by dropping them. The splits are left as they are so that every number
in the paper refers to one fixed evaluation set; five items in 413 sit well inside the ±0.05
bootstrap interval the paper reports.

```python
import pandas as pd
ev = pd.read_csv("evaluation_set_metadata.csv")
clean = ev[ev.near_duplicate_across_splits == 0]      # 408 items
```

## What can be verified from this package alone

- every per-class and per-source count in the paper, and the full source-by-class breakdown
  of both splits, by cross-tabulating `source_family` against `label_l2`;
- the class-prevalence and support-sampling analysis of Section V-D;
- the explicit/implicit Shame split of Section VI-C, via `has_shame_marker`;
- the per-class and macro figures of Tables III–VII, once a column of predicted labels is
  joined in (see below);
- which items overlap between the splits, by intersecting `text_sha256`.

It does **not** allow the model to be retrained or re-run: that needs the text. This is
metric verification, not replication, and it does not let a reader check whether a label is
correct.

## Adding model predictions

To let others score a system without the text, release one column of predicted class names
aligned to `item_id`:

```python
import pandas as pd
ev = pd.read_csv("evaluation_set_metadata.csv")
ev["predicted_l2"] = [L2_NAMES[i] for i in ens_pred]   # from the training notebook
ev[["item_id", "predicted_l2"]].to_csv("predictions_hierarchical_ensemble.csv", index=False)
```

## Scoring

```python
import pandas as pd
from sklearn.metrics import f1_score, classification_report

ev = pd.read_csv("evaluation_set_metadata.csv")
pr = pd.read_csv("predictions_hierarchical_ensemble.csv")
d  = ev.merge(pr, on="item_id", validate="one_to_one")

print("12-class macro-F1 :", round(f1_score(d.label_l2, d.predicted_l2, average="macro"), 3))
print("8-class macro-F1  :", round(f1_score(d.label_l1,
      d.predicted_l2.map(dict(zip(ev.label_l2, ev.label_l1))), average="macro"), 3))
print(classification_report(d.label_l2, d.predicted_l2, zero_division=0))

c = d[d.near_duplicate_across_splits == 0]            # same, without the five leaked items
print("12-class macro-F1, leak removed :",
      round(f1_score(c.label_l2, c.predicted_l2, average="macro"), 3))
```

## Access to the post text

The anonymised post text is available from the authors for non-commercial research use under a
data-use agreement whose terms are: the recipient does not redistribute the text, does not
attempt to re-identify authors or link posts to accounts, does not use the data to make
determinations about identifiable individuals, and cites the paper. Direct identifiers
(usernames, telephone numbers, e-mail addresses, URLs, channel prefixes and signatures) were
removed at collection time; posts naming or sexualising minors, and posts expressing suicidal
ideation, were excluded from the released corpus and were used neither for training nor for
evaluation.

The annotation guidelines are included in this package, in both the Russian working
version actually used by the annotators and an English rendering.
