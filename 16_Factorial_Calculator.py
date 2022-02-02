#For döngüsü kullanarak faktöriyel hesabı yapan program yazacağız.

factor=1
value = int(input("Enter a number: "))

for i in range(1,value+1):
    factor = factor*i
print("{}! = {}".format(value , factor))
