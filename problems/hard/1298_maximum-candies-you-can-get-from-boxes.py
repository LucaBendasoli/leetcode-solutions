from collections import deque
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        have_not_opened = set()
        keys_set = set()
        queue = deque()
        opened = set()
        total = 0

        for b in initialBoxes:
            if status[b] == 1:
                queue.append(b)
            else:
                have_not_opened.add(b)

        while queue:
            box = queue.popleft()
            if box in opened:
                continue
            opened.add(box)
            total += candies[box]

            for k in keys[box]:
                if k not in keys_set:
                    keys_set.add(k)
                    have_not_opened.discard(k)
                    if k not in opened:
                        queue.append(k)

            for cb in containedBoxes[box]:
                if cb in opened:
                    continue
                if status[cb] == 1 or cb in keys_set:
                    have_not_opened.discard(cb)
                    queue.append(cb)
                else:
                    have_not_opened.add(cb)

        return total