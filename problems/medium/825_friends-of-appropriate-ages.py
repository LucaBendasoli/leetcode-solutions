class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        freq = [0] * 121
        for age in ages:
            freq[age] += 1
        
        total = 0
        for x in range(1, 121):
            cnt_x = freq[x]
            if cnt_x == 0:
                continue
            for y in range(1, 121):
                cnt_y = freq[y]
                if cnt_y == 0:
                    continue
                # condition 1: age[y] <= 0.5 * age[x] + 7  => 2*y <= x + 14
                if 2 * y <= x + 14:
                    continue
                # condition 2: age[y] > age[x]
                if y > x:
                    continue
                # condition 3: age[y] > 100 and age[x] < 100
                if y > 100 and x < 100:
                    continue
                if x == y:
                    total += cnt_x * (cnt_x - 1)
                else:
                    total += cnt_x * cnt_y
        return total