from __future__ import annotations

class Solution:
    def gcdSort(self, nums: list[int]) -> bool:
        limit = max(nums)

        spf = [0] * (limit + 1)
        for i in range(2, int(limit ** 0.5) + 1):
            if spf[i] == 0:
                for j in range(i * i, limit + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
        for i in range(2, limit + 1):
            if spf[i] == 0:
                spf[i] = i

        parent = list(range(limit + 1))
        size = [1] * (limit + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for num in nums:
            x = num
            while x > 1:
                p = spf[x]
                while x % p == 0:
                    x //= p
                union(num, p)

        sorted_nums = sorted(nums)
        for a, b in zip(nums, sorted_nums):
            if find(a) != find(b):
                return False
        return True