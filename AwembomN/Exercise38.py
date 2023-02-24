#Create a function that will convert an array containing ASCII codes in a string

import array as arr
def ret_string():
    array = arr.array('i', [77, 97, 110, 105, 110, 99, 104, 97, 114, 103, 101])
    string = ""
    for items in array:
        string += chr(items)
    return string

string = ret_string()
print(string)

'''copying the codes fromt he prevvious exercise and converting it using the chr method'''