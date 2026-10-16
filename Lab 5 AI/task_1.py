class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Edge:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.next = None

class Graph:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_edge(self, a, b):
        e = Edge(a, b)
        if self.head is None:
            self.head = e
        else:
            self.tail.next = e
        self.tail = e

    def seen(self, chain, x):
        while chain is not None:
            if chain.data == x:
                return True
            chain = chain.next
        return False

    def BFS(self, s, goal=None):
        visited = Node(s)
        front = back = Node(s)
        while front is not None:
            v = front.data
            front = front.next
            print(v, end=" ")
            if goal is not None and v == goal:
                print("\nGoal", goal, "found!")
                return
            e = self.head
            while e is not None:
                if e.a == v and not self.seen(visited, e.b):
                    n = Node(e.b)
                    n.next = visited
                    visited = n
                    q = Node(e.b)
                    if front is None:
                        front = q
                    else:
                        back.next = q
                    back = q
                e = e.next
        print()

print("Task 1: BFS from vertex 0")
g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(0, 4)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(1, 4)
g1.add_edge(2, 3)
g1.add_edge(3, 4)
g1.BFS(0)

print("\nTask 2: BFS from A, goal G")
g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('A', 'F')
g2.add_edge('A', 'D')
g2.add_edge('A', 'E')
g2.add_edge('B', 'K')
g2.add_edge('B', 'J')
g2.add_edge('D', 'G')
g2.add_edge('E', 'C')
g2.add_edge('E', 'H')
g2.add_edge('E', 'I')
g2.add_edge('K', 'N')
g2.add_edge('K', 'M')
g2.add_edge('I', 'L')

g2.BFS('A', 'L')