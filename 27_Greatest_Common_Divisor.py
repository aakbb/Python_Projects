#Programın amacı fonksiyon yardımıyla en büyük ortak böleni (EBOB) hesaplamak 

def find_gcd(a,b):
    if a<b :
        min = a
    else:
        min =b
    
    for i in range(1 , min):
        if a % i == 0 and b % i == 0:
            min = i
    print("EBOB({} , {}) = {}".format(a , b , min))
    
print("Sayıları Girin:")
a = int(input("1.Sayı= "))
b = int(input("2.Sayı= "))

find_gcd(a,b)