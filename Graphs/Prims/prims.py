import sys


def prims(G):
    V = len(G)
    # Set to hold results
    result = set()
    # Track visited nodes and set the first one to true
    visited = [0 for i in range(V)]
    visited[0] = True
    seen = 0
    while (seen < V - 1):
        # Initialize minimum to some large number
        minimum = sys.maxsize
        x = y = 0
        for i in range(V):
            if visited[i]:
                for j in range(V):
                    if ((not visited[j]) and G[i][j]):
                        # not in visited and there is an edge
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        result.add((x, y, G[x][y]))
        visited[y] = True
        seen += 1
    return result


# Example Graph

G = [
    [0, 8, 5, 0, 0, 0, 0],
    [8, 0, 10, 2, 18, 0, 0],
    [5, 10, 0, 3, 0, 16, 0],
    [0, 2, 3, 0, 12, 30, 14],
    [0, 18, 0, 12, 0, 0, 4],
    [0, 0, 16, 30, 0, 0, 26],
    [0, 0, 0, 14, 4, 26, 0]
]

print(prims(G))
