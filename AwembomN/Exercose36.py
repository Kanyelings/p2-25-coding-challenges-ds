#Create a function that converts a string to an array of characters
import array as arr
def string_array(string):
    array = arr.array("u", [])
    word = ",".join(string)
    word = word.split(",")
    for items in word:
        array.append(items)
    return array

answer = string_array("theme")
print(answer)