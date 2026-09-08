from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        # max-heap (invert values) for the smaller half
        self.small = []   # stores -num
        # min-heap for the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Insert into the appropriate heap
        if not self.small or num <= -self.small[0]:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)

        # Rebalance to maintain |small| >= |large| and difference at most 1
        if len(self.small) > len(self.large) + 1:
            moved = -heappop(self.small)
            heappush(self.large, moved)
        elif len(self.large) > len(self.small):
            moved = heappop(self.large)
            heappush(self.small, -moved)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0