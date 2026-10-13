class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = []
        current_num = 0
        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            elif ch == '[':
                stack.append((current_str, current_num))
                current_str = []
                current_num = 0
            elif ch == ']':
                prev_str, repeat = stack.pop()
                current_str = prev_str + current_str * repeat
            else:
                current_str.append(ch)
        return ''.join(current_str)