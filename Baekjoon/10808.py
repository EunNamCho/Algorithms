import sys

# input
S = sys.stdin.readline().strip()
alphas = [0]*26

for s in S:
    alphas[ord(s)-97] += 1
   
for alpha in alphas:
    print(alpha, end=" ")