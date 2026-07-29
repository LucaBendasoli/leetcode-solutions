class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')
        
        max_len = max(len(v1_parts), len(v2_parts))
        
        for i in range(max_len):
            rev1 = int(v1_parts[i]) if i < len(v1_parts) else 0
            rev2 = int(v2_parts[i]) if i < len(v2_parts) else 0
            
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        return 0