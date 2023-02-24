'''Create a function that will return a Boolean value indicating if two circles
defined by center coordinates and radius are intersecting'''

import math
def To_check_circles():
    cor_circle1 = input("Enter the x and y coordinates of cirlce 1 separtated by a comma: ")
    rad_circle1 = int(input("Enter the radius of circle 1: "))
    cor_circle2 = input("Enter the x and y coordinates of cirlce 2 separtated by a comma: ")
    rad_circle2 = int(input("Enter the radius of circle 2: "))

    # to find the distance between center of the circles, this has been rounded to 2 decimal places
    cor_circle1 = cor_circle1.split(',')
    cor_circle2 = cor_circle2.split(',')
    diff_circle = round(math.sqrt((int(cor_circle2[0]) - int(cor_circle1[0])) * (int(cor_circle2[0]) - int(cor_circle1[0]))
                  + (int(cor_circle2[1]) - int(cor_circle1[1])) * (int(cor_circle2[1]) - int(cor_circle1[1]))))

    # to find the distance between radii of circle, will also use power and sqrt function to make the difference always +ve
    diff_radii = round(math.sqrt(pow((rad_circle1 - rad_circle2), 2)))

    #to check for  intersection
    if diff_radii == diff_circle:
        return True
    else:
        return False

   To_check_circles()