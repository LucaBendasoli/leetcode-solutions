from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second, prev = None, None, None
        cur = root

        # Morris traversal
        while cur:
            if cur.left is None:
                # Visit the current node
                if prev and prev.val > cur.val:
                    if first is None:
                        first = prev
                    second = cur
                prev = cur
                cur = cur.right
            else:
                # Find the inorder predecessor
                predecessor = cur.left
                while predecessor.right and predecessor.right != cur:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    # Create a thread to the current node
                    predecessor.right = cur
                    cur = cur.left
                else:
                    # Remove the thread and visit the current node
                    predecessor.right = None
                    if prev and prev.val > cur.val:
                        if first is None:
                            first = prev
                        second = cur
                    prev = cur
                    cur = cur.right

        # Swap the values of the two misplaced nodes
        if first and second:
            first.val, second.val = second.val, first.val