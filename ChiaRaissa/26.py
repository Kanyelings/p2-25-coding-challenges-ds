def elements_in_first_array_only(arr1, arr2):
    result = []
    return [elt for elt in arr1 if elt not in arr2]
print(elements_in_first_array_only([1, 2, 3, 4, 6], [ 5, 3, 9, 8, 4]))
