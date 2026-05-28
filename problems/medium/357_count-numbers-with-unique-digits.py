class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        if n > 10:
            n = 10
        
        total = 10
        unique_digits = 9
        available = 9
        
        for i in range(2, n + 1):
            unique_digits *= available
            total += unique_digits
            available -= 1
        
        return total