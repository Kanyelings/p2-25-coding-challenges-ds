'''Create a function that will convert a string containing a binary number into a
number'''

def binary_decimal():
    number = input("Enter the binary number you want to convert to dicimal: ")
    decimal = 0
    #j starts from minus so as to slice the string from behind
    j = -1
    for i in range(len(number)):
        value = int(number[j]) * pow(2, i)
        j -= 1
        decimal += value
    return decimal

answer = binary_decimal()
print(answer)