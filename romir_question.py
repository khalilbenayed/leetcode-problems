# /*
#  * Complete the 'variantsCount' function below.
#  *
#  * The function is expected to return a LONG_INTEGER.
#  * The function accepts following parameters:
#  *  1. INTEGER n
#  *  2. INTEGER s0
#  *  3. INTEGER k
#  *  4. INTEGER b
#  *  5. INTEGER m
#  *  6. LONG_INTEGER a
#  */
#
# long variantsCount(int n, int s0, int k, int b, int m, long a) {
#
# }


def variants_count(n, s0, k, b, m, a):
    # first produce set of lengths
    s = [0] * n
    s[0] = s0
    for i in range(1, n):
        s[i] = ((k*s[i-1]+b) % m) + 1 + s[i-1]

    count = 0
    # first count # squares
    for i in range(n):
        if s[i]*s[i] <= a:
            count += 1
        else:
            break

    # now number of rectangles
    # array is sorted so can use left and right pointers
    i, j = 0, n-1
    while i < j:
ADS
    return count


print(variants_count(3, 1, 1, 1, 2, 4))
