import array
def sum_of_jagged_array(array):
    result = 0
    for elt in array:
        if elt in array:
            if isinstance(elt, list):
                result += sum(elt)
            else:
                    result += elt
                    return result
            print(sum_of_jagged_array([2, [3,4,2], 5, 2]))
