import queue

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    time, waiting_time, turnaround_time = 0, [], []
    gantt_chart = []
    
    for process in processes:
        pid, arrival, burst = process
        start_time = max(time, arrival)
        gantt_chart.append((start_time, pid))
        time = start_time + burst
        waiting_time.append(start_time - arrival)
        turnaround_time.append(time - arrival)
    
    return gantt_chart, waiting_time, turnaround_time

def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time, then burst time
    ready_queue = []
    time, waiting_time, turnaround_time = 0, {}, {}
    completed = 0
    gantt_chart = []
    
    while completed < len(processes):
        available = [p for p in processes if p[1] <= time and p[0] not in waiting_time]
        if available:
            available.sort(key=lambda x: x[2])  # Shortest burst time first
            process = available[0]
            pid, arrival, burst = process
            gantt_chart.append((time, pid))
            time += burst
            waiting_time[pid] = time - arrival - burst
            turnaround_time[pid] = time - arrival
            completed += 1
        else:
            time += 1
    
    return gantt_chart, list(waiting_time.values()), list(turnaround_time.values())

def srt_scheduling(processes):
    time = 0
    remaining_time = {p[0]: p[2] for p in processes}
    waiting_time, turnaround_time = {}, {}
    gantt_chart = []
    completed = 0
    
    while completed < len(processes):
        available = [p for p in processes if p[1] <= time and remaining_time[p[0]] > 0]
        if available:
            available.sort(key=lambda x: remaining_time[x[0]])  # Shortest remaining time
            process = available[0]
            pid, arrival, _ = process
            gantt_chart.append((time, pid))
            remaining_time[pid] -= 1
            time += 1
            if remaining_time[pid] == 0:
                turnaround_time[pid] = time - arrival
                waiting_time[pid] = turnaround_time[pid] - process[2]
                completed += 1
        else:
            time += 1
    
    return gantt_chart, list(waiting_time.values()), list(turnaround_time.values())

def round_robin_scheduling(processes, quantum):
    ready_queue = queue.Queue()
    time, waiting_time, turnaround_time = 0, {}, {}
    remaining_time = {p[0]: p[2] for p in processes}
    gantt_chart = []
    
    for process in processes:
        ready_queue.put(process)
    
    while not ready_queue.empty():
        pid, arrival, burst = ready_queue.get()
        if remaining_time[pid] > 0:
            start_time = max(time, arrival)
            gantt_chart.append((start_time, pid))
            if remaining_time[pid] > quantum:
                time = start_time + quantum
                remaining_time[pid] -= quantum
                ready_queue.put((pid, arrival, burst))
            else:
                time = start_time + remaining_time[pid]
                waiting_time[pid] = time - arrival - burst
                turnaround_time[pid] = time - arrival
                remaining_time[pid] = 0
    
    return gantt_chart, list(waiting_time.values()), list(turnaround_time.values())

def print_results(gantt_chart, waiting_time, turnaround_time):
    print("Gantt Chart:", gantt_chart)
    print("Waiting Times:", waiting_time)
    print("Turnaround Times:", turnaround_time)
    print("Average Waiting Time:", sum(waiting_time) / len(waiting_time))
    print("Average Turnaround Time:", sum(turnaround_time) / len(turnaround_time))

def main():
    while True:
        print("\nCPU Scheduling Algorithms")
        print("1. FCFS")
        print("2. SJF")
        print("3. SRT")
        print("4. Round Robin")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 5:
            break


        n = int(input("Enter number of processes: "))
        processes = []
        for i in range(n):
            pid = input(f"Enter Process ID for P{i + 1}: ")
            arrival = int(input(f"Enter Arrival Time for {pid}: "))
            burst = int(input(f"Enter Burst Time for {pid}: "))
            processes.append((pid, arrival, burst))
        
        if choice == 4:
            quantum = int(input("Enter Time Quantum: "))
        
        if choice == 1:
            gantt_chart, wt, tat = fcfs_scheduling(processes)
        elif choice == 2:
            gantt_chart, wt, tat = sjf_scheduling(processes)
        elif choice == 3:
            gantt_chart, wt, tat = srt_scheduling(processes)
        elif choice == 4:
            gantt_chart, wt, tat = round_robin_scheduling(processes, quantum)
        else:
            print("Invalid choice. Try again.")
            continue

        print_results(gantt_chart, wt, tat)

if __name__ == "__main__":
    main()
