""""
Programın amacı girilen bir sayının mükemmel sayı olup olmadığını ekrana yazmak 
mükemmel sayı:
bölenlerinin toplamı yine kendine eşit olan sayıdır.
6 = 3+2+1
6 = Mükemmel Sayı
"""
n = int(input("Enter a Number: "))

i = 1
sum = 0
while (i < n):
    if (n % i == 0):
        sum += i
    i += 1

if sum == n:
    print("{} = a Perfect Number".format(n))
else:
    print("{} = Not a Perfect Number".format(n))
    