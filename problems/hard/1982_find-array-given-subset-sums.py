from collections import Counter
from typing import List

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        ans = []

        for _ in range(n):
            diff = sums[-1] - sums[-2]

            if diff == 0:
                ans.append(0)
                sums = sums[::2]
                continue

            for cand in (diff, -diff):
                new_sums = self._try_partition(sums, cand)
                if new_sums is not None:
                    ans.append(cand)
                    sums = sorted(new_sums)
                    break

        return ans

    def _try_partition(self, sums: List[int], cand: int) -> List[int] | None:
        if cand == 0:
            return None

        # Try ascending order: the base part is the smaller elements.
        cnt = Counter(sums)
        new = []
        ok = True
        for x in sorted(cnt.keys()):
            while cnt[x] > 0:
                y = x + cand
                if cnt.get(y, 0) > 0:
                    cnt[x] -= 1
                    cnt[y] -= 1
                    new.append(x)
                else:
                    ok = False
                    break
            if not ok:
                break

        if ok and len(new) == len(sums) // 2 and 0 in new:
            return new

        # Try descending order: the base part is the larger elements.
        cnt = Counter(sums)
        new = []
        ok = True
        for x in sorted(cnt.keys(), reverse=True):
            while cnt[x] > 0:
                y = x + cand
                if cnt.get(y, 0) > 0:
                    cnt[x] -= 1
                    cnt[y] -= 1
                    new.append(x)
                else:
                    ok = False
                    break
            if not ok:
                break

        if ok and len(new) == len(sums) // 2 and 0 in new:
            return new

        return None