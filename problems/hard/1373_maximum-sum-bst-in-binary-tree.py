from __future__ import annotations
import sys

class Solution:
    def maxSumBST(self, root: TreeNode | None) -> int:
        ans = 0

        def dfs(node: TreeNode | None) -> tuple[bool, int, int, int]:
            nonlocal ans
            if not node:
                return True, sys.maxsize, -sys.maxsize, 0

            left_bst, left_min, left_max, left_sum = dfs(node.left)
            right_bst, right_min, right_max, right_sum = dfs(node.right)

            if left_bst and right_bst and left_max < node.val < right_min:
                cur_sum = left_sum + right_sum + node.val
                cur_min = min(left_min, node.val)
                cur_max = max(right_max, node.val)
                ans = max(ans, cur_sum)
                return True, cur_min, cur_max, cur_sum
            else:
                return False, 0, 0, 0

        dfs(root)
        return ans