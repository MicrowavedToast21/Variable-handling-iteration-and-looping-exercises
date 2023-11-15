import math
from math import pi

def circle_perimeter(radius):
    print("The perimeter of the circle is: ", 2 * pi * radius, "m2")
def circle_area(radius):
    print("The area of the circle is:", pi * radius**2, "m2")
def sphere_volume(radius):
    print("The volume of the sphere is: ", 4/3 * pi * radius**3, "m3")


while True:
    menu = """
    A) Circle Perimeter
    B) Circle Area
    C) Sphere Volume
    D) Quit
    Pick a letter(A-D): """

    print(menu)
    choice = input().strip().upper()

    if choice == "D":
        print("Exiting the program. Bye!")
        break
    elif choice in ["A", "B", "C"]:
        radius = float(input("Enter the radius of the circle or sphere: "))
        if choice == "A":
           circle_perimeter(radius)
        elif choice == "B":
            circle_area(radius)
        elif choice== "C":
            sphere_volume(radius)
    else:
        print("Invalid choice. PLease enter a valid option(A-D): ")
