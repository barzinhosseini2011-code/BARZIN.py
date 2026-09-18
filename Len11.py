def perfect_number(n):
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum += i

    if sum == n:
        return True
    else:
        return False


print(perfect_number(6))
# **********************************************
def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return reverse


print(reverse_number(1234))
# **********************************************]
def sum_numbers(*numbers):
    sum = 0

    for i in numbers:
        sum += i

    return sum


print(sum_numbers(2, 5, 10, 3))
# **********************************************
