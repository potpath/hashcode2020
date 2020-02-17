def cal(M, N, Ss):
    cursum = 0
    maxsum = 0
    begin = 0
    end = 0
    ans = 0, 0
    while end < N:
        while end < N and cursum + Ss[end] <= M:
            cursum += Ss[end]
            end += 1
        if cursum > maxsum:
            ans = begin, end
        cursum -= Ss[begin]
        begin += 1
    return list(range(*ans))
