class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # Handle negative numbers using two's complement (32-bit)
        if num < 0:
            num = (1 << 32) + num
        
        hex_chars = "0123456789abcdef"
        result = []
        
        while num > 0:
            result.append(hex_chars[num % 16])
            num //= 16
        
        return ''.join(reversed(result))