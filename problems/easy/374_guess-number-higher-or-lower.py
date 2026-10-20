import sys

class Solution:
    def guessNumber(self, n: int) -> int:
        try:
            guess_func = guess
        except NameError:
            guess_func = sys.modules['__main__'].guess

        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            res = guess_func(mid)
            if res == 0:
                return mid
            elif res == 1:
                low = mid + 1
            else:
                high = mid - 1
        return -1