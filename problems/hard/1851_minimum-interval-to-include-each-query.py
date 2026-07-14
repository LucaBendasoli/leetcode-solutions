from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        result = [-1] * len(queries)
        min_heap = []
        interval_idx = 0
        
        for query, original_idx in sorted_queries:
            # Add all intervals that start at or before this query
            while interval_idx < len(intervals) and intervals[interval_idx][0] <= query:
                left, right = intervals[interval_idx]
                size = right - left + 1
                heapq.heappush(min_heap, (size, right))
                interval_idx += 1
            
            # Remove intervals that end before this query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            # The smallest valid interval (if any exists)
            if min_heap:
                result[original_idx] = min_heap[0][0]
        
        return result