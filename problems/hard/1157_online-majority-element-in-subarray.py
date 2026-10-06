from __future__ import annotations
import random
import bisect

class MajorityChecker:

    def __init__(self, arr: list[int]):
        self.arr = arr
        self.pos = {}
        for i, val in enumerate(arr):
            if val not in self.pos:
                self.pos[val] = []
            self.pos[val].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        length = right - left + 1
        # Random sampling approach: try up to 20 random candidates
        for _ in range(20):
            idx = random.randint(left, right)
            candidate = self.arr[idx]
            cnt = self._count_in_range(candidate, left, right)
            if cnt >= threshold:
                return candidate
        return -1

    def _count_in_range(self, val: int, left: int, right: int) -> int:
        if val not in self.pos:
            return 0
        indices = self.pos[val]
        l = bisect.bisect_left(indices, left)
        r = bisect.bisect_right(indices, right)
        return r - l