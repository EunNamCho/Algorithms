def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor]==1 and not visited[neighbor]:
                dfs(neighbor)

    visited = [False] * n
    answer = 0
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))