class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # A power of four is positive, has exactly one 1-bit (power of two),
        # and that bit is at an even position (0, 2, 4, ...).
        # Mask 0x55555555 = 010101...0101 (bits at even positions set)
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0