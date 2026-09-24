class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        total = 0
        current_len = 0  # length of current arithmetic subarray (at least 2 means we have a valid difference)
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current_len += 1
                total += current_len
            else:
                current_len = 0
        return total