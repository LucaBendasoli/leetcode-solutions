from typing import List
import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        heap = [(p, p, 0) for p in primes]
        heapq.heapify(heap)
        
        while len(ugly) < n:
            val, prime, idx = heapq.heappop(heap)
            
            if val != ugly[-1]:
                ugly.append(val)
            
            heapq.heappush(heap, (prime * ugly[idx + 1], prime, idx + 1))
        
        return ugly[-1]