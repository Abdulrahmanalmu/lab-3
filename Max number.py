numbers = []

for i in range(10):
    num = int(input("Enter value {}: ".format(i + 1)))
    numbers.append(num)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)
