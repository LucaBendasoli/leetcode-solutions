from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # Sort by width ascending, and for equal width by height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Extract heights after sorting
        heights = [h for _, h in envelopes]
        
        # Longest increasing subsequence on heights (strictly increasing)
        tails = []
        for h in heights:
            idx = bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h
        return len(tails)