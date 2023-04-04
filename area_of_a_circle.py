def area_of_a_circle(r):
    pi = 3.14
    area = pi*float(r*r)
    print("Area of a circle :  {}".format(area))


radius = float(input("enter the radius of the circle : "))
area_of_a_circle(radius)    