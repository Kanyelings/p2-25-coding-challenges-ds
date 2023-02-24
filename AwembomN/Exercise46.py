#Find the maximum number in a jagged array of numbers or array of numbers

def largestNoIn_jarray(array):
    max = 0
    for i in range(len(array)):
        #checking for data type of every element in array
        if type(array[i]) == int:
            if array[i] > max:
                max = array[i]
        else:
            for items in array[i]:
                if items > max:
                    max = items
    return max

answer = largestNoIn_jarray([1,2, [4,5,7,9,2], 5, 6, [76,5,4,2,8], [4,6], 6])
print(answer)