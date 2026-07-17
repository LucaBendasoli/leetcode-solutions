from typing import List
from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Track visit count for each node
        visit_count = defaultdict(int)
        visit_count[0] = 1
        
        max_quality = [values[0]]  # Start at node 0, so initial quality is values[0]
        
        def dfs(node, time_spent, current_quality):
            # If we're back at node 0, update max quality
            if node == 0:
                max_quality[0] = max(max_quality[0], current_quality)
            
            # Explore neighbors
            for neighbor, travel_time in graph[node]:
                new_time = time_spent + travel_time
                
                # Prune if exceeds maxTime
                if new_time > maxTime:
                    continue
                
                # Calculate new quality
                new_quality = current_quality
                if visit_count[neighbor] == 0:
                    new_quality += values[neighbor]
                
                # Visit neighbor
                visit_count[neighbor] += 1
                dfs(neighbor, new_time, new_quality)
                visit_count[neighbor] -= 1
        
        # Start DFS from node 0
        dfs(0, 0, values[0])
        
        return max_quality[0]