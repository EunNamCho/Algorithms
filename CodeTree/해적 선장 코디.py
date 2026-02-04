"""
애매한 지점:
    1. 맨 처음부터 시간이 1시간이 흐른걸로 치나? yes
    2. 장전시간에 발사한 시점도 1시간 지났다고 치나? yes
    3. 함포 교체를 레이지수정으로 하는데, 어젠 반영하나? 그냥 쏠 때? 아니면, 새로운 함포 추가할때?
"""

import heapq 

# input
T = int(input())
N = 0
actives = []
pending = dict()
delays = dict()
valid = dict()
non_actives = dict()



for _ in range(T):
    ops = list(map(int,input().split()))
    if ops[0]==100:
        # 공격 준비
        N = ops[1]
        infos = ops[2:]
        cnt = 0
        while infos:
            r = infos.pop()
            p = infos.pop()
            i = infos.pop()
            valid[i]=-p
            heapq.heappush(actives, (-p,i))
            delays[i] = r
        # print(f"ACTIVES INITAL: {actives}")
        # print(f"DELAY: {delays}")
            
    elif ops[0]==200:
        i = ops[1]
        p = ops[2]
        r = ops[3]
        valid[i]=-p
        heapq.heappush(actives, (-p,i))
        delays[i] = r
        
    elif ops[0]==300:
        i = ops[1]
        p = ops[2]
        valid[i]=-p
        heapq.heappush(actives, (-p,i))
        
    elif ops[0]==400:
        cnt = 0
        total_attack = 0
        total_id = []
        while actives:
            p, i = heapq.heappop(actives)
            if not valid[i]==p:
                continue
            total_attack+=p
            total_id.append(i)
            pending[i] = 0
            non_actives[i] = p
            cnt+=1
            if cnt==5:
                break
        print(-total_attack, len(total_id), " ".join(map(str,total_id)))
        
    for i in pending.keys():
        pending[i]+=1
        if pending[i]==delays[i]:
            p = non_actives[i]
            # del pending[i]
            heapq.heappush(actives,(p,i))
    # print(f"PENDING: {pending}")
    # print(f"ACTIVES: {actives}")
    # print(f"EXCHANGE: {exchange}")
    