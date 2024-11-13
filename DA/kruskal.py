class DisjointSet:
    def __init__(self, n):
        # Initialize the parent and rank arrays for Union-Find
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        # Find the representative of the set containing u
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        # Union the sets containing u and v
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    # Sort edges based on their weights
    edges.sort(key=lambda x: x[2])  # Sorting by the third element (weight)
    
    # Initialize the Disjoint Set for union-find
    ds = DisjointSet(n)
    
    mst = []  # To store the edges of the MST
    mst_cost = 0  # To store the total cost of the MST
    
    # Process each edge in sorted order
    for u, v, weight in edges:
        # If u and v are in different sets, include this edge in the MST
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            mst_cost += weight
    
    return mst, mst_cost

# Example usage:
if __name__ == "__main__":
    # Number of vertices
    n = 4
    
    # List of edges (u, v, weight)
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    mst, mst_cost = kruskal(n, edges)
    
    print("Minimum Cost Spanning Tree:")
    for u, v, weight in mst:
        print(f"Edge ({u}, {v}) with weight {weight}")
    print(f"Total cost of the MST: {mst_cost}")
