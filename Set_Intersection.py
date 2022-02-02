#Set Intersection
#Kümelerdeki kesişim kümesi ile aynı mantıkta.
#İki setin elemanlarını kıyaslayıp ortak olanlardan yeni bir set yazma olayıdır.
#Bir tane ve operatörü (&) ile ya da set1.intersection(set2) şeklinde gösterilir
setA = {1,2,3,4,5,6}
setB = {2,4,6,8,6,5,9,0}

print(setA &setB)
print(setA.intersection(setB))