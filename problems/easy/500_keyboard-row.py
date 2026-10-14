from __future__ import annotations

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        for word in words:
            chars = set(word.lower())
            if chars <= row1 or chars <= row2 or chars <= row3:
                result.append(word)
        return result