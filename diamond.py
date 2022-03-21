def print_diamond(n):
    output = ''
    for i in range(1, n+1):
        new_i = i if i <= (n+1)/2 else n-i+1
        for j in range((n+1)/2-new_i+1):
            output += ' '
        for j in range(1, new_i+1):
            output += str(j)
        for j in range(1, new_i):
            output += str(new_i-j)
        output += '\n'
    print(output)


print_diamond(51)
