from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and 
                    (nr, nc) not in visited and 
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
        
        # Start DFS from Pacific Ocean borders (top row and left column)
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)
        
        # Start DFS from Atlantic Ocean borders (bottom row and right column)
        for i in range(m):
            dfs(i, n - 1, atlantic)
        for j in range(n):
            dfs(m - 1, j, atlantic)
        
        # Find intersection
        result = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        
        return result