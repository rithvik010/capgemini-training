weight=float(input("enter your weight in kilograms "))
height=float(input("enter your height in meters "))
BMI=weight/(height*height)
BMI_value=round(BMI, 2)
if BMI_value<18.5:
    print(f"your BMI_value is {BMI_value} and it is underweight")
elif BMI_value>18.5 and BMI_value<24.9:
    print(f"your BMI_value is {BMI_value} and it is normal")
elif BMI_value>25 and BMI_value<29.9:
    print(f"your BMI_value is{BMI_value} and it is overweight")
else:
    print(f"your BMI_value is {BMI_value} and it is Obese")