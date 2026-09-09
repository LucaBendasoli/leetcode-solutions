class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        # Try all possible lengths for the first number
        for first_end in range(1, n):
            # Leading zero check for first number
            if num[0] == '0' and first_end > 1:
                break
            first = num[:first_end]
            # Try all possible lengths for the second number
            for second_end in range(first_end + 1, n):
                # Leading zero check for second number
                if num[first_end] == '0' and second_end - first_end > 1:
                    break
                second = num[first_end:second_end]
                # Now check if the remaining part can be an additive sequence
                # starting with first and second
                if self._is_valid(num, first, second, second_end):
                    return True
        return False

    def _is_valid(self, num: str, first: str, second: str, start: int) -> bool:
        # Convert first and second to integers
        a = int(first)
        b = int(second)
        n = len(num)
        while start < n:
            c = a + b
            c_str = str(c)
            # Check if the remaining string starts with c_str
            if not num.startswith(c_str, start):
                return False
            start += len(c_str)
            a, b = b, c
        return True