from typing import List
import bisect

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # Map each distinct target value to its index
        idx_map = {val: i for i, val in enumerate(target)}
        
        # Extract the indices of arr elements that appear in target
        indices = []
        for x in arr:
            if x in idx_map:
                indices.append(idx_map[x])
        
        # Compute LIS length on indices using patience sorting
        lis = []
        for x in indices:
            pos = bisect.bisect_left(lis, x)
            if pos == len(lis):
                lis.append(x)
            else:
                lis[pos] = x
        
        # Minimum operations = total target length - longest common subsequence length
        return len(target) - len(lis)