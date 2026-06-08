from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # dp[r][c1][c2] = max cherries when robot1 at (r, c1) and robot2 at (r, c2)
        # Use two arrays for space optimization
        prev = {}
        prev[(0, cols - 1)] = grid[0][0] + (grid[0][cols - 1] if cols > 1 else 0)
        
        for r in range(1, rows):
            curr = {}
            for c1 in range(cols):
                for c2 in range(cols):
                    max_cherries = -1
                    # Try all 9 combinations of moves for both robots
                    for dc1 in [-1, 0, 1]:
                        for dc2 in [-1, 0, 1]:
                            prev_c1 = c1 - dc1
                            prev_c2 = c2 - dc2
                            if 0 <= prev_c1 < cols and 0 <= prev_c2 < cols:
                                if (prev_c1, prev_c2) in prev:
                                    max_cherries = max(max_cherries, prev[(prev_c1, prev_c2)])
                    
                    if max_cherries >= 0:
                        # Collect cherries at current position
                        cherries = grid[r][c1]
                        if c1 != c2:
                            cherries += grid[r][c2]
                        curr[(c1, c2)] = max_cherries + cherries
            
            prev = curr
        
        # Find maximum in the last row
        return max(prev.values()) if prev else 0