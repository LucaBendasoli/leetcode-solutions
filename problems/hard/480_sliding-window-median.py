from __future__ import annotations
import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or k <= 0:
            return []
        
        # max heap (inverted min-heap) for smaller half
        max_heap = []  # stores negative values
        # min heap for larger half
        min_heap = []
        
        # balance factor: max_heap_size == min_heap_size or max_heap_size == min_heap_size + 1
        # max_heap always has either same or one more element than min_heap
        
        result = []
        
        for i, num in enumerate(nums):
            # Add new element
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
            
            # rebalance
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            
            # remove element outside window
            if i >= k:
                removed = nums[i - k]
                # decide which heap it came from
                if removed <= -max_heap[0]:
                    # remove from max_heap, lazy deletion
                    idx = max_heap.index(-removed)
                    max_heap[idx] = max_heap[-1]
                    max_heap.pop()
                    if idx < len(max_heap):
                        heapq._siftup(max_heap, idx) or heapq._siftdown(max_heap, 0, idx)
                else:
                    idx = min_heap.index(removed)
                    min_heap[idx] = min_heap[-1]
                    min_heap.pop()
                    if idx < len(min_heap):
                        heapq._siftup(min_heap, idx) or heapq._siftdown(min_heap, 0, idx)
                
                # rebalance after removal
                if len(max_heap) > len(min_heap) + 1:
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))
                elif len(min_heap) > len(max_heap):
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
            
            # compute median when window is full
            if i >= k - 1:
                if len(max_heap) == len(min_heap):
                    median = (-max_heap[0] + min_heap[0]) / 2.0
                else:
                    median = float(-max_heap[0])
                result.append(median)
        
        return result