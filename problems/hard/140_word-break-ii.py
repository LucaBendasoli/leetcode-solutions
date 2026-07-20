from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def can_break(start):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and can_break(end):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False
        
        if not can_break(0):
            return []
        
        result = []
        
        def backtrack(start, path):
            if start == len(s):
                result.append(' '.join(path))
                return
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    path.append(word)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0, [])
        return result