#### Hacktober Fest 2022 - Hacktoberfest2022
### Tower of Hanoi in Python
## Problem Statement
The Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
3. No disk may be placed on top of a smaller disk.
#### Input Format
Create a function that takes an integer n as an argument and returns the minimum number of moves required to solve the Tower of Hanoi puzzle.
#### Output Format
Return an integer denoting the minimum number of moves required to solve the Tower of Hanoi puzzle.
#### Sample Input
```
n = 3
```
#### Sample Output
```
7
```
#### Explanation
The steps required to solve a Tower of Hanoi puzzle with 3 disks are:
1. Move disk 1 from rod 1 to rod 2
2. Move disk 2 from rod 1 to rod 3
3. Move disk 1 from rod 2 to rod 3
4. Move disk 3 from rod 1 to rod 2
5. Move disk 1 from rod 3 to rod 1
6. Move disk 2 from rod 3 to rod 2
7. Move disk 1 from rod 1 to rod 2

#### Testing
Run the following command:
```
python3 tests.py
```
If your code passes all test cases, then your solution will be accepted.

#### Contributing
If all test cases pass, your solution will be merged with the main branch. If you have any questions, feel free to open an issue.
