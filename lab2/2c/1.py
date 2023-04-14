fahren=0
for i in range(15):
    fahren=float(input("Enter temperature in Fahrenheit: "))
    print("Celcius: ", ((fahren-32)*(5/9)))
print("All temperatures processed")