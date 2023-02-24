#Deep copy a jagged array with numbers or other arrays in a new array

import copy

jagg_array = [[3,4,6], [45,3,1], [2,3]]
Ncopy = copy.deepcopy(jagg_array)
print(f"this is the new copy of array: {Ncopy}")
#changing values in Ncopy to see whether it changes in the orignal array
Ncopy[0][2] = 15
print(f"this is the new copy after changing a value: {Ncopy}")
print(f"this is the original array: {jagg_array}")