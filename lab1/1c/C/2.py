'''
If one person is vegetarian, the restaurants must be vegetarian
If nobody is vegetarian, the restaurants can be vegetarian or non-vegetarian
'''

inp1=input("Is anyone is a vegetarian? ")
inp2=input("Is anyone is a vegan? ")
inp3=input("Is anyone is a gluten-free? ")

vege=True if inp1.lower().strip()=="yes" else False
vegan=True if inp2.lower().strip()=="yes" else False
gluten=True if inp3.lower().strip()=="yes" else False

rest=["Joe's Gourmet Burgers", "Main Street Pizza Company", "Corner Cafe",
    "Mama's Fine Italian", "The Chef's Kitchen"] # A list of restaurants can go

if vege: # If got ppl vege, restaurants must "Yes" with vege
    if "Joe's Gourmet Burgers" in rest: rest.remove("Joe's Gourmet Burgers") # Remove restaurants with "No" vege

if vegan: # If got ppl vegan, restaurants must "Yes" with vegan
    # Remove restaurants with "No" vegan
    if "Joe's Gourmet Burgers" in rest: rest.remove("Joe's Gourmet Burgers")
    rest.remove("Main Street Pizza Company")
    if "Mama's Fine Italian" in rest: rest.remove("Mama's Fine Italian")

if gluten: # If got ppl gluten-free, restaurants must "Yes" with gluten-free
    # Remove restaurants with "No" vegan
    if "Joe's Gourmet Burgers" in rest: rest.remove("Joe's Gourmet Burgers")
    if "Mama's Fine Italian" in rest: rest.remove("Mama's Fine Italian")


print("\n".join(rest))