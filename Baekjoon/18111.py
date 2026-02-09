import sys
input = sys.stdin.readline

# Input
N, M, B = map(int, input().split())
blocks = [0] * 257
max_h = 0
for _ in range(N):
    for height in map(int,input().split()):
        blocks[height] += 1
        max_h = max(max_h, height)
    
# Algorithm - BruteForce
answer_time = float("inf")
answer_height = 0

for tgt_h in range(max_h,-1,-1):
    time_spent = 0
    has_block = B
    possible = True
    
    for height in range(max_h,-1,-1):
        num_blocks = blocks[height]
        cost = (tgt_h - height) * num_blocks
        if cost >= 0:
            if has_block-cost>=0:
                time_spent += cost
                has_block -= cost
            else:
                possible = False
                break
        else:
            time_spent -= cost*2
            has_block -= cost
            
    if possible:
        if time_spent < answer_time:
            answer_time = time_spent
            answer_height = tgt_h
        else:
            break

print(answer_time, answer_height)