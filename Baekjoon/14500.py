import sys
from typing import Tuple, List
input = sys.stdin.readline

def main():
    # Input
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    # Algorithm - BruteForce + Implementation
    def normalize(shape: List) -> Tuple[List]:
        min_x, min_y = float("inf"), float("inf")
        for x,y in shape:
            min_x = min(min_x,x)
            min_y = min(min_y,y)
        
        norm_shape = []
        for x,y in shape:
            norm_shape.append((x-min_x, y-min_y))
        norm_shape.sort()
        return tuple(norm_shape)

    def rotation(shape: List) -> Tuple[List]:
        # x=y, y=-x
        rot_shape = []
        for x,y in shape:
            rot_shape.append((y,-x))
        return normalize(rot_shape)
    
    def y_reflect(shape: List) -> Tuple[List]:
        # x=-x, y=y
        ref_shape = []
        for x,y in shape:
            ref_shape.append((-x,y))
        return normalize(ref_shape)

    basis = [
        [(0,0),(0,1),(0,2),(0,3)], # ㅡ
        [(0,0),(0,1),(1,1),(1,0)], # ㅁ
        [(0,0),(1,0),(2,0),(2,1)], # L
        [(0,0),(1,0),(1,1),(2,1)], # Z
        [(0,0),(0,1),(0,2),(1,1)], # ㅜ
    ]
    
    tetrominos = set()
    for base in basis:
        # rotation
        for i in range(4):
            base = rotation(base)
            tetrominos.add(base)
        
        # reflect then rotate
        base = y_reflect(base)
        for i in range(4):
            base = rotation(base)
            tetrominos.add(base)
    
    max_point = 0
    for row in range(N):
        for col in range(M):
            for tetro in tetrominos:
                tmp = 0
                out_of_range = False
                for r,c in tetro:
                    nr,nc = r+row, c+col
                    if 0<=nr<N and 0<=nc<M:
                        tmp += matrix[nr][nc]
                    else:
                        out_of_range = True
                        break
                if not out_of_range:
                    max_point = max(max_point, tmp)

    print(max_point)

main()