import csv
from datetime import datetime, timedelta
from collections import defaultdict

# -- Threshhold intervals in seconds
WARNING_THRESHOLD = 300
ERROR_THRESHOLD = 600
    
# function to parse the log file
def parse_logfile (file):
    task = defaultdict(dict)
    period = {}
    
    with open(file, newline='') as filename:
        for row in filename:
            part = [line.strip() for line in row.split(",")]
            if len(part) >= 4:
                try:
                    time_stamp = datetime.strptime(part[0], "%H:%M:%S")
                    job_parts = part[1].split()
                    job_type = ' '.join(job_parts[:-1])
                    job_id = job_parts[-1]
                    status = part[2].strip().lower()
                    task_id = part[3]
                    task[(job_type, job_id, task_id)][status] = time_stamp
                except (ValueError, IndexError):
                    continue
    return {
        key: (time_spent["end"] - time_spent["start"]).total_seconds()
        if "start" in time_spent and "end" in time_spent else None
        for key, time_spent in task.items()
    }
    

# function to analyze the time spent on the task
def analyze_time(periods):
    for (job_type, job_id, task_id), duration in periods.items():
        label = f"{job_type} {job_id} (pid {task_id})"
        if duration is None:
            print(f"[ERROR] {label} missing START or END time")
        else:
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            time_str = f"{minutes} minutes and {seconds} seconds"
            if duration > ERROR_THRESHOLD:
                print(f"[ERROR] {label} took {time_str}")
            elif duration > WARNING_THRESHOLD:
                print(f"[WARNING] {label} took {time_str}")
            else:
                print(f"{label} completed in {time_str}")
            
if __name__ == "__main__":
    log_file = "logs.log"
    periods = parse_logfile(log_file)
    analyze_time(periods)
    
