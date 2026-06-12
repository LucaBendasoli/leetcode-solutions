from typing import List
from bisect import bisect_left

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        
        # Split array into two halves
        left = nums[:n//2]
        right = nums[n//2:]
        
        # Generate all possible subset sums for each half
        def get_all_sums(arr):
            sums = [0]
            for num in arr:
                sums.extend([s + num for s in sums])
            return sums
        
        left_sums = get_all_sums(left)
        right_sums = get_all_sums(right)
        
        # Sort right_sums for binary search
        right_sums.sort()
        
        min_diff = abs(goal)  # Case where we pick empty subsequence
        
        # For each sum from left half, find best match in right half
        for left_sum in left_sums:
            target = goal - left_sum
            
            # Binary search for closest value to target in right_sums
            pos = bisect_left(right_sums, target)
            
            # Check the value at pos (if exists)
            if pos < len(right_sums):
                current_sum = left_sum + right_sums[pos]
                min_diff = min(min_diff, abs(current_sum - goal))
            
            # Check the value before pos (if exists)
            if pos > 0:
                current_sum = left_sum + right_sums[pos - 1]
                min_diff = min(min_diff, abs(current_sum - goal))
        
        return min_diff