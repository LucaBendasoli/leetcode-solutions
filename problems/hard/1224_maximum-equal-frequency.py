from typing import List
from collections import defaultdict

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = defaultdict(int)
        freq = defaultdict(int)
        max_freq = 0
        result = 0
        
        for i, num in enumerate(nums):
            if count[num] > 0:
                freq[count[num]] -= 1
                if freq[count[num]] == 0:
                    del freq[count[num]]
            
            count[num] += 1
            freq[count[num]] += 1
            max_freq = max(max_freq, count[num])
            
            length = i + 1
            
            # Check if we can remove one element to make all frequencies equal
            # Case 1: All elements appear exactly once
            if max_freq == 1:
                result = length
            
            # Case 2: All elements appear max_freq times, except one appears max_freq - 1 times
            # and there are only 2 distinct frequencies
            elif len(freq) == 2:
                freq1, freq2 = sorted(freq.keys())
                count1, count2 = freq[freq1], freq[freq2]
                
                # One element appears once more than others
                if freq2 == freq1 + 1 and count2 == 1:
                    result = length
                # One element appears once and all others appear the same
                elif freq1 == 1 and count1 == 1:
                    result = length
                # All elements appear freq1 times except one appears freq2 times
                # and we can remove one occurrence from freq2 to make it freq1
                elif freq2 == freq1 + 1 and count2 * freq2 == length - freq1 * count1 and count2 * freq2 + freq1 * count1 == length:
                    result = length
            
            # Case 3: Only one distinct frequency
            elif len(freq) == 1:
                f = list(freq.keys())[0]
                c = freq[f]
                
                # All elements have frequency f
                # We can remove if: f * c - 1 elements all have same frequency
                # Sub-case: all same frequency and removing one element leaves f-1 for all
                if f * c == length - 1:
                    result = length
                # Sub-case: only one distinct number
                elif c == 1:
                    result = length
                # Sub-case: all elements appear max_freq times, we remove one entire element
                elif f == 1:
                    result = length
        
        return result