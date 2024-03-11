import math as m

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit\n")

Shape = int(input("Which shape: "))

if Shape == 1:
    Base = int(input("Base: "))
    Height = int(input("Height: "))
    Triangle = Base*Height/2
    print("The area is " + str(Triangle))
elif Shape == 2:
    Base = int(input("Base: "))
    Height = int(input("Height: "))
    Rectangle = Base*Height
    print("The area is " + str(Rectangle))
elif Shape == 3:
    Side = int(input("Side: "))
    Square = Side ** 2
    print("The area is " + str(Square))
elif Shape == 4:
    Radius = int(input("Radius: "))
    Circle = Radius ** 2*m.pi
    print("The area is " + str(Circle))
elif Shape == 5:
    print("Operation cancelled")
else:
    print("Invalid input")
