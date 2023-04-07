sell=int(input("Enter the selling price: "))
buy=int(input("Enter the buying price: "))

if sell > buy:
    print("You have a profit in trading this item. ")
elif sell == buy:
    print("Neither profit or loss. ")
else:
    print("You have a loss in trading this item. ")