'''Create a function that will receive a bi-dimensional array as argument and a
number and will extract as a unidimensional array the column specified by the
number'''

def xtraction(array, number):
    if number > len(array):
        print("number is out of range of array")
        return "end"
    else:
        return array[number]

answer = xtraction([1,2, [2,4,5,6], 4, 6], 2)
print(answer)

#use list to do it, sincerely could not find how to create a bidimensional array in
#python after extensice research