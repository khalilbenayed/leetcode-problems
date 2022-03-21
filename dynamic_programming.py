

def num_combinations_for_final_score(final_score, individual_play_scores):
    # m[i][j] is the number of combinations to get the final score j using play_scores up to i-1
    m = [[1]+[0]*final_score for _ in individual_play_scores]
    for i, combinations_for_score in enumerate(m):
        for j in range(1, final_score+1):
            without_this_play = m[i-1][j] if i >= 1 else 0
            with_this_play = m[i][j-individual_play_scores[i]] if j >= individual_play_scores[i] else 0
            m[i][j] = with_this_play + without_this_play
    return m[-1][-1]


def levenshtein_distance(w_1, w_2):
    # m[i][j] is the levenshtein distance between w_1[:i] and w_2[:j]
    m = [[0]*len(w_2) for _ in w_1]
    for i in range(len(w_1)):
        m[i][0] = i
    for i in range(len(w_2)):
        m[0][i] = i

    print(m)
    for i in range(1, len(w_1)):
        for j in range(1, len(w_2)):
            if w_1[i] == w_2[j]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = 1+min([m[i-1][j], m[i][j-1], m[i-1][j-1]])
    print(m)
    return m[-1][-1]


#### PICTURES PROBLEM ####

class Picture:
    def __init__(self, height, width):
        self.height=height
        self.width = width


def position_pictures(pictures, max_width):
    # row_height[i][j] is the height on row having pictures i...j
    # m[i] is the min height of placing pictures 1...i
    row_heights = [[0]*(len(pictures)) for _ in range(len(pictures))]
    for i in range(len(pictures)):
        row_width, row_height = 0, 0
        for j in range(i, len(pictures)):
            row_width += pictures[j].width
            if row_width > max_width:
                row_height = 100000000
            if pictures[j].height > row_height:
                row_height = pictures[j].height
            row_heights[i][j] = row_height

            # for k in range(i, j+1):
            #     row_width += pictures[k].width
            #     if row_width > max_width:
            #         row_height = 100000000
            #     if pictures[k].height > row_height:
            #         row_height = pictures[k].height
    print(row_heights)

    m = [0] * (len(pictures)+1)
    for i in range(len(pictures)):
        min_height = 1000000000
        for j in range(i+1):
            total_height = m[j-1] + row_heights[j][i]
            print(i, j, total_height)
            if total_height < min_height:
                min_height = total_height
        m[i+1] = min_height
        print(min_height)
    print(m)
    return m[len(pictures)-1]


# pics = [Picture(4, 4), Picture(4, 4), Picture(4, 4), Picture(6, 6), Picture(6, 6), Picture(6, 6)]
# print(position_pictures(pics, 19))


#### MAXIMIZE SUM PROBLEMS ####

def maximize_sum(numbers, operations):
    # max_sum[i][j]: max sum for nums i..j
    # min_sum[i][j]: min sum for nums i..j
    max_sum = [[0] * len(numbers) for _ in numbers]
    min_sum = [[0] * len(numbers) for _ in numbers]

    for i in range(len(numbers)):
        max_sum[i][i] = numbers[i]
        min_sum[i][i] = numbers[i]

    for d in range(1, len(numbers)):  # d=j-i
        for i in range(len(numbers)-d):  # i=j-d, j=d+i
            # solve for max_sum[i][i+d] and min_sum[i][i+d]
            best_max, best_min = 0, 10000000
            for k in range(i, i+d):
                temp_max = ((max_sum[i][k-1] if k-1 >= i else 0) +
                            (numbers[k] if k-1 <= i or operations[k-1] == '+' else -numbers[k]) +
                            (max_sum[k+1][i+d] if operations[k] == '+' else -min_sum[k+1][i+d]))

                temp_min = ((min_sum[i][k-1] if k-1 >= i else 0) +
                            (numbers[k] if k-1 <= i or operations[k-1] == '+' else -numbers[k]) +
                            (min_sum[k+1][i+1] if operations[k] == '+' else -min_sum[k+1][i+d]))
                best_max = temp_max if temp_max > best_max else best_max
                best_min = temp_min if temp_min < best_min else best_min

            max_sum[i][i+d] = best_max
            min_sum[i][i+d] = best_min

    return max_sum[0][len(numbers)-1]


# print(maximize_sum([1, 3, 2, 5, 1, 6, 7], ['+', '-', '-', '+', '-', '+']))


#### NUMBER OF WAYS FROM TOP LEFT TO BOTTOM RIGHT OF 2D ARRAY ####

def number_of_ways(height, width):
    # m[x][y] is # of ways to go from top left corner to pt (x,y)
    m = [[0] * width for _ in range(height)]
    for i in range(height):
        m[i][0] = 1
    for j in range(width):
        m[0][j] = 1

    for i in range(1, height):
        for j in range(1, width):
            m[i][j] = m[i-1][j] + m[i][j-1]
    return m[height-1][width-1]


# print(number_of_ways(5, 7))
infty = 2**31


def format_concrete_poetry(words, lines):
    table = {}
    for line_length in lines:
        if line_length in table:
            continue
        m = [[0 for _ in range(len(words) - i)] for i in range(len(words))]
        for i in range(len(words)):
            words_lengths = 0
            for j in range(i, len(words)):
                num_words = j - i + 1
                words_lengths += len(words[j])
                min_spaces = num_words - 1
                if words_lengths + min_spaces > line_length or (num_words == 1 and words_lengths < line_length):
                    m[i][j-i] = infty
                else:
                    m[i][j-i] = int(
                        (line_length - words_lengths) / min_spaces +
                        (1 if (line_length - words_lengths) % min_spaces != 0 else 0))
        table[line_length] = m

    g = [(0, 0)] * (len(words))
    subproblems_needed = {}
    for i in range(len(words)):
        min_max_spaces, best_j, best_num_lines = infty, 0, 0
        for j in range(i):
            num_lines = min(g[j - 1][1]+1 if j > 0 else 1, len(lines))
            last_line = lines[num_lines-1]
            max_spaces = max(g[j-1][0] if j > 0 else 0, table[last_line][j][i-j])
            if max_spaces < min_max_spaces:
                min_max_spaces = max_spaces
                best_j = j
                best_num_lines = num_lines
        g[i] = (min_max_spaces, best_num_lines)
        subproblems_needed[i] = best_j-1 if i > 0 else 0

    subproblem_chain = []
    i = len(words)-1
    while i > 0:
        subproblem_chain.append(i)
        i = subproblems_needed[i]

    print(subproblems_needed)
    print(g)
    # spaces_needed = x * max_spaces + (num_words-1-x) * (max_spaces-1)
    # spaces_needed = x * max_spaces - x * (max_spaces-1) + (num_words-1) * (max_spaces-1)
    # x = spaces_needed - (num_words-1) * (max_spaces-1)
    poem = ''
    for line_num in range(len(subproblem_chain)):
        line_length = lines[line_num]
        last_subproblem = 0 if line_num == 0 else subproblem_chain[len(subproblem_chain)-line_num] + 1
        subproblem = subproblem_chain[len(subproblem_chain)-line_num-1]
        spaces_needed = line_length
        for word_num in range(last_subproblem, subproblem+1):
            spaces_needed -= len(words[word_num])
        max_spaces = table[line_length][last_subproblem][subproblem-last_subproblem]
        num_words = subproblem+1-last_subproblem
        no_times_with_max_spaces = spaces_needed - (num_words-1) * (max_spaces-1)

        # print(last_subproblem, subproblem, line_length, spaces_needed, max_spaces, num_words, no_times_with_max_spaces)

        for word_num in range(last_subproblem, subproblem):
            poem += words[word_num] + ' ' * (max_spaces - 1)
            if word_num - last_subproblem < no_times_with_max_spaces:
                poem += ' '
        poem += words[subproblem] + ('\n' if line_num < len(subproblem_chain) - 1 else '')
    return poem


words = "a a a a a a a a".split(" ")
lines = [6, 6, 6, 6]
# words = 'khalil ben ayed rocks'.split(" ")
# lines = [15, 13]
# words = "The number e is of eminent importance in mathematics, alongside 0, 1, " +\
#         "pi and i. All five of these numbers play important and recurring roles " +\
#         "across mathematics, and are the five constants appearing in one formulation " +\
#         "of Euler’s identity. Like the constant pi, e is irrational: it is not " +\
#         "a ratio of integers. Also like pi, e is transcendental: it is not a " +\
#         "root of any non-zero polynomial with rational coefficients."
# words = words.split(" ")
# lines = [50, 50, 26, 26, 47, 47, 26, 26, 51, 51, 51]
print(format_concrete_poetry(words, lines))
