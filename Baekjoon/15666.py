import sys
from typing import List
input = sys.stdin.readline

def main():
    # Input
    N, M = map(int, input().split())
    sequence = list(map(int,input().split()))
    sequence.sort()
    
    # Algorithm - BackTracking
    combinations = set()
    
    def back(base_idx: int, combination: List) -> None:
        if len(combination)==M:
            combinations.add(tuple(combination))
            return
        
        for idx, number in enumerate(sequence):
            if base_idx > idx:
                continue
            combination.append(number)
            back(idx, combination)
            combination.pop()
            
    back(0, [])
    for combination in sorted(combinations):
        print(" ".join(map(str,combination)))
        
main()
    