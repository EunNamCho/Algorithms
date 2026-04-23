import sys
input = sys.stdin.readline

def main():
    # Input
    N = input().rstrip()
    
    # Algorithm - Implementation
    msb = True
    for n in N:
        n = int(n)
        if msb:
            print(f"{bin(n)[2:]}",end="")
            msb = False
        else:
            print(f"{bin(n)[2:]:0>3}",end="")

main()