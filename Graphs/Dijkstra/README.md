# Problem
You are given a 2-D puzzle of size MxN, that has N rows and M column (N>=3 ; M >= 3; M and N can be different). Each cell in the puzzle is either empty or has a barrier. An empty cell is marked by ‘-’ (hyphen) and the one with a barrier is marked by ‘#’. You are given two coordinates from the puzzle (a,b) and (x,y). You are currently located at (a,b) and want to reach (x,y). 

You can move only in the following directions:
L: move to left cell from the current cell R: move to right cell from the current cell
U: move to upper cell from the current cell
D: move to the lower cell from the current cell

You can move to only an empty cell and cannot move to a cell with a barrier in it. Your goal is to find the minimum number of cells that you have to cover to reach the destination cell (do not count the starting cell and the destination cell). The coordinates (1,1) represent the first cell; (1,2) represents the second cell in the first row. If there is not possible path from source to destination return None.

Sample Input Puzzle Board: [[-,-,-,-,-],[-,-,#,-,-],[-,-,-,-,-],[#,-,#,#,-],[-#,-,-,-]]

![graph board](https://user-images.githubusercontent.com/23641129/172778516-70381d95-bfa6-45b9-b1b6-8b34b2982df5.PNG)

Example 1: (a,b) : (1,3) ; (x,y): (3,3)
Output: 3
On possible direction to travel: LDDR (1,3) (1,2)  (2,2)  (3,2)(3,3)

Example 2: (a,b): (1,1) ; (x,y): (5,5)
Output: 7
One possible direction to travel: DDRRRRDD
(1,1) (2,1)(3,1)(3,2)(3,3)(3,4)(3,5)(4,5)(5,5)

Example 3: (a,b): (1,1); (x,y) : (5,1)
Output: None


# How I chose to solved it

Solving this problem is similar to Dijkstra’s algorithm for shortest path. We can use a BFS to check all of the neighboring nodes of the current node (starting at the inputted ‘Source’ node) and if the node is in bounds of the board, not already visited, and not a ‘wall’ then add it to the queue and mark it as visited. Then pop the next node from the queue and do the same with that one.

If we pop all the elements out of the queue and we have not reached the destination cell then return ‘None’ as we were not able to reach it, but if we do come across the destination cell then we reconstruct the path by working backwards and checking the current node (which will be the destination node) with the the node it came from in the visited dictionary and add that to a new path list. The node that one came from will then be checked until the path is traced back to the beginning. Once the path list contains the path, we will have to reverse it so it is tracing in a forward direction from Source to Destination.
