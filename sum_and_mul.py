def sum(num_list):
    sum1 = 0
    for i in num_list:
        sum1 = sum1 + i
    return  sum1

def mul(num_list):
    product=1
    for i in num_list:
        product = product*i
    return product

print("Sum is: "+str(sum([1,2,3,4]))+"\nProduct is: "+str(mul([1,2,3,4])))