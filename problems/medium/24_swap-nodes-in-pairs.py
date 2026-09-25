from __future__ import annotations

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # Dummy node to handle edge cases
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # Swap the two nodes
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev to the node after the pair
            prev = first
        
        return dummy.next