def merge1(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i < len(a):
        return result + a[i:]
    else:
        return result + b[j:]


def merge_sort(a):
    if len(a) <= 1:
        return a
    a1 = a[:len(a)/2]
    a2 = a[len(a)/2:]
    return merge1(merge_sort(a1), merge_sort(a2))


def merge2(a, left, mid, right):
    new_a = []
    l, r = left, mid+1
    while l <= mid and r <= right:
        if a[l] < a[r]:
            new_a.append(a[l])
            l += 1
        else:
            new_a.append(a[r])
            r += 1
    if l <= mid:
        for i in range(l, mid+1):
            new_a.append(a[i])
    elif r <= right:
        for i in range(r, right+1):
            new_a.append(a[i])
    for i in range(left, right+1):
        a[i] = new_a[i-left]


def mergeSort(a):
    current_size = 1

    # Outer loop for traversing Each
    # sub array of current_size
    while current_size < len(a) - 1:

        left = 0
        # Inner loop for merge call
        # in a sub array
        # Each complete Iteration sorts
        # the iterating sub array
        while left < len(a) - 1:
            # mid index = left index of
            # sub array + current sub
            # array size - 1
            mid = left + current_size - 1

            # (False result,True result)
            # [Condition] Can use current_size
            # if 2 * current_size < len(a)-1
            # else len(a)-1
            right = ((2 * current_size + left - 1,
                      len(a) - 1)[2 * current_size
                                  + left - 1 > len(a) - 1])

            # Merge call for each sub array
            merge2(a, left, mid, right)
            left = left + current_size * 2

        # Increasing sub array size by
        # multiple of 2
        current_size = 2 * current_size
    return b


def non_recursive_merge_sort(a):
    current_size = 1
    while current_size < len(a)-1:
        left = 0
        while left < len(a)-1:
            mid = left + current_size - 1 if left+current_size-1 < len(a) else len(a)-1
            right = 2*current_size+left-1 if 2*current_size+left-1 < len(a) else len(a)-1
            print(a, left, mid, right)
            merge2(a, left, mid, right)
            left = left+2*current_size
        current_size = current_size*2
    return a

a = [1,5,1,2,0,6,10,4,-3,12]
b = [2,0,3,-1,7,100,9,11,-10]
print(non_recursive_merge_sort(a))
#print(mergeSort(a))


