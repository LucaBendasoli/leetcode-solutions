class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        # If strings are equal, we need at least one duplicate character to swap
        if s == goal:
            return len(set(s)) < len(s)

        # Find indices where characters differ
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False

        # Exactly two differences needed for a valid swap
        if len(diff) != 2:
            return False

        i, j = diff
        # Check if swapping s[i] and s[j] matches goal at those positions
        return s[i] == goal[j] and s[j] == goal[i]