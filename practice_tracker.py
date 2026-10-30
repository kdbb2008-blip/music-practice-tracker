"""Record music practice sessions in a local CSV file."""

import csv
from datetime import date
from pathlib import Path

LOG_FILE = Path("practice_log.csv")


def main():
    instrument = input("Instrument: ").strip()
    if not instrument:
        print("Please enter an instrument.")
        return

    try:
        minutes = int(input("Minutes practiced: "))
        if minutes <= 0:
            raise ValueError
    except ValueError:
        print("Minutes must be a positive whole number.")
        return

    notes = input("Practice notes: ").strip()
    needs_header = not LOG_FILE.exists() or LOG_FILE.stat().st_size == 0

    with LOG_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if needs_header:
            writer.writerow(["date", "instrument", "minutes", "notes"])
        writer.writerow([date.today().isoformat(), instrument, minutes, notes])

    print(f"Saved {minutes} minutes of {instrument} practice.")


if __name__ == "__main__":
    main()
