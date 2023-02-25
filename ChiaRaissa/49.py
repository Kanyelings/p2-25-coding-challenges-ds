import random
import array
arr = array.array('B', [1, 2, 3, 4, 5, 6])
print("original array: ", arr)
random.shuffle(arr)
print("Shuffled array: ", arr)