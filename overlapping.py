def overlapping(l1,l2):
    for i in l1:
        for j in l2:
            if(i==j):
                return True
    return False


l1 = [1,2,3,4,5]
l2 = []
for i in range(5):
    num = int(input("Enter a number: "))
    l2 = l2 + [num]
print(overlapping(l1,l2))