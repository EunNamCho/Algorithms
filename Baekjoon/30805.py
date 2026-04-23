import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    A = list(map(int,input().split()))
    M = int(input())
    B = list(map(int,input().split()))
    answer = []
    
    # Algorithm - Greedy
    a_cnt, b_cnt = defaultdict(deque), defaultdict(deque)
    for i,a in enumerate(A):
        a_cnt[a].append(i)
    for i,b in enumerate(B):
        b_cnt[b].append(i)
    
    pa, pb = 0, 0
    while True:
        update = False
        for i in range(100,0,-1):
            # print(i,pa,pb,a_cnt[i],b_cnt[i])
            while True:
                if a_cnt[i] and b_cnt[i]:
                    ta, tb = a_cnt[i].popleft(), b_cnt[i].popleft()
                    if ta >= pa and tb >= pb:
                        pa = ta
                        pb = tb
                        answer.append(i)
                        update = True
                        break
                    else:
                        if ta >= pa:
                            a_cnt[i].appendleft(ta)
                        if tb >= pb:
                            b_cnt[i].appendleft(tb)     
                else: break
            if update: break
        if not update: break
        
    print(len(answer))
    print(*answer)
                
main()                 
    