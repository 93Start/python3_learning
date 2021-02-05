#string

name = "  testPythonstring 64 "

#concat
fname = "leaning"
lname = "python"
age = 93
fullname = fname+lname+str(age)
print(fullname)
print("name:",fname," ",lname)
text= "name: {} \tlname {}"
#text= "name: {0} \tlname {1}"
print(text.format(fname,lname))

#count
text = "cat dog cat cat fishcat tigercat liconcat"
print(text.count("cat"))

#stratwith
test = "catcatcat"
print(test.startswith("cat"))
print(test.endswith("dog"))