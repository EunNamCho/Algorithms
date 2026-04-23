import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

def main():
    # Input
    N, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    stopover1, stopover2 = map(int,input().split())
    
    # Algorithm - Daikstra
    def get_dist(src,dst):
        dist=[float("inf")]*(N+1)
        dist[src] = 0
        heap = [(0,src)]
        
        while heap:
            cur_dist, src = heapq.heappop(heap)
            
            if cur_dist > dist[src]:
                continue
            if src==dst:
                break
            
            for neighbor, weight in graph[src]:
                new_dist = weight+dist[src]
                if new_dist<dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap,(new_dist,neighbor))
        
        return dist[dst] if dist[dst]!=float("inf") else -1

    answer1, answer2 = 0, 0
    for src, dst in [(1,stopover1),(stopover1,stopover2),(stopover2,N)]:
        dist = get_dist(src,dst)
        if dist==-1:
            answer1 = -1
            break
        answer1 += dist
    for src, dst in [(1,stopover2),(stopover2,stopover1),(stopover1,N)]:
        dist = get_dist(src,dst)
        if dist==-1:
            answer2 = -1
            break
        answer2 += dist
    if answer1==-1 and answer2!=-1:
        print(answer2)
    elif answer1!=-1 and answer2==-1:
        print(answer1)
    else:
        print(min(answer1,answer2))
    
main()
            
    