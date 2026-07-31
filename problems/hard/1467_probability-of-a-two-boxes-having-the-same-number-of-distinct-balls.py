from typing import List
from math import factorial

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls) // 2
        
        def multinomial(counts):
            result = factorial(sum(counts))
            for c in counts:
                result //= factorial(c)
            return result
        
        def dfs(idx, box1, box2, count1, count2, colors1, colors2):
            if count1 > n or count2 > n:
                return 0, 0
            
            if idx == len(balls):
                if count1 == n and count2 == n and colors1 == colors2:
                    ways = multinomial(box1) * multinomial(box2)
                    return ways, ways
                elif count1 == n and count2 == n:
                    ways = multinomial(box1) * multinomial(box2)
                    return ways, 0
                else:
                    return 0, 0
            
            total_ways = 0
            valid_ways = 0
            
            for i in range(balls[idx] + 1):
                j = balls[idx] - i
                new_box1 = box1 + [i]
                new_box2 = box2 + [j]
                new_colors1 = colors1 + (1 if i > 0 else 0)
                new_colors2 = colors2 + (1 if j > 0 else 0)
                
                t, v = dfs(idx + 1, new_box1, new_box2, count1 + i, count2 + j, new_colors1, new_colors2)
                total_ways += t
                valid_ways += v
            
            return total_ways, valid_ways
        
        total, valid = dfs(0, [], [], 0, 0, 0, 0)
        
        return valid / total if total > 0 else 0.0