from typing import List

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [0] * size
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
            
            def connected(self, x, y):
                return self.find(x) == self.find(y)
        
        # Sort edges by distance
        edgeList.sort(key=lambda x: x[2])
        
        # Sort queries by limit, keeping track of original indices
        indexed_queries = [(q[0], q[1], q[2], i) for i, q in enumerate(queries)]
        indexed_queries.sort(key=lambda x: x[2])
        
        uf = UnionFind(n)
        answer = [False] * len(queries)
        edge_idx = 0
        
        for p, q, limit, original_idx in indexed_queries:
            # Add all edges with distance < limit
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                u, v, dis = edgeList[edge_idx]
                uf.union(u, v)
                edge_idx += 1
            
            # Check if p and q are connected
            answer[original_idx] = uf.connected(p, q)
        
        return answer