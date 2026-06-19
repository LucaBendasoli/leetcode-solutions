from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for num in nums:
            # Add current num to twos if it's already in ones
            twos |= ones & num
            # XOR with ones to toggle the bit
            ones ^= num
            # Create mask for bits that appear 3 times
            threes = ones & twos
            # Remove bits that appeared 3 times from both
            ones &= ~threes
            twos &= ~threes
        
        return ones