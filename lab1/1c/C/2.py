inp1=input("Is anyone is a vegetarian? ")
inp2=input("Is anyone is a vegan? ")
inp3=input("Is anyone is a gluten-free? ")

vege=True if inp1=="yes" else False
vegan=True if inp2=="yes" else False
gluten=True if inp3=="yes" else False

if vege and vegan and gluten: # If all are yes
    print("Corner Cafe")
    print("The Chef's Kitchen")

elif not vege and not vegan and not gluten: # All no
    print("Joe Gourmet Burgers")
    print("Corner Cafe")
    print("The Chef's Kitchen")
    print("Main Street Pizza Company")
    print("Mama's Fine Italian")
elif not vege and not vegan and gluten: # have gluten-free
    print("Main Street Pizza Company\nCorner Cafe\nThe Chef's Kitchen")
elif not vege and vegan and not gluten: # have vegan
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif not vege and vegan and gluten: # have vegan and gluten-free
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vege and not vegan and not gluten: # have vege
    print("Main Street Pizza Company\nCorner Cafe\nMama's Fine Italian\nThe Chef's Kitchen")
elif vege and not vegan and gluten: # have vege and gluten-free
    print("Main Street Pizza Company")
elif vege and vegan and not gluten:  # have vege and vegan
    print("Mama's Fine Italian")