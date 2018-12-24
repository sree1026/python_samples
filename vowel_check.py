vowel = ('a','e','i','o','u')
def vowel_check(str1):
    for i in str1:

        if(i.lower() not in vowel):
            return False
    return True

str1 = input("Enter a string: ")
print(str(vowel_check(str1)))