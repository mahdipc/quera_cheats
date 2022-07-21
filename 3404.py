weight_in_kilograms = int(input())
height_in_meters = float(input())
BMI = weight_in_kilograms/(height_in_meters**2)
print("%.2f" % BMI)
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
elif BMI >= 30:
    print("Obese")
