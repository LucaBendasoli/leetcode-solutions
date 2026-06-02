from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        stone_set = set(stones)
        target = stones[-1]
        memo = {}
        
        def dfs(pos, k):
            if pos == target:
                return True
            
            if (pos, k) in memo:
                return memo[(pos, k)]
            
            for next_k in [k - 1, k, k + 1]:
                if next_k > 0:
                    next_pos = pos + next_k
                    if next_pos in stone_set and dfs(next_pos, next_k):
                        memo[(pos, k)] = True
                        return True
            
            memo[(pos, k)] = False
            return False
        
        return dfs(1, 1)