#list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmak
#List compherension'un  yapısı:
#listeye yazılacak değer  loop yapısı(for döngüsü)  (opsiyonel)koşul durumu


even_list = [i for i in range(1,101) if i%2==0]
print(even_list)