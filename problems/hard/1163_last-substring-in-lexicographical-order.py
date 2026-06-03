class Solution:
    def lastSubstring(self, s: str) -> str:
        i = 0  # current best candidate
        j = 1  # challenger
        k = 0  # offset for comparison
        n = len(s)
        
        while j + k < n:
            if s[i + k] == s[j + k]:
                # Characters match, extend comparison
                k += 1
            elif s[i + k] > s[j + k]:
                # i is better, move j past the compared region
                j = j + k + 1
                k = 0
            else:
                # j is better, move i to max(i+k+1, j) and reset
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
        
        return s[i:]