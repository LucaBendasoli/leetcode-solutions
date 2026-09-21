from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        need = Counter(t)
        window = defaultdict(int)
        
        required = len(need)   # number of distinct chars in t
        formed = 0             # how many distinct chars meet the frequency requirement
        
        left = 0
        best_left = 0
        best_len = float('inf')
        
        for right, ch in enumerate(s):
            window[ch] += 1
            
            if ch in need and window[ch] == need[ch]:
                formed += 1
            
            while left <= right and formed == required:
                # update best answer
                curr_len = right - left + 1
                if curr_len < best_len:
                    best_len = curr_len
                    best_left = left
                
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        
        return "" if best_len == float('inf') else s[best_left:best_left + best_len]