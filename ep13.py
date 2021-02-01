#ฺBMI Calculator
# BMI kg/m^2

w = int( input("Enter your weight:"))
h = int (input("Enter your tall:"))

bmi = w / ((h/100)**2)
print(bmi)