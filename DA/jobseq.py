class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, n):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    result = [-1] * n 
    total_profit = 0
    
    for job in jobs:
        for slot in range(min(n, job.deadline) - 1, -1, -1):
            if result[slot] == -1:
                result[slot] = job.id 
                total_profit += job.profit  
                break
    
    print("Job Sequence:", end=" ")
    for job_id in result:
        if job_id != -1:
            print(job_id, end=" ")
    print(f"\nTotal Profit: {total_profit}")

n = int(input("Enter the number of jobs: "))
jobs = []

for i in range(n):
    job_id = input(f"Enter Job {i+1} ID: ")
    deadline = int(input(f"Enter Job {i+1} Deadline: "))
    profit = int(input(f"Enter Job {i+1} Profit: "))
    jobs.append(Job(job_id, deadline, profit))

job_sequencing(jobs, n)
