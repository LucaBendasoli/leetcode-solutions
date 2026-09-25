class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(start: int, remaining: int, path: list[int]) -> None:
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, n):
                num = candidates[i]
                if num > remaining:
                    break

                path.append(num)
                backtrack(i, remaining - num, path)
                path.pop()

        backtrack(0, target, [])
        return res