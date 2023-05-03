text=input("Enter a string: ")

lowercase=[x for x in text if x==x.lower()]
uppercase=[x for x in text if x==x.upper()]

print("".join(lowercase)+"".join(uppercase))