import sys
from collections import deque
input = sys.stdin.readline

def main():
    # Input
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        
        # Algorithm - BFS
        queue = deque([A])
        dist = {A: ""}
        
        while queue:
            number = queue.popleft()
            for operation in ["D", "S", "L", "R"]:
                if operation=="D":
                    new_number = (number*2)%10000
                elif operation=="S":
                    new_number = (number-1)%10000
                elif operation=="L":
                    new_number = f"{number:0>4}"
                    new_number = new_number[1:]+new_number[0]
                    new_number = int(new_number)
                elif operation=="R":
                    new_number = f"{number:0>4}"
                    new_number = new_number[-1]+new_number[:-1]
                    new_number = int(new_number)
                    
                if dist.get(new_number) is None:
                    dist[new_number] = dist[number]+operation
                    queue.append(new_number)
            if dist.get(B) is not None:
                break        
        print(dist[B])
        
main()