class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0  # index in name
        j = 0  # index in typed
        
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif i > 0 and name[i-1] == typed[j]:
                # long press: current typed char matches previous name char
                j += 1
            else:
                return False
        
        # All characters in typed processed; now check if whole name was matched
        return i == len(name)