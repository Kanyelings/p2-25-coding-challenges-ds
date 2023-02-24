string = input("Enter your text")
list1 = string.split()
rstring = " "
for e in list1:
    rstring = rstring + e.capitalize() + " "
    print(rstring)
