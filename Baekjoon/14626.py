import sys
input = sys.stdin.readline

# input
ISBN = input().strip()

# Algorithm - Implementation
weights = [1,3,1,3,1,3,1,3,1,3,1,3,1]

m = int(ISBN[-1])
unknown_idx = 0
total = 0
for idx,number in enumerate(ISBN[:-1]):
    if number!="*":
        total += int(number)*weights[idx]
    else:
        unknown_idx = idx

for i in range(10):
    if (10-(total+i*weights[unknown_idx])%10)%10==m:
        break

print(i)