class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            min_rotation = s
            for i in range(len(s)):
                rotation = s[i:] + s[:i]
                if rotation < min_rotation:
                    min_rotation = rotation
            return min_rotation
        else:
            return ''.join(sorted(s))