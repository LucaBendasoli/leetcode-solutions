class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        
        s = [1, 2, 2]
        idx = 2
        num = 1
        
        while len(s) < n:
            count = s[idx]
            s.extend([num] * count)
            num = 3 - num
            idx += 1
        
        return sum(1 for i in range(n) if s[i] == 1)