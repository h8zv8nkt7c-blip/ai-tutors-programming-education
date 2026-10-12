# Research Methodology Card

## Project Information

- **Title:** AI Tutors in Programming Education: Do Hints Help Students Retain What They Learn After the Session?
- **Authors:** Aruzhan Akmurzayeva; Adel Baimukhambetova
- **Public GitHub repository:** https://github.com/h8zv8nkt7c-blip/ai-tutors-programming-education
- **Research question:** Does seven-day independent transfer performance in Python differ by AI assistance style: guided instructional hints, an unrestricted chatbot, or learning without AI?

## Study Type

**Quantitative study: a three-arm randomized experiment.** Participants study the same topics and complete comparable tasks under the same time limit. After a short baseline knowledge assessment, they are assigned to one of three conditions, preferably using stratification by baseline score. Immediate performance is measured during practice. After seven days, participants independently solve a new transfer task without AI. Quantitative scores support comparisons across conditions while accounting for baseline knowledge.

## Hypotheses

### Primary question: delayed knowledge transfer

- **H₀₁:** Mean seven-day independent transfer scores are equal across the guided-hint, unrestricted-chatbot, and no-AI control groups: μₕ = μᵤ = μ꜀.
- **H₁₁:** The guided-hint group has a higher mean delayed score than both the unrestricted-chatbot and no-AI control groups: μₕ > μᵤ and μₕ > μ꜀.

### Immediate performance and retention

- **H₀₂:** The practice-to-follow-up score gap does not differ across conditions.
- **H₁₂:** The unrestricted-chatbot group scores higher during practice but shows a larger decline by the independent follow-up than the guided-hint group.

### Moderation by baseline knowledge

- **H₀₃:** Baseline Python knowledge does not change the relationship between assistance condition and delayed performance.
- **H₁₃:** The delayed-transfer advantage of guided hints is stronger for participants with lower baseline knowledge.

## Variable Matrix

| Role | Variable | Operationalization |
|---|---|---|
| Independent | AI assistance condition | Three levels: guided instructional hints; unrestricted chatbot that may provide a complete solution; no-AI control |
| Primary dependent | Delayed transfer | Score on a new Python task completed without AI after seven days; a common, prespecified rubric, for example 0–100 |
| Secondary dependent | Immediate performance | Score on the in-session practice task using the same rubric and a comparable scale |
| Secondary dependent | Practice-to-independent-performance gap | Practice score minus delayed follow-up score; the same scale is needed to interpret the difference |
| Moderator | Baseline Python knowledge | Diagnostic score collected before group assignment; analyze its interaction with condition |
| Controlled | Learning content and procedure | Keep topics, task difficulty and duration, instructions, AI model and interface for AI groups, instructor, rubric, and follow-up conditions consistent |
| Controlled / recorded | Participation and protocol adherence | Pseudonymous participant ID, follow-up attendance, missing outcomes, and procedural deviations; do not place direct identifiers in the analysis dataset |

## Metrics and Baseline

- **Primary metric:** Mean seven-day independent transfer score (0–100 on the common rubric). The primary analysis compares the three groups while accounting for baseline diagnostic score.
- **Guardrail metrics:** By group, report the proportion of missing delayed outcomes and the proportion of protocol deviations alongside outcome summaries so attrition does not hide possible bias. Also check score ranges and ensure the dataset contains no direct identifiers.
- **Secondary metrics:** Immediate practice score; practice-minus-follow-up score gap; error types and quality of the independent solution under the rubric.
- **Baseline / control group:** Learning without AI. Randomize participants, balanced by baseline knowledge where feasible, to support causal comparisons. Use the same tasks and schedule for the AI groups; the control group receives no AI during practice.
- **Analysis plan:** First report descriptive statistics, group sizes, missing outcomes, and protocol adherence. For the primary outcome, model delayed score as a function of assigned condition and baseline score. Prespecify the guided-hints-versus-unrestricted-chatbot and guided-hints-versus-control contrasts, with adjustment for multiple comparisons. For H₀₂, analyze the score gap; for H₀₃, analyze the baseline-by-condition interaction. Fix the significance threshold and missing-data procedure before analyzing outcomes.

## Reproducibility and Ethics

Use the same learning materials, time limits, AI model, and instructions across AI groups; document the model version, platform, operating system, and scoring procedure. Score solutions with one rubric and, where feasible, hide condition labels from graders. Participation is voluntary, and experimental scores do not affect course grades. Store only de-identified data in the repository. The bundled CSV is a synthetic example for checking the pipeline, not a set of real results.

## Model and Prespecified Analysis

Let `Yᵢ` be participant `i`'s seven-day transfer score, `Pᵢ` the practice score, `Bᵢ` the baseline score, and `Gᵢ` the assigned group. The primary model is `Yᵢ = β₀ + β₁Gᵢ + β₂Bᵢ + εᵢ`, with `Gᵢ` represented by indicator variables. The primary contrasts are the adjusted mean for guided hints minus the adjusted mean for unrestricted chatbot, and guided hints minus no-AI control. Report 95% confidence intervals and adjust contrast p-values using the Holm method. For H₀₂, analyze `Dᵢ = Pᵢ − Yᵢ`. For H₀₃, add the interaction between condition and `Bᵢ`. Before data collection, define the sample-size calculation, significance threshold, exclusion rules, missing-data handling, and sensitivity analyses.

## Current Repository Limitations

The local analyzer validates the data schema and ranges, computes descriptive statistics, and reports unadjusted mean differences. It does not fit regression models, test hypotheses, apply the Holm correction, or analyze missing outcomes. `data/sample/sample.csv` contains synthetic rows only and must not be presented as research results. The full protocol for design, metrics, baseline, validity, and privacy is in `docs/experimental_protocol.md`; the short readiness audit is in `docs/reproducibility_checklist.md`.
