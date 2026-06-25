from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(0, 0, self.n - 1)
    
    def _build(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.nums[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self._build(left_child, start, mid)
            self._build(right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def update(self, index: int, val: int) -> None:
        self._update(0, 0, self.n - 1, index, val)
    
    def _update(self, node: int, start: int, end: int, index: int, val: int) -> None:
        if start == end:
            self.nums[index] = val
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if index <= mid:
                self._update(left_child, start, mid, index, val)
            else:
                self._update(right_child, mid + 1, end, index, val)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def sumRange(self, left: int, right: int) -> int:
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or left > end:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_sum = self._query(left_child, start, mid, left, right)
        right_sum = self._query(right_child, mid + 1, end, left, right)
        return left_sum + right_sum