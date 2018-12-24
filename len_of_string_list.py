def length(a):
    b = list(a)
    i = 0
    for character in b:
        i=i+1
    return i

str1 = input("Enter a string: ")
print("Length of the string is: "+ str(length(str1)))