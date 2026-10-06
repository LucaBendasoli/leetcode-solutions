from __future__ import annotations

class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total = 0
        end = 0  # exclusive end time of the current poison interval
        
        for t in timeSeries:
            if t >= end:
                total += duration
            else:
                total += t + duration - end
            end = t + duration
        
        return total