assign=int(input("Enter your assignment marks: "))

if assign>=25:
    test=int(input("Enter your test marks: "))
    if test >=25:
        exam=int(input("Enter your exam marks: "))
        if exam >=50:
            print("Congratulations, you have passed the module! ")
        else:
            print("Please resit the exam.")
    else:
        print("Please resit the test. ")
else:
    print("Please redo the assignment.")

    