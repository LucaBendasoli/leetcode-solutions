class Iterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0
    
    def hasNext(self):
        return self.index < len(self.nums)
    
    def next(self):
        val = self.nums[self.index]
        self.index += 1
        return val

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked_value = None
        self.has_peeked = False
        
    def peek(self):
        if not self.has_peeked:
            self.peeked_value = self.iterator.next()
            self.has_peeked = True
        return self.peeked_value
        
    def next(self):
        if self.has_peeked:
            self.has_peeked = False
            return self.peeked_value
        return self.iterator.next()
        
    def hasNext(self):
        return self.has_peeked or self.iterator.hasNext()