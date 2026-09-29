class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(m):
            for j in range(n):
                digit_mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                res[i + j] += digit_mul
                if res[i + j] >= 10:
                    res[i + j + 1] += res[i + j] // 10
                    res[i + j] %= 10
        # Remove trailing zeros (in reversed order) and build result
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return ''.join(str(d) for d in reversed(res))