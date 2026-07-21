from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        n = len(nums)
        mid = (n + 1) // 2
        
        # Split into smaller and larger halves
        smaller = sorted_nums[:mid]
        larger = sorted_nums[mid:]
        
        # Fill from the end to avoid adjacent equal values
        # Place smaller elements at even indices (0, 2, 4...)
        # Place larger elements at odd indices (1, 3, 5...)
        j = len(smaller) - 1
        for i in range(0, n, 2):
            nums[i] = smaller[j]
            j -= 1
        
        j = len(larger) - 1
        for i in range(1, n, 2):
            nums[i] = larger[j]
            j -= 1