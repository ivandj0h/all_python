# Find the missing number in a given list
def getMissingNumber(A):

    # get the array's length
    n = len(A)

    # actual size is `n+1` since a number is missing from the list
    m = n + 1

    # get a sum of integers between 1 and `n+1`
    total = m * (m + 1) // 2

    # the missing number is the difference between the expected sum and
    # the actual sum of integers in the list
    return total - sum(A)


if __name__ == '__main__':

    A = [1, 2, 3, 4, 5, 7, 8, 9, 10]

    print("The missing number is", getMissingNumber(A))
