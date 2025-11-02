def solution(s: str) -> int:
    stack = []
    push, pop = stack.append, stack.pop  # 속성 조회 캐싱(미세 최적화)
    for ch in s:
        if stack and stack[-1] == ch:
            pop()
        else:
            push(ch)
    return 1 if not stack else 0
