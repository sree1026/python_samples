def is_member(x,a):
    for i in a:
        if(x == str(i)):
            return True
    return False

x = input("Enter a member: ")
a = [1,2,'a','b',1.0,2.0]
print(str(is_member(x,a)))