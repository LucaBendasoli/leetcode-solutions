class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Initialize n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        # Direction vectors: right, down, left, up
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = 0          # starting position
        dir_idx = 0        # start moving right
        for num in range(1, n * n + 1):
            matrix[r][c] = num
            # Compute next cell
            nr = r + dr[dir_idx]
            nc = c + dc[dir_idx]
            # If next cell is out of bounds or already filled, change direction
            if not (0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 0):
                dir_idx = (dir_idx + 1) % 4
                nr = r + dr[dir_idx]
                nc = c + dc[dir_idx]
            r, c = nr, nc
        return matrix