from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            # Check if there are k nodes remaining
            kth = self.getKth(prev_group, k)
            if not kth:
                break
            
            # Save the next group start
            next_group = kth.next
            
            # Reverse the current group
            prev, curr = kth.next, prev_group.next
            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Connect with previous group
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
        
        return dummy.next
    
    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr