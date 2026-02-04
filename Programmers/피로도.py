def solution(k, dungeons):
    answer = -1
    visited = [False]*len(dungeons)
    def back(visited,remain,answer):
        # print(answer)
        for idx, dungeon in enumerate(dungeons):
            least, spent = dungeon
            new_remain = remain - spent
            if not visited[idx] and remain>=least and new_remain>=0:
                visited[idx]=True
                answer = back(visited,remain-spent,answer)
                visited[idx]=False
        return max(answer,sum(visited))
    answer = back(visited,k,answer)
    return answer


def solution(k, dungeons):
    n = len(dungeons)
    used = [False] * n
    best = 0

    def dfs(remain, cnt):
        nonlocal best
        if cnt > best:
            best = cnt
            # 최댓값 n에 도달하면 더 볼 필요 없음 (작은 가지치기)
            if best == n:
                return

        for i, (need, cost) in enumerate(dungeons):
            if not used[i] and remain >= need:
                used[i] = True
                dfs(remain - cost, cnt + 1)
                used[i] = False

    dfs(k, 0)
    return best
