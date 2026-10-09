def count_letters(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print("Uppercase:", upper)
    print("Lowercase:", lower)

count_letters("Hello World")
#==============================
def sum_list(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

numbers = [10, 9, 9, 6, 5, 20, 11]
print(sum_list(numbers))
#==============================
def multiply_list(numbers):
    result = 1

    for num in numbers:
        result *= num

    return result

numbers = [10, 9, 9, 6, 5, 20, 11]
print(multiply_list(numbers))