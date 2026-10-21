class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        digit = [0] * 10

        digit[0] = cnt[ord('z') - ord('a')]
        digit[2] = cnt[ord('w') - ord('a')]
        digit[4] = cnt[ord('u') - ord('a')]
        digit[6] = cnt[ord('x') - ord('a')]
        digit[8] = cnt[ord('g') - ord('a')]

        digit[3] = cnt[ord('h') - ord('a')] - digit[8]
        digit[5] = cnt[ord('f') - ord('a')] - digit[4]
        digit[7] = cnt[ord('s') - ord('a')] - digit[6]
        digit[1] = cnt[ord('o') - ord('a')] - digit[0] - digit[2] - digit[4]
        digit[9] = cnt[ord('i') - ord('a')] - digit[5] - digit[6] - digit[8]

        return ''.join(str(d) * digit[d] for d in range(10))