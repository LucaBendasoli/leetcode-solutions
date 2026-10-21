from collections import Counter
from typing import List

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_count = Counter()

        # Build a frequency map of word bitmasks.
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            word_count[mask] += 1

        ans = []

        for puzzle in puzzles:
            # Build the puzzle bitmask.
            puzzle_mask = 0
            for ch in puzzle:
                puzzle_mask |= 1 << (ord(ch) - ord('a'))

            first_letter = puzzle[0]
            first_bit = 1 << (ord(first_letter) - ord('a'))

            # Special handling for puzzles whose first letter is 'a'.
            # These puzzles should additionally count words that are subsets
            # of the puzzle but do not contain 'a', as long as they are not
            # single‑letter words (which would be only the word 'a' itself).
            if first_letter == 'a':
                # Sum over all subsets of the puzzle mask.
                total = 0
                sub = puzzle_mask
                while True:
                    total += word_count[sub]
                    if sub == 0:
                        break
                    sub = (sub - 1) & puzzle_mask

                # Subtract single‑letter words that are not 'a' (e.g., "b").
                bit = 1
                while bit <= puzzle_mask:
                    if bit & puzzle_mask and bit != first_bit:
                        total -= word_count.get(bit, 0)
                    bit <<= 1
                ans.append(total)
            else:
                # Standard algorithm: only count subsets that include the first letter.
                rest_mask = puzzle_mask ^ first_bit
                total = 0
                sub = rest_mask
                while True:
                    total += word_count[sub | first_bit]
                    if sub == 0:
                        break
                    sub = (sub - 1) & rest_mask
                ans.append(total)

        return ans