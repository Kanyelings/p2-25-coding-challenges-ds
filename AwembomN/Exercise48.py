#Create a function to return the longest word in a string
def get_longest_word(string):
    L_word = ''
    string = string.split()
    for words in string:
        #compare the lenth of different words
        if len(words) > len(L_word):
            L_word = words

    return L_word

answer = get_longest_word("the great men come for a reason and we believe that")
print(answer)