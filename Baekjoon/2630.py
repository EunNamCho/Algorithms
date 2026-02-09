import sys
input = sys.stdin.readline

# Input
matrix = []
N = int(input())
for _ in range(N):
    matrix.append(list(map(int,input().split())))
    
# Algorithm - Implementation
def check(r1,c1,r2,c2):
    color = matrix[r1][c1]
    for r in range(r1,r2):
        for c in range(c1,c2):
            if color!=matrix[r][c]:
                return "F"
    return "B" if color==1 else "W"

def divide(r1,c1,r2,c2):
    center_r, center_c = int((r1+r2)/2+0.5), int((c1+c2)/2+0.5)
    squares = [
        [r1,c1,center_r,center_c],
        [r1,center_c,center_r,c2],
        [center_r,c1,r2,center_c],
        [center_r,center_c,r2,c2]
    ]
    return squares

squares = [[0,0,N,N]]
white, blue = 0, 0
while squares:
    square = squares.pop()
    color = check(*square)
    if color=="B":
        blue+=1
    elif color=="W":
        white+=1
    elif color=="F":
        for s in divide(*square):
            squares.append(s)
            
print(white)
print(blue)