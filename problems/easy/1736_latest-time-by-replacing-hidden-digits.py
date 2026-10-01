class Solution:
    def maximumTime(self, time: str) -> str:
        chars = list(time)
        # Hour tens
        if chars[0] == '?':
            if chars[1] == '?' or chars[1] <= '3':
                chars[0] = '2'
            else:
                chars[0] = '1'
        # Hour ones
        if chars[1] == '?':
            if chars[0] == '2':
                chars[1] = '3'
            else:
                chars[1] = '9'
        # Minute tens
        if chars[3] == '?':
            chars[3] = '5'
        # Minute ones
        if chars[4] == '?':
            chars[4] = '9'
        return ''.join(chars)