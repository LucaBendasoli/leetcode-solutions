class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        place = 1

        while place <= n:
            higher = n // (place * 10)
            current = (n // place) % 10
            lower = n % place

            if current == 0:
                count += higher * place
            elif current == 1:
                count += higher * place + lower + 1
            else:
                count += (higher + 1) * place

            place *= 10

        return count