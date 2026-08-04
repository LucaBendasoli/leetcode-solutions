from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Find length and last node
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        
        # Normalize k
        k = k % length
        if k == 0:
            return head
        
        # Find the new tail (length - k - 1 steps from head)
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # Rotate
        new_head = new_tail.next
        new_tail.next = None
        last.next = head
        
        return new_head