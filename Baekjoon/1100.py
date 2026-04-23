import sys
input = sys.stdin.readline

def main():
    board = []
    answer = 0
    for _ in range(8):
        board.append(input().rstrip())
    for i in range(8):
        color = -1 if i%2==0 else 1 # -1: white, 1: black
        for j in range(8):
            if board[i][j]=="F" and color==-1:
                answer += 1
            color*=-1
    print(answer)
main()