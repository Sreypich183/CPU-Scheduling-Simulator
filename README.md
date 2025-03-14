# CPU Scheduling Algorithms

## Description
This project implements four different CPU scheduling algorithms in Python:
- **First-Come, First-Served (FCFS)**
- **Shortest Job First (SJF)**
- **Shortest Remaining Time (SRT) (Preemptive SJF)**
- **Round Robin (RR)**

The program allows users to select a scheduling algorithm, input process details, and view the Gantt chart, waiting times, turnaround times, and average times for scheduling analysis.

---

## Compilation & Execution Instructions
### Prerequisites:
- Python 3.x installed

### Steps to Run the Program:
1. Clone the repository:
   ```sh
   git clone https://github.com/Sreypich183/cpu-scheduling.git
   ```
2. Navigate to the project folder:
   ```sh
   cd cpu-scheduling
   ```
3. Run the Python script:
   ```sh
   python scheduling.py
   ```
4. Follow the on-screen instructions to select a scheduling algorithm and enter process details.

---

## Example Usage
### Sample Input:
```
Enter your choice: 3
Enter number of processes: 4
Enter Process ID for P1: A
Enter Arrival Time for A: 0
Enter Burst Time for A: 5
Enter Process ID for P2: B
Enter Arrival Time for B: 1
Enter Burst Time for B: 3
Enter Process ID for P3: C
Enter Arrival Time for C: 2
Enter Burst Time for C: 8
Enter Process ID for P4: D
Enter Arrival Time for D: 3
Enter Burst Time for D: 6
```

### Sample Output:
```
Gantt Chart: [(0, 'A'), (1, 'B'), (2, 'B'), (3, 'B'), (4, 'A'), (5, 'A'), (6, 'A'), (7, 'A'), 
              (8, 'D'), (9, 'D'), (10, 'D'), (11, 'D'), (12, 'D'), (13, 'D'), 
              (14, 'C'), (15, 'C'), (16, 'C'), (17, 'C'), (18, 'C'), (19, 'C'), (20, 'C'), (21, 'C')]

Waiting Times: [0, 3, 5, 12]
Turnaround Times: [3, 8, 11, 20]
Average Waiting Time: 5.0
Average Turnaround Time: 10.5
```

---

## License
This project is open-source and available under the MIT License.

