num=int(input("Enter a number: "))

if num != 0 :
    print("You picked an even number" if num%2==0 else "You picked an odd number")
else:
    print("0 is neither even or odd")