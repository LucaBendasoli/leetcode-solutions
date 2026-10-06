class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        # Compute prefix sum for each row
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c-1]
        
        ans = 0
        # For each pair of columns (c1, c2)
        for c1 in range(cols):
            for c2 in range(c1, cols):
                # Map prefix sum of row segments to count
                prefix_counts = {0: 1}
                cur_sum = 0
                for r in range(rows):
                    # Sum of row r from c1 to c2
                    row_sum = matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                    cur_sum += row_sum
                    # Check if cur_sum - target exists in map
                    ans += prefix_counts.get(cur_sum - target, 0)
                    prefix_counts[cur_sum] = prefix_counts.get(cur_sum, 0) + 1
        
        return ans