#!/usr/bin/env python3
"""Generate docs/framework-mapping.md and docs/question-guide.md from data/questionnaire.csv.

Usage:  python tools/build_docs.py
The CSV is the single source of truth; edit it and rebuild both the docs and the workbook.
"""
import csv
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEVEL_NAMES = ['0 – Not in place', '1 – Initial', '2 – Developing', '3 – Defined', '4 – Optimized']


def split_list(text):
    return [t.strip() for t in (text or '').split(' | ') if t.strip()]


def cell(text):
    return (text or '—').replace('|', '\\|').replace('\n', ' ')


def load():
    with open(ROOT / 'data' / 'questionnaire.csv', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def by_service(questions):
    groups = OrderedDict()
    for q in questions:
        groups.setdefault(q['service'], []).append(q)
    return groups


def anchor(text):
    return ''.join(ch for ch in text.lower().replace(' ', '-') if ch.isalnum() or ch == '-')


def framework_mapping(questions):
    L = ['# Framework Mapping', '',
         "Each question in the kit and the frameworks it references. The mapping is the author's interpretation for "
         'self-assessment; it is not an official crosswalk and does not establish compliance.', '',
         'Abbreviations: **CPG-E** = HHS Cybersecurity Performance Goal (Essential); **CPG-X** = HHS Cybersecurity '
         'Performance Goal (Enhanced); **ZTMM** = CISA Zero Trust Maturity Model v2.0; **CSF** = NIST Cybersecurity '
         'Framework 2.0; **SSDF** = NIST SP 800-218.', '',
         'This file is generated from `data/questionnaire.csv` by `tools/build_docs.py`. '
         'For scoring anchors, interview probes and evidence, see the [Question Guide](question-guide.md).', '']
    for svc, items in by_service(questions).items():
        L += [f'## {svc}', '', '| ID | Dimension | Question | HHS CPG | Other references | Weight |', '|---|---|---|---|---|---|']
        L += [f'| {q["id"]} | {q["dimension"]} | {cell(q["question"])} | {cell(q["hhs_cpg"])} | {cell(q["references"])} | {q["weight"]} |'
              for q in items]
        L.append('')
    return '\n'.join(L)


def question_guide(questions):
    groups = by_service(questions)
    L = ['# Question Guide', '',
         'How to assess every question in the ACS Health Maturity Kit: the observable criteria for each maturity level, '
         'what to ask, what evidence proves the level and how to obtain it, the signs that an answer is overstated, '
         'what is different in hospitals and clinics, and how to reach the next level.', '',
         '**How to choose a level.** Pick the highest level whose description is fully true today. If part of it is '
         'missing, choose the level below. Plans and pilots do not count. A 3 or a 4 requires evidence you have seen. '
         'See [methodology.md](methodology.md) for weights and scoring.', '',
         'This file is generated from `data/questionnaire.csv` by `tools/build_docs.py`; the same content is in the '
         '*Question Guide* sheet of the workbook.', '',
         '## Contents', '']
    for svc, items in groups.items():
        dims = list(OrderedDict.fromkeys(q['dimension'] for q in items))
        L.append(f'- **[{svc}](#{anchor(svc)})** ({len(items)} questions) — ' + ' · '.join(dims))
    L.append('')
    for svc, items in groups.items():
        L += ['---', '', f'## {svc}', '']
        dim = None
        for q in items:
            if q['dimension'] != dim:
                dim = q['dimension']
                L += [f'### {dim}', '']
            L += [f'#### {q["id"]} — {q["question"]}', '',
                  f'**Weight:** {q["weight"]} · **HHS CPG:** {q["hhs_cpg"] or "—"} · **References:** {q["references"]}', '',
                  '| Level | What you would see |', '|---|---|']
            texts = [q['level_0'], q['level_1'], q['level_2'], q['level_3'], q['target_state']]
            L += [f'| {n} | {cell(t)} |' for n, t in zip(LEVEL_NAMES, texts)]
            L.append('')
            for label, key in (('Probing questions', 'probing_questions'), ('Evidence and how to obtain it', 'evidence'),
                               ('Red flags', 'red_flags'), ('Healthcare considerations', 'healthcare_considerations')):
                L += [f'**{label}**', ''] + [f'- {t}' for t in split_list(q[key])] + ['']
            L += ['**Path to the next level**', '',
                  f'- **To 2 – Developing:** {q["action_to_2"]}',
                  f'- **To 3 – Defined:** {q["action_to_3"]}',
                  f'- **To 4 – Optimized:** {q["action_to_4"]}', '',
                  f'**Recommended action if gap:** {q["recommended_action"]}', '']
            srcs = split_list(q['sources'])
            if srcs:
                L += ['**Sources:** ' + ' · '.join(f'<{u}>' for u in srcs), '']
    return '\n'.join(L)


def main():
    questions = load()
    (ROOT / 'docs' / 'framework-mapping.md').write_text(framework_mapping(questions), encoding='utf-8')
    (ROOT / 'docs' / 'question-guide.md').write_text(question_guide(questions), encoding='utf-8')
    print(f'Wrote docs/framework-mapping.md and docs/question-guide.md ({len(questions)} questions)')


if __name__ == '__main__':
    main()
