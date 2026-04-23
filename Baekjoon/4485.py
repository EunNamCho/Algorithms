import sys
import heapq
input = sys.stdin.readline

# def main():
#     dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    
#     while True:
#         # Input
#         N = int(input())
#         if N==0: break
#         matrix = [list(map(int,input().split())) for _ in range(N)]
        
#         # Algorithm - Daikstra
#         dist = [[float('inf')]*N for _ in range(N)]
#         dist[0][0] = matrix[0][0]
#         heap = [(matrix[0][0],(0,0))]
        
#         while heap:
#             # print(heap)
#             cur_dist,(r,c) = heapq.heappop(heap)
#             if cur_dist>dist[r][c]: continue
#             if (r,c)==(N-1,N-1): break
            
#             for dr,dc in dirs:
#                 nr,nc = dr+r, dc+c
#                 if 0<=nr<N and 0<=nc<N:
#                     new_dist = cur_dist+matrix[nr][nc]
#                     dist[nr][nc] = new_dist
#                     heapq.heappush(heap,(new_dist,(nr,nc)))
#         for row in dist:
#             for col in row:
#                 print(col, end=" ")
#         print()
#         print(dist[N-1][N-1])
        
import sys
import heapq
input = sys.stdin.readline

def main():
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    problem_num = 1

    while True:
        N = int(input())
        if N == 0:
            break

        matrix = [list(map(int, input().split())) for _ in range(N)]

        dist = [[float('inf')] * N for _ in range(N)]
        dist[0][0] = matrix[0][0]
        heap = [(matrix[0][0], 0, 0)]

        while heap:
            cur_dist, r, c = heapq.heappop(heap)

            if cur_dist > dist[r][c]:
                continue

            if (r, c) == (N - 1, N - 1):
                break

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    new_dist = cur_dist + matrix[nr][nc]
                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist
                        heapq.heappush(heap, (new_dist, nr, nc))

        print(f"Problem {problem_num}: {dist[N-1][N-1]}")
        problem_num += 1

main()