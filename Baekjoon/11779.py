import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    M = int(input())
    
    graph = defaultdict(list)
    for _ in range(M):
        a,b,c = map(int, input().split())
        graph[a].append((c,b))
    A,B = map(int, input().split())
    
    # Algorithm - Daikstra
    heap = [(0,A,[A])]
    dists = [[float('inf'),[]] for _ in range(N+1)]
    # for i in range(N):
    #     dists[i][i] = [0,[]]
    while heap:
        cur_dist, cur_node, path = heapq.heappop(heap)
        if cur_dist>dists[cur_node][0]: continue
        if cur_node==B: break
        
        for dist, neighbor in graph[cur_node]:
            new_dist = cur_dist+dist
            if new_dist<dists[neighbor][0]:
                new_path = path+[neighbor]
                dists[neighbor] = [new_dist,new_path]
                heapq.heappush(heap,(new_dist,neighbor,new_path))
    
    print(dists[B][0])
    print(len(dists[B][1]))
    for node in dists[B][1]:
        print(node, end=" ")
# main()


import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    M = int(input())
    
    graph = defaultdict(list)
    for _ in range(M):
        a,b,c = map(int, input().split())
        graph[a].append((c,b))
    A,B = map(int, input().split())
    
    # Algorithm - Daikstra
    prev = [i for i in range(N+1)]
    heap = [(0,A)]
    dists = [float('inf')]*(N+1)

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if cur_dist>dists[cur_node]: continue
        if cur_node==B: break
        
        for dist, neighbor in graph[cur_node]:
            new_dist = cur_dist+dist
            if new_dist<dists[neighbor]:
                prev[neighbor] = cur_node
                dists[neighbor] = new_dist
                heapq.heappush(heap,(new_dist,neighbor))
    
    print(dists[B])
    path = [B]
    cur_node = B
    # print(prev)
    while True:
        prev_node = prev[cur_node]
        if prev_node==A: break
        path.append(prev_node)
        cur_node = prev_node
    path.append(A)
    
    print(len(path))
    for i in range(len(path)-1,-1,-1):
        print(path[i], end=" ")

main()