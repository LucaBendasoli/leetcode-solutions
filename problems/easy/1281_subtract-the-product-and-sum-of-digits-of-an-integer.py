class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        
        product = 1
        for digit in digits:
            product *= digit
        
        sum_digits = sum(digits)
        
        return product - sum_digits