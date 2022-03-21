def has_a_fake(a, l, r):
    return l < r+1 and reduce(lambda x, y: x + y, a[l:r+1]) != len(a[l:r+1])


def binary_search_first_fake(a, l, r):
    while l <= r:
        m = l + (r - l) / 2
        if has_a_fake(a, l, m - 1):
            r = m - 1
        elif has_a_fake(a, m, m):
            return m
        else:
            l = m + 1


def find_first_fake(a, l):
    bound = 1
    while l+bound < len(a) and not has_a_fake(a, l, l+bound):
        l += bound
        bound = bound * 2
    return binary_search_first_fake(a, l, min(l+bound, len(a)))


def find_all_fakes(a):
    l, d = 0, 0
    fakes = []
    while l < len(a) and has_a_fake(a, l, len(a)):
        i = find_first_fake(a, l)
        fakes.append(i)
        l = i+1
        d += 1
    return d, fakes




a = [0.99,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.99]
print(find_all_fakes(a))
