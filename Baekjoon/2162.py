import sys
input = sys.stdin.readline

def main():
    # Input
    N = int(input())
    lines = []
    for i in range(N):
        x1,y1,x2,y2 = map(int,input().split())
        # if x1 > x2:
        #     x1,y1,x2,y2= x2,y2,x1,y1
        lines.append((i,((x1,y1,x2,y2))))
    
    # Algorithm - Implementation, UnionFind
    parents = [i for i in range(N)]
    size = [1 for _ in range(N)]
    
    def ccw(x1, y1, x2, y2, x3, y3):
        val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        if val > 0:
            return 1
        elif val < 0:
            return -1
        return 0


    def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
        ab_c = ccw(x1, y1, x2, y2, x3, y3)
        ab_d = ccw(x1, y1, x2, y2, x4, y4)
        cd_a = ccw(x3, y3, x4, y4, x1, y1)
        cd_b = ccw(x3, y3, x4, y4, x2, y2)

        # 일직선 위에 있는 경우
        if ab_c == 0 and ab_d == 0 and cd_a == 0 and cd_b == 0:
            if (x1, y1) > (x2, y2):
                x1, y1, x2, y2 = x2, y2, x1, y1
            if (x3, y3) > (x4, y4):
                x3, y3, x4, y4 = x4, y4, x3, y3
            return (x3, y3) <= (x2, y2) and (x1, y1) <= (x4, y4)

        return ab_c * ab_d <= 0 and cd_a * cd_b <= 0
    
    def find(x):
        if x!=parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(a,b):
        ra,rb = find(a),find(b)
        if ra!=rb:
            if size[ra]<size[rb]:
                ra,rb = rb,ra
            parents[rb] = ra
            size[ra] += size[rb]
            return True
        return False
    
    # print(lines)
    for i in range(N):
        for j in range(i+1,N):
            # print(lines[i],lines[j],is_intersect(*lines[i][1],*lines[j][1]))
            if is_intersect(*lines[i][1],*lines[j][1]):
                union(lines[i][0],lines[j][0])
    
    for i in range(N):
        find(i)
    
    print(len(set(parents)))
    print(max(size))
    
main()