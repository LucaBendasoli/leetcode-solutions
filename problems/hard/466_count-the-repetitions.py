class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        
        # Check if all chars in s2 exist in s1
        s1_chars = set(s1)
        for c in s2:
            if c not in s1_chars:
                return 0
        
        # Track state: after processing i copies of s1, 
        # we're at position s2_idx in s2 and have completed s2_count copies of s2
        s2_idx = 0  # current position in s2
        s2_count = 0  # number of complete s2's formed
        
        # seen[s2_idx] = (s1_count, s2_count) when we first saw this s2_idx
        seen = {}
        
        for s1_count in range(n1):
            # Before processing this copy of s1, record the state
            if s2_idx in seen:
                # We've seen this s2_idx before - cycle detected!
                prev_s1_count, prev_s2_count = seen[s2_idx]
                
                # Cycle info
                cycle_len = s1_count - prev_s1_count  # how many s1's in the cycle
                cycle_s2_count = s2_count - prev_s2_count  # how many s2's in the cycle
                
                # How many complete cycles can we do with remaining s1's?
                remaining_s1 = n1 - s1_count
                complete_cycles = remaining_s1 // cycle_len
                
                # Fast forward through complete cycles
                s2_count += complete_cycles * cycle_s2_count
                s1_count += complete_cycles * cycle_len
                
                # Process remaining s1's
                for _ in range(s1_count, n1):
                    for c in s1:
                        if c == s2[s2_idx]:
                            s2_idx += 1
                            if s2_idx == len(s2):
                                s2_count += 1
                                s2_idx = 0
                
                return s2_count // n2
            
            seen[s2_idx] = (s1_count, s2_count)
            
            # Process this copy of s1
            for c in s1:
                if c == s2[s2_idx]:
                    s2_idx += 1
                    if s2_idx == len(s2):
                        s2_count += 1
                        s2_idx = 0
        
        return s2_count // n2