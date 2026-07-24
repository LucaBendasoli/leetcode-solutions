from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Remove duplicates and sort
        unique_nums = sorted(set(nums))
        
        max_keep = 0
        left = 0
        
        # For each possible starting position
        for right in range(len(unique_nums)):
            # The window is [unique_nums[left], unique_nums[left] + n - 1]
            # We need to find how many unique elements fit in this window
            
            # Move left pointer to maintain window size constraint
            while unique_nums[right] - unique_nums[left] >= n:
                left += 1
            
            # Count of unique elements in current window
            max_keep = max(max_keep, right - left + 1)
        
        return n - max_keep