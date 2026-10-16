from collections import Counter
from functools import lru_cache
import math

class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        # Count frequencies of each distinct number
        freq = Counter(nums)
        distinct = list(freq.keys())

        # Build adjacency: which numbers can follow a given number
        adj = {x: [] for x in distinct}
        for i, a in enumerate(distinct):
            for j, b in enumerate(distinct):
                s = a + b
                if math.isqrt(s) ** 2 == s:
                    adj[a].append(b)

        # Memoized DFS on state (prev_value, tuple of (num, count) sorted)
        @lru_cache(None)
        def dfs(prev, state):
            # state is a sorted tuple of (num, count)
            remaining = sum(cnt for _, cnt in state)
            if remaining == 0:
                return 1
            total = 0
            # Convert to list to modify
            state_list = list(state)
            for i, (num, cnt) in enumerate(state_list):
                if cnt == 0:
                    continue
                if prev is not None and num not in adj[prev]:
                    continue
                # Decrement count
                new_state_list = state_list[:]
                new_state_list[i] = (num, cnt - 1)
                # Re-sort to keep canonical form
                new_state = tuple(sorted(new_state_list, key=lambda x: x[0]))
                total += dfs(num, new_state)
            return total

        initial_state = tuple(sorted((num, cnt) for num, cnt in freq.items()))
        return dfs(None, initial_state)