#ฺBMI Calculator
# BMI kg/m^2

w = int( input("Enter your weight:"))
h = int (input("Enter your tall:"))

bmi = w / ((h/100)**2)
print(bmi)

if bmi <18.0 :
    print("ต่ำกว่าเกณฑ์")
elif bmi >=18.5 and bmi <=22.5 :
    print("สมส่วน")
elif bmi >=23.0 and bmi <=24.9 :
    print("น้ำหนักเกิน")    
elif bmi >=25.0 and bmi <=29.9 :
    print("อ้วนระดับ1")  
elif bmi >=30.0  :
    print("อ้วน")     
else:
    print("ไม่ทราบชัดเจน")