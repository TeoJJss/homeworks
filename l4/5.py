str1 = "Abc"
str2 = "Xyz"
j=1
for i in str1:
    print(i, end="")
    while j <=len(str2):
        print(str2[-j], end="")
        j+=1
        break