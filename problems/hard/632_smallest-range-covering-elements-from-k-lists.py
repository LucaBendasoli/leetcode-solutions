from __future__ import annotations
import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        k = len(nums)
        heap = []
        max_val = float('-inf')
        
        # Initialize heap with first element from each list
        for i in range(k):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])
        
        min_range = float('inf')
        result = []
        
        while True:
            min_val, list_idx, elem_idx = heapq.heappop(heap)
            
            # Update result if current range is smaller
            if max_val - min_val < min_range:
                min_range = max_val - min_val
                result = [min_val, max_val]
            elif max_val - min_val == min_range and min_val < result[0]:
                result = [min_val, max_val]
            
            # If we've reached end of any list, break
            if elem_idx + 1 == len(nums[list_idx]):
                break
            
            # Move to next element in the same list
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            max_val = max(max_val, next_val)
        
        return result