# Project 2 - A weight converter to convert your weight from KG to LBs or vice-versa !

weight = float(input("Enter your weight: "))
unit = input("Select the unit you want (kg/lbs): ")

if unit == "kg":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight, 1)} {unit}")
elif weight == "lbs":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print("Invalid input !")

