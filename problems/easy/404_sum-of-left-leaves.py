from __future__ import annotations

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None, is_left: bool) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)