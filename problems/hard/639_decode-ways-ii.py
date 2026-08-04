class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        if n == 0 or s[0] == '0':
            return 0
        
        # dp[i] represents number of ways to decode s[0:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string
        
        # First character
        if s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n + 1):
            curr = s[i-1]
            prev = s[i-2]
            
            # Single digit decoding
            if curr == '*':
                dp[i] = (dp[i] + 9 * dp[i-1]) % MOD
            elif curr != '0':
                dp[i] = (dp[i] + dp[i-1]) % MOD
            
            # Two digit decoding
            if prev == '1':
                if curr == '*':
                    dp[i] = (dp[i] + 9 * dp[i-2]) % MOD  # 11-19
                else:
                    dp[i] = (dp[i] + dp[i-2]) % MOD  # 10-19
            elif prev == '2':
                if curr == '*':
                    dp[i] = (dp[i] + 6 * dp[i-2]) % MOD  # 21-26
                elif '0' <= curr <= '6':
                    dp[i] = (dp[i] + dp[i-2]) % MOD  # 20-26
            elif prev == '*':
                if curr == '*':
                    dp[i] = (dp[i] + 15 * dp[i-2]) % MOD  # 11-19, 21-26
                elif '0' <= curr <= '6':
                    dp[i] = (dp[i] + 2 * dp[i-2]) % MOD  # 1X and 2X both valid
                else:  # 7-9
                    dp[i] = (dp[i] + dp[i-2]) % MOD  # only 1X valid
        
        return dp[n]