#Calculating the sum of numbers received in a comma delimited string
string = input("Enter the numbers you want to sum separated by a comma (','): ")
list = string.split(",")
sum = 0
for items in list:
   sum += int(items)
print(sum)