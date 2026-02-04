from collections import deque


def bfs(micro, start):
    polygons = [start]
    queue = deque([start])
    visited[start[0]][start[1]] = micro
    while queue:
        r,c = queue.popleft()
        for dr,dc in dirs:
            nr,nc = r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and matrix[nr][nc]==micro and not visited[nr][nc]==micro:
                visited[nr][nc] = micro
                queue.append((nr,nc))
                polygons.append((nr,nc))
    return len(polygons),polygons

def show():
    for row in matrix:
        for col in row:
            print(f"{col:>4}", end="")
        print()


# Input
N, Q = map(int, input().split())
matrix = [[0]*(N) for _ in range(N)]
overlapped = set()
area = dict()
pos = dict()
dirs = [(1,0),(0,1),(-1,0),(0,-1)]

for idx in range(1,Q+1):
    r1,c1,r2,c2 = map(int,input().split())
    area[idx] = (r2-r1)*(c2-c1)
    pos[idx] = [r1,c1,r2,c2]
    
    # Injection
    visited = [[0]*N for _ in range(N)]
    for i in range(c1,c2):
        for j in range(r1,r2):
            if matrix[i][j]!=0:
                overlapped.add(matrix[i][j])
                if area.get(matrix[i][j]) is not None:
                    area[matrix[i][j]] -= 1
            matrix[i][j] = idx
    # print(f"[Just Input]")
    # show()
            
    for micro in overlapped:
        start = (-1,-1)
        delete = False
        did_bfs = False
        full_area = area.get(micro)
        # print(f"[Removing: {micro}], Full area: {full_area}, Pos: {pos[micro]}")
        if full_area>0:
            r1,c1,r2,c2 = pos[micro]
            for i in range(c1,c2):
                for j in range(r1,r2):
                    if matrix[i][j]==micro and not did_bfs:
                        start = (i,j)
                        detected_area,_ = bfs(micro, start)
                        # print(f"Full area: {full_area}, Detected area: {detected_area}")
                        did_bfs = True
                        if full_area!=detected_area:
                            delete = True
                    if matrix[i][j]==micro and delete and did_bfs:
                        matrix[i][j]=0
            if delete:
                del area[micro]
                del pos[micro]
        else:
            del area[micro]
            del pos[micro]
    overlapped = set()
    # print(f"[After Removing]")
    # show()
    # print(pos)
    
    # Transfer      
    visited = [[0]*N for _ in range(N)]                      
    tmp = [[0]*(N) for _ in range(N)]
    remain_area = N*N
    # print(sorted(list(area.items()),key=lambda x: (-x[1],x[0])))
    for micro, full_area in sorted(list(area.items()),key=lambda x: (-x[1],x[0])):
        r1,c1,r2,c2 = pos[micro]
        find = False
        for i in range(c1,c2):
            for j in range(r1,r2):
                if matrix[i][j]==micro:
                    start = (i,j)
                    _,polygons = bfs(micro, start)
                    find = True
                    break
            if find:
                break
        
        min_x,min_y = float("inf"),float("inf")
        max_x,max_y = float("-inf"),float("-inf")
        for y,x in polygons:
            min_x = min(min_x,x)
            min_y = min(min_y,y)
            max_x = max(max_x,x)
            max_y = max(max_y,y)
        new_polygons = []
        for y,x in polygons:
            new_polygons.append((y-min_y,x-min_x))
        
        final_polygons = []
        possible = False
        # if micro==35:
        #     print(f"Micro {micro}")
        #     for row in tmp:
        #         for col in row:
        #             print(f"{col:>4}", end="")
        #         print()
        for i in range(N):
            for j in range(N):
                # if tmp[j][i]==0:
                for y,x in new_polygons:
                    if 0<=y+j<N and 0<=x+i<N and tmp[y+j][x+i]==0:
                        final_polygons.append((y+j,x+i))
                    else:
                        final_polygons = []
                        break     
                # if micro==35:
                #     print(j,i,final_polygons,new_polygons)
                if len(final_polygons)==len(new_polygons):
                    min_x,min_y = float("inf"),float("inf")
                    max_x,max_y = float("-inf"),float("-inf")
                    for y,x in final_polygons:
                        tmp[y][x]=micro
                        min_x = min(min_x,x)
                        min_y = min(min_y,y)
                        max_x = max(max_x,x)
                        max_y = max(max_y,y)
                    area[micro]=len(final_polygons)
                    pos[micro]=(min_x,min_y,max_x+1,max_y+1)
                    possible = True
                if possible:
                    break
            if possible:
                break
        if not possible:
            del area[micro]
            del pos[micro]
    matrix = tmp
    # print(f"[After Transfer]")
    # show()
    # print(pos)
                     
    # Caculate
    graph = [[0]*(max(area.keys())+1) for _ in range(max(area.keys())+1)]
    answer = 0
    for micro,(x1,y1,x2,y2) in pos.items():
        for i in range(y1,y2):
            if 0<=x1-1<N:
                # left
                if matrix[i][x1-1]!=0 and matrix[i][x1-1]!=micro and matrix[i][x1]==micro and not graph[micro][matrix[i][x1-1]]:
                    graph[matrix[i][x1-1]][micro]=1
                    graph[micro][matrix[i][x1-1]]=1
                    answer += (area[micro]*area[matrix[i][x1-1]])
            if 0<=x2+1<N:
                # right
                if matrix[i][x2+1]!=0 and matrix[i][x2+1]!=micro and matrix[i][x2]==micro and not graph[micro][matrix[i][x2+1]]:
                    graph[matrix[i][x2+1]][micro]=1
                    graph[micro][matrix[i][x2+1]]=1
                    answer += (area[micro]*area[matrix[i][x2+1]])

        for i in range(x1,x2):
            if 0<=y1-1<N:
                # bottom
                if matrix[y1-1][i]!=0 and matrix[y1-1][i]!=micro and matrix[y1][i]==micro and not graph[micro][matrix[y1-1][i]]:
                    graph[matrix[y1-1][i]][micro]=1
                    graph[micro][matrix[y1-1][i]]=1
                    answer += (area[micro]*area[matrix[y1-1][i]])
            if 0<=y2+1<N:
                # bottom
                if matrix[y2+1][i]!=0 and matrix[y2+1][i]!=micro and matrix[y2][i]==micro and not graph[micro][matrix[y2+1][i]]:
                    graph[matrix[y2+1][i]][micro]=1
                    graph[micro][matrix[y2+1][i]]=1
                    answer += (area[micro]*area[matrix[y2+1][i]])
    print(answer)
        