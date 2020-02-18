# https://en.wikipedia.org/wiki/Subset_sum_problem#Polynomial_time_approximate_algorithm

import numpy as np
C = 1e-1


def cal(M, N, Ss):
    step = (C * M) // N
    s = {0}
    slice_to_id = np.zeros(M + 1, dtype=np.int32)
    to_cut = np.zeros(M + 1, dtype=np.int32)
    for i, n_slice in enumerate(Ss):
        if slice_to_id[n_slice] == 0:
            slice_to_id[n_slice] = i
        t = []
        for y in s:
            new_slice = y + n_slice
            if new_slice not in s and new_slice <= M:
                t.append(new_slice)
                if to_cut[new_slice] == 0:
                    to_cut[new_slice] = n_slice
        s.update(t)
        y = 0
        next_s = [0]
        for z in sorted(s):
            if y + step < z:
                y = z
                next_s.append(z)
        s = set(next_s)
    ans = []
    remain = max(s)
    while remain:
        n_slice = to_cut[remain]
        ans.append(slice_to_id[n_slice])
        remain -= n_slice
        slice_to_id[n_slice] += 1
    return ans
