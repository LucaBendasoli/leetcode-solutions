class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def live_neighbors(r: int, c: int) -> int:
            count = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if board[nr][nc] == 1 or board[nr][nc] == 2:
                        count += 1
            return count

        # Encoding:
        # 0: dead, stays dead
        # 1: live, stays live
        # 2: live, becomes dead
        # 3: dead, becomes live
        for r in range(m):
            for c in range(n):
                live = live_neighbors(r, c)
                if board[r][c] == 1:
                    if live < 2 or live > 3:
                        board[r][c] = 2
                else:
                    if live == 3:
                        board[r][c] = 3

        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1