from __future__ import annotations

class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # factorials and inverse factorials
        fac = [1] * (n + 1)
        for i in range(1, n + 1):
            fac[i] = fac[i-1] * i % MOD
        invfac = [1] * (n + 1)
        invfac[n] = pow(fac[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfac[i-1] = invfac[i] * i % MOD

        # count occurrences of each lowercase letter
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # base = ∏ invfac[cnt[c]]  (product over all 26 letters)
        base = 1
        for c in cnt:
            base = base * invfac[c] % MOD

        ans = 0
        remaining = n          # number of characters not yet fixed
        for i, ch in enumerate(s):
            remaining -= 1     # characters left after fixing position i
            cur = ord(ch) - 97

            # for every character lexicographically smaller than s[i]
            for c in range(cur):
                if cnt[c] == 0:
                    continue
                # ways = factorial(remaining) * (∏ invfac of updated counts)
                ways = fac[remaining] * base % MOD
                ways = ways * fac[cnt[c]] % MOD
                ways = ways * invfac[cnt[c] - 1] % MOD
                ans = (ans + ways) % MOD

            # fix s[i] in the prefix: decrease its count
            old = cnt[cur]
            cnt[cur] -= 1
            # update the base product to reflect the decreased count
            base = base * fac[old] % MOD
            base = base * invfac[old - 1] % MOD

        return ans