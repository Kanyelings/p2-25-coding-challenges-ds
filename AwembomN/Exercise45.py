'''Create a function to calculate the sum of all the numbers in a jagged array
(contains numbers or other arrays of numbers on an unlimited number of
levels)'''

def sum_jarray(array):
    max = 0
    for i in range(len(array)):
        #checking for data type of every element in array
        if type(array[i]) == int:
                max += array[i]
        else:
            for items in array[i]:
                    max += items
    return max

answer = sum_jarray([1,2, [4,5,7,9,2], 5, 6, [76,5,4,2,8], [4,6], 6])
print(answer)