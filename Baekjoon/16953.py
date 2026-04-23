import sys
from collections import deque
input = sys.stdin.readline

def main():
    # Input
    A, B = map(int, input().split())
    
    # Algorithm - BFS
    queue = deque([A])
    dist = {A: 1}
    
    while queue:
        number = queue.popleft()
        
        for operation in [lambda x: 2*x, lambda x: 10*x+1]:
            new_number = operation(number)
            if 1<= new_number<=1e9 and dist.get(new_number) is None:
                dist[new_number] = dist[number]+1
                queue.append(new_number)
                
            if dist.get(B) is not None:
                print(dist.get(B))
                return
    print(-1)
    
main()


def main():
    # Input
    A, B = map(int, input().split())
    
    # Algorithm - Greedy
    answer = 1
    while True:
        q,r = divmod(B,2)
        if r==0:
            B = q
            answer += 1
        else:
            q,r = divmod(B,10)
            if r==1:
                B = q
                answer += 1
            else:
                print(-1)
                return
        if A==B:
            break
        elif A>B:
            print(-1)
            return
    print(answer)
    
main()

