from __future__ import annotations

class Solution:
    def longestAwesome(self, s: str) -> int:
        # mask represents parity of counts for digits 0-9
        # map from mask to first index where it appears
        first_occurrence = {0: -1}
        mask = 0
        ans = 0

        for i, char in enumerate(s):
            digit = int(char)
            mask ^= (1 << digit)

            # Check if same mask occurred before => all even counts
            if mask in first_occurrence:
                ans = max(ans, i - first_occurrence[mask])
            else:
                first_occurrence[mask] = i

            # Check masks that differ by exactly one bit (one odd count)
            for bit in range(10):
                neighbor = mask ^ (1 << bit)
                if neighbor in first_occurrence:
                    ans = max(ans, i - first_occurrence[neighbor])

        return ans