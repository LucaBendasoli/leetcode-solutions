from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        n = len(data)
        
        while i < n:
            # Use only the least significant 8 bits
            byte = data[i] & 0xFF
            
            # Determine number of bytes in this character
            num_bytes = 0
            
            # Check the leading bits
            if (byte >> 7) == 0b0:
                # 1-byte character (0xxxxxxx)
                num_bytes = 1
            elif (byte >> 5) == 0b110:
                # 2-byte character (110xxxxx)
                num_bytes = 2
            elif (byte >> 4) == 0b1110:
                # 3-byte character (1110xxxx)
                num_bytes = 3
            elif (byte >> 3) == 0b11110:
                # 4-byte character (11110xxx)
                num_bytes = 4
            else:
                # Invalid starting byte
                return False
            
            # Check if we have enough bytes left
            if i + num_bytes > n:
                return False
            
            # Check continuation bytes (if any)
            for j in range(1, num_bytes):
                continuation_byte = data[i + j] & 0xFF
                # Continuation bytes must start with 10xxxxxx
                if (continuation_byte >> 6) != 0b10:
                    return False
            
            i += num_bytes
        
        return True