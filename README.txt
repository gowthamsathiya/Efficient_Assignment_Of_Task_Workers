**Project**
#6  Network Flow: Resource Allocation and Project Scheduling
**Project**

**Description**

The code is organized in 2 folders.
Problem_1_3 : For Problem 6.1 and 6.3 
Problem_2 : For Problem 6.2

The folders contain sample input files and result files.
Please delete the result files before executing the commands, as the results get appended.

Input Files must be named inputfile_tasks.txt, inputfile_workers.txt, inputfile_6.3.txt
The format followed is:

T1,2,3,[W1;W2] for task file where T1 is task ID, 2 is min, 3 is max and [W1;W2] are qualified workers

W1,2,5 for worker file where W1 is worker ID, 2 is min and 5 is max
2,-50,[3] for 6.3 profit file where 2 is the task ID, -50 is the profit and 3 is a dependency task

Command to run Fordfulkersan and Edmond karp for Problem 2:
python Problem_2/main_start_2.py

Command to run Fordfulkersan and Edmond karp for Problem 1 and 3:
python Problem_1_3/main_start_1.py

Result Files are created in the respective directories.
Result Files are named Result_File_x.txt

**Description**
