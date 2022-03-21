def word_frequency(string):
    words = string.split(' ')
    map = {}
    for word in words:
        if word in map:
            map[word] += 1
        else:
            map[word] = 1

    output = []
    for key, value in map.iteritems():
        output.append({
            'word': key,
            'frequency': value,
        })
    print(output)

word_frequency('My name in in Khalil.')