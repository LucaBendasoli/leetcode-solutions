from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def get_prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors
        
        class UnionFind:
            def __init__(self):
                self.parent = {}
                self.rank = {}
            
            def find(self, x):
                if x not in self.parent:
                    self.parent[x] = x
                    self.rank[x] = 0
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
        
        uf = UnionFind()
        
        for num in nums:
            prime_factors = get_prime_factors(num)
            for pf in prime_factors:
                uf.union(num, pf)
        
        from collections import Counter
        component_count = Counter()
        for num in nums:
            root = uf.find(num)
            component_count[root] += 1
        
        return max(component_count.values())