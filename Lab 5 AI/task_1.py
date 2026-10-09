from collections import deque

graph = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}

def bfs(graph, start):
    visited = []        
    queue = deque()       

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.popleft()      
        print(node, end=" ")

        for hmsay in graph[node]:
            if hmsay not in visited:
                visited.append(hmsay)
                queue.append(hmsay)

print("BFS starting from node 0:")
bfs(graph, 0)