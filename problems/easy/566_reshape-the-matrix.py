from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        flat = []
        for row in mat:
            for val in row:
                flat.append(val)
        
        result = []
        for i in range(r):
            result.append(flat[i * c:(i + 1) * c])
        
        return result