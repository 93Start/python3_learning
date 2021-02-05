#ะtemperature calcuate
#C=(F-32)*(5/9)
#F=(C*(9/5))+32

temp = input("enter temp(degree):")
print(temp)
degree = temp[:-1]
unit = temp[-1].upper()
print(degree," = ",unit)

if unit == 'C' :
    result =(9*int(degree))/5+32
    unit_result = "F"
if unit == 'F' :
    result =(int(degree)-32)*5/9
    unit_result = "C"
    
print(result)