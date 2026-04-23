import sys
input = sys.stdin.readline

def main():
    # Input
    N,L = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    
    # Algorithm - Implementation
    for i in range(N):
        # print(f"{i}th row: ")
        flag, cnt = False, 1
        road = True
        for j in range(1,N):
            if matrix[i][j]-matrix[i][j-1]==-1:
                if flag:
                    road = False
                    break
                cnt = 0
                flag = True
            elif matrix[i][j]-matrix[i][j-1]==1:
                if cnt<L:
                    road = False
                    break
                cnt = 0
            elif matrix[i][j]-matrix[i][j-1]==0:
                pass
            else:
                road = False
                break
            cnt+=1
            if flag and cnt==L:
                flag = False
                cnt = 0
        if flag:
            road = False
        if road:
            answer += 1
        # print(f"road: {road}, flag: {flag}, cnt: {cnt}")
        
        # print(f"{i}th col: ")
        flag, cnt = False, 1
        road = True
        for j in range(1,N):
            if matrix[j][i]-matrix[j-1][i]==-1:
                if flag:
                    road = False
                    break
                cnt = 0
                flag = True
            elif matrix[j][i]-matrix[j-1][i]==1:
                if cnt<L:
                    road = False
                    break
                cnt = 0
            elif matrix[j][i]-matrix[j-1][i]==0:
                    pass
            else:
                road = False
                break
            cnt+=1
            if flag and cnt==L:
                flag = False
                cnt = 0
        if flag:
            road = False
        if road:
            answer += 1
        # print(f"road: {road}, flag: {flag}, cnt: {cnt}")
    
    print(answer)
    
main()