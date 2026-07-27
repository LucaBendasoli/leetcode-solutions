from typing import List

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        # Parse the expression into numbers and operators
        nums = []
        ops = []
        for c in s:
            if c.isdigit():
                nums.append(int(c))
            else:
                ops.append(c)
        
        # Calculate correct answer
        correct = self.evaluateCorrect(s)
        
        # Get all possible wrong answers using DP
        n = len(nums)
        possible = self.getAllPossible(nums, ops, n)
        
        # Score the answers
        total_score = 0
        for ans in answers:
            if ans == correct:
                total_score += 5
            elif ans in possible:
                total_score += 2
        
        return total_score
    
    def evaluateCorrect(self, s: str) -> int:
        # First do all multiplications
        nums = []
        ops = []
        i = 0
        current = int(s[0])
        
        for i in range(1, len(s)):
            if s[i] == '*':
                i += 1
                current *= int(s[i])
            elif s[i] == '+':
                nums.append(current)
                ops.append('+')
                i += 1
                current = int(s[i])
            elif s[i].isdigit():
                pass
        nums.append(current)
        
        # Now do additions
        result = nums[0]
        for num in nums[1:]:
            result += num
        
        return result
    
    def getAllPossible(self, nums, ops, n):
        # dp[i][j] = set of all possible values for subexpression from index i to j
        dp = [[set() for _ in range(n)] for _ in range(n)]
        
        # Base case: single numbers
        for i in range(n):
            dp[i][i].add(nums[i])
        
        # Fill dp table for increasing lengths
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Try all possible split points
                for k in range(i, j):
                    op = ops[k]
                    left_vals = dp[i][k]
                    right_vals = dp[k + 1][j]
                    
                    for lv in left_vals:
                        for rv in right_vals:
                            if op == '+':
                                val = lv + rv
                            else:  # op == '*'
                                val = lv * rv
                            
                            # Only keep values <= 1000 to avoid explosion
                            if val <= 1000:
                                dp[i][j].add(val)
        
        result = dp[0][n - 1].copy()
        # Remove the correct answer if it's there (we'll handle it separately)
        return result