"""
주의사항:
    1. 개미집 정찰
    2. 철거는 valid dict로 관리하자.
"""

# Input
Q = int(input())
antVillage = []
valid = []
for _ in range(Q):
    action = list(map(int,input().split()))
    if action[0]==100:
        antVillage = action[2:]
        valid = [True]*len(antVillage)
        # print(antVillage)
        # print(valid)
    elif action[0]==200:
        antVillage.append(action[1])
        valid.append(True)
    elif action[0]==300:
        valid[action[1]] = False
    elif action[0]==400:
        lowerBound = 0
        upperBound = 1000000000
        while lowerBound<=upperBound:
            down = True
            startidx = 0
            ant = action[1]-1
            midTime = (lowerBound+upperBound)//2
            tmpTime = midTime
            print(f"midTime: {midTime}, Upper: {upperBound}, Lower: {lowerBound}")
            for i,pos in enumerate(antVillage):
                if valid[i]:
                    if i==startidx:
                        continue
                    else:
                        print(f"{i}th Home, Remaining Ant: {ant}, tmpTime: {tmpTime}")
                        if (tmpTime-(antVillage[i]-antVillage[i-1]))<0:
                            if ant>0:
                                ant-=1
                                startidx = i+1
                                tmpTime = midTime
                            else:
                                down = False
                                break
                        else:
                            tmpTime-=(antVillage[i]-antVillage[i-1])
                            down = True
            print(f"Down: {down}, tmpTime: {tmpTime}, Ant: {ant}")
            if down:
                upperBound=midTime-1
            else:
                lowerBound=midTime+1
        print(midTime)
            
            
            