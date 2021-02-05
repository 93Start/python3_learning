#string
name = "  testPythonstring 64 "

print(name)

#accress string
print(name[0])
print(name[0:4])
print(name[-4:])

#length of string
print(len(name))

#ลบช่องว่าง
name = name.strip()
#name = name.lstrip()
#name = name.rstrip()
print(name)

#Upper/lower case
print(name.upper())
print(name.lower())
print(name.capitalize())

#replace
print(name.replace("64","93"))
print(name.replace("t","a",1))
print(name.replace("t","a",4))

#check string >true or flase
x = "test" in name
print(x)
if x :
    name = name.replace("test","learn")
    print(name)


