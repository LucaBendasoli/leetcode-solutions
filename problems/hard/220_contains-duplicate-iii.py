from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        bucket_width = valueDiff + 1
        buckets = {}
        
        for i, num in enumerate(nums):
            bucket_id = num // bucket_width
            
            # Check if the same bucket already has a number
            if bucket_id in buckets:
                return True
            
            # Check adjacent buckets
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            # Add current number to its bucket
            buckets[bucket_id] = num
            
            # Remove the oldest element if window size exceeds indexDiff
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_width
                del buckets[old_bucket_id]
        
        return False