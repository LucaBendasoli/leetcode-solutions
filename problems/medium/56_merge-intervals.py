from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            current = intervals[i]
            last_merged = merged[-1]
            
            if current[0] <= last_merged[1]:
                merged[-1] = [last_merged[0], max(last_merged[1], current[1])]
            else:
                merged.append(current)
        
        return merged