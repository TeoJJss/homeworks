mark=int(input("Enter your mark: "))
grade=""
status="Pass"

if mark<0 or mark>100:
    print("Invalid entry")
else:
    if mark>=80:
        grade="A"
    elif mark>=70:
        grade="B"
    elif mark>=60:
        grade="C"
    elif mark>=50:
        grade="D"
    else:
        grade="F"
        status="Fail"

print(f"Mark: {mark}\nGrade: {grade}\nStatus: {status}")