import sys

# input
N, M = map(int, sys.stdin.readline())
matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
basis = [
    [(0,0),(0,1),(0,2),(0,3)], #l
    [(0,0),(0,1),(1,0),(1,1)], #O
    [(0,0),(1,0),(2,0),(2,1)], #L
    [(0,0),(1,0),(1,1),(2,1)], #Z
    [(0,0),(0,1),(0,2),(1,1)], #T
]
tetrominos = set()
answer = 0

#algorithm - Implementation
def norm(polygon):
    min_r = min_c = 0
    for p in polygon:
        r,c = p
        min_r = min(min_r,r)
        min_c = min(min_c,c)
        
    for i,p in enumerate(polygon):
        polygon[i] = (p[0]-min_r,p[1]-min_c)
    return polygon

def clock_rotate(polygon):
    # x->-y, y->x ==> c->-r, r->c
    for i,p in enumerate(polygon):
        polygon[i] = (-p[1], p[0])
    polygon=norm(polygon)
    return polygon

def y_reflect(polygon):
    for i,p in enumerate(polygon):
        polygon[i] = (p[0],-p[1])
    polygon=norm(polygon)
    return polygon

def Imple():
    for base in basis:
        tetrominos.add(base)
        tmp = base
        for _ in range(3):
            tmp = clock_rotate(tmp)
            tetrominos.add(tmp)
            
        tmp = y_reflect(base)
        tetrominos.add(tmp)
        for _ in range(3):
            tmp = clock_rotate(tmp)
            tetrominos.add(tmp)
    
    for tetro in tetrominos:
        
            
        