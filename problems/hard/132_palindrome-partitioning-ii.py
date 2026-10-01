class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # Precompute palindrome table
        pal = [[False] * n for _ in range(n)]
        for i in range(n):
            pal[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = min cuts for s[0:i]
        dp = [i for i in range(n)]  # initialize with worst case (i cuts)
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = i - 1  # worst case: cut after each character

        for i in range(1, n + 1):
            for j in range(i):
                if pal[j][i - 1]:  # substring s[j:i] is palindrome
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n]