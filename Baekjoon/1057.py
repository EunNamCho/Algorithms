import sys
input = sys.stdin.readline

def main():
    # Input
    N, a, b = map(int, input().split())
    
    # Algorithm - BinaryTree
    a -= 1
    b -= 1
    
    round_count = 0
    while a != b:
        a //= 2
        b //= 2
        round_count += 1
        
    print(round_count)
    
main()