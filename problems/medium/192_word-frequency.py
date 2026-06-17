#!/usr/bin/env python3
import sys
from collections import Counter

def main():
    word_count = Counter()
    
    for line in sys.stdin:
        words = line.split()
        word_count.update(words)
    
    for word, count in sorted(word_count.items(), key=lambda x: -x[1]):
        print(f"{word} {count}")

if __name__ == "__main__":
    main()