from typing import List

def solution(brown: int, yellow: int) -> List[int]:
    answer = []
    if yellow==1 and brown==8:
        return [3,3]
    for i in range(1, yellow//2+1):
        q,r = divmod(yellow,i)
        if r==0:
            r,c = i,q
            if ((c+2)*2+2*r)==brown:
                return [c+2,r+2]

if __name__=="__main__":
    print(solution(10,2))