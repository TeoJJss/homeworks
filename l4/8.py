str1="Ally is a system analyst. Ally works at APU"
ind=0

for i in range(len(str1)):
    if str1[i:i+4]=="Ally":
        ind=i

print("Original String is:", str1)
print("Last occurrence of Ally starts at index",ind)