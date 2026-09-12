from __future__ import annotations
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        stack: List[tuple[Optional[TreeNode], bool]] = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                result.append(node.val)
            else:
                # Push node back with visited flag, then right, then left
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return result