from collections import deque

tree = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}

def bfs(tree, start, val):
    visited = []
    queue = deque()

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(f"Visiting node: {node}")

        if node == val:
            print(f"Value {val} found!")
            return

        for child in tree[node]:
            if child not in visited:
                visited.append(child)
                queue.append(child)

    print("Goal not found")

bfs(tree, 'A', 'G')




# from collections import deque

# tree = {
#     'A': ['B', 'F', 'D', 'E'],
#     'B': ['K', 'J'],
#     'F': [],
#     'D': ['G'],
#     'E': ['C', 'H', 'I'],
#     'K': ['N', 'M'],
#     'J': [],
#     'G': [],
#     'C': [],
#     'H': [],
#     'I': ['L'],
#     'N': [],
#     'M': [],
#     'L': []
# }

# def bfs(tree, start, val):
#     visited = []
#     queue = deque()
#     parent = {start: None}                

#     visited.append(start)
#     queue.append(start)

#     while queue:
#         node = queue.popleft()
#         print(f"Visiting node: {node}")

#         if node == val:
#             print(f"Value {val} found!")

#             # ADDED: trace the path back from the goal to the start
#             path = []
#             while node is not None:
#                 path.append(node)
#                 node = parent[node]
#             path.reverse()
#             print("Path:", " -> ".join(path))
#             return

#         for child in tree[node]:
#             if child not in visited:
#                 visited.append(child)
#                 queue.append(child)
#                 parent[child] = node      

#     print("Goal not found")

# bfs(tree, 'A', 'G')