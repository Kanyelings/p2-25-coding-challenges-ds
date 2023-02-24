'''Create a function that will add two positive numbers of indefinite size. The numbers
are received as strings and the result should be also provided as string.'''

def adding_numbers():
    def reverse_string(string):
        string = string[::-1]
        return string

    num1 = reverse_string(input("Enter the first number you want to add"))
    num2 = reverse_string(input("Enter the next number you want ot add"))
    answer = ""
    while True:
        if len(num1) == len(num2):
            break
        elif len(num1) > len(num2):
            num2 += "0"
        else:
            num1 += "0"
    remainder = 0
    for i in range(len(num1)):
        result = int(num1[i]) + int(num2[i]) + remainder
        remainder = int(result / 10)
        if result >= 10 and i != (len(num1) - 1):
            result -= 10
        if i == (len(num1) - 1):
            break
        answer += str(result)

    return str(result) + reverse_string(answer)
print(adding_numbers())



