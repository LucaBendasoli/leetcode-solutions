from typing import List
import bisect

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals.append([value, value])
            return
        
        # Find insertion position using binary search
        left, right = 0, len(self.intervals)
        while left < right:
            mid = (left + right) // 2
            if self.intervals[mid][0] <= value:
                left = mid + 1
            else:
                right = mid
        
        pos = left
        
        # Check if value already covered by existing interval
        if pos > 0 and self.intervals[pos - 1][1] >= value:
            return
        
        # Determine merge behavior
        merge_prev = pos > 0 and self.intervals[pos - 1][1] + 1 == value
        merge_next = pos < len(self.intervals) and self.intervals[pos][0] - 1 == value
        
        if merge_prev and merge_next:
            # Merge with both previous and next intervals
            self.intervals[pos - 1][1] = self.intervals[pos][1]
            self.intervals.pop(pos)
        elif merge_prev:
            # Extend previous interval
            self.intervals[pos - 1][1] = value
        elif merge_next:
            # Extend next interval
            self.intervals[pos][0] = value
        else:
            # Insert new interval
            self.intervals.insert(pos, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals