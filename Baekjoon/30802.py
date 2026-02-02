import sys
input = sys.stdin.readline

# input
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

# Algorithm - Implementation
tshirt_bundle, pen_bundle = 0, 0
pen_single = 0
for size in sizes:
    q, r = divmod(size,T)
    if r > 0:
        tshirt_bundle += (q+1)
    else:
        tshirt_bundle += q

pen_bundle, pen_single = divmod(N,P)

print(tshirt_bundle)
print(pen_bundle, pen_single)