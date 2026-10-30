# music-practice-tracker
A Python tool for recording music practice sessions and summarizing practice time.
# Music Practice Tracker

A Python command-line tool for recording music practice and viewing
total practice time by instrument.

## Requirements

Python 3. No additional packages are needed.

## Record a session

Download the project, open a terminal in its folder, and run:

```
python3 practice_tracker.py
```

Enter your instrument, minutes practiced, and notes.
Sessions are saved in practice_log.csv in the current folder.

## View practice totals

From the same folder, run:

```
python3 practice_summary.py
```

The summary displays total minutes for each instrument.

## Privacy

Practice logs are local data. Avoid uploading personal notes or credentials.

## Branches

- main: base practice tracker
- feature/practice-summary: adds practice summaries and usage instructions
