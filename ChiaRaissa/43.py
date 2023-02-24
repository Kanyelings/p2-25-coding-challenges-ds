def unidimensional(array, num):
    return[row[num] for row in array]
print(unidimensional([[2, 5, 7], [3, 4, 8], [0, 1, 2]], 1))
