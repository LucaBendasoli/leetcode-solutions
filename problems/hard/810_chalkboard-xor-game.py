from typing import List
from functools import reduce
from operator import xor

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        total_xor = reduce(xor, nums, 0)
        return total_xor == 0 or len(nums) % 2 == 0