from __future__ import annotations

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            if ch.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                # Process the current number with the previous sign
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    # Integer division truncating toward zero
                    stack[-1] = int(stack[-1] / num)
                continue  # i already moved to next non-digit
            elif ch in '+-*/':
                sign = ch
            # else it's a space, ignore
            i += 1
        return sum(stack)