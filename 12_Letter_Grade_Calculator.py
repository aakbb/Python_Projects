"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.
    Vize1 toplam notun %30'una etki edecek.
    Vize2 toplam notun %30'una etki edecek.
    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 ------> FF
"""

print("""
      *************************************
      Welcome to Letter Grade Calculator
      *************************************
      
      """)

midterm_exam1 = int(input("The First Midterm Exam = "))
midterm_exam2 = int(input("The Second Midterm Exam = "))
final_exam = int(input("Final Exam = "))

average = midterm_exam1*0.3 + midterm_exam2*0.3 + final_exam*0.4

if average >= 90:
    print("Ortalamanız: {} ------------> AA".format(average))
elif average>=85:
    print("Ortalamanız: {} ------------> BA".format(average))
elif average>=80:
    print("Ortalamanız: {} ------------> BB".format(average))
elif average>=75:
    print("Ortalamanız: {} ------------> CB".format(average))
elif average>=70:
    print("Ortalamanız: {} ------------> CC".format(average))
elif average>=65:
    print("Ortalamanız: {} ------------> DC".format(average))
elif average>60:
    print("Ortalamanız: {} ------------> DD".format(average))
elif average>=55:
    print("Ortalamanız: {} ------------> FD".format(average))
else:
    print("Ortalamanız: {} ------------> FF (Kaldınız)".format(average))