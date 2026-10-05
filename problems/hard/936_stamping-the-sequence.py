from collections import deque

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        n, m = len(target), len(stamp)
        windows = n - m + 1

        todo = [m] * windows
        for i in range(windows):
            for j in range(m):
                if target[i + j] == stamp[j]:
                    todo[i] -= 1

        done = [False] * n
        q = deque(i for i in range(windows) if todo[i] == 0)
        ans = []

        while q:
            i = q.popleft()
            ans.append(i)

            for j in range(i, i + m):
                if done[j]:
                    continue
                done[j] = True

                left = max(0, j - m + 1)
                right = min(j, windows - 1)

                for k in range(left, right + 1):
                    if target[j] != stamp[j - k]:
                        todo[k] -= 1
                        if todo[k] == 0:
                            q.append(k)

        return ans[::-1] if all(done) else []