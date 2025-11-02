def solution(n: int) -> int:
    # snoob: next higher with same popcount
    c = n & -n        # lowest set bit
    r = n + c         # ripple carry
    return r | (((n ^ r) >> 2) // c)
