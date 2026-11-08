# -*- coding: utf-8 -*-
"""
Cohen's kappa for the second-annotator study (IEEE camera-ready, reviewer point
raised by all three reviewers).

Run AFTER the second annotator has filled the `label` column of
kappa_sample_to_annotate.xlsx without having seen any existing label.

    python compute_kappa.py

Inputs  : kappa_sample_to_annotate.xlsx   (annotator B's labels)
          kappa_key_DO_NOT_SHARE.xlsx     (annotator A's labels = released gold)
Outputs : kappa_report.txt                (numbers to paste into the paper)
          kappa_disagreements.xlsx        (items to adjudicate)

What it reports and why:
  * overall Cohen's kappa on the RANDOM stratum only (n = 100). This is the
    headline figure: the random stratum preserves the natural class
    distribution, so the chance-agreement baseline is the real one.
  * class-wise one-vs-rest kappa on the FULL sample (n = 181). The top-up
    stratum exists so every class has 15 items; class-wise kappa on a
    label-stratified sample is reportable but its baseline is not the
    corpus baseline, and the paper must say so in one sentence.
  * raw agreement and the confusion table, so the text can name the pairs
    that drive the disagreement.
"""

import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score, confusion_matrix

ORDER = ["Hopelessness", "Worthlessness", "Exhaustion", "Loneliness", "Frustration",
         "Indignation", "Shame", "Joy", "Fear", "Surprise", "Disgust", "Neutral"]

b = pd.read_excel("kappa_sample_to_annotate.xlsx")
a = pd.read_excel("kappa_key_DO_NOT_SHARE.xlsx")
df = a.merge(b[["item_id", "label", "uncertain", "note"]], on="item_id", how="left")
df = df.rename(columns={"label": "label_B"})

missing = df["label_B"].isna().sum()
bad = sorted(set(df["label_B"].dropna()) - set(ORDER))
if missing:
    print(f"WARNING: {missing} items have no label from annotator B; they are dropped.")
if bad:
    raise SystemExit(f"Unknown labels in annotator B's file: {bad}\nAllowed: {ORDER}")
df = df.dropna(subset=["label_B"]).copy()

lines = []
def say(s=""):
    print(s)
    lines.append(s)

rnd = df[df["stratum"] == "random"]
k_overall = cohen_kappa_score(rnd["label_A"], rnd["label_B"], labels=ORDER)
agree_rnd = (rnd["label_A"] == rnd["label_B"]).mean()

say("=" * 68)
say("OVERALL AGREEMENT  (random stratum, natural class distribution)")
say("=" * 68)
say(f"n                     : {len(rnd)}")
say(f"raw agreement         : {agree_rnd:.3f}")
say(f"Cohen's kappa         : {k_overall:.3f}")
say("")

k_full = cohen_kappa_score(df["label_A"], df["label_B"], labels=ORDER)
say(f"(for reference, kappa over the full {len(df)}-item sample incl. top-up: {k_full:.3f};")
say(" this one is inflated/deflated by the artificial balance - do not headline it)")
say("")

say("=" * 68)
say("CLASS-WISE ONE-VS-REST KAPPA  (full sample, 15 items per class)")
say("=" * 68)
say(f"{'class':<16}{'n_A':>5}{'n_B':>5}{'agreed':>8}{'kappa':>8}")
rows = []
for c in ORDER:
    ya = (df["label_A"] == c).astype(int)
    yb = (df["label_B"] == c).astype(int)
    k = cohen_kappa_score(ya, yb)
    both = int(((ya == 1) & (yb == 1)).sum())
    say(f"{c:<16}{int(ya.sum()):>5}{int(yb.sum()):>5}{both:>8}{k:>8.3f}")
    rows.append({"class": c, "n_A": int(ya.sum()), "n_B": int(yb.sum()),
                 "agreed": both, "kappa": round(float(k), 3)})
say("")

say("=" * 68)
say("WHERE THE DISAGREEMENT IS  (rows = annotator A, cols = annotator B)")
say("=" * 68)
cm = confusion_matrix(df["label_A"], df["label_B"], labels=ORDER)
cmdf = pd.DataFrame(cm, index=ORDER, columns=[c[:4] for c in ORDER])
say(cmdf.to_string())
say("")

off = []
for i, ca in enumerate(ORDER):
    for j, cb in enumerate(ORDER):
        if i != j and cm[i, j] > 0:
            off.append((cm[i, j] + cm[j, i] if j > i else 0, ca, cb, cm[i, j]))
pairs = {}
for i, ca in enumerate(ORDER):
    for j, cb in enumerate(ORDER):
        if i < j:
            n = cm[i, j] + cm[j, i]
            if n:
                pairs[(ca, cb)] = n
say("Most frequent confusion pairs (both directions):")
for (ca, cb), n in sorted(pairs.items(), key=lambda x: -x[1])[:8]:
    say(f"  {ca} <-> {cb}: {n}")
say("")

dis = df[df["label_A"] != df["label_B"]].copy()
say(f"items to adjudicate: {len(dis)} of {len(df)} ({len(dis)/len(df)*100:.1f} %)")
say("")
say("SENTENCE FOR THE PAPER (fill nothing, the numbers are above):")
say(f'  "A second native Kazakh speaker independently annotated a {len(rnd)}-post random')
say(f'   subsample of the evaluation set using the annotation guidelines alone, without')
say(f'   access to the existing labels. Raw agreement was {agree_rnd:.2f} and Cohen\'s kappa')
say(f'   {k_overall:.2f}. A further {len(df)-len(rnd)} posts were added so that each class reached')
say(f'   fifteen items, and class-wise one-vs-rest kappa on that {len(df)}-item sample is')
say(f'   reported in Table X; because that sample is label-stratified, its chance')
say(f'   baseline is not the corpus baseline. All disagreements were adjudicated by')
say(f'   discussion and the adjudicated labels are the released ones."')

open("kappa_report.txt", "w", encoding="utf-8").write("\n".join(lines))
pd.DataFrame(rows).to_csv("kappa_classwise.csv", index=False)
dis[["item_id", "gold_id", "label_A", "label_B", "stratum", "uncertain", "note"]] \
    .assign(adjudicated="").to_excel("kappa_disagreements.xlsx", index=False)
print("\nwritten: kappa_report.txt, kappa_classwise.csv, kappa_disagreements.xlsx")
