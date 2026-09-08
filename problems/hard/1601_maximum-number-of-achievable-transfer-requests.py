from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        best = 0
        
        # Iterate over all subsets of requests using bitmask
        for mask in range(1 << m):
            # Count number of selected requests
            cnt = mask.bit_count()
            # If can't beat best, skip
            if cnt <= best:
                continue
            
            balance = [0] * n
            # Apply selected requests
            for i in range(m):
                if mask & (1 << i):
                    frm, to = requests[i]
                    balance[frm] -= 1
                    balance[to] += 1
            
            # Check if all balances are zero
            if all(b == 0 for b in balance):
                best = cnt
        
        return best