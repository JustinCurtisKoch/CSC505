# Module 6: Critical Thinking Assignment (Common Personality Traits)
# Write a Python script to develop a simple task-scheduling algorithm for an operating system. 

# Create a Job class and define the associated attributes
class Job:
    def __init__(self, arrival_time, processing_time, process_id):
        self.arrival_time = arrival_time
        self.processing_time = processing_time
        self.process_id = process_id

# Create the Shortest Job First function
def shortest_job_first(jobs):
    time = 0                    # initial system time
    chart_metrics = []          # will be used to track how jobs complete
    completed_jobs = {}         # creates a store for completed jobs

# Create the main loop that will iterate through received jobs
    while jobs:
        current_jobs = []
        for job in jobs:
            if job.arrival_time <= time:
                current_jobs.append(job)

        if current_jobs == []:
            time += 1
            chart_metrics.append("Idle")
        else:
            current_jobs.sort(key=lambda x: x.processing_time) # Sort current jobs by processing time
            job = current_jobs[0]
            time += job.processing_time
            chart_metrics.append(job.process_id)
            current_time = time                                # Set time and compute results based on run times
            turnaround_time = current_time - job.arrival_time
            wait_time = turnaround_time - job.processing_time
            jobs.remove(job)                                   # Remove job from list once complete
            completed_jobs[job.process_id] = [current_time, turnaround_time, wait_time]

    return chart_metrics, completed_jobs  # Return the results

# Create a sample list of jobs
if __name__ == "__main__":
    jobs = [
        Job(0, 2, "P1"),
        Job(1, 3, "P2"),
        Job(1, 2, "P3"),
        Job(2, 8, "P4"),
        Job(3, 5, "P5"),
        Job(3, 3, "P6"),
    ]
    chart_metrics, completed_jobs = shortest_job_first(jobs)  # Call the function and print results
    print(f"Completion Order: {chart_metrics}")
    print("Completed Jobs:")
    for process_id, values in completed_jobs.items():
        print(f"Process {process_id}:")
        print(f"  Completion Time: {values[0]}")
        print(f"  Turnaround Time: {values[1]}")
        print(f"  Waiting Time: {values[2]}")
        print("-" * 20)  # Separator line

