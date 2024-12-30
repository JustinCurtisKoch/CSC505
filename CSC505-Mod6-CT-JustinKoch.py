class Job:
    def __init__(self, arrival_time, processing_time, process_id):
        self.arrival_time = arrival_time
        self.processing_time = processing_time
        self.process_id = process_id

def sjf(jobs):
    time = 0
    chart_metrics = []
    completed_jobs = {}

    while jobs:
        current_jobs = []
        for job in jobs:
            if job.arrival_time <= time:
                current_jobs.append(job)

        if current_jobs == []:
            time += 1
            chart_metrics.append("Idle")
        else:
            # Sort available jobs by processing time (shortest first)
            current_jobs.sort(key=lambda x: x.processing_time)
            job = current_jobs[0]

            time += job.processing_time
            chart_metrics.append(job.process_id)
            current_time = time
            total_time = current_time - job.arrival_time
            wait_time = total_time - job.processing_time
            jobs.remove(job)
            completed_jobs[job.process_id] = [current_time, total_time, wait_time]

    return chart_metrics, completed_jobs  # Return the results

if __name__ == "__main__":
    jobs = [
        Job(2, 1, "P1"),
        Job(0, 2, "P2"),
        Job(4, 3, "P5"),
        Job(2, 4, "P4"),
        Job(8, 5, "P3")
    ]
    chart_metrics, completed_jobs = sjf(jobs)  # Call the function and get results
    print(f"Completion Order: {chart_metrics}")
    print("Completed Jobs:")
    for process_id, values in completed_jobs.items():
        print(f"Process {process_id}:")
        print(f"  Completion Time: {values[0]}")
        print(f"  Turnaround Time: {values[1]}")
        print(f"  Waiting Time: {values[2]}")
        print("-" * 20)  # Separator line

