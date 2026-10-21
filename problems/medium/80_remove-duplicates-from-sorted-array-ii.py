class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for x in nums:
            if i < 2 or nums[i - 2] != x:
                nums[i] = x
                i += 1
        return i