# Experimental Setup and Variables

## Study design

Three-arm, participant-level randomized experiment in introductory Python learning. The study compares guided AI hints, an unrestricted chatbot, and a no-AI control. Each arm receives the same topics, practice materials, time allowance, instructor instructions, and scoring rubric. After seven days, all participants complete a new transfer task independently without AI.

The design choice follows the research question: it asks whether assistance condition changes a numeric learning outcome, so a quantitative controlled comparison is appropriate. The primary inference concerns the assigned assistance condition and the independent seven-day outcome. This protocol is a plan; no participants have been recruited and no results are reported in this repository.

## Hypotheses

- **H₀₁:** Mean seven-day transfer score is equal in all three assigned conditions.
- **H₁₁:** The guided-hint group has a higher mean seven-day transfer score than each of the unrestricted-chatbot and no-AI groups.
- **H₀₂:** The practice-minus-follow-up score gap is equal across conditions.
- **H₁₂:** The unrestricted-chatbot group has a higher assisted-practice score but a larger practice-to-follow-up decrease than the guided-hint group.
- **H₀₃:** Baseline Python knowledge does not interact with assistance condition when predicting seven-day score.
- **H₁₃:** The guided-hint transfer advantage is larger at lower baseline Python knowledge.

## Variable classification matrix

| Class | Variable | Definition / handling |
|---|---|---|
| Independent | Assigned assistance condition | Categorical: guided hints, unrestricted chatbot, no-AI control |
| Primary dependent | Seven-day transfer score | 0–100 score on a new Python task; no AI or outside assistance |
| Secondary dependent | Assisted practice score | 0–100 score on the common in-session task and rubric |
| Secondary dependent | Practice-to-follow-up gap | Practice score minus seven-day score, in points |
| Baseline covariate / moderator | Python diagnostic score | 0–100 pre-randomization score; center before interaction modeling |
| Process guardrail | Follow-up completion | Completed follow-up count divided by assigned count, reported by arm |
| Process guardrail | Protocol deviations | Count and description of deviations by assigned arm |
| Controlled | Content and exposure | Same topics, examples, tasks, difficulty, time limits, and instructions |
| Controlled | Assessment | Same new follow-up task, timing, scoring scale, and rubric across arms |
| Controlled / recorded | AI setup | Record provider, model/version, interface, system instructions, and access settings for both AI arms |
| Controlled | Session conditions | Same instructor, session format, equipment policy, and testing environment where feasible |

Randomize at the participant level. Prefer blocked or stratified randomization by baseline-score band so the three arms are balanced on prior knowledge. Keep the randomization sequence separate from scoring. Do not change materials or task difficulty after assignment begins without documenting a protocol amendment.

## Evaluation metrics and formulas

Let `Y_i` be participant *i*'s seven-day score, `P_i` their practice score, `B_i` their baseline diagnostic score, and `G_i` their assigned group.

| Metric | Formula / summary | Role |
|---|---|---|
| Adjusted seven-day mean by arm | Estimate from `Y_i = β₀ + β₁G_i + β₂B_i + ε_i` (use indicator variables for the three-arm condition) | Primary |
| Planned condition contrasts | `Δguided,chat = adjusted mean(guided) − adjusted mean(chat)`; `Δguided,control = adjusted mean(guided) − adjusted mean(control)` | Primary; report 95% confidence intervals and Holm-adjusted tests |
| Practice-to-follow-up gap | `D_i = P_i − Y_i`; compare mean `D_i` by assigned group | Secondary, H₂ |
| Baseline moderation | Add `G_i × B_i` interaction to the adjusted outcome model; report interaction estimates and uncertainty | Secondary, H₃ |
| Follow-up completion | `number with observed Y_i / number randomized` by assigned group | Guardrail |
| Protocol deviation rate | `number with a recorded deviation / number randomized` by assigned group | Guardrail |

All scores use the same pre-specified 0–100 rubric. Include rubric dimensions and scoring examples in the study materials before data collection. The rubric should measure correctness and successful transfer to the novel task. Where feasible, have graders blinded to group assignment and double-score a subset; report agreement. Do not include latency, GPU utilization, or model accuracy as student-learning outcomes: those are system metrics and do not answer this education research question.

## Baseline, execution, and reproducibility

- **Control baseline:** the no-AI group receives the same lesson and practice time, but no AI assistance.
- **Comparative baselines:** guided hints and unrestricted chat are compared against the same tasks and schedule; the no-AI arm estimates learning without AI support.
- **Execution:** administer the baseline diagnostic, assign groups, deliver the common learning session, score immediate practice, and conduct the independent transfer task seven days later.
- **Pre-registration:** before recruitment, document the target population, recruitment method, sample-size/power calculation, randomization method, exclusion rules, missing-data strategy, primary model, contrasts, and significance threshold.
- **Reproducible record:** version the protocol, rubric, task materials, code, configuration, Python/container versions, AI model/version, and randomization seed where ethically appropriate. Record package and container digests for a final release.
- **Data minimization:** assign pseudonymous IDs; keep the identity key outside the analysis repo; do not place names, emails, student IDs, or raw identifiable submissions in GitHub.

The supplied sample is synthetic. The current `src/benchmark.py` validates the expected data schema and reports descriptive summaries only; it does not execute this inferential analysis plan.

## Validity threats and mitigations

| Threat | Why it matters | Mitigation |
|---|---|---|
| Baseline imbalance | Prior Python skill may affect the outcome | Randomize; stratify on baseline score; adjust for baseline in the pre-specified model |
| Attrition at day seven | Missing follow-up scores can differ by condition | Use identical follow-up reminders and scheduling; report completion by arm; pre-specify missing-data handling and sensitivity analyses |
| Grader expectation | Knowledge of condition can bias rubric scores | Blind graders to assignment; use written rubric examples; double-score a subset and report agreement |
| Treatment contamination | Control participants may use AI or groups may share solutions | Give clear condition instructions; record deviations; use comparable, supervised practice settings where feasible |
| Unequal AI exposure | Different model versions or access can create unintended differences | Fix and record model, version, settings, prompt rules, and access window for AI arms |
| Novelty / Hawthorne effects | Behavior may reflect study attention more than assistance style | Match session attention and time across arms; describe the study setting and limits |
| Limited generalizability | One course, institution, language, or task may not represent other learners | Describe sample and context; avoid claims beyond the recruited population; replicate across courses and tasks |
| Test-task alignment | A follow-up task too similar to practice may inflate transfer scores | Use a new task that assesses the same concepts with different surface features; finalize it before data collection |

## Ethics and privacy

Participation should be voluntary, and experimental participation or scores should not affect course grades. Obtain required institutional approval and informed consent before recruitment. Store only pseudonymized analysis data in this repository; keep any re-identification key separately with restricted access.
