from __future__ import annotations

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        vals = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                vals.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                vals.append("null")
        # Remove trailing nulls to match LeetCode official format
        while vals and vals[-1] == "null":
            vals.pop()
        return ",".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        queue = [root]
        idx = 1
        while queue and idx < len(tokens):
            node = queue.pop(0)
            # left child
            if idx < len(tokens) and tokens[idx] != "null":
                node.left = TreeNode(int(tokens[idx]))
                queue.append(node.left)
            idx += 1
            # right child
            if idx < len(tokens) and tokens[idx] != "null":
                node.right = TreeNode(int(tokens[idx]))
                queue.append(node.right)
            idx += 1
        return root

# Alias for test compatibility
Solution = Codec

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))