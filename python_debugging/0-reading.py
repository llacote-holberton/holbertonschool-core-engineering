#!/usr/bin/env python3
"""
Lab: Reading the bug.

Batch summary for a stub sensor: sum numeric readings.
This script is intentionally broken for debugging practice.
"""


def accumulate_readings(values):
    """Sum all readings into a single running sum."""
    running_sum = 0
    for value in values:
        # Before: direct attempt to use arithmetic on raw value
        # running_sum += value
        try:
            # value = float(value)  # In fact we can convert on the fly.
            running_sum += float(value)
        except (ValueError, TypeError) as e:
            print(f"Value {value} skipped from aggregation, confer error...")
            print(e)
    return running_sum


def load_today_batch():
    """Return today's readings from the (stub) pipeline."""
    # In production this might come from a file or API; here it is hard-coded.
    return ["12", "5", "7"]


def main():
    batch = load_today_batch()
    result = accumulate_readings(batch)
    print("Total readings:", result)


if __name__ == "__main__":
    main()
    # TRACE STACK: triggered main -> load_today_batch -> accumulate_readings
    # Error msg: TypeError: unsupported operand type(s) for +=: 'int' and 'str'

    # DIAGNOSIS: bug comes from propagating values of non-guaranteed type
    #   up to a function which would only accept arithmetic compatible types.

    # BRAINSTORM: first intuition would have been to force-convert to int
    #   the values in their "source" function "load today's batch".
    # But it may not be a great idea in real life case
    #   since same "source data" may possibly be used elsewhere.
    # -> Went instead for "in-place fix" closest to actual source.

    # DESIGN CHOICE: since accumulate_readings is the one requiring numbers,
    #   it is inside it which we will try to convert each value to a float
    #   (better real-life "use-case range" than int)
