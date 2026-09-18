colors = ['red', 'green', 'purple', 'crimson', 'blue', 'blue', 'yellow', 'blue']

item = input("  en ur col : ")

if item in colors:
    print("tedad:", colors.count(item))
    print("num index:", colors.index(item))
else:
    print("The desired color doesnt exist")
print (50*"=")
word = input("en ur harf: ")

vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print("harf seda dar:", count)
print (50*"=")
a = int(input("Fnum: "))
b = int(input("Snum: "))

for num in range(a, b + 1):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print(num)
print (50*"=")
sum = 0

for i in range(1, 1001):
    if i % 2 == 0:
        sum += i

print(sum)
print (50*"=")
numbers = [2, 4, 2, 7, 4, 9, 7, 10, 7]

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print(new_list)

numbers = [12, 45, 7, 89, 34, 67, 23]

max1 = numbers[0]
max2 = numbers[0]
print (50*"=")
for i in numbers:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2:
        max2 = i

print(max2)

number = int(input(" en ur num: "))

sum = 0
print (50*"=")
while number > 0:
    digit = number % 10
    sum += digit
    number //= 10

print(sum)