from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        target = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            current = Counter()

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in target:
                    current.clear()
                    left = right + word_len
                    continue

                current[word] += 1

                while current[word] > target[word]:
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len

                if (right - left) // word_len + 1 == word_count:
                    result.append(left)

        return result