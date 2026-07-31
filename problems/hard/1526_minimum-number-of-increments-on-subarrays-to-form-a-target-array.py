from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = target[0]
        current_level = target[0]
        
        for i in range(1, len(target)):
            if target[i] > current_level:
                operations += target[i] - current_level
            current_level = target[i]
        
        return operations