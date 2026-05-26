#!/usr/bin/env python3
"""
Lab: Defensive debugging and validation.

Goal: compute average score from user-provided text.
Starter assumes ideal input and fails with non-numeric tokens.
"""

import logging  # Adding module for logging


def parse_scores_csv(scores_text):
    """Parse comma-separated scores into a list of ints."""

    # LARGELY insufficient and over-optimistic code xd
    # parts = scores_text.split(",")
    # return [int(part) for part in parts]

    # Defining a clean variable to score actually exploitable data.
    exploitable_scores = []

    if not isinstance(scores_text, str):
        invalid_input_type_msg = "Error, provided param {} is NOT a string!"
        logging.error(invalid_input_type_msg.format(scores_text))
        return exploitable_scores

    parts = scores_text.split(",")
    for item in parts:
        # Try INSIDE the loop to ensure we can traverse ALL list
        #   and retrieve at least all exploitable values.
        # A try "outside" would make the loop stop at 1st raised exception.
        try:
            score = int(item)
            exploitable_scores.append(score)
        except ValueError as e:
            # Info because usually error/misunderstanding from user
            logging.info(f"Input '{score}' can't be read as int, skipped")
        except TypeError as e:
            # Warning because this usually shouldn't happen but it doesn't
            #   block processing as the value will simply be ignored.
            wrong_type_msg = "Input provided {} read as type {}"
            logging.warning(wrong_type_msg.format(score, type(score)))
    return exploitable_scores


def average_score(scores):
    """Return arithmetic mean of a non-empty score list."""
    # As overoptimistic as above
    # return sum(scores) / len(scores)

    if len(scores) == 0:
        return None
    else:
        return sum(scores) / len(scores)


def score_band(avg):
    """Classify average score into a textual band."""
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"


def evaluate_scores(scores_text):
    """Return (average, band) from comma-separated score text."""
    scores = parse_scores_csv(scores_text)
    print(scores)
    # Nope, not good enough ;)
    # avg = round(average_score(scores), 2)
    # return avg, score_band(avg)
    if scores is None or len(scores) == 0:
        logging.info("No exploitable score found to process!")
        return None, None
    else:
        avg = round(average_score(scores), 2)
        return avg, score_band(avg)


# Adding a method to setup logging
def start_logging():
    logging.basicConfig(level=level, format="%(levelname)s:%(message)s")


def main():
    scores_text = "90,85,invalid,100"
    avg, band = evaluate_scores(scores_text)
    print("Average:", avg)
    print("Band:", band)


if __name__ == "__main__":
    main()

    print("==== ADDITIONAL TESTS ====")
    print("Case 1: full valid scores")
    fullvalid_scores_as_text = "1, 30, 55, 60"
    full_valid = evaluate_scores(fullvalid_scores_as_text)

    print("Parsed scores:", parse_scores_csv(fullvalid_scores_as_text))
    print("Respective average and band full_valid", full_valid)

    print("Case 2: mixed ints and floats")
    mixed_int_and_floats = "1, 30, 55.55, 80.40"
    print("Parsed scores:", parse_scores_csv(mixed_int_and_floats))
    mixed_result = evaluate_scores(mixed_int_and_floats)
    print("Respective average and band mixed", mixed_result)

    print("Case 3: full invalid types")
    fully_invalid_types = [{"key": "value"}, False, "haha"]
    print("Parsed scores:", parse_scores_csv(fully_invalid_types))
    full_invalid = evaluate_scores(fully_invalid_types)
    print("Respective average and band full_valid", full_invalid)
