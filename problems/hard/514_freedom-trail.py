class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        
        n = len(ring)
        m = len(key)
        
        # Build a map of character positions in ring
        char_positions = defaultdict(list)
        for i, ch in enumerate(ring):
            char_positions[ch].append(i)
        
        # dp[i][j] = minimum steps to spell key[0:i] with ring position j at 12:00
        # We use a dictionary for current state
        dp = {0: 0}  # Initially at position 0 with 0 steps
        
        for i in range(m):
            next_dp = {}
            target_char = key[i]
            
            for curr_pos, curr_steps in dp.items():
                # Try all positions where target_char exists
                for target_pos in char_positions[target_char]:
                    # Calculate rotation distance
                    clockwise = (target_pos - curr_pos) % n
                    counterclockwise = (curr_pos - target_pos) % n
                    rotation_steps = min(clockwise, counterclockwise)
                    
                    # Total steps: current steps + rotation + 1 press
                    total_steps = curr_steps + rotation_steps + 1
                    
                    # Update next_dp with minimum steps to reach target_pos
                    if target_pos not in next_dp or total_steps < next_dp[target_pos]:
                        next_dp[target_pos] = total_steps
            
            dp = next_dp
        
        return min(dp.values())