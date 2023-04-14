count=num=0
ls=[]

while count<20:
    ls.append(str(num))
    num+=2
    count+=1

print(", ".join(ls))