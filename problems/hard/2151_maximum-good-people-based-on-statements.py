from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        max_good = 0
        
        # Try all possible combinations of good/bad people
        # mask: bit i = 1 means person i is good, 0 means bad
        for mask in range(1 << n):
            if self.is_valid(mask, statements, n):
                good_count = bin(mask).count('1')
                max_good = max(max_good, good_count)
        
        return max_good
    
    def is_valid(self, mask: int, statements: List[List[int]], n: int) -> bool:
        # Check if this assignment of good/bad is consistent
        for i in range(n):
            # If person i is good, their statements must all be true
            if mask & (1 << i):  # person i is good
                for j in range(n):
                    if statements[i][j] == 2:
                        continue
                    
                    # Person i (good) says person j is good (statement == 1)
                    if statements[i][j] == 1:
                        # Person j must actually be good
                        if not (mask & (1 << j)):
                            return False
                    
                    # Person i (good) says person j is bad (statement == 0)
                    elif statements[i][j] == 0:
                        # Person j must actually be bad
                        if mask & (1 << j):
                            return False
        
        return True