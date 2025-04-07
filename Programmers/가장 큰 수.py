def solution(numbers):
    numbers = sorted(list(map(str,numbers)),reverse=True)
    return "".join(numbers)

solution([6, 10, 2])