class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        in_stack = set()
        
        for i, char in enumerate(s):
            if char in in_stack:
                continue
            
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed = stack.pop()
                in_stack.remove(removed)
            
            stack.append(char)
            in_stack.add(char)
        
        return ''.join(stack)