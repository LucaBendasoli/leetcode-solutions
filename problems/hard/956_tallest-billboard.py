from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        
        for rod in rods:
            new_dp = dp.copy()
            for diff, taller in dp.items():
                # Add rod to taller support
                new_diff = diff + rod
                new_taller = taller + rod
                if new_diff not in new_dp or new_dp[new_diff] < new_taller:
                    new_dp[new_diff] = new_taller
                
                # Add rod to shorter support
                shorter = taller - diff
                new_shorter = shorter + rod
                new_taller_val = max(taller, new_shorter)
                new_diff_val = abs(taller - new_shorter)
                
                if new_diff_val not in new_dp or new_dp[new_diff_val] < new_taller_val:
                    new_dp[new_diff_val] = new_taller_val
            
            dp = new_dp
        
        return dp.get(0, 0)