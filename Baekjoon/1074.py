import sys
input = sys.stdin.readline

# Input
N, r, c = map(int, input().split())

# Algorithm - Implementation
r1,c1,r2,c2 = 0,0,2**N-1,2**N-1
stack = [[r1,c1,r2,c2]]
answer = 0

while stack:
    # print("stack: ", stack)
    r1,c1,r2,c2 = stack.pop()
    size = (r2-r1+1)*(c2-c1+1)
    if size>4:
        half_r, half_c = (r2-r1)//2, (c2-c1)//2
        squares = [
            [r1,c1,half_r,half_c],
            [r1,half_c+1,half_r,c2],
            [half_r+1,c1,r2,half_c],
            [half_r+1,half_c+1,r2,c2]
        ]
        
        # print(squares)
        for idx, (r1,c1,r2,c2) in enumerate(squares):
            if r1<=r<=r2 and c1<=c<=c2:
                # print("SQUARE: ", [r1,c1,r2,c2], idx, (idx)*((2**(N-1))**2))
                r, c = r-r1, c-c1
                r1,c1,r2,c2 = r1-r1,c1-c1,r2-r1,c2-c1
                answer += (idx)*((2**(N-1))**2)
                stack.append([r1,c1,r2,c2])
                N -= 1
                # print("NORM APPEND: ", [r1,c1,r2,c2], [r,c])
                
    
    elif size==4:
        if r==0 and c==0:
            answer += 1
        elif r==0 and c==1:
            answer += 2
        elif r==1 and c==0:
            answer += 3
        elif r==1 and c==1:
            answer += 4
            
print(answer-1)