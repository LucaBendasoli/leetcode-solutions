from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current, current_sum):
            if len(current) == k:
                if current_sum == n:
                    result.append(current[:])
                return
            
            if current_sum >= n or len(current) >= k:
                return
            
            for num in range(start, 10):
                if current_sum + num > n:
                    break
                current.append(num)
                backtrack(num + 1, current, current_sum + num)
                current.pop()
        
        backtrack(1, [], 0)
        return result