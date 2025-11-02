import sys

# input
N = int(sys.stdin.readline())
TP = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)] # List[Tuple[Ti,Pi]]
answer = 0

#input check
# print(TP)

# algorithm - Back Tracking
def back(day, pay):
    global answer
    if day<N:
        answer = max(answer, pay)
    elif day==N:
        answer = max(answer,pay)
        return
    else:
        return 
    
    next_day = day+(TP[day][0])
    # print("day, pay: ", day, pay)
    # print("next_day: ", next_day)
    # import pdb; pdb.set_trace()
    if next_day<=N:
        back(next_day, pay+TP[day][1])
    back(day+1, pay)
        
back(0,0)
print(answer)
