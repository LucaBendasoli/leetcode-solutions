class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(n):
            s = str(n)
            return s == s[::-1]
        
        L = int(left)
        R = int(right)
        
        count = 0
        
        # Generate palindromes by constructing them from smaller numbers
        # For a range up to 10^18, we need palindromes up to sqrt(10^18) = 10^9
        # We can generate palindromes by taking first half and mirroring
        
        # Check palindromes of length 1 to 9 (covering up to 10^9)
        # Generate from base numbers
        
        limit = 100000  # sqrt(10^9) is about 31623, but we need some buffer
        
        # Generate odd-length palindromes
        for i in range(1, limit):
            s = str(i)
            palin = int(s + s[-2::-1])  # odd length
            square = palin * palin
            if square > R:
                break
            if square >= L and is_palindrome(square):
                count += 1
        
        # Generate even-length palindromes
        for i in range(1, limit):
            s = str(i)
            palin = int(s + s[::-1])  # even length
            square = palin * palin
            if square > R:
                break
            if square >= L and is_palindrome(square):
                count += 1
        
        return count