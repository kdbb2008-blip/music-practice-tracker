"""Show total practice minutes for each instrument."""

import csv
from collections import defaultdict
from pathlib import Path

LOG_FILE = Path("practice_log.csv")


def main():
    if not LOG_FILE.exists():
        print("No practice recorded yet. Run practice_tracker.py first.")
        return

    totals = defaultdict(int)

    with LOG_FILE.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            totals[row["instrument"]] += int(row["minutes"])

    print("Practice totals:")
    for instrument, minutes in sorted(totals.items()):
        print(f"{instrument}: {minutes} minutes")


if __name__ == "__main__":
    main()
