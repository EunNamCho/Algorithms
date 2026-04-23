import sys
from typing import List
input = sys.stdin.readline

def main():
    # Input
    N, M = map(int, input().split())
    sequence = list(map(int, input().split()))
    sequence.sort()
    
    # Algorithm - BackTracking
    visited = [False]*N
    
    def back(combination: List) -> None:
        if len(combination)==M:
            print(" ".join(map(str,combination)))
            return 
        
        for idx, number in enumerate(sequence):
            if not visited[idx]:
                visited[idx] = True
                combination.append(number)
                back(combination)
                combination.pop()
                visited[idx] = False
                
    back([])
    
main()