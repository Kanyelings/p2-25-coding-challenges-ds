#Shuffle an array of strings

import random
strings = "MagicalPeopleExist"
array = ",".join(strings)
array = array.split(",")
list = []
for i in range(len(array)):
    #generating random number to shuffle
    number = random.randint(0, len(array) - 1)
    #while loop to check if random number has already been generated
    while number in list or number == i:
        number = random.randint(0, len(array) - 1)
    list.append(number)
    #switching position of items in array to shuffle
    array[i],array[number] = array[number],array[i]

print(array)

