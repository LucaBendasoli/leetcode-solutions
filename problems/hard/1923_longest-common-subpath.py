from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def get_hashes(path, length, base, mod):
            if length > len(path):
                return set()
            
            hashes = set()
            h = 0
            power = 1
            
            for i in range(length):
                h = (h * base + path[i]) % mod
                if i < length - 1:
                    power = (power * base) % mod
            
            hashes.add(h)
            
            for i in range(length, len(path)):
                h = (h - path[i - length] * power) % mod
                h = (h * base + path[i]) % mod
                hashes.add(h)
            
            return hashes
        
        def check(length):
            if length == 0:
                return True
            
            base = 100001
            mod = 2**63 - 1
            
            common = get_hashes(paths[0], length, base, mod)
            if not common:
                return False
            
            for i in range(1, len(paths)):
                path_hashes = get_hashes(paths[i], length, base, mod)
                if not path_hashes:
                    return False
                common = common & path_hashes
                if not common:
                    return False
            
            return len(common) > 0
        
        min_len = min(len(path) for path in paths)
        
        left, right = 0, min_len
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result