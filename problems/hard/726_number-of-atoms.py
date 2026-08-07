class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from collections import defaultdict
        
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                # Parse the multiplier after ')'
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i]) if i > start else 1
                
                # Pop the top dictionary and merge with previous
                top = stack.pop()
                for elem, count in top.items():
                    stack[-1][elem] += count * multiplier
            else:
                # Parse element name (uppercase followed by optional lowercase)
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[start:i]
                
                # Parse count
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if i > start else 1
                
                stack[-1][elem] += count
        
        # Build result string
        result = []
        for elem in sorted(stack[0].keys()):
            count = stack[0][elem]
            result.append(elem)
            if count > 1:
                result.append(str(count))
        
        return ''.join(result)