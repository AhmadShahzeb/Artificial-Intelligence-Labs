class Edge:
    def __init__(self, to):
        self.to = to
        self.next = None


class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.parent = None
        self.edges = None        # first edge
        self.last = None         # last edge
        self.next = None         # next vertex in the graph's chain
        self.qnext = None        # next vertex in the queue


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def push(self, v):
        if self.back is None:
            self.front = v
        else:
            self.back.qnext = v
        self.back = v

    def pop(self):
        v = self.front
        self.front = v.qnext
        if self.front is None:
            self.back = None
        return v


class Graph:
    def __init__(self):
        self.head = None         # first vertex
        self.tail = None         # last vertex

    def get_vertex(self, name):  # find vertex, create it if missing
        v = self.head
        while v is not None:
            if v.name == name:
                return v
            v = v.next
        v = Vertex(name)
        if self.head is None:
            self.head = v
        else:
            self.tail.next = v
        self.tail = v
        return v

    def add_edge(self, a, b):    # one direction: a -> b
        va, vb = self.get_vertex(a), self.get_vertex(b)
        e = Edge(vb)
        if va.edges is None:
            va.edges = e
        else:
            va.last.next = e
        va.last = e

    def add_undirected_edge(self, a, b):   # both directions
        self.add_edge(a, b)
        self.add_edge(b, a)

    def print_path(self, v):
        if v.parent is not None:
            self.print_path(v.parent)
            print(" -> ", end="")
        print(v.name, end="")

    def BFS(self, s, goal=None):
        q = Queue()
        start = self.get_vertex(s)
        start.visited = True
        q.push(start)

        while q.front is not None:
            v = q.pop()
            print(v.name, end=" ")

            if goal is not None and v.name == goal:
                print("\nGoal", goal, "found!")
                print("Path: ", end="")
                self.print_path(v)
                print()
                return

            e = v.edges
            while e is not None:
                if not e.to.visited:
                    e.to.visited = True
                    e.to.parent = v
                    q.push(e.to)
                e = e.next
        print()



# ---------- Task 2 ----------
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

print("\nTask 2: BFS from A, goal G")
g2.BFS('A', 'G')