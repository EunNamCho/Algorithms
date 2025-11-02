from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    matrix = [[0]*101 for _ in range(101)]
    visited = [[0]*101 for _ in range(101)]
    queue = deque([(2*characterX,2*characterY)])
    visited[2*characterY][2*characterX] = 1
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
            
    for i,r in enumerate(rectangle):
        lbx,lby,rtx,rty = r
        for j in range(2*lbx,2*rtx+1):
            for k in range(2*lby,2*rty+1):
                matrix[k][j] = 1

    for i,r in enumerate(rectangle):
        lbx,lby,rtx,rty = r
        for j in range(2*lbx+1,2*rtx):
            for k in range(2*lby+1,2*rty):
                matrix[k][j] = 0
    
    while queue:
        x,y = queue.pop()
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if 1<=nx<=100 and 1<=ny<=100 and matrix[ny][nx] and not visited[ny][nx]:
                queue.appendleft((nx,ny))
                visited[ny][nx] = visited[y][x]+1
                
    # for row in matrix:
    #     for col in row:
    #         print(f"{col:>2}", end=" ")
    #     print()
    # print("="*50)
    # for row in visited:
    #     for col in row:
    #         print(f"{col:>2}", end=" ")
    #     print()
    
    return (visited[itemY*2][itemX*2]-1)//2

if __name__=="__main__":
    print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1,3,7,8))