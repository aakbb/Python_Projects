#Projenin Amacı: Modüller yardımıyla gelişmiş bir hesap makinesi programı yapmak
from math import*
import time

print("""
      **************************************************
      Gelişmiş Hesap Makinesi Uygulamasına Hoşgeldiniz
      **************************************************
      İşlemler:
      1.Bir üst sayıya yuvarlama 
      2.Bir alt sayıya yuvarlama
      3.Faktöriyel bulma
      4.Mutlak değer bulma
      5.Mod alma
      6.EBOB bulma
      7.Kuvvet(üs) alma
      8.Karekök alma
      Q.Çıkış
      """)

while True:
    choose = input("İşlem Numaranız: ")
    if choose =="Q":
        print("Programdan çıkılıyor...")
        time.sleep(1)
        break
    number1 = input("Sayı: ")
    
    if choose == "1":
        number1 = float(number1)
        print(ceil(number1))
    elif choose == "2":
        number1 = float(number1)
        print(floor(number1))
    elif choose == "3":
        number1 = int(number1)
        print(factorial(number1))
    elif choose == "4":
        number1 = float(number1)
        print(fabs(number1))
    elif choose == "5":
        number1 = int(number1)
        number2 = int(input("2.Sayı: "))
        print(fmod(number1 , number2))
    elif choose == "6":
        number1 = int(number1)
        number2 = int(input("2.Sayı: "))
        print(gcd(number1 , number2))
    elif choose == "7":
        number1 = int(number1)
        number2 = int(input("2.Sayı: "))
        print(pow(number1,number2))
    elif choose == "8":
        number1 = int(number1)
        print(sqrt(number1))
    else:
        print("Geçersiz İşlem Numarası.Lütfen Tekrar Deneyin!")
    