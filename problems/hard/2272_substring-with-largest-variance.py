from __future__ import annotations

class Solution:
    def largestVariance(self, s: str) -> int:
        # Consider all pairs of characters (major, minor)
        chars = set(s)
        max_variance = 0
        
        for major in chars:
            for minor in chars:
                if major == minor:
                    continue
                # Run Kadane's algorithm variant:
                # We treat major as +1, minor as -1, others as 0
                # But we must ensure that at least one minor appears in the substring
                count_major = 0
                count_minor = 0
                # We can reset the running sum if the minor count has been zero so far
                # But we need to allow restarting substrings
                # We'll track the current balance and also a "with_minor" flag
                balance = 0
                # The best variance ending at current position, allowing reset
                # To enforce at least one minor, we keep a separate track:
                # We'll use two running sums: one that can start fresh (no minor yet),
                # and one that already has a minor.
                cur_without_minor = 0  # sum of major - minor, but minor count=0 so far
                cur_with_minor = float('-inf')  # must have seen at least one minor
                
                for ch in s:
                    if ch == major:
                        # Update both: major adds +1 to balance
                        # If we already have a minor, the value increases
                        if cur_with_minor != float('-inf'):
                            cur_with_minor += 1
                        cur_without_minor += 1
                    elif ch == minor:
                        # For the "without minor" path, seeing minor moves it to "with minor"
                        # The balance for that new path is: cur_without_minor - 1
                        # (since minor subtracts 1)
                        new_with_minor = cur_without_minor - 1
                        # The existing with_minor also gets -1
                        if cur_with_minor != float('-inf'):
                            cur_with_minor -= 1
                        # Now we also can start a new substring with this minor as first char
                        # That gives balance -1 (one minor, zero major)
                        cur_without_minor = 0  # reset, because any substring without minor starting here is just 0 (we ignore it)
                        # Pick the best among paths that now have a minor
                        cur_with_minor = max(cur_with_minor, new_with_minor, -1)
                    else:
                        # Other characters: no change to counts, but they affect balance as 0
                        # They don't change the counts, but they keep existing paths alive
                        # Actually they don't change the balance, so nothing to do
                        pass
                    
                    # Update max variance from paths that have at least one minor
                    if cur_with_minor != float('-inf'):
                        max_variance = max(max_variance, cur_with_minor)
        
        return max_variance