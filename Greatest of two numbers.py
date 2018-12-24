def max(a,b):
    if (a>b):
        return a
    else:
        return b
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))

print(a,b)

c = max(a,b)
print(str(c)+' is greater')