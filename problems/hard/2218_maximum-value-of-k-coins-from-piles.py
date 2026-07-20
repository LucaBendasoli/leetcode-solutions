from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        
        # dp[j] = max value when picking exactly j coins
        dp = [0] * (k + 1)
        
        for pile in piles:
            # Process each pile
            new_dp = dp[:]
            
            # Precompute prefix sums for this pile
            pile_sum = [0]
            for coin in pile:
                pile_sum.append(pile_sum[-1] + coin)
            
            # For each possible number of coins we might have picked so far
            for j in range(k + 1):
                # Try taking t coins from current pile (0 to min(len(pile), k - j))
                max_take = min(len(pile), k - j)
                for t in range(1, max_take + 1):
                    # If we take t coins from this pile, we need j coins from previous piles
                    # and we get pile_sum[t] value from this pile
                    new_dp[j + t] = max(new_dp[j + t], dp[j] + pile_sum[t])
            
            dp = new_dp
        
        return dp[k]