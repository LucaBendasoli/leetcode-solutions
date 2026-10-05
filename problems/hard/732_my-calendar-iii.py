class MyCalendarThree:
    def __init__(self):
        # difference map: time -> change in number of active events
        self.delta = {}

    def book(self, startTime: int, endTime: int) -> int:
        # update the difference map
        self.delta[startTime] = self.delta.get(startTime, 0) + 1
        self.delta[endTime] = self.delta.get(endTime, 0) - 1

        # sweep through all times in sorted order to compute current overlap
        sorted_times = sorted(self.delta.keys())
        cur = 0
        max_k = 0
        for t in sorted_times:
            cur += self.delta[t]
            if cur > max_k:
                max_k = cur
        return max_k