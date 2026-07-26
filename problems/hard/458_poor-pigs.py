class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = minutesToTest // minutesToDie
        states = tests + 1
        
        pigs = 0
        while states ** pigs < buckets:
            pigs += 1
        
        return pigs