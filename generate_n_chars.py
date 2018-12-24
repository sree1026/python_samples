def generate_n_chars(n,ch):
    l1 = []
    for i in range(n):
        l1 = l1 + [ch]
    str1 = ''.join(l1)
    return str1

ch = input("Enter the character to print: ")
n = int(input("Enter no of items to print the character: "))
print(generate_n_chars(n,ch))