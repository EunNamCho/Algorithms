import sys
from collections import defaultdict
from math import ceil
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    
    # Algorithm - Implementation
    counts = defaultdict(int)
    for n in str(N):
        if n=="9":
            n="6"
        counts[n]+=1
    
    counts["6"] = ceil(counts["6"]/2)
    print(max(counts.values()))
    
main()