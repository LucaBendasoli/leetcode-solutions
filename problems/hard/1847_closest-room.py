from typing import List
import bisect

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        # ---- coordinate compression of all relevant ids ----
        ids = set()
        for rid, _ in rooms:
            ids.add(rid)
        for pref, _ in queries:
            ids.add(pref)
        uniq = sorted(ids)
        comp = {v: i+1 for i, v in enumerate(uniq)}  # 1-indexed for BIT
        decomp = {i+1: v for i, v in enumerate(uniq)}

        # ---- sort rooms by size descending ----
        rooms.sort(key=lambda x: -x[1])   # (roomId, size)

        # ---- sort queries by minSize descending, keep original index ----
        queries_sorted = sorted(
            [(ms, pref, idx) for idx, (pref, ms) in enumerate(queries)],
            key=lambda x: -x[0]
        )

        # ---- Fenwick Tree (Binary Indexed Tree) ----
        n = len(uniq)
        bit = [0] * (n + 2)

        def add(i: int, delta: int) -> None:
            while i <= n:
                bit[i] += delta
                i += i & -i

        def prefix_sum(i: int) -> int:
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        # find smallest idx such that prefix_sum(idx) >= k
        def kth(k: int) -> int:
            # binary lifting
            idx = 0
            bitmask = 1 << (n.bit_length())  # largest power of two > n
            while bitmask:
                nxt = idx + bitmask
                if nxt <= n and bit[nxt] < k:
                    k -= bit[nxt]
                    idx = nxt
                bitmask >>= 1
            return idx + 1

        # ---- process queries offline ----
        ans = [-1] * len(queries)
        ptr = 0
        for ms, pref, orig_idx in queries_sorted:
            # add all rooms with size >= ms
            while ptr < len(rooms) and rooms[ptr][1] >= ms:
                rid = rooms[ptr][0]
                add(comp[rid], 1)
                ptr += 1

            total = prefix_sum(n)
            if total == 0:
                continue

            target_comp = comp[pref]
            cnt_le = prefix_sum(target_comp)

            candidates = []
            # floor: largest index <= target_comp that is present
            if cnt_le > 0:
                floor_idx = kth(cnt_le)
                candidates.append(decomp[floor_idx])
            # ceiling: smallest index >= target_comp that is present
            if cnt_le < total:
                ceil_idx = kth(cnt_le + 1)
                candidates.append(decomp[ceil_idx])

            if not candidates:
                continue

            # choose the best among candidates
            best = -1
            best_diff = float('inf')
            for cid in candidates:
                diff = abs(cid - pref)
                if diff < best_diff or (diff == best_diff and cid < best):
                    best = cid
                    best_diff = diff
            ans[orig_idx] = best

        return ans