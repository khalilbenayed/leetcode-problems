decimals = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
elevenToNineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                    "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
magnitude_names = ["thousand", "million", "billion", "trillion", "quadrilion"]


def recursiveSolution(n):
    if n >= 1000000000000000000:
        return "we can't process this number"

    if n < 10:
        return decimals[n]
    elif n < 20:
        return elevenToNineteen[n - 10]
    elif n < 100:
        return tens[int(n / 10) - 2] + " " + recursiveSolution(n % 10)
    elif n < 1000:
        return recursiveSolution(int(n / 100)) + " hundred " + recursiveSolution(n % 100)
    else:
        n_length = len(str(n))
        magnitude = 10 ** (int((n_length - 1) / 3) * 3)

        return recursiveSolution(int(n / magnitude)) + " " + magnitude_names[
            int((n_length - 4) / 3)] + " " + recursiveSolution(int(n % magnitude))