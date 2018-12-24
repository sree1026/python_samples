def reverse_string(string):
    i = len(string)-1
    rev =''
    while(i>=0):
        rev = rev + string[i]
        i=i-1
    return rev

str1 = input("Enter a string: ")
print(reverse_string(str1))