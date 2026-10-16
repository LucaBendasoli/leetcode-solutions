from __future__ import annotations

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return TreeNode(val)

        cur = root
        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    break
                cur = cur.right

        return root