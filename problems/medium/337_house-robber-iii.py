# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from __future__ import annotations

class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if not node:
                return (0, 0)  # (rob, not_rob)
            left = dfs(node.left)
            right = dfs(node.right)
            # rob this node
            rob_here = node.val + left[1] + right[1]
            # not rob this node
            not_rob_here = max(left) + max(right)
            return (rob_here, not_rob_here)

        return max(dfs(root))