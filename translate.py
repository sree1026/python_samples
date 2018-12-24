vowel = ('a','e','i','o','u',' ')
def translate(str1):
    s = list(str1)
    l = len(s)
    i = 0
    while(i<l):
        if(s[i].lower() not in vowel):
            s.insert(i+1,s[i])
            s.insert(i+1,'o')
            l=len(s)
            i=i+2
        i=i+1
    return s


str1 = input("Enter a string: ")
s = translate(str1)
trans = ''.join(s)
print(trans)