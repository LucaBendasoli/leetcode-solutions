from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # If there's only one element, we are already at the end
        if n <= 1:
            return 0

        jumps = 0          # Number of jumps taken
        current_end = 0    # Farthest index we can reach with current number of jumps
        farthest = 0       # Farthest index we can reach overall

        # We don't need to consider the last index; we stop before it
        for i in range(n - 1):
            # Update the farthest index we can reach from current position
            farthest = max(farthest, i + nums[i])

            # If we've reached the end of the current jump's range,
            # we must take another jump
            if i == current_end:
                jumps += 1
                current_end = farthest

                # Early exit if we can already reach the end
                if current_end >= n - 1:
                    break

        return jumps