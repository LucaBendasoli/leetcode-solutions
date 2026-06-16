class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        leftmost = root
        
        while leftmost:
            curr = leftmost
            prev = None
            leftmost = None
            
            while curr:
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        leftmost = curr.left
                    prev = curr.left
                
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        leftmost = curr.right
                    prev = curr.right
                
                curr = curr.next
        
        return root