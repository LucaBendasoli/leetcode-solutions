from __future__ import annotations

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    continue
                # Check row
                if ch in rows[i]:
                    return False
                rows[i].add(ch)
                # Check column
                if ch in cols[j]:
                    return False
                cols[j].add(ch)
                # Check 3x3 box
                box_i = i // 3
                box_j = j // 3
                if ch in boxes[box_i][box_j]:
                    return False
                boxes[box_i][box_j].add(ch)
        return True