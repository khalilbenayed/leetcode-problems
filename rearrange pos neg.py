import json

def rearrange(array):
    n = -1
    for i in range(0, len(array)):
        if array[i] < 0:
            n += 1
            array[i], array[n] = array[n], array[i]

    neg = 0
    pos = n+1
    size = len(array)
    while neg < pos < size and array[neg] < 0:
        array[neg], array[pos] = array[pos], array[neg]
        neg += 2
        pos += 1

    return array


array = [1,-1,-2,4,50,-30, 40, 100]
array2 = [-1, -2, -3, -4, 1, 2]

"""
2, -2, -3, -4, 1 -1

"""

print(json.dumps(rearrange(array)))


