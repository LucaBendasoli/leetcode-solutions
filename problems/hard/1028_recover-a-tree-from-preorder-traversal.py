from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        n = len(traversal)
        
        def parse_node():
            nonlocal i
            
            if i >= n:
                return None
            
            # Count dashes (depth)
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Parse value
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            
            return (depth, val)
        
        # Parse all nodes
        nodes = []
        while i < n:
            nodes.append(parse_node())
        
        # Build tree using stack
        stack = []
        
        for depth, val in nodes:
            node = TreeNode(val)
            
            # Pop nodes from stack until we find the parent (depth - 1)
            while len(stack) > depth:
                stack.pop()
            
            # Attach to parent
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            
            stack.append(node)
        
        # Root is the first node
        return stack[0] if stack else None