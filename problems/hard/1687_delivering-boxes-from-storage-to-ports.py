from typing import List
from collections import deque

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        
        # Precompute port changes
        # changes[i] = number of port changes from box 0 to box i
        changes = [0] * n
        for i in range(1, n):
            changes[i] = changes[i-1] + (1 if boxes[i][0] != boxes[i-1][0] else 0)
        
        # dp[i] = minimum trips to deliver first i boxes
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # For optimization, use a deque to maintain candidates
        # We need to find optimal j for each i efficiently
        
        # Sliding window approach
        j = 0
        weight = 0
        
        for i in range(n):
            # Extend window to include box i
            weight += boxes[i][1]
            
            # Shrink window if constraints violated
            while j < i and (i - j + 1 > maxBoxes or weight > maxWeight):
                weight -= boxes[j][1]
                j += 1
            
            # Try all valid starting positions from j to i
            for start in range(j, i + 1):
                # Cost of trip from start to i
                port_changes = changes[i] - (changes[start] if start > 0 else 0)
                trip_cost = 2 + port_changes
                
                # Check weight constraint
                trip_weight = sum(boxes[k][1] for k in range(start, i + 1))
                if trip_weight <= maxWeight and (i - start + 1) <= maxBoxes:
                    dp[i + 1] = min(dp[i + 1], dp[start] + trip_cost)
        
        # Optimize with monotonic deque
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Use sliding window with optimization
        for i in range(1, n + 1):
            j = i - 1
            weight = 0
            boxes_count = 0
            
            # Find all valid ranges ending at i-1
            while j >= 0 and boxes_count < maxBoxes and weight + boxes[j][1] <= maxWeight:
                weight += boxes[j][1]
                boxes_count += 1
                
                # Calculate trips for range [j, i-1]
                port_changes = changes[i-1] - (changes[j] if j > 0 else 0)
                trip_cost = 2 + port_changes
                dp[i] = min(dp[i], dp[j] + trip_cost)
                
                j -= 1
        
        return dp[n]