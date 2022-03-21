def n_sum(array, start, n, x):
    if n < 2:
        raise Exception()
    if n == 2:
        d = {}
        for i in range(start, len(array)):
            item = array[i]
            if x-item in d:
                return item, x-item
            else:
                d[item] = True
        return False

    for i in range(start, len(array)-n+1):
        item = array[i]
        result = n_sum(array, i+1, n-1, x-item)
        if result is not False:
            return item, result
    return False

a = [2,3,4,5,6]
print(n_sum(a, 0, 4, 17))
