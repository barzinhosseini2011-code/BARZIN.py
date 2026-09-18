number1 = int(input("whats your fnum"))
number2 = int(input("whats your snum"))
numbers = []
if number1 < number2:
    for i in range(number1 + 1, number2):
        numbers.append(i)
else:
    for i in range(number2 + 1, number1):
        numbers.append(i)
print(numbers)
print("=" *50)
colors = ["red" , "green" , "purple" , "yellow" , "crimson" , "white" , "black" , "pink" ]
new_list = []
for i in range(0, len(colors), 2):
    new_list.append(colors[i:i+2])
print(new_list)
print("=" *50)
num = int(input("whats your number????"))

while num > 0:
    print(num % 10, end="")
    num = num // 10
print("=" *50)
num1 = int(input(" fnum: "))
num2 = int(input(" snum: "))

while num1 <= num2:

    count = 0
    i = 1

    while i <= num1:
        if num1 % i == 0:
            count += 1
        i += 1

    if count == 2:
        print(num1)

    num1 += 1
print("=" *50)
number = int(input("please enter a number : "))

a = 0
b = 1

if number <= 2:
    print(number - 1) 
else:
    for i in range(2, number):
        c = a + b
        a = b
        b = c
        print(c, end=" ")
print("=" *50)

F = int(input("whats your number ??????????:"))

fibon = [0, 1]

i = 2

while i < F:
    fibon.append(fibon[i - 1] + fibon[i - 2])
    i += 1

print(fibon)