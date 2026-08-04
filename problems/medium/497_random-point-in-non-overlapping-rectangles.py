import random
import bisect
from typing import List

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        total = 0
        for a, b, x, y in rects:
            count = (x - a + 1) * (y - b + 1)
            total += count
            self.weights.append(total)
    
    def pick(self) -> List[int]:
        target = random.randint(1, self.weights[-1])
        idx = bisect.bisect_left(self.weights, target)
        if idx < len(self.weights) and self.weights[idx] < target:
            idx += 1
        
        a, b, x, y = self.rects[idx]
        return [random.randint(a, x), random.randint(b, y)]