from __future__ import annotations

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Quick win: if the sum of all numbers is less than desiredTotal, no one can win
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False
        # If desiredTotal is 0 or negative, first player wins without playing
        if desiredTotal <= 0:
            return True
        
        # Use memoization: key = bitmask of used numbers, value = can the current player win
        memo = {}
        
        def can_win(mask: int, current_total: int) -> bool:
            if current_total >= desiredTotal:
                return False  # the player who just moved already won, so current player cannot be here
            if mask in memo:
                return memo[mask]
            
            # Try all possible choices
            for i in range(maxChoosableInteger):
                if not (mask >> i) & 1:  # number (i+1) is not used
                    # Choose number (i+1)
                    new_total = current_total + (i + 1)
                    # If this move reaches or exceeds desiredTotal, current player wins
                    if new_total >= desiredTotal:
                        memo[mask] = True
                        return True
                    # Otherwise, check if the opponent loses after we pick this number
                    new_mask = mask | (1 << i)
                    if not can_win(new_mask, new_total):
                        memo[mask] = True
                        return True
            
            memo[mask] = False
            return False
        
        return can_win(0, 0)