import math
def calculating_distance():
    X1 = int(input("Enter the point X1: "))
    Y1 = int(input("Enter the point Y1: "))
    X2 = int(input("Enter the point X2: "))
    Y2 = int(input("Enter the point Y2: "))
    return math.sqrt((X2 - X1) * (X2 - X1) + (Y2 - Y1) * (Y2 - Y1) )

answer = calculating_distance()
print(answer)