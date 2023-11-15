import math
from math import pi
def circle_perimeter(radius):
    print("The perimeter of the circle is: ", 2 * pi * radius, "m²")
def circle_area(radius):
    print("The area of the circle is:", pi * radius**2, "m²")
def sphere_volume(radius):
    print("The volume of the sphere is: ", 4/3 * pi * radius**3, "m³")

def sphere_area(radius):
    print("The area of the sphere is: ", 4 * pi * radius**2, "m²")

def cube_volume(side_length):
    print("The volume of the cube is: ", side_length**3, "m³")

def cube_area(side_length):
    print("The area of the cube is: ", 6 * side_length**2, "m²")

def cylinder_volume(radius, height):
    print("The volume of the cylinder is: ", pi * radius**2 * height, "m³")

def cylinder_area(radius, height):
    print("The area of the cylinder is: ", 2 * pi * radius * (radius + height), "m²")


while True:
    menu = """
    A) Circle Perimeter
    B) Circle Area
    C) Sphere Volume
    D) Sphere Area
    E) Cube Volume
    F) Cube Area
    G) Cylinder Volume
    H) Cylinder Area
    I) Exit
    Pick a letter(A-I): """

    print(menu)
    choice = input().strip().upper()

    if choice == "I":
        print("Exiting the program. Bye!")
        break
    elif choice in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        radius = float(input("Enter the radius of the circle, sphere or cyllinder: "))
        if choice in ["A", "B", "C", "D"]:
           result = 0
           if choice == "A":
              circle_perimeter(radius)
           elif choice == "B":
              circle_area(radius)
           elif choice == "C":
            sphere_volume(radius)
           elif choice == "D":
            sphere_area(radius)
        else:
            side_length = float(input("Enter the length of the cube or cyllinder: "))
            if choice == "E":
               cube_volume(side_length)
            elif choice == "F":
                cube_area(side_length)
            elif choice == "G":
                height = float(input("Enter the height of the cyllinder: "))
                cylinder_volume(radius, height)
            elif choice == "H":
                height = float(input("Enter the height of the cyllinder: "))
                cylinder_area(radius, height)
    else:
        print("Invalid choice. PLease enter a valid option(A-I): ")