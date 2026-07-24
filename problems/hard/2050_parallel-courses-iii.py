from typing import List
from collections import deque, defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Build adjacency list and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        
        for prev, next_course in relations:
            graph[prev].append(next_course)
            in_degree[next_course] += 1
        
        # earliest_completion[i] = earliest time when course i can be completed
        earliest_completion = [0] * (n + 1)
        
        # Start with courses that have no prerequisites
        queue = deque()
        for course in range(1, n + 1):
            if in_degree[course] == 0:
                queue.append(course)
                earliest_completion[course] = time[course - 1]
        
        # Process courses in topological order
        while queue:
            course = queue.popleft()
            
            # For each dependent course
            for next_course in graph[course]:
                # Update earliest completion time for next_course
                # It can start only after current course is completed
                earliest_completion[next_course] = max(
                    earliest_completion[next_course],
                    earliest_completion[course] + time[next_course - 1]
                )
                
                # Decrease in-degree
                in_degree[next_course] -= 1
                
                # If all prerequisites are satisfied, add to queue
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # Return the maximum completion time among all courses
        return max(earliest_completion[1:])