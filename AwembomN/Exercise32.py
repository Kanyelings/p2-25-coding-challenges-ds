#Creatimg a function that will capitalize the first letter of each word in a text

def capitalizing_first_letter(text):
    list = text.split()
    Nlist = []
    for items in list:
        Nlist.append((items[0].upper()) + items[1::])
    return " ".join(Nlist)
answer = capitalizing_first_letter("the great men come for a reason and they keep moving no matter what")
print(answer)

