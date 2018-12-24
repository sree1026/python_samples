def max_of_three_nums(x,y,z):
    if (x>y and x>z):
        return x
    elif (y>z):
        return y
    else:
        return z

x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))

print(max_of_three_nums(x,y,z), " is greatest of the three numbers")