from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) lookup
        index_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(in_left: int, in_right: int, post_left: int, post_right: int) -> Optional[TreeNode]:
            if in_left > in_right or post_left > post_right:
                return None
            
            # The last element of the current postorder segment is the root
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            
            # Find the index of the root in inorder traversal
            idx = index_map[root_val]
            
            # Number of nodes in the left subtree
            left_size = idx - in_left
            
            # Recursively build left and right subtrees
            root.left = helper(in_left, idx - 1, post_left, post_left + left_size - 1)
            root.right = helper(idx + 1, in_right, post_left + left_size, post_right - 1)
            
            return root
        
        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)