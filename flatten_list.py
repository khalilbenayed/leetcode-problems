def flatten_list(l):
    output = []
    sublists = []
    for i in l:
        while len(sublists) != 0:
            sublist = sublists.pop()
            for j in range(len(sublist)):
                item = sublist[j]
                if isinstance(item, int):
                    output.append(item)
                else:
                    sublists.append(item)
                    sublists.append(sublist[j+1:])
                    break
        if isinstance(i, int):
            output.append(i)
        else:
            sublists.append(i)
    return output


print(flatten_list([1,2,[3,4,[5],6],7]))