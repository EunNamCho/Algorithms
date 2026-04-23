import sys
from typing import List
input = sys.stdin.readline

def main():
    # Input
    N, M = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    # Algorithm - BackTracking
    visited = [False]*N
    permutations = set()
    
    def back(permutation: List) -> None:
        if len(permutation)==M:
            permutations.add(tuple(permutation))
            return
        
        for idx, number in enumerate(sequence):
            if not visited[idx]:
                visited[idx] = True
                permutation.append(number)
                back(permutation)
                permutation.pop()
                visited[idx] = False
    
    back([])
    for permutation in sorted(permutations):
        print(" ".join(map(str,permutation)))

main()