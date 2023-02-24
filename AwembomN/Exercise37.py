#Create a function that will convert a string in an array containing the ASCII codes of
#each character
def ASCII_codes(string):
    import array as crazy
    string = ','.join(string)
    string = string.split(',')
    array = crazy.array("i", [])
    for items in string:
        array.append(ord(items))
    return array

answer = ASCII_codes("Manincharge")
print(answer)
#using the ord function to get the ASCII code of every character