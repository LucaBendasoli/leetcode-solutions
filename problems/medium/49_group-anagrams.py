from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Sort the string to create a key for anagrams
            key = ''.join(sorted(s))
            anagram_groups[key].append(s)
        
        return list(anagram_groups.values())