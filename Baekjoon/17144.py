import sys
input = sys.stdin.readline

def main():
    # Input
    R,C,T = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(R)]
    u_machine, d_machine = (0,0), (0,0)
    for i in range(R):
        if matrix[i][0]==-1:
            u_machine = (i,0)
            d_machine = (i+1,0)
            break
    
    # Algorithm - Implementation
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    def propagate():
        update = [[0]*C for _ in range(R)]
        update[u_machine[0]][u_machine[1]] = -1
        update[d_machine[0]][d_machine[1]] = -1
        for r in range(R):
            for c in range(C):
                if matrix[r][c]>0:
                    # if r==4 and c==6:
                    #     print('here')
                    #     print(matrix[r][c], update[r][c])
                    total = matrix[r][c]
                    division = total//5
                    for dr,dc in dirs:
                        nr,nc = r+dr,c+dc
                        if 0<=nr<R and 0<=nc<C and update[nr][nc]!=-1:
                            update[nr][nc] += division
                            total -= division
                    update[r][c] += total
                    # if r==4 and c==6:
                    #     print('here')
                    #     print(matrix[r][c], update[r][c])
                    #     print(update[r-1][c],update[r+1][c],update[r][c-1],update[r][c+1])
        return update
    
    def blow():
        for r in range(u_machine[0]-2,-1,-1):
            matrix[r+1][0] = matrix[r][0]
            matrix[r][0] = 0
        for c in range(1,C):
            matrix[0][c-1] = matrix[0][c]
            matrix[0][c] = 0
        for r in range(1, u_machine[0]+1):
            matrix[r-1][C-1] = matrix[r][C-1]
            matrix[r][C-1] = 0
        for c in range(C-2,0,-1):
            matrix[u_machine[0]][c+1] = matrix[u_machine[0]][c]
            matrix[u_machine[0]][c] = 0
            
        for r in range(d_machine[0]+2,R):
            matrix[r-1][0] = matrix[r][0]
            matrix[r][0] = 0
        for c in range(1,C):
            matrix[R-1][c-1] = matrix[R-1][c]
            matrix[R-1][c] = 0
        for r in range(R-2,d_machine[0]-1,-1):
            matrix[r+1][C-1] = matrix[r][C-1]
            matrix[r][C-1] = 0
        for c in range(C-2,0,-1):
            matrix[d_machine[0]][c+1] = matrix[d_machine[0]][c]
            matrix[d_machine[0]][c] = 0
    
    for i in range(T):
        matrix = propagate()
        # print(f"{i+1} State - propagate:")
        # for row in matrix:
        #     print(*row)
        # print()
        blow()
        # print(f"{i+1}th State - blow:")
        # for row in matrix:
        #     print(*row)
        # print()
    
    answer = 2
    for row in matrix:
        answer += sum(row)
    print(answer)
    
main()
