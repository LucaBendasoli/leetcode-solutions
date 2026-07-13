from typing import List

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [0] * size
                self.components = size
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                
                if root_x == root_y:
                    return False
                
                if self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = root_y
                elif self.rank[root_x] > self.rank[root_y]:
                    self.parent[root_y] = root_x
                else:
                    self.parent[root_y] = root_x
                    self.rank[root_x] += 1
                
                self.components -= 1
                return True
            
            def is_connected(self):
                return self.components == 1
        
        alice_uf = UnionFind(n)
        bob_uf = UnionFind(n)
        
        edges_used = 0
        
        # Process type 3 edges first (both Alice and Bob can use)
        for edge_type, u, v in edges:
            if edge_type == 3:
                u -= 1
                v -= 1
                # Try to add to both Alice and Bob
                alice_added = alice_uf.union(u, v)
                bob_added = bob_uf.union(u, v)
                # If at least one was added, the edge is needed
                if alice_added or bob_added:
                    edges_used += 1
        
        # Process type 1 edges (Alice only)
        for edge_type, u, v in edges:
            if edge_type == 1:
                u -= 1
                v -= 1
                if alice_uf.union(u, v):
                    edges_used += 1
        
        # Process type 2 edges (Bob only)
        for edge_type, u, v in edges:
            if edge_type == 2:
                u -= 1
                v -= 1
                if bob_uf.union(u, v):
                    edges_used += 1
        
        # Check if both graphs are fully connected
        if alice_uf.is_connected() and bob_uf.is_connected():
            return len(edges) - edges_used
        else:
            return -1