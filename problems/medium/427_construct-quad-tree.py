from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def build(r1: int, r2: int, c1: int, c2: int) -> Node:
            # Check if all values in the subgrid are the same
            first = grid[r1][c1]
            is_uniform = True
            for i in range(r1, r2):
                for j in range(c1, c2):
                    if grid[i][j] != first:
                        is_uniform = False
                        break
                if not is_uniform:
                    break
            if is_uniform:
                return Node(bool(first), True, None, None, None, None)

            # Split into four quadrants
            mid_r = (r1 + r2) // 2
            mid_c = (c1 + c2) // 2

            topLeft = build(r1, mid_r, c1, mid_c)
            topRight = build(r1, mid_r, mid_c, c2)
            bottomLeft = build(mid_r, r2, c1, mid_c)
            bottomRight = build(mid_r, r2, mid_c, c2)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, n, 0, n)