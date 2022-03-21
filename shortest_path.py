def shortest_path(array):
    count = 1
    i = 0
    while i < len(array):
        if i+array[i] >= len(array):
            return count+1

        best_choice = array[i+1]
        reach = i+array[best_choice]
        for j in range(i+2, i+array[i]+1):
            if i+array[j] > reach:
                best_choice = j
                reach = i+array[j]

        i = best_choice
        count += 1

    return count


array = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9,1,2,3,4,5,6,7,1,3,1]

print(shortest_path(array))


