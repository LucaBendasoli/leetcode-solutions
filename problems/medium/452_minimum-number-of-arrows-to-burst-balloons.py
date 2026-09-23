class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for start, e in points[1:]:
            if start > end:
                arrows += 1
                end = e
        return arrows