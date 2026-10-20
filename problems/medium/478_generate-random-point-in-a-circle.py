import random
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> list[float]:
        # Uniform sampling inside the circle
        # sqrt(random) to compensate for area proportion
        r = math.sqrt(random.random()) * self.radius
        theta = random.random() * 2 * math.pi
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        return [x, y]