# AI Tutors in Programming Education

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) ![Status: protocol](https://img.shields.io/badge/status-protocol%20and%20analysis%20scaffold-lightgrey)

**Authors:** Aruzhan Akmurzayeva; Adel Baimukhambetova  
**Project status:** Experimental protocol and reproducibility scaffold; no participant results are included.
**Public repository:** [github.com/h8zv8nkt7c-blip/ai-tutors-programming-education](https://github.com/h8zv8nkt7c-blip/ai-tutors-programming-education)

## Project Overview and Research Aim

This project studies whether the style of generative AI assistance in introductory Python affects students' independent transfer performance seven days later.

**Research question:** Does guided-hint assistance improve seven-day independent transfer performance compared with unrestricted chatbot assistance and learning without AI?

The study is a planned three-arm randomized experiment: (1) guided hints, (2) an unrestricted chatbot, and (3) a no-AI control. All groups use the same learning content, practice tasks, time limits, follow-up task, and scoring rubric. The seven-day follow-up is completed without AI.

The repository contains the experimental setup, a pinned container, and a small analysis program for input validation and descriptive summaries. The bundled eight-row CSV is **synthetic fixture data** for demonstrating the run path. It is not participant data, benchmark evidence, or a study result.

## Hypotheses

- **H₀₁:** Mean seven-day independent transfer scores are equal across the three groups.
- **H₁₁:** The guided-hint group has a higher mean seven-day score than both the unrestricted-chatbot and no-AI groups.
- **H₀₂:** The practice-to-follow-up score gap is equal across groups.
- **H₁₂:** The unrestricted-chatbot group scores higher during assisted practice but shows a larger practice-to-follow-up decrease than the guided-hint group.
- **H₀₃:** Baseline Python knowledge does not moderate the effect of assistance condition on follow-up score.
- **H₁₃:** The transfer benefit of guided hints is larger for students with lower baseline Python knowledge.

## Experimental Setup and Measures

| Role | Variable / metric | Operational definition |
|---|---|---|
| Independent variable | Assistance condition | Guided hints, unrestricted chatbot, or no AI; assigned at participant level |
| Primary dependent variable | Seven-day transfer score | Score from 0–100 on a new Python task, completed independently without AI |
| Secondary dependent variable | Practice score | Score from 0–100 on the in-session task using the same rubric scale |
| Secondary dependent variable | Practice-to-follow-up gap | Practice score − seven-day score, in rubric points |
| Moderator / covariate | Baseline Python score | Score from 0–100 on a short diagnostic administered before randomization |
| Guardrails | Follow-up completion and protocol deviations | Counts and rates by assigned group; report missing outcome counts alongside score summaries |

Primary analysis: regress the seven-day score on assigned condition and baseline score; report adjusted group contrasts and 95% confidence intervals. The two planned primary contrasts are guided hints vs. unrestricted chatbot and guided hints vs. no AI; control family-wise error with Holm adjustment. Analyze H₂ with the practice-to-follow-up gap, and H₃ with a pre-specified condition-by-baseline interaction. Freeze the analysis plan, missing-data handling, and significance threshold before examining study outcomes. Determine sample size using an a priori power analysis before recruitment; no sample-size estimate is fabricated here.

Keep topic coverage, time, task difficulty, instructions, instructor, scoring rubric, test timing, and follow-up conditions constant. Record the AI model/version and interface for AI arms. Randomize participants, preferably stratifying on baseline score. Have graders use a common rubric and, where feasible, hide condition labels. See [the full protocol](docs/experimental_protocol.md).

## Repository Structure

```text
.
├── config.json
├── data/sample/sample.csv       # Synthetic fixture only
├── docs/
│   ├── experimental_protocol.md
│   └── reproducibility_checklist.md
├── notebooks/                   # Optional exploratory notebooks
├── results/                     # Generated output; ignored by Git
├── src/benchmark.py             # Validation and descriptive summaries
├── methodology_card.md          # Research methodology card
├── .dockerignore
├── Dockerfile
├── requirements.txt
├── LICENSE
└── README.md
```

## System Requirements

- Docker Engine (recommended), or Python 3.12.8 for the standard-library analysis script
- Docker image: `python:3.12.8-slim-bookworm`
- JupyterLab 4.6.3 is pinned for the optional interactive workspace
- CPU-only; no GPU or CUDA is required for this descriptive scaffold
- No third-party package is required to run `src/benchmark.py` directly

## Quickstart and Reproducibility Guide

### Run the analysis

With Python 3.12.8:

```bash
python src/benchmark.py --config config.json
```

Build and run the descriptive analysis in Docker:

```bash
docker build -t ai-tutors-study .
docker run --rm -v "$PWD/results:/workspace/results" ai-tutors-study python src/benchmark.py --config config.json
```

The program prints a JSON summary and writes `results/latest.json`. It validates column names, unique pseudonymous IDs, group labels, and score ranges; then reports group counts, means, standard deviations, medians, ranges, and unadjusted mean contrasts. It does **not** fit the planned inferential models, calculate p-values, handle missing outcomes, or establish causal effects.

### Start JupyterLab in Docker

```bash
docker build -t ai-tutors-study .
docker run --rm -p 127.0.0.1:8888:8888 -v "$PWD:/workspace" ai-tutors-study
```

Open the localhost URL and token printed in the container log. The server binds to the container interface; the host port is published only on `127.0.0.1`. To analyze collected data, preserve the documented columns and use anonymized IDs. Do not place names, emails, student numbers, or other direct identifiers in the CSV.

## Expected Results and Benchmark Table

No empirical benchmark result is available yet. The fixture run is only a pipeline demonstration.

| Measure | Expected output | Evidence status |
|---|---|---|
| Seven-day independent transfer score | Adjusted means, planned contrasts, 95% CIs | Planned; not collected |
| Practice score | Group means and spread | Planned; not collected |
| Practice-to-follow-up gap | Mean score-point difference by group | Planned; not collected |
| Follow-up completion / deviations | Counts and rates by assigned group | Planned; not collected |
| Synthetic fixture summary | Descriptive JSON from eight fabricated rows | Demonstration only |

## Reproducibility and Git Workflow

1. Record the code revision, Docker image, Python/Jupyter versions, configuration, AI model/version, task materials, rubric, and randomization seed.
2. Keep raw identifiable data out of Git; store only approved, anonymized data or synthetic fixtures. Version large datasets and model weights outside Git (for example, with DVC, Git LFS, or an approved repository).
3. Use small, descriptive commits and inspect `git status` before pushing.

For a new checkout, the basic initial workflow is:

```bash
git init
git checkout -b main  # when starting from Git's default branch, such as master
git add .
git status --short  # review the staged file list before committing
git commit -m "Add reproducible study scaffold"
git remote add origin <public-repository-url>
git push -u origin main
```

## Citation and License

```bibtex
@misc{akmurzayeva_ai_tutors_2026,
  author       = {Akmurzayeva, Aruzhan and Baimukhambetova, Adel},
  title        = {AI Tutors in Programming Education: Do Hints Help Students Retain What They Learn After the Session?},
  year         = {2026},
  howpublished = {\url{https://github.com/h8zv8nkt7c-blip/ai-tutors-programming-education}},
  note         = {Experimental protocol and reproducibility scaffold}
}
```

Code is released under the MIT License. The license does not grant rights to redistribute third-party course materials or participant data.

Use the [reproducibility checklist](docs/reproducibility_checklist.md) for a two-minute reviewer audit.
