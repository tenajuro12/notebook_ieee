# Emotion Classification in Kazakh Social Media

Code, annotation guidelines and evaluation package for

> T. Sabyrov and Zh. Sadirmekova, "Emotion Classification in Kazakh Social Media: What Limits
> Performance in a Low-Resource Setting?", ICTACS-2026.

The corpus is 2,467 authentic Kazakh and Kazakh–Russian social-media posts — 2,054 in the
training pool and 413 in the evaluation set — annotated over twelve affective states grouped
under eight base classes, including **Shame** (ұят), a self-conscious emotion prominent in the
Kazakh confessional genre that the standard Ekman scheme does not cover.

## Contents

| Path | What it is |
|---|---|
| `eval_package/` | the privacy-preserving evaluation package and the annotation guidelines — see its own README |
| `train_hierarchical_model.ipynb` | the hierarchical LaBSE classifier reported in the paper: training, three seeds, ensemble, per-class results |
| `reference_systems.ipynb` | the nine reference systems of Table IV, under the same protocol |
| `experiments_ablation_and_learning_curve.ipynb` | the design-choice ablation of Table V and the learning curve of Table VII, with the paired bootstrap |
| `results/` | the numbers produced by those runs, as CSVs, plus the learning curve as a 300 dpi figure |
| `compute_kappa.py` | inter-annotator agreement: overall and class-wise Cohen's κ, confusion pairs, disagreement list |
| `telegram_collect.py` | the collection script, with the language filter and the anonymisation applied at collection time |

The notebooks are committed without execution outputs, which is why `results/` carries the
numbers each run produced: `ablation_final.csv` (Table V), `learning_curve.csv` (Table VII),
`shame_explicit_vs_implicit.csv` (Section VI-C) and `inter_annotator_agreement.csv`
(Section III-C). Everything was run on Kaggle with a single T4 GPU; the full set of
experiments takes about four hours.

## The evaluation package

`eval_package/` is public and unrestricted. For every post in both splits it gives a SHA-256
hash of the normalised text together with its label, Level-1 parent, source family, length and
explicit-shame-marker flag. That is enough to verify the counts and, given a column of
predicted labels, to recompute the per-class and macro figures of the paper — without the post
text. It also contains the annotation guidelines, in the Russian working version actually used
and in an English rendering.

Two things it deliberately does not do: it does not allow the model to be retrained, which
needs the text, and the hashes are a verification mechanism rather than an anonymisation
guarantee. Both are explained in `eval_package/README.md`.

## Known defect in the corpus

The near-duplicate filter used during construction tokenised on whitespace without stripping
punctuation first, so a pair differing only by a comma scored Jaccard 0.56 instead of 1.00 and
passed the 0.7 threshold. Five evaluation posts (1.2 %) therefore have a near-duplicate in the
training pool; two pairs are identical and one of those carries a different label on each
side. They are flagged by `near_duplicate_across_splits` in the package so that their effect
can be bounded, and the splits are left unchanged so that every number in the paper refers to
one fixed evaluation set. This is stated in Section III-A of the paper.

## Access to the post text

The anonymised post text is available from the authors for non-commercial research under a
data-use agreement: no redistribution, no attempt to re-identify authors or link posts to
accounts, no determinations about identifiable individuals, and a citation to the paper.
Direct identifiers were removed at collection time; posts naming or sexualising minors, and
posts expressing suicidal ideation, were excluded from the released corpus and used neither
for training nor for evaluation.

Contact: sabyrtena@gmail.com

## Citation

```bibtex
@inproceedings{sabyrov2026kazakh,
  title     = {Emotion Classification in Kazakh Social Media:
               What Limits Performance in a Low-Resource Setting?},
  author    = {Sabyrov, Tenelbek and Sadirmekova, Zhanna},
  booktitle = {Proc. Int. Conf. on Innovative Computing and Communication
               Technologies and Applied Computing Systems (ICTACS)},
  year      = {2026}
}
```
