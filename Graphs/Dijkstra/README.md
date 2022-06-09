# Problem

# How I solved it

Solving this problem is similar to Dijkstra’s algorithm for shortest path. We can use a BFS to check all of the neighboring nodes of the current node (starting at the inputted ‘Source’ node) and if the node is in bounds of the board, not already visited, and not a ‘wall’ then add it to the queue and mark it as visited. Then pop the next node from the queue and do the same with that one.

If we pop all the elements out of the queue and we have not reached the destination cell then return ‘None’ as we were not able to reach it, but if we do come across the destination cell then we reconstruct the path by working backwards and checking the current node (which will be the destination node) with the the node it came from in the visited dictionary and add that to a new path list. The node that one came from will then be checked until the path is traced back to the beginning. Once the path list contains the path, we will have to reverse it so it is tracing in a forward direction from Source to Destination.
