class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        
        upper = 10**n - 1
        lower = 10**(n-1)
        
        # Start from the largest possible first half
        for i in range(upper, lower - 1, -1):
            # Create palindrome by mirroring i
            s = str(i)
            palindrome = int(s + s[::-1])
            
            # Check if this palindrome can be expressed as product of two n-digit numbers
            # Start from upper bound and go down
            j = upper
            while j * j >= palindrome:
                if palindrome % j == 0:
                    other = palindrome // j
                    if other <= upper and other >= lower:
                        return palindrome % 1337
                j -= 1
        
        return 0