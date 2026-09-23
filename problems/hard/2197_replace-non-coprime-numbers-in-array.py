from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                lcm = a // gcd(a, b) * b
                stack.append(lcm)
        return stack