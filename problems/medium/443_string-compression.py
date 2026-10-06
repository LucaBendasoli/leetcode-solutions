from __future__ import annotations

class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        i = 0
        n = len(chars)
        
        while i < n:
            ch = chars[i]
            count = 0
            # Count consecutive identical characters
            while i < n and chars[i] == ch:
                i += 1
                count += 1
            
            # Write the character
            chars[write] = ch
            write += 1
            
            # Write the count if more than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write