import sys
import heapq
input = sys.stdin.readline
insert = heapq.heappush
delete = heapq.heappop
write = sys.stdout.write

def main():
    # Input
    T = int(input())
    outputs = []
    
    for _ in range(T):
        K = int(input())
        descent_pq, ascent_pq = [], []
        numbers = dict()
        for _ in range(K):
            # Algorithm - Implementation
            cmd = input().split()
            number = int(cmd[1])
            if cmd[0]=="I":
                if numbers.get(number) is not None:
                    numbers[number]+=1
                else:
                    numbers[number]=1
                insert(ascent_pq, number)
                insert(descent_pq, -number)
            elif cmd[0]=="D":
                if len(numbers)>0:
                    if cmd[1]=="-1":
                        while ascent_pq:
                            number = delete(ascent_pq)
                            if numbers.get(number) is not None:
                                numbers[number]-=1
                                if numbers[number]==0:
                                    del numbers[number]
                                break
                    elif cmd[1]=="1":
                        while descent_pq:
                            number = -delete(descent_pq)
                            if numbers.get(number) is not None:
                                numbers[number]-=1
                                if numbers[number]==0:
                                    del numbers[number]
                                break
        if len(numbers)>0:
            # print(numbers)
            # print(ascent_pq)
            # print(descent_pq)
            while descent_pq:
                number = -delete(descent_pq)
                if numbers.get(number) is not None:
                    break
            print(number, end=" ")
            while ascent_pq:
                number = delete(ascent_pq)
                if numbers.get(number) is not None:
                    break
            print(number)
        else:
            print("EMPTY")
        
                        
main()
