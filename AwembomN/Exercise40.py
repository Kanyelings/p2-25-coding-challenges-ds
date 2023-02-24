#Implement the bubble sort algorithm for an array of numbers

import array as arr
numbers = arr.array("i", [5,4,9,2,1])
j = 1
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)