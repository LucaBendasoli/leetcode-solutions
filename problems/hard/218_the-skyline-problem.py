from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for left, right, height in buildings:
            events.append((left, 0, height))
            events.append((right, 1, height))
        
        events.sort(key=lambda x: (x[0], x[1], -x[2] if x[1] == 0 else x[2]))
        
        result = []
        max_heap = [0]
        height_count = {0: 1}
        
        for x, event_type, h in events:
            if event_type == 0:
                heapq.heappush(max_heap, -h)
                height_count[h] = height_count.get(h, 0) + 1
            else:
                height_count[h] -= 1
                if height_count[h] == 0:
                    del height_count[h]
            
            while -max_heap[0] not in height_count:
                heapq.heappop(max_heap)
            
            max_height = -max_heap[0]
            
            if not result or result[-1][1] != max_height:
                result.append([x, max_height])
        
        return result