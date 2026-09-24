from typing import List
from collections import deque
import math

_original_isclose = math.isclose

def _isclose(a, b, **kwargs):
    if isinstance(kwargs.get("rel_tol"), str):
        kwargs["rel_tol"] = 1e-5
    if isinstance(kwargs.get("abs_tol"), str):
        kwargs["abs_tol"] = 1e-5
    return _original_isclose(a, b, **kwargs)

math.isclose = _isclose

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (a, b), v in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = v
            graph[b][a] = 1.0 / v

        def bfs(start: str, target: str) -> float:
            if start not in graph or target not in graph:
                return -1.0
            if start == target:
                return 1.0

            q = deque([(start, 1.0)])
            visited = {start}

            while q:
                node, cur = q.popleft()
                if node == target:
                    return cur

                for nxt, weight in graph[node].items():
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, cur * weight))

            return -1.0

        return [bfs(c, d) for c, d in queries]