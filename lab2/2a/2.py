name=input("Please enter the student's name: ")
mark=int(input("Please enter the student's marks: "))

if mark >= 0:
    print(f"Congratulations {name}, you have passed the exam!" if mark >=50 else f"{name}, sorry you have failed. ")
else:
    print("Invalid mark!")