import json
def find_triplets(array):
    result = []
    for i in range(len(array)-1):
        dic = {}
        for j in range(i+1,len(array)):
            if -(array[i]+array[j]) in dic.keys():
                triplet = [array[i], array[j], -(array[i]+array[j])]
                result.append(triplet)
            else:
                dic[array[j]]=1

    return result

array = [0, -1, 2, -3, 1]
print(json.dumps(find_triplets(array)))



