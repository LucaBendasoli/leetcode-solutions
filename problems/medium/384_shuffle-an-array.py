from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.array = nums[:]

    def reset(self) -> List[int]:
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            j = random.randint(i, len(self.array) - 1)
            self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array