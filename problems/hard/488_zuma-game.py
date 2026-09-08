from functools import lru_cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # map colors to indices
        color_index = {'R': 0, 'Y': 1, 'B': 2, 'G': 3, 'W': 4}
        colors = ['R', 'Y', 'B', 'G', 'W']

        # initial hand as tuple of counts
        init_hand = [0] * 5
        for c in hand:
            init_hand[color_index[c]] += 1
        init_hand = tuple(init_hand)

        # remove all consecutive groups of 3 or more same colour repeatedly
        def compress(s: str) -> str:
            while True:
                n = len(s)
                i = 0
                res = []
                while i < n:
                    j = i
                    while j < n and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        # remove this group
                        i = j
                        continue
                    else:
                        res.append(s[i:j])
                        i = j
                new_s = ''.join(res)
                if len(new_s) == n:
                    break
                s = new_s
            return s

        @lru_cache(maxsize=None)
        def dfs(board: str, hand_counts: tuple) -> int:
            if not board:
                return 0
            if all(c == 0 for c in hand_counts):
                return float('inf')

            best = float('inf')
            for idx, cnt in enumerate(hand_counts):
                if cnt == 0:
                    continue
                color = colors[idx]
                # try inserting at each valid position
                for i in range(len(board) + 1):
                    # only insert where it can form a group immediately
                    if (i > 0 and board[i-1] == color) or (i < len(board) and board[i] == color):
                        new_board = board[:i] + color + board[i:]
                        new_board = compress(new_board)
                        new_hand = list(hand_counts)
                        new_hand[idx] -= 1
                        new_hand = tuple(new_hand)
                        steps = dfs(new_board, new_hand)
                        if steps != float('inf'):
                            best = min(best, 1 + steps)
            return best

        result = dfs(board, init_hand)
        return -1 if result == float('inf') else result