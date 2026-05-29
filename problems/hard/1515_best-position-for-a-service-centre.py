from typing import List

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def distance_sum(x, y):
            total = 0.0
            for px, py in positions:
                total += ((x - px) ** 2 + (y - py) ** 2) ** 0.5
            return total
        
        def gradient(x, y):
            dx, dy = 0.0, 0.0
            for px, py in positions:
                dist = ((x - px) ** 2 + (y - py) ** 2) ** 0.5
                if dist > 1e-9:
                    dx += (x - px) / dist
                    dy += (y - py) / dist
            return dx, dy
        
        # Start from the centroid
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)
        
        # Gradient descent
        step = 100.0
        epsilon = 1e-7
        
        while step > epsilon:
            dx, dy = gradient(x, y)
            
            # Try moving in the negative gradient direction
            new_x = x - step * dx
            new_y = y - step * dy
            
            # If we improve, update position
            if distance_sum(new_x, new_y) < distance_sum(x, y):
                x = new_x
                y = new_y
            else:
                # Decrease step size
                step *= 0.5
        
        return distance_sum(x, y)