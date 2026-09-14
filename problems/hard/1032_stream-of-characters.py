from typing import List
from collections import deque

class StreamChecker:
    def __init__(self, words: List[str]) -> None:
        self.max_len = max((len(w) for w in words), default=0)
        self.trie = [[-1] * 26]
        self.is_end = [False]

        for word in words:
            node = 0
            for ch in reversed(word):
                idx = ord(ch) - 97
                nxt = self.trie[node][idx]
                if nxt == -1:
                    nxt = len(self.trie)
                    self.trie[node][idx] = nxt
                    self.trie.append([-1] * 26)
                    self.is_end.append(False)
                node = nxt
            self.is_end[node] = True

        self.stream = deque(maxlen=self.max_len) if self.max_len > 0 else deque()

    def query(self, letter: str) -> bool:
        self.stream.append(letter)

        node = 0
        for ch in reversed(self.stream):
            idx = ord(ch) - 97
            nxt = self.trie[node][idx]
            if nxt == -1:
                break
            node = nxt
            if self.is_end[node]:
                return True

        return False

class Solution:
    pass