from __future__ import annotations

class Solution:
    def friendRequests(self, n: int, restrictions: list[list[int]], requests: list[list[int]]) -> list[bool]:
        parent = list(range(n))
        rank = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1

        # Build adjacency of root groups for restriction checking
        # restriction_groups: for each pair of restricted roots, track them
        restrict_set = set()
        for a, b in restrictions:
            ra, rb = find(a), find(b)
            if ra != rb:
                if ra > rb:
                    ra, rb = rb, ra
                restrict_set.add((ra, rb))

        def violates_restrictions(u: int, v: int) -> bool:
            ru, rv = find(u), find(v)
            if ru == rv:
                return True  # already same group -> future requests are fine, but for new union we check
            # After hypothetical union, root of merged group would be root of one of them
            # We need to check if any restricted pair becomes within same group.
            # Collect all nodes in components ru and rv (by root)
            # Since n <= 1000, we can just iterate over all restrictions
            for a, b in restrictions:
                ra, rb = find(a), find(b)
                # After union, ru and rv will be same, so if ra is ru/rv and rb is ru/rv and they are different restricted roots -> violation
                # Simpler: check if (ra, rb) would become same after union
                if (ra == ru and rb == rv) or (ra == rv and rb == ru):
                    return True
                if (ra == ru and rb == ru) or (ra == rv and rb == rv):
                    continue
                # If one of the roots is ru or rv and the other is also ru or rv but they are the restricted pair
                # Already covered above.
            return False

        answer = []
        for u, v in requests:
            ru, rv = find(u), find(v)
            if ru == rv:
                answer.append(True)
                continue

            # temporarily simulate union to check restrictions
            # We'll check all restrictions if merging would cause any restricted pair to be in same group
            conflict = False
            # Check if any restriction pair becomes satisfied
            for a, b in restrictions:
                ra, rb = find(a), find(b)
                # After union ru and rv become same, so:
                # if ra == ru and rb == rv or vice versa -> conflict
                if (ra == ru and rb == rv) or (ra == rv and rb == ru):
                    conflict = True
                    break
                # Also if one is ru/rv and the other is some other that itself forms restriction? No, restriction is only between a and b.
                # Also if ru == rv not possible here because we checked.
            
            if conflict:
                answer.append(False)
            else:
                answer.append(True)
                union(u, v)

        return answer