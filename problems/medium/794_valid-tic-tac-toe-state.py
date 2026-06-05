from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def count_pieces(board):
            x_count = 0
            o_count = 0
            for row in board:
                x_count += row.count('X')
                o_count += row.count('O')
            return x_count, o_count
        
        def has_winner(board, player):
            # Check rows
            for row in board:
                if all(c == player for c in row):
                    return True
            
            # Check columns
            for col in range(3):
                if all(board[row][col] == player for row in range(3)):
                    return True
            
            # Check diagonals
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2-i] == player for i in range(3)):
                return True
            
            return False
        
        x_count, o_count = count_pieces(board)
        
        # X goes first, so x_count should be equal to o_count or o_count + 1
        if x_count < o_count or x_count > o_count + 1:
            return False
        
        x_wins = has_winner(board, 'X')
        o_wins = has_winner(board, 'O')
        
        # Both can't win
        if x_wins and o_wins:
            return False
        
        # If X wins, X must have just played (x_count == o_count + 1)
        if x_wins and x_count != o_count + 1:
            return False
        
        # If O wins, O must have just played (x_count == o_count)
        if o_wins and x_count != o_count:
            return False
        
        return True