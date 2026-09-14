from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        # Quick length check
        if len(word) > m * n:
            return False
        
        # Frequency pruning: count letters in board and word
        from collections import Counter
        board_counter = Counter()
        for row in board:
            board_counter.update(row)
        word_counter = Counter(word)
        for c, cnt in word_counter.items():
            if board_counter.get(c, 0) < cnt:
                return False
        
        # Directions: up, down, left, right
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        
        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if board[r][c] != word[idx]:
                return False
            # Mark as visited temporarily
            temp, board[r][c] = board[r][c], '#'
            for dr, dc in dirs:
                if dfs(r + dr, c + dc, idx + 1):
                    return True
            # Restore
            board[r][c] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False