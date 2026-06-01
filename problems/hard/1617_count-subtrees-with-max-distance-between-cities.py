from typing import List
from collections import deque

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        result = [0] * (n - 1)
        
        # Iterate through all possible subsets of cities (at least 2 cities)
        for mask in range(3, 1 << n):
            if bin(mask).count('1') < 2:
                continue
            
            cities = []
            for i in range(n):
                if mask & (1 << i):
                    cities.append(i + 1)
            
            # Check if subset forms a connected subtree
            if not self.is_connected(cities, adj):
                continue
            
            # Calculate max distance in this subtree
            max_dist = self.get_max_distance(cities, adj)
            if max_dist > 0:
                result[max_dist - 1] += 1
        
        return result
    
    def is_connected(self, cities, adj):
        if len(cities) == 0:
            return False
        
        city_set = set(cities)
        visited = set()
        queue = deque([cities[0]])
        visited.add(cities[0])
        
        while queue:
            city = queue.popleft()
            for neighbor in adj[city]:
                if neighbor in city_set and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return len(visited) == len(cities)
    
    def get_max_distance(self, cities, adj):
        city_set = set(cities)
        max_dist = 0
        
        # BFS from each city to find maximum distance
        for start in cities:
            dist = {start: 0}
            queue = deque([start])
            
            while queue:
                city = queue.popleft()
                for neighbor in adj[city]:
                    if neighbor in city_set and neighbor not in dist:
                        dist[neighbor] = dist[city] + 1
                        queue.append(neighbor)
                        max_dist = max(max_dist, dist[neighbor])
        
        return max_dist