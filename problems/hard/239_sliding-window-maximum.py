from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        result = []
        dq = deque()
        
        for i in range(len(nums)):
            # Remove indices that are out of the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove indices whose corresponding values are less than current value
            # because they will never be the maximum
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add current index
            dq.append(i)
            
            # Start adding to result once we have at least k elements
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result