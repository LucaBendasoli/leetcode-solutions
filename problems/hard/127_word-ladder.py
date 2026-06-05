from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        word_set = set(wordList)
        word_len = len(beginWord)
        
        # Build a pattern dictionary
        pattern_dict = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_dict[pattern].append(word)
        
        # BFS
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            # Generate all possible patterns for current word
            for i in range(word_len):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                
                # Get all words matching this pattern
                for next_word in pattern_dict[pattern]:
                    if next_word == endWord:
                        return level + 1
                    
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
                
                # Clear the pattern to avoid revisiting
                pattern_dict[pattern] = []
        
        return 0