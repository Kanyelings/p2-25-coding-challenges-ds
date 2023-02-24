import string
def frequency(string):
    return[[elt, string.count(elt)] for elt in string]
print(frequency("Raissa Chia"))
