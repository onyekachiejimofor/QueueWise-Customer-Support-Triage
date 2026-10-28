#!/usr/bin/env python3
"""Verify QueueWise published evidence. Standard library only; no file changes."""
from pathlib import Path
from collections import Counter, defaultdict
import csv, json, re

ROOT=Path(__file__).resolve().parents[1]
def read(path):
    with (ROOT/path).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def indexed(rows):
    d={x['task_id']:x for x in rows}
    assert len(d)==len(rows), 'Duplicate task_id'
    return d

a=indexed(read('data/raw/label_studio_export_FINAL.csv'))
initial=indexed(read('data/history/01_initial_export.csv'))
intermediate=indexed(read('data/history/02_first_revision_export.csv'))
source=indexed(read('data/source/annotation_tasks.csv'))
ref=indexed(read('data/source/reference_labels.csv'))
processed=indexed(read('data/processed/final_labeled_tickets.csv'))
assert len(a)==len(initial)==len(intermediate)==len(source)==len(ref)==len(processed)==240
assert a.keys()==initial.keys()==intermediate.keys()==source.keys()==ref.keys()==processed.keys()
assert len({r['annotation_id'] for r in a.values()})==240
vocab={'Billing & Payment','Refund & Return','Delivery & Tracking','Account Access','Product Defect','Subscription & Cancellation','Technical Issue','General Inquiry'}
assert Counter(r['label'] for r in a.values())==Counter({cat:30 for cat in vocab})
assert all(a[k]['text']==source[k]['text']==ref[k]['text']==processed[k]['message'] for k in a)
assert all(a[k]['label']==processed[k]['final_label']==ref[k]['reference_label'] for k in a)
assert sum(initial[k]['label']==ref[k]['reference_label'] for k in a)==232
assert sum(intermediate[k]['label']==ref[k]['reference_label'] for k in a)==239
assert sum(a[k]['label']==ref[k]['reference_label'] for k in a)==240
assert sum(ref[k]['difficulty']=='Boundary / multi-intent' for k in a)==48
assert all(not a[k]['confidence'] and not a[k]['review_note'] for k in a)
def normalized(s):return re.sub(r'^hello support team\s*[—–-]\s*','',s.lower().strip()).strip(' .?!\t\n')
group=defaultdict(list)
for k in a:group[normalized(a[k]['text'])].append(k)
pairs=[keys for keys in group.values() if len(keys)==2]
assert len(group)==144 and len(pairs)==96
assert all(a[p[0]]['label']==a[p[1]]['label'] for p in pairs)
changes=read('reports/revision_history.csv')
assert len(changes)==10
s=json.loads((ROOT/'reports/qa_summary.json').read_text())
assert s['final_provisional_reference_matches']==240
assert s['independent_blind_review_completed'] is False
print('PASS: 240 unique tasks, 240 annotated, 8 valid classes; source text fully aligned')
print('PASS: initial 232/240, intermediate 239/240, final 240/240 reference matches')
print('PASS: 48 designed hard cases; 96/96 consistent greeting pairs; 144 normalized texts')
print('IMPORTANT: Final reference-guided concordance is not independent accuracy.')
