"""
vücut kitle endeksi : kilo(kg) / boy(m)**2
"""

print("\nWelcome to Body-Mass Index Program")
print("--------------------------------------------------")

weight = int(input("Your Weight(kg): "))
height = float(input("Your Height(m): "))

bmi = weight /(height**2)

if bmi>=30:
    print("BMI= {}: Overweight- Obesity".format(bmi))
elif bmi>=25 and bmi<30:
    print("BMI= {}: Fat".format(bmi))
elif bmi>=18.5 and bmi<25:
    print("BMI= {}: Healthy".format(bmi))
elif bmi<18.5:
    print("BMI= {}: Weak".format(bmi))
