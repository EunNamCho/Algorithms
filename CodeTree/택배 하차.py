def possible(box, direction):
    ltr,ltc,rbr,rbc = box
    if direction==0:
        # down
        for i in range(ltc,rbc+1):
            # print(20,i,ltr,ltc,rbr,rbc,0<=rbr+1<N and matrix[rbr+1][i]==0)
            if 0<=rbr+1<N and matrix[rbr+1][i]==0:
                pass
            else:
                return False
        return True
    elif direction==1:
        # left
        for i in range(ltr,rbr+1):
            if 0<=ltc-1<N and matrix[i][ltc-1]==0:
                pass
            else:
                return False
        return True
    elif direction==2:
        # right
        for i in range(ltr,rbr+1):
            if 0<=rbc+1<N and matrix[i][rbc+1]==0:
                pass
            else:
                return False
        return True

def move(box,direction):
    ltr,ltc,rbr,rbc = box
    while True:
        if possible((ltr,ltc,rbr,rbc), direction):
            # print(ltr,ltc,rbr,rbc)
            if direction==0:
                # down
                ltr+=1
                rbr+=1
            elif direction==1:
                # left
                ltc-=1
                rbc-=1
            elif direction==2:
                # right
                ltc+=1
                rbc+=1
        else:
            break
    return ltr,ltc,rbr,rbc
            
def put(box,boxid):
    if boxes[boxid]!=0:
        # print(boxid,box)
        ltr0,ltc0,rbr0,rbc0 = boxes[boxid]
        for i in range(ltr0,rbr0+1):
            for j in range(ltc0,rbc0+1):
                matrix[i][j]=0
    ltr,ltc,rbr,rbc = box
    boxes[boxid] = [ltr,ltc,rbr,rbc]
    for i in range(ltr,rbr+1):
        for j in range(ltc,rbc+1):
            matrix[i][j]=boxid
            
def remove(box,boxid):
    ltr,ltc,rbr,rbc = box
    for i in range(ltr,rbr+1):
        for j in range(ltc,rbc+1):
            matrix[i][j]=0
    boxes[boxid] = 0
            
def show():
    for row in matrix:
        for col in row:
            print(f"{col:>2}",end="")
        print()
        
# Input
N, M = map(int, input().split())
matrix = [[0]*N for _ in range(N)]
boxes = [0]*101

# Algorithm - Implementation
# Initailization
for _ in range(M):
    k,h,w,c = map(int, input().split())
    ltr,ltc,rbr,rbc = 0,c-1,0+h-1,c-1+w-1
    # print(k,ltr,ltc,rbr,rbc)
    put(move((ltr,ltc,rbr,rbc),0),k)
# show()
# print(boxes)
# put(move(boxes[2],),1)
# print()
# show()

# Remove
turn = 0
while True:
    even = turn%2==0
    # print(turn, even)
    if even:
        for boxid, box in enumerate(boxes):
            if box==0:
                continue
            if move(box,1)[1]==0:
                remove(box,boxid)
                print(boxid)
                break

    else:
        for boxid, box in enumerate(boxes):
            if box==0:
                continue
            if move(box,2)[3]==N-1:
                remove(box,boxid)
                print(boxid)
                break
    alive = []
    for boxid, box in enumerate(boxes):
        if box != 0:
            ltr,ltc,rbr,rbc = box
            alive.append((rbr, boxid))
    alive.sort(reverse=True)
    for _,boxid in alive:
        put(move(boxes[boxid], 0), boxid)

    # print()
    # show()
    if boxes==[0]*101:
        break
    turn+=1
    