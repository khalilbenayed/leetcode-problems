def solution(a):
    b = []
    for i in a:
        if i > 0:
            b.append(i)

    for i in range(0, len(b)):
        if abs(b[i]) - 1 < len(b) and b[abs(b[i]) - 1] > 0:
            b[abs(b[i]) - 1] = -b[abs(b[i]) - 1]

    for j in range(0,len(b)):
        if b[j] > 0:
            return j+1
    return len(b) + 1

a = [1,3,5,2]
print(solution(a))