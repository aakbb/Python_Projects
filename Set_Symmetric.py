#Set Symmetric
#Kümelerdeki fark kümelerinin birleşimi diyebiliriz. Yani:
#(A - B) u (B - A) şeklinde diyebiliriz
# '^' ile ya da 'set1.symmetric_difference(set2)' şeklinde gösterilir.

setA = {1,2,3,4,5,6}
setB = {2,4,6,8,6,5,9,0}

print(setA ^ setB)
print(setA.symmetric_difference(setB))
