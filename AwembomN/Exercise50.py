#Create a function that will receive n as argument and return an array of n
#random numbers from 1 to n. The numbers should be unique inside the array.

import random
import array as arr
def unique_numbers(n):
    array = arr.array("i", [])
    #defining list range and generating a random samples of list
    li = range(0, n)
    li = random.sample(li, n)
    #adding those uniques numbers into an array
    for items in li:
        array.append(items)
    return array

answer = unique_numbers(15)
print(answer)

