'''

calculate the area of a rectangle and allows the user to calculate
as many operations they want and exit the program

a = l*w

'''

while True:
    print("This program calculates area of triangles.")
    l = float(input("Enter length of triangle: "))
    w = float(input("Enter width of triangle: "))
    a = l*w/2
    print("Area:", a)
    user_input = input("Would you like to make another calculation? Y/N?:")
    if user_input == "Y" or user_input == "y":
        continue
    elif user_input == "N" or user_input == "n":
        break
