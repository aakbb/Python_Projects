""""
Bölenlerinin toplamı kendine eşit olan sayılara Mükemmel Sayı denir.
1+2+3 = 6
Programın amacı fonksiyon yardımıyla Mükemmel sayıyı bulmak
"""
def isPerfect(number):
    sum =0
    for i in range(1,number):
        if number % i == 0:
            sum +=i
    if sum == number:
        return True
    return False


for i in range(1,1000):
    if isPerfect(i):
        print(i, " is a Perfect Number")

    
            