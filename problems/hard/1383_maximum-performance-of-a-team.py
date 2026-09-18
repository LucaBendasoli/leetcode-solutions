from __future__ import annotations
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        MOD = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        speed_sum = 0
        min_heap = []
        best = 0
        
        for eff, spd in engineers:
            speed_sum += spd
            heapq.heappush(min_heap, spd)
            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)
            if len(min_heap) == k:
                candidate = speed_sum * eff
                if candidate > best:
                    best = candidate
        
        return best % MOD