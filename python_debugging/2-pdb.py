#!/usr/bin/env python3
"""
Lab: First steps with pdb.

Compute an adjusted average from raw scores. The script runs, but the result
is wrong due to a logic bug that is easier to isolate with pdb than with
ad-hoc prints.
"""
import pdb


def normalize_score(raw, bonus):
    """Apply bonus and cap score at 100."""
    adjusted = raw + bonus
    if adjusted > 100:
        adjusted = 100
    return adjusted


def compute_adjusted_average(scores, bonus):
    """Return rounded average after normalization."""
    raw_sum = 0
    count = 0

    for raw in scores:
        adjusted = normalize_score(raw, bonus)
        # breakpoint()
        # Error: business goal is to average *with normalization*
        # raw_sum += raw
        raw_sum += adjusted
        count += 1

    if count == 0:
        return 0.0

    return round(raw_sum / count, 2)


def main():
    scores = [40, 60, 80]
    bonus = 10
    final_avg = compute_adjusted_average(scores, bonus)
    print("Adjusted average:", final_avg)

    other_scores = [5, 18, 34, 79, 96, 81]
    no_bonus_average = sum(other_scores) / len(other_scores)
    print("Plain avg for other_scores should be ~52.17, got", no_bonus_average)
    other_scores_adjusted = compute_adjusted_average(other_scores, bonus)
    print("Adjusted avg for other_scores should be ~62.17, got",
          other_scores_adjusted)


if __name__ == "__main__":
    main()
