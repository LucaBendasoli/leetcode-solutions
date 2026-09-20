from __future__ import annotations

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Mark visited numbers by negating the value at the corresponding index
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Collect indices that are still positive -> missing numbers
        missing = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missing.append(i + 1)
        return missing