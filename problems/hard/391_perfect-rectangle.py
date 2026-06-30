from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        points = set()
        
        min_x = float('inf')
        min_y = float('inf')
        max_a = float('-inf')
        max_b = float('-inf')
        
        for x, y, a, b in rectangles:
            # Calculate total area
            area += (a - x) * (b - y)
            
            # Track bounding box
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            
            # Track corners
            corners = [(x, y), (x, b), (a, y), (a, b)]
            for corner in corners:
                if corner in points:
                    points.remove(corner)
                else:
                    points.add(corner)
        
        # Check if area matches
        expected_area = (max_a - min_x) * (max_b - min_y)
        if area != expected_area:
            return False
        
        # Check if only 4 corners remain (the outer corners)
        expected_corners = {(min_x, min_y), (min_x, max_b), (max_a, min_y), (max_a, max_b)}
        
        return points == expected_corners