def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            total = 0
            for k in range(len(arr1[0])):
                total+=(arr1[i][k]*arr2[k][j])
            tmp.append(total)
        answer.append(tmp)
    return answer

def solution(arr1, arr2):
    arr2_t = list(zip(*arr2))  # 전치 행렬
    return [[sum(a*b for a, b in zip(row, col)) for col in arr2_t] for row in arr1]
