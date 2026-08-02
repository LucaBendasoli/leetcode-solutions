from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], current_num: int) -> int:
            if not node:
                return 0
            
            current_num = current_num * 10 + node.val
            
            if not node.left and not node.right:
                return current_num
            
            return dfs(node.left, current_num) + dfs(node.right, current_num)
        
        return dfs(root, 0)