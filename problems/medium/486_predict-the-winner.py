from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        
        def dp(left, right):
            if left == right:
                return nums[left]
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            pick_left = nums[left] - dp(left + 1, right)
            pick_right = nums[right] - dp(left, right - 1)
            
            result = max(pick_left, pick_right)
            memo[(left, right)] = result
            return result
        
        return dp(0, n - 1) >= 0