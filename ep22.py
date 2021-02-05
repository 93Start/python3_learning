#แลกเงิน

number = int(input("enter your money:"))

if number >= 1000 :
    print("1000bath:",number//1000," ea")
    number%=1000
if number >= 500 :
    print("500bath:",number//500," ea")
    number%=500
if number >=100 :
    print("100bath:",number//100," ea")
    number%=100
if number >=50 :
    print("50bath:",number//50," ea")
    number%=50
if number >=20 :
    print("20bath:",number//20," ea")
    number%=20