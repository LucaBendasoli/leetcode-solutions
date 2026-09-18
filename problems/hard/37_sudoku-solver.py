from __future__ import annotations

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        # Convert board to mutable list of lists if needed (it already is)
        # Initialize constraints
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + c // 3
                    boxes[box_idx].add(val)
        
        def is_valid(r: int, c: int, val: str) -> bool:
            box_idx = (r // 3) * 3 + c // 3
            return val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]
        
        def place(r: int, c: int, val: str) -> None:
            board[r][c] = val
            rows[r].add(val)
            cols[c].add(val)
            box_idx = (r // 3) * 3 + c // 3
            boxes[box_idx].add(val)
        
        def remove(r: int, c: int, val: str) -> None:
            board[r][c] = '.'
            rows[r].remove(val)
            cols[c].remove(val)
            box_idx = (r // 3) * 3 + c // 3
            boxes[box_idx].remove(val)
        
        def backtrack() -> bool:
            # Find next empty cell
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for digit in '123456789':
                            if is_valid(r, c, digit):
                                place(r, c, digit)
                                if backtrack():
                                    return True
                                remove(r, c, digit)
                        return False  # no digit works
            return True  # all cells filled
        
        backtrack()