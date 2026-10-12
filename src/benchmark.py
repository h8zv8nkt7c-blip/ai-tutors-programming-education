#!/usr/bin/env python3
"""Summarize anonymized outcomes for the AI tutoring study (stdlib only)."""
import argparse
import csv
import json
import statistics
from pathlib import Path

REQUIRED = {"participant_id", "condition", "baseline_score", "practice_score", "delayed_transfer_score"}


def read_rows(path, minimum, maximum):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
        rows = []
        seen = set()
        for line, row in enumerate(reader, start=2):
            pid = row["participant_id"].strip()
            if not pid or pid in seen:
                raise ValueError(f"Line {line}: participant_id must be non-empty and unique")
            seen.add(pid)
            record = {"participant_id": pid, "condition": row["condition"].strip()}
            for key in ("baseline_score", "practice_score", "delayed_transfer_score"):
                try:
                    score = float(row[key])
                except (TypeError, ValueError):
                    raise ValueError(f"Line {line}: {key} must be numeric")
                if not minimum <= score <= maximum:
                    raise ValueError(f"Line {line}: {key} outside [{minimum}, {maximum}]")
                record[key] = score
            record["practice_to_delayed_gap"] = record["practice_score"] - record["delayed_transfer_score"]
            rows.append(record)
    if not rows:
        raise ValueError("No participant rows found")
    return rows


def summarize(values):
    return {
        "n": len(values),
        "mean": statistics.mean(values),
        "sd": statistics.stdev(values) if len(values) > 1 else None,
        "median": statistics.median(values),
        "min": min(values),
        "max": max(values),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="config.json")
    args = parser.parse_args()
    cfg_path = Path(args.config).resolve()
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    root = cfg_path.parent
    data_path = (root / cfg["dataset"]).resolve()
    output_path = (root / cfg["output"]).resolve()
    low, high = float(cfg["score_min"]), float(cfg["score_max"])
    rows = read_rows(data_path, low, high)
    order = cfg["condition_order"]
    unknown = sorted({r["condition"] for r in rows} - set(order))
    if unknown:
        raise ValueError(f"Unknown conditions: {', '.join(unknown)}")
    grouped = {condition: [r for r in rows if r["condition"] == condition] for condition in order}
    outcomes = ("baseline_score", "practice_score", "delayed_transfer_score", "practice_to_delayed_gap")
    result = {
        "study": "AI tutors in introductory Python education",
        "dataset": str(data_path.relative_to(root)),
        "synthetic_sample": "data/sample/sample.csv" in cfg["dataset"],
        "primary_outcome": cfg["primary_outcome"],
        "follow_up_days": cfg["follow_up_days"],
        "n_total": len(rows),
        "groups": {},
        "primary_contrasts_delayed_score_points": {},
        "note": "Descriptive summary only; this script does not perform inferential tests or establish causal effects.",
    }
    for condition, group in grouped.items():
        result["groups"][condition] = {"n": len(group)}
        for outcome in outcomes:
            vals = [r[outcome] for r in group]
            result["groups"][condition][outcome] = summarize(vals) if vals else None
    guided = result["groups"]["guided_hints"]["delayed_transfer_score"]
    for other in ("unrestricted_chatbot", "no_ai_control"):
        comparison = result["groups"][other]["delayed_transfer_score"]
        result["primary_contrasts_delayed_score_points"][f"guided_hints_minus_{other}"] = round(guided["mean"] - comparison["mean"], 4) if guided and comparison else None
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
