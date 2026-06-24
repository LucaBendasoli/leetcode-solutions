from typing import List
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        same_location = 0
        angles = []
        
        for x, y in points:
            if [x, y] == location:
                same_location += 1
            else:
                dx = x - location[0]
                dy = y - location[1]
                angles.append(math.atan2(dy, dx) * 180 / math.pi)
        
        angles.sort()
        
        extended_angles = angles + [a + 360 for a in angles]
        
        max_visible = 0
        left = 0
        
        for right in range(len(extended_angles)):
            while extended_angles[right] - extended_angles[left] > angle:
                left += 1
            max_visible = max(max_visible, right - left + 1)
        
        return max_visible + same_location