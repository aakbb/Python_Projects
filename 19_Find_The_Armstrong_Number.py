""""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

"""

n = input("Enter a Number: ")
number_of_dijit = len(n)  #Basamak Sayısı

n = int(n)
division = n  #Bölüm
sum = 0   
i = 1

while division> 0:
    remainder = division%10   #Her seferinde kalan sayesinde basamaktaki sayıları elde ediyoruz
    sum += remainder ** number_of_dijit  
    division //= 10

if (sum == n):
    print(n,"= an Armstrong Number.")
else:
    print(n,"= Not an Armstrong Number.")