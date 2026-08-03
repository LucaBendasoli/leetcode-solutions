from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]
        
        word_dict = {word: i for i, word in enumerate(words)}
        result = []
        
        for i, word in enumerate(words):
            # Check all possible splits of the word
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                # Case 1: prefix is palindrome
                # We need reverse of suffix to come before word
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_dict and word_dict[reversed_suffix] != i:
                        result.append([word_dict[reversed_suffix], i])
                
                # Case 2: suffix is palindrome
                # We need reverse of prefix to come after word
                # j != len(word) to avoid duplicates (when suffix is empty, already covered in case 1)
                if j != len(word) and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_dict and word_dict[reversed_prefix] != i:
                        result.append([i, word_dict[reversed_prefix]])
        
        return result