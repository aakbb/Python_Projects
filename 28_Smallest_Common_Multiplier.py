#Programın amacı fonksiyon yardımıyla en küçük ortak çarpanı(EKOK) bulmak

def find_ekok(a,b):
    for i in range(1,(a*b) +1):
        if i % a ==0 and i % b == 0:
            ekok = i
            break
    print("EKOK({} , {}) = {}".format(a,b,ekok))
    
print("Sayıları Giriniz:")
a = int(input("1.Sayı: "))
b = int(input("2.Sayı: "))

find_ekok(a,b)