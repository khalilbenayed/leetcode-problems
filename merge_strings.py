def  MergeStrings(strings):
    result = ''
    for string in strings:
        sorted_string = ''.join(sorted(string))
        new_result = ''
        i, j = 0,0
        while i<len(result) and j<len(sorted_string):
            if result[i] < sorted_string[j]:
                new_result += result[i]
                i += 1
            else:
                new_result += sorted_string[j]
                j+=1
        if i < len(result):
            new_result += result[i:]
        elif j < len(sorted_string):
            new_result += sorted_string[j:]
        result = new_result
    return result

print(MergeStrings(['greeneggs', 'ham', 'sam', 'i', 'am']))