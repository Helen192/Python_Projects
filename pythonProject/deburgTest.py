def summe(a,b):
    c = a + b
    return c

for i in range(5):
    erg = summe(10,i)
    print(erg)


num = int(input("Enter a positive number: "))

if num<0:
    raise Exception("Please input only positive value ")

print("num = ", num)