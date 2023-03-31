count=int(input("How many scores in total? "))

for i in range(count):
    score=int(input(f"Enter Score {i+1}: "))
    if score >=80:
        print("A")
    elif score >=60:
        print("B")
    elif score >=40:
        print("C")
    else:
        print("D")

