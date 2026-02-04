import random

# tgt = random.randint(1,100)
tgt=100
print(tgt)
upper,lower=100,1
ops = 0
while lower<=upper:
    mid = (upper+lower)//2
    if tgt==mid:
        break
    elif tgt>mid:
        lower=mid+1
    else:
        upper=mid-1
    ops+=1
print(tgt, ops, mid)