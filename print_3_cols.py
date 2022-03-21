def prettyprint(array):
    col1 = []
    col2 = []
    col3 = []
    length = len(array)/3
    col1_length = length + 1 if len(array) % 3 != 0 else length
    col2_length = length + 1 if len(array) % 3 == 2 else length
    for i in range(length):
        col1.append(array[i])
        col2.append(array[i+col1_length])
        col3.append(array[i+col1_length+col2_length])

    if col1_length != length:
        col1.append(array[col1_length-1])

    if col2_length != length:
        col2.append(array[col1_length+col2_length-1])

    for i in range(length):
        print col1[i], col2[i], col3[i]

    if col1_length != length:
        if col2_length != length:
            print col1[-1], col2[-1]
        else:
            print col1[-1]


array = [1,2,3,4,5,6,7,8,9,0,10]

prettyprint(array)