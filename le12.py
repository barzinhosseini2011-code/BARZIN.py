def divide(a, b):
    if a < b:
        return 0
    return 1 + divide(a - b, b)

print(divide(17, 5))
print (50*"*")
def sum_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))
print (50*"*")
def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum

numbers = [12, 7, 25, 3, 19]

print(find_max(numbers))
