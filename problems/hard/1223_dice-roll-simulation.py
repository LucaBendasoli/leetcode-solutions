from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        
        # dp[f][r] = number of sequences ending with face f and exactly r consecutive f's
        dp = [[0] * (rollMax[f] + 1) for f in range(6)]
        for f in range(6):
            dp[f][1] = 1
        
        total = 6 % MOD
        
        for _ in range(2, n + 1):
            new_dp = [[0] * (rollMax[f] + 1) for f in range(6)]
            new_total = 0
            
            for f in range(6):
                # Previous roll is different
                sum_face_f = sum(dp[f]) % MOD
                diff = (total - sum_face_f) % MOD
                new_dp[f][1] = diff
                
                # Previous roll is the same face
                for r in range(2, rollMax[f] + 1):
                    new_dp[f][r] = dp[f][r - 1]
                
                new_total = (new_total + sum(new_dp[f])) % MOD
            
            dp = new_dp
            total = new_total
        
        return total % MOD