class Solution:
    def rand10(self):
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
            if idx <= 40:
                return (idx - 1) % 10 + 1