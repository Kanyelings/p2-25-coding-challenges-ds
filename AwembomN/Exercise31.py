#Creating a function that will return the number of words in a text

def no_of_words(text):
    list = text.split()
    count = 0
    for items in list:
        count += 1
    return count

answer = no_of_words("the great men come for a reason and they keep moving no matter what")
print(answer)