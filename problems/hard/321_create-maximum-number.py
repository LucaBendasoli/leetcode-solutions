from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxSingleArray(nums, length):
            if length == 0:
                return []
            drop = len(nums) - length
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]
        
        def merge(nums1, nums2):
            result = []
            while nums1 or nums2:
                if nums1 > nums2:
                    result.append(nums1[0])
                    nums1 = nums1[1:]
                else:
                    result.append(nums2[0])
                    nums2 = nums2[1:]
            return result
        
        max_result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            sub1 = maxSingleArray(nums1, i)
            sub2 = maxSingleArray(nums2, k - i)
            candidate = merge(sub1, sub2)
            if candidate > max_result:
                max_result = candidate
        
        return max_result