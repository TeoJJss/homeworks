str1="Ally1995 is a 50thData Scientist and AI experts"

ls=str1.split(" ")
out=""
print(ls)
for i in ls:
    if any(j.isnumeric() for j in i) and any(x.isalpha() for x in i):
        print(i)
