class NumArray:
    def __init__(self, nums: list[int]):
        # Build prefix sums where prefix[i] = sum of nums[0..i-1]
        self.prefix = [0] * (len(nums) + 1)
        for i, val in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + val

    def sumRange(self, left: int, right: int) -> int:
        # Sum from left to right inclusive = prefix[right+1] - prefix[left]
        return self.prefix[right + 1] - self.prefix[left]