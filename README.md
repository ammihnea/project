# Log Analyzer

This Python script analyzes a log file to track the duration of scheduled tasks and background jobs, providing warnings and errors based on predefined thresholds.

## Features

- Read file and parses CSV-formatted log entries from `logs.log`
- Calculates the time spent on each task from START to END timestamps
- Reports tasks that exceed warning (5 minutes) or error (10 minutes) thresholds
- Handles missing START or END entries with error messages
- Outputs durations in minutes and seconds format

## Requirements

- Python 3.x
- Standard library modules: `datetime`, `collections`

## Log File Format

The script expects a file given as argument, with each line in the format:

```
HH:MM:SS,job description,START/END,PID
```

Example:
```
11:35:23,scheduled task 032,START,37980
11:35:56,scheduled task 032,END,37980
```

- **HH:MM:SS**: Timestamp in 24-hour format
- **job description**: Description like "scheduled task 032" or "background job wmy"
- **START/END**: Status of the job
- **PID**: Process ID or task identifier

!!! In case the file 
## How to Run

1. Ensure argument is given when running the script
2. Run the script:

```bash
python monitor.py logs.log
```

## Output Example

```
scheduled task 032 (task 37980) completed in 0 minutes and 33 seconds
[WARNING] background job wmy (task 81258) took 5 minutes and 46 seconds
[ERROR] scheduled task 374 (task 23703) took 13 minutes and 43 seconds
[ERROR] scheduled task 333 (task 72029) missing START or END time
```

## Thresholds

- **Warning**: Tasks taking longer than 5 minutes (300 seconds)
- **Error**: Tasks taking longer than 10 minutes (600 seconds)

## Notes

- The script assumes all timestamps are on the same day (no date handling)
- Jobs without both START and END entries will be flagged as errors
- Output is printed to the console
