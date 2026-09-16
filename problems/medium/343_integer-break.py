class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        # For n > 3, break into as many 3's as possible
        quotient, remainder = divmod(n, 3)
        
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            # Remove one 3 and use two 2's instead (3+1 = 2+2)
            return 3 ** (quotient - 1) * 4
        else:  # remainder == 2
            return 3 ** quotient * 2