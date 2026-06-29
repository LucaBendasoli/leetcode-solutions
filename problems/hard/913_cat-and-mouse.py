from typing import List
from collections import deque

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2
        
        # color[mouse][cat][turn] = outcome
        # turn: 1 = mouse's turn, 2 = cat's turn
        color = [[[0] * 3 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 3 for _ in range(n)] for _ in range(n)]
        
        # Calculate degrees (number of possible moves from each state)
        for m in range(n):
            for c in range(n):
                degree[m][c][1] = len(graph[m])
                degree[m][c][2] = len([node for node in graph[c] if node != 0])
        
        # Queue stores (mouse, cat, turn, color)
        queue = deque()
        
        # Initialize known outcomes
        for i in range(n):
            for t in range(1, 3):
                # Mouse wins: mouse at hole (node 0)
                color[0][i][t] = MOUSE
                queue.append((0, i, t, MOUSE))
                
                # Cat wins: cat catches mouse (same position, but not at hole)
                if i > 0:
                    color[i][i][t] = CAT
                    queue.append((i, i, t, CAT))
        
        # BFS to propagate outcomes
        while queue:
            mouse, cat, turn, outcome = queue.popleft()
            
            if mouse == 1 and cat == 2 and turn == 1:
                return outcome
            
            if turn == 1:
                # Previous turn was cat's turn
                for prev_cat in graph[cat]:
                    if prev_cat == 0:  # Cat cannot be at hole
                        continue
                    if color[mouse][prev_cat][2] > 0:
                        continue
                    
                    if outcome == CAT:
                        # Cat can win from this previous state
                        color[mouse][prev_cat][2] = CAT
                        queue.append((mouse, prev_cat, 2, CAT))
                    else:
                        # outcome == MOUSE
                        # Cat loses from one move, decrement degree
                        degree[mouse][prev_cat][2] -= 1
                        if degree[mouse][prev_cat][2] == 0:
                            # All moves lead to mouse winning
                            color[mouse][prev_cat][2] = MOUSE
                            queue.append((mouse, prev_cat, 2, MOUSE))
            else:
                # Previous turn was mouse's turn
                for prev_mouse in graph[mouse]:
                    if color[prev_mouse][cat][1] > 0:
                        continue
                    
                    if outcome == MOUSE:
                        # Mouse can win from this previous state
                        color[prev_mouse][cat][1] = MOUSE
                        queue.append((prev_mouse, cat, 1, MOUSE))
                    else:
                        # outcome == CAT
                        # Mouse loses from one move, decrement degree
                        degree[prev_mouse][cat][1] -= 1
                        if degree[prev_mouse][cat][1] == 0:
                            # All moves lead to cat winning
                            color[prev_mouse][cat][1] = CAT
                            queue.append((prev_mouse, cat, 1, CAT))
        
        return color[1][2][1]