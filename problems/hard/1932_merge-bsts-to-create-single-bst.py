from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        if not trees:
            return None

        # map root value -> node
        root_map = {}
        # map root value -> (min_val, max_val)
        minmax_map = {}

        # compute minima, maxima and collect leaf values
        for root in trees:
            # collect all values in this small tree
            vals = [root.val]
            if root.left:
                vals.append(root.left.val)
            if root.right:
                vals.append(root.right.val)
            minmax_map[root.val] = (min(vals), max(vals))
            root_map[root.val] = root

        # indegree: how many leaves (from other trees) point to a given root value
        indegree = {val: 0 for val in root_map}
        for root in trees:
            # collect leaves of this tree (nodes with no children)
            leaves = []
            if root.left is None and root.right is None:
                leaves.append(root.val)
            else:
                if root.left and root.left.left is None and root.left.right is None:
                    leaves.append(root.left.val)
                if root.right and root.right.left is None and root.right.right is None:
                    leaves.append(root.right.val)
            for v in leaves:
                if v in root_map and root_map[v] is not root:
                    indegree[v] += 1

        # exactly one root with indegree 0 -> final root
        final_root_val = None
        for val, cnt in indegree.items():
            if cnt == 0:
                if final_root_val is None:
                    final_root_val = val
                else:
                    return None
        if final_root_val is None:
            return None
        # all other roots must have indegree 1
        for val, cnt in indegree.items():
            if val != final_root_val and cnt != 1:
                return None

        # remove final root from maps – it will not be attached
        final_root = root_map.pop(final_root_val)
        minmax_map.pop(final_root_val)

        # iterative DFS to attach trees at leaves
        INF = float('inf')
        stack = [(final_root, -INF, INF, None, None)]   # (node, lower, upper, parent, side)

        while stack:
            node, lower, upper, parent, side = stack.pop()
            if node is None:
                continue

            # if this node is a leaf and its value matches an unattached root, attach it
            if node.left is None and node.right is None and node.val in root_map:
                new_root = root_map.pop(node.val)
                orig_min, orig_max = minmax_map.pop(node.val)   # original min/max of the attached tree

                # check that the whole attached subtree fits within bounds
                if not (lower < orig_min and orig_max < upper):
                    return None

                # attach to parent
                if parent is None:
                    final_root = new_root
                elif side == 'left':
                    parent.left = new_root
                else:   # side == 'right'
                    parent.right = new_root

                # process the children of the newly attached root
                if new_root.right:
                    stack.append((new_root.right, node.val, upper, new_root, 'right'))
                if new_root.left:
                    stack.append((new_root.left, lower, node.val, new_root, 'left'))
                continue

            # not replaced: push children for later processing
            if node.right:
                stack.append((node.right, node.val, upper, node, 'right'))
            if node.left:
                stack.append((node.left, lower, node.val, node, 'left'))

        # all unattached roots must have been used
        if root_map:
            return None

        return final_root