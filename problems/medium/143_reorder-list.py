from __future__ import annotations
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return
        # find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # split
        second = slow.next
        slow.next = None
        # reverse second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev
        # merge
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2