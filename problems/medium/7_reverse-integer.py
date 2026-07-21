class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        result = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before actually adding
            if result > (2**31 - 1) // 10:
                return 0
            if result == (2**31 - 1) // 10 and digit > 7:
                return 0
            
            result = result * 10 + digit
        
        result *= sign
        
        # Final boundary check
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result