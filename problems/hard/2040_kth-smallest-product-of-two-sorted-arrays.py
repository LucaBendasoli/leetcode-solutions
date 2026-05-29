from typing import List
import bisect

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_less_equal(target):
            count = 0
            for num1 in nums1:
                if num1 > 0:
                    # For positive num1, we want num2 <= target / num1
                    # Since arrays are sorted, use binary search
                    idx = bisect.bisect_right(nums2, target / num1)
                    count += idx
                elif num1 < 0:
                    # For negative num1, we want num2 >= target / num1
                    # Which means num2 is in the right portion
                    idx = bisect.bisect_left(nums2, target / num1)
                    count += len(nums2) - idx
                else:  # num1 == 0
                    # Product is 0, count if target >= 0
                    if target >= 0:
                        count += len(nums2)
            return count
        
        # Binary search on the answer
        left, right = -10**10, 10**10
        
        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left