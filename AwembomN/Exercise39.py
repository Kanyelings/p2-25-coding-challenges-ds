#Implementing the Caesar cypher

def Caesar_cypher():
    string = input("Enter a string you want to use: ")
    string = ','.join(string)
    string = string.split(',')
    Nstring = ""
    for items in string:
        Nstring += chr(ord(items) + 3)
    return Nstring

answer = Caesar_cypher()
print(answer)

'''the caesar cypher is an encription format whare every letter
is change to the letter 3 charracters ahead of it, so i used the 
chr and ord methods to play around to increased that'''

