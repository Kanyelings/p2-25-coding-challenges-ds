def sum_of_numbers(string):
    list = string.split(',')
    sum = 0
    for num in list:
        sum += float(num)
        return sum
    print(sum_of_numbers("6, 2, 5"))
