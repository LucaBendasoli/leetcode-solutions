from __future__ import annotations

class NestedInteger:
    """Helper class to simulate the NestedInteger structure."""
    
    def __init__(self, value=None):
        self._value = value
        self._list = []
        self._is_integer = value is not None
    
    def isInteger(self) -> bool:
        return self._is_integer
    
    def getInteger(self) -> int:
        return self._value
    
    def setInteger(self, value: int) -> None:
        self._value = value
        self._is_integer = True
    
    def add(self, ni: 'NestedInteger') -> None:
        self._list.append(ni)
        self._is_integer = False
    
    def getList(self) -> list:
        return self._list
    
    def __eq__(self, other):
        # Structural equality: compare attributes even if other is a different class.
        if hasattr(other, '_is_integer') and hasattr(other, '_value') and hasattr(other, '_list'):
            if self._is_integer != other._is_integer:
                return False
            if self._is_integer:
                return self._value == other._value
            if len(self._list) != len(other._list):
                return False
            return all(a == b for a, b in zip(self._list, other._list))
        return NotImplemented
    
    def __repr__(self):
        if self._is_integer:
            return str(self._value)
        return '[' + ','.join(repr(item) for item in self._list) + ']'


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()

        # Single integer case (no brackets)
        if s[0] != '[':
            return NestedInteger(int(s))

        # Iterative parsing using a stack
        n = len(s)
        i = 1  # skip initial '['
        root = NestedInteger()   # outermost list
        stack = [root]

        while i < n:
            ch = s[i]
            if ch == '[':
                new_list = NestedInteger()
                stack[-1].add(new_list)
                stack.append(new_list)
                i += 1
            elif ch == ']':
                stack.pop()
                i += 1
            elif ch == ',':
                i += 1
            else:
                # Parse integer (may be negative)
                start = i
                if s[i] == '-':
                    i += 1
                while i < n and s[i].isdigit():
                    i += 1
                num = int(s[start:i])
                ni = NestedInteger(num)
                stack[-1].add(ni)

        return root