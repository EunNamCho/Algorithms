import sys
input = sys.stdin.readline

def main():
    # Input
    N, M, H = map(int, input().split())
    matrix = [[0]*(2*N-1) for _ in range(H)]
    for _ in range(M):
        a, b = map(lambda x:int(x)-1, input().split())
        b*=2
        matrix[a][b] = 1
        matrix[a][b+1] = 1
        matrix[a][b+2] = 1
    points = []
    for i in range(N-1):
        for j in range(H):
            if matrix[j][2*i]==0 and matrix[j][2*i+2]==0:
                points.append((j,2*i))
                # matrix[j][2*i]="*"
    L = len(points)
    answer = 4
    
    # Check
    # for row in matrix:
    #     print(*row)
    # print(points)
    
    # Algorithm - BruteForce + Implementation
    dirs = [(0,1),(0,-1)]
    def add(point):
        a,b=point
        nb = b+2
        if nb<2*N-1 and matrix[a][b]==0 and matrix[a][nb]==0:
            matrix[a][b]=1
            matrix[a][nb-1]=1
            matrix[a][nb]=1
            return True
        return False
    def remove(point):
        # print("before")
        # for row in matrix:
        #     print(*row)
        # print()
        a,b = point
        matrix[a][b]=0
        matrix[a][b+1]=0
        matrix[a][b+2]=0
        # print("after")
        # for row in matrix:
        #     print(*row)
        # print()
    def simulate():
        # for row in matrix:
        #     print(*row)
        for i in range(N):
            line = 2*i
            for j in range(H):
                if matrix[j][line]==1:
                    # print(True)
                    for dr,dc in dirs:
                        nr,nc = j+dr,line+dc
                        if 0<=nr<H and 0<=nc<2*N-1 and matrix[nr][nc]==1:
                            line=(nc+dc)
                            break
                # print(f"{i}th col, {j}th row: {line}")
            if i*2!=line:
                # print("fail")
                return False
        # print("success")
        return True
    
    if simulate():
        print(0)
        return

    for i in range(L):
        # print(f"{i}th")
        # for row in matrix:
        #     print(*row)
        # print()
        if add(points[i]): pass#print(f"i:{i}th: {points[i]}")
        else: continue
        # add(points[i])
        if simulate():
            print(1)
            return
        if answer>2:
            for j in range(i+1,L):
                if add(points[j]): pass#print(f"j:{j}th: {points[j]}")
                else: continue
                if simulate():
                    answer=2
                    remove(points[j])
                    break
                if answer>3:
                    for k in range(j+1,L):
                        if add(points[k]): pass#print(f"k:{k}th: {points[k]}")
                        else: continue
                        # print('here')
                        # for row in matrix:
                        #     print(*row)
                        # print()
                        # if i==3 and j==5 and k==9:
                        #     print(i,j,k)
                        #     for row in matrix:
                        #         print(*row)
                        #     # print(simulate())
                        #     # for row in matrix:
                        #     #     print(*row)
                        #     for i in range(N):
                        #         line = 2*i
                        #         for j in range(H):
                        #             if matrix[j][line]==1:
                        #                 # print(True)
                        #                 for dr,dc in dirs:
                        #                     nr,nc = j+dr,line+dc
                        #                     if 0<=nr<H and 0<=nc<2*N-1 and matrix[nr][nc]==1:
                        #                         line=(nc+dc)
                        #                         break
                        #             print(f"{i}th col, {j}th row: {line}")
                        #         if i*2!=line:
                        #             print("fail")
                        #             break
                        #             # return False
                        #     print("success")
                        #     # return True
                                
                        if simulate():
                            answer=3
                            remove(points[k])
                            break
                        else:
                            remove(points[k])
                remove(points[j])
        remove(points[i])
    if answer>3:
        print(-1)
        return
    print(answer)
    
main()