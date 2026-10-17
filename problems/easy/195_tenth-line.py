from typing import Optional

class Solution:
    def tenthLine(self) -> None:
        with open("file.txt", "r") as f:
            for i, line in enumerate(f, start=1):
                if i == 10:
                    print(line, end="")
                    return