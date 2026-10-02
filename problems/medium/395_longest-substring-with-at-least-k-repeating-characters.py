from __future__ import annotations

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Base case: if the string is shorter than k, no substring can be valid
        if len(s) < k:
            return 0

        # Count frequencies of each character
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Find the first character that appears less than k times
        split_char = None
        for ch, count in freq.items():
            if count < k:
                split_char = ch
                break

        # If no such character, the whole string is valid
        if split_char is None:
            return len(s)

        # Otherwise, split at each occurrence of split_char and recurse
        max_len = 0
        parts = s.split(split_char)
        for part in parts:
            max_len = max(max_len, self.longestSubstring(part, k))

        return max_len