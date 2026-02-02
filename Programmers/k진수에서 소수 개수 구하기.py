def solution(n, k):
    answer = 0

    # transform
    digits = []
    while n:
        q,r = divmod(n, k)
        digits.append(r)
        n = q
    digits.reverse()
    digits = ''.join(map(str, digits))

    # split by '0'
    candidates = digits.split('0')

    # judge prime
    for candidate in candidates:
        is_prime = True
        if candidate!="":
            candidate = int(candidate)
            if candidate < 2:
                continue
            for i in range(2, int(candidate**0.5)+1):
                if candidate % i == 0:
                    is_prime = False
                    break
            if is_prime:
                answer+=1

    return answer