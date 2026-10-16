class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        if n > m:
            m, n = n, m

        states = 3 ** n
        pow3 = [1] * (n + 1)
        for i in range(n):
            pow3[i + 1] = pow3[i] * 3

        gain = [
            [0, 0, 0],
            [0, -60, -10],
            [0, -10, 40],
        ]

        cnt_intro = [0] * states
        cnt_extro = [0] * states
        base = [0] * states
        horizontal = [0] * states

        for mask in range(states):
            types = []
            tmp = mask
            for _ in range(n):
                types.append(tmp % 3)
                tmp //= 3

            c1 = types.count(1)
            c2 = types.count(2)
            cnt_intro[mask] = c1
            cnt_extro[mask] = c2
            base[mask] = 120 * c1 + 40 * c2

            h = 0
            for col in range(n - 1):
                a = types[col]
                b = types[col + 1]
                if a and b:
                    h += gain[a][b]
            horizontal[mask] = h

        vertical = [[0] * states for _ in range(states)]
        for prev in range(states):
            for cur in range(states):
                v = 0
                for col in range(n):
                    a = (prev // pow3[col]) % 3
                    b = (cur // pow3[col]) % 3
                    if a and b:
                        v += gain[a][b]
                vertical[prev][cur] = v

        NEG = -10 ** 9
        dp = [[[NEG] * (extrovertsCount + 1) for _ in range(introvertsCount + 1)] for _ in range(states)]
        dp[0][0][0] = 0

        for _ in range(m):
            ndp = [[[NEG] * (extrovertsCount + 1) for _ in range(introvertsCount + 1)] for _ in range(states)]

            for prev in range(states):
                for used_i in range(introvertsCount + 1):
                    for used_e in range(extrovertsCount + 1):
                        cur_val = dp[prev][used_i][used_e]
                        if cur_val == NEG:
                            continue

                        for cur in range(states):
                            ni = used_i + cnt_intro[cur]
                            ne = used_e + cnt_extro[cur]
                            if ni <= introvertsCount and ne <= extrovertsCount:
                                add = base[cur] + horizontal[cur] + vertical[prev][cur]
                                val = cur_val + add
                                if val > ndp[cur][ni][ne]:
                                    ndp[cur][ni][ne] = val

            dp = ndp

        ans = 0
        for prev in range(states):
            for used_i in range(introvertsCount + 1):
                for used_e in range(extrovertsCount + 1):
                    if dp[prev][used_i][used_e] > ans:
                        ans = dp[prev][used_i][used_e]

        return ans