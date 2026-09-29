from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        # Create list of (start, original_index) and sort by start
        starts = [(intervals[i][0], i) for i in range(n)]
        starts.sort(key=lambda x: x[0])
        start_vals = [s[0] for s in starts]

        result = [-1] * n
        for i in range(n):
            end = intervals[i][1]
            # find first start >= end
            pos = bisect_left(start_vals, end)
            if pos < n:
                result[i] = starts[pos][1]
            # else remains -1
        return result