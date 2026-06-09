from collections import deque
from typing import List

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # BFS to compute fire spread times
        def fire_bfs():
            fire_time = [[float('inf')] * n for _ in range(m)]
            queue = deque()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        fire_time[i][j] = 0
                        queue.append((i, j, 0))
            
            while queue:
                x, y, t = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and fire_time[nx][ny] == float('inf'):
                        fire_time[nx][ny] = t + 1
                        queue.append((nx, ny, t + 1))
            
            return fire_time
        
        # BFS to check if person can reach safehouse with delay
        def person_bfs(delay):
            if fire_time[0][0] <= delay:
                return False
            
            person_time = [[float('inf')] * n for _ in range(m)]
            person_time[0][0] = delay
            queue = deque([(0, 0, delay)])
            
            while queue:
                x, y, t = queue.popleft()
                
                if x == m - 1 and y == n - 1:
                    return True
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and person_time[nx][ny] == float('inf'):
                        new_time = t + 1
                        # Person arrives at (nx, ny) at time new_time
                        # Check conditions
                        if nx == m - 1 and ny == n - 1:
                            # Can arrive at safehouse if fire hasn't reached it yet, or arrives at same time
                            if new_time <= fire_time[nx][ny]:
                                person_time[nx][ny] = new_time
                                queue.append((nx, ny, new_time))
                        else:
                            # For non-safehouse cells, must arrive strictly before fire
                            if new_time < fire_time[nx][ny]:
                                person_time[nx][ny] = new_time
                                queue.append((nx, ny, new_time))
            
            return False
        
        fire_time = fire_bfs()
        
        # Binary search on delay
        left, right = 0, 10**9
        result = -1
        
        # Check if any path exists
        if not person_bfs(0):
            return -1
        
        # Check if infinite delay works
        if fire_time[m - 1][n - 1] == float('inf'):
            return 10**9
        
        # Binary search for maximum delay
        while left <= right:
            mid = (left + right) // 2
            if person_bfs(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result if result != 10**9 else min(result, fire_time[m - 1][n - 1])