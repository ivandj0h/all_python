# Python3 Program to check whether the String or charracter Array is palindromic or not
# Create function that take in put as parameters

# Pseudocode
# n := size of nums
# reset is_palindrome
# i := 0
# while i <= quotient of (n / 2) and n is not 0, do
# if nums[i] is not same as nums[n - i - 1], then
# set is_palindrome
# come out from the loop
# i := i + 1
# if is_palindrome is set, then
# return False
# otherwise,
# return True


def palindrome(input):
    n = len(input)
    is_palindrome = 0
    i = 0
    while i <= n // 2 and n != 0:
        if input[i] != input[n - i - 1]:
            is_palindrome = 1
            break
        i += 1
    if is_palindrome == 1:
        return f'is not palindrome'
    else:
        return f'is palindrome'


print(palindrome(['k', 'o', 'd', 'o', 'k']))
