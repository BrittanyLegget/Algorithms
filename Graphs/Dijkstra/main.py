from collections import deque as queue


def solve_puzzle(Board, Source, Destination):
    visited = {Source: None}
    q = queue([Source])
    # While the queue is not empty, popleft and evaluate all the nodes neighbors (BFS)
    while q:
        node = q.popleft()
        row = node[0]
        col = node[1]
        # If we have reached destination cell the create path
        if node == Destination:
            path = []
            commands = []
            while node is not None:
                path.append(node)
                temp = node
                temp2 = visited[node]
                node = visited[node]
                # Use math to determine which direction was moved between nodes and add to command
                if temp2 == None:
                    break
                elif temp[0] - temp2[0] == 1 and temp[1] - temp2[1] == 0:
                    commands.append('D')
                elif temp[0] - temp2[0] == 0 and temp[1] - temp2[1] == 1:
                    commands.append('R')
                elif temp[0] - temp2[0] == -1 and temp[1] - temp2[1] == 0:
                    commands.append('U')
                elif temp[0] - temp2[0] == 0 and temp[1] - temp2[1] == -1:
                    commands.append('L')

            commands.reverse()
            path.reverse()
            return path[::], commands[::]

        # All directions that need to be checked from current node
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Loop through neighboring cells
        for x, y in directions:
            next_row = row + x
            next_col = col + y
            neighbor = (next_row, next_col)

            # If in bounds, not visited already, and not a wall then add to queue and mark as visited
            if len(Board) > next_row >= 0 <= next_col < len(Board[0]) and (next_row, next_col) not in visited and Board[next_row][next_col] != '#':
                visited[neighbor] = node
                q.append(neighbor)
    return None


Board = [['-', '-', '-', '-', '-'], ['-', '-', '#', '-', '-'],
         ['-', '-', '-', '-', '-'], ['#', '-', '#', '#', '-']]
Source = (0, 0)
Destination = (3, 4)
print(solve_puzzle(Board, Source, Destination))
