import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.val_to_indices = {}

    def insert(self, val: int) -> bool:
        is_new = val not in self.val_to_indices
        
        if val not in self.val_to_indices:
            self.val_to_indices[val] = set()
        
        self.val_to_indices[val].add(len(self.nums))
        self.nums.append(val)
        
        return is_new

    def remove(self, val: int) -> bool:
        if val not in self.val_to_indices or not self.val_to_indices[val]:
            return False
        
        idx_to_remove = self.val_to_indices[val].pop()
        last_val = self.nums[-1]
        
        self.nums[idx_to_remove] = last_val
        
        if last_val != val:
            self.val_to_indices[last_val].remove(len(self.nums) - 1)
            self.val_to_indices[last_val].add(idx_to_remove)
        
        self.nums.pop()
        
        if not self.val_to_indices[val]:
            del self.val_to_indices[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)