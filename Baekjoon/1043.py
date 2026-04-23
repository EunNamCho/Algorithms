import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b, truth):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    # 두 루트 중 하나라도 진실을 아는 집합에 속해있다면, 
    # 합쳐진 집합 전체가 진실을 아는 것으로 처리하기 위해 작은 번호를 부모로 하거나
    # 단순히 합칩니다. (여기서는 아래 로직에서 진실 여부를 다시 체크합니다.)
    if rootA != rootB:
        if rootA in truth:
            parent[rootB] = rootA
        elif rootB in truth:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA

def solve():
    N, M = map(int, input().split())
    # 진실을 아는 사람 정보
    truth_input = list(map(int, input().split()))
    truth_count = truth_input[0]
    
    if truth_count == 0:
        # 진실을 아는 사람이 없으면 모든 파티에서 거짓말 가능
        for _ in range(M): input()
        print(M)
        return

    truth_people = set(truth_input[1:])
    parent = [i for i in range(N + 1)]
    parties = []

    for _ in range(M):
        party_info = list(map(int, input().split()))
        p_count = party_info[0]
        p_members = party_info[1:]
        parties.append(p_members)
        
        # 파티에 참석한 사람들을 하나로 묶음
        for i in range(p_count - 1):
            union(parent, p_members[i], p_members[i+1], truth_people)

    # 진실을 아는 사람들과 연결된 모든 사람을 찾음
    # (루트 노드가 진실을 아는 사람과 연결되어 있는지 확인)
    real_truth = set()
    for person in truth_people:
        real_truth.add(find(parent, person))

    ans = 0
    for party in parties:
        can_lie = True
        for member in party:
            # 해당 멤버의 루트가 진실을 아는 루트와 같다면 거짓말 불가
            if find(parent, member) in real_truth:
                can_lie = False
                break
        if can_lie:
            ans += 1
            
    print(ans)

solve()