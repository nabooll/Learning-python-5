#Area of Circle

#First we need to import the module
import math

#Next step is input the number of radius
radius = int(input("Radius = "))

#Now we count the area of circle by using this formula
#Don't forget to round by 2 decimal number it, so we can read the result easily
area_of_circle = math.pi * radius ** 2
result = round(area_of_circle, 2)
print(f"Area of the circle is {result} cm ")
