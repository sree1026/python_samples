def reverse_string(str1):
    i = len(str1)-1
    b = ''
    while i>=0:
        b = b + str1[i]
        i=i-1
    return b

def is_palindrome(string2):
    if(string2 == reverse_string(string2)):
        return True
    else:
        return  False
    
str2 = input("Enter a string to check for palindrome: ")
print(is_palindrome(str2))
