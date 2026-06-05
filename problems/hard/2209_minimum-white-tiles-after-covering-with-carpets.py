class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        
        # If we have enough carpets to cover everything
        if numCarpets * carpetLen >= n:
            return 0
        
        # dp[i][j] = minimum white tiles visible in floor[0:i] using j carpets
        # We'll use space optimization with two arrays
        prev = [0] * (n + 1)
        
        # Base case: 0 carpets used
        for i in range(1, n + 1):
            prev[i] = prev[i - 1] + (1 if floor[i - 1] == '1' else 0)
        
        for j in range(1, numCarpets + 1):
            curr = [0] * (n + 1)
            for i in range(1, n + 1):
                # Option 1: Don't place a carpet covering position i-1
                curr[i] = curr[i - 1] + (1 if floor[i - 1] == '1' else 0)
                
                # Option 2: Place a carpet ending at position i
                # The carpet covers positions [max(0, i - carpetLen), i)
                start = max(0, i - carpetLen)
                curr[i] = min(curr[i], prev[start])
            
            prev = curr
        
        return prev[n]