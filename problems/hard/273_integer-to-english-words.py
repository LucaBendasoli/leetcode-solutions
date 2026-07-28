class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            if n == 0:
                return ""
            elif n < 10:
                return ones[n]
            elif n < 20:
                return teens[n - 10]
            elif n < 100:
                return tens[n // 10] + ("" if n % 10 == 0 else " " + ones[n % 10])
            else:
                return ones[n // 100] + " Hundred" + ("" if n % 100 == 0 else " " + helper(n % 100))
        
        result = []
        group_index = 0
        
        while num > 0:
            if num % 1000 != 0:
                group_words = helper(num % 1000)
                if thousands[group_index]:
                    group_words += " " + thousands[group_index]
                result.append(group_words)
            num //= 1000
            group_index += 1
        
        return " ".join(reversed(result))