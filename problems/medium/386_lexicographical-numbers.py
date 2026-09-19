from __future__ import annotations

class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []
        current = 1
        for _ in range(n):
            result.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                # When we cannot multiply by 10, we need to find the next number
                # that is not ending with 9 and still <= n
                while current % 10 == 9 or current + 1 > n:
                    current //= 10
                current += 1
        return result