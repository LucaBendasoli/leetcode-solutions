class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        # Start from the second last row and move upward
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update current cell with minimum path sum from below
                triangle[row][col] += min(
                    triangle[row + 1][col],
                    triangle[row + 1][col + 1]
                )
        # The top element now contains the minimum path sum
        return triangle[0][0]