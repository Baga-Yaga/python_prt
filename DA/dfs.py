from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(self.V)}
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  

    # BFS traversal function
    def bfs(self, start):
        visited = [False] * self.V
        
        queue = deque([start])
        
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)


g = Graph(6)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("Breadth-First Traversal (BFS) starting from node 0:")
g.bfs(0)
