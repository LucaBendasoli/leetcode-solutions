class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        total = 0
        ans = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            if satisfaction[i] + total > 0:
                total += satisfaction[i]
                ans += total
        return ans