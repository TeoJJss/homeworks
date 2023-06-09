# No data validation in this script

def createQuiz() -> list :
    master=[]
    tmp=[]
    num=int(input("Enter number of questions to be created: "))
    for i in range(num):
        tmp=[]
        tmp.extend([input(f"Question {i+1}: "), 
                    input("Option A: "),
                    input("Option B: "), 
                    input("Option C: "),
                    input("Option D: "),
                    input("Correct option: ")
                    ])
        master.append(tmp)
        print(master)
    return master
    
def saveQuiz(quiz:list) -> None :
    with open("quiz.txt", "a") as file:
        for q in quiz:
            file.write("\t".join(q))
            file.write("\n")

def takeQuiz(name:str)->None:
    file=open("quiz.txt", "r")
    ls=[]
    score=0
    for line in file:
        ls=line.split("\t")
        print("Question: ", ls[0])
        print("A.",ls[1])
        print("B.",ls[2])
        print("C.",ls[3])
        print("D.",ls[4])

        if input("Your option: ").strip() == ls[5].strip():
            print("Correct answer!")
            score+=1
        else:
            print("Wrong! The correct answer is ", ls[5])
    file.close()
    print("Your score is", score)
    save_best(name, int(score))

def menu() -> None:
    name, role=login()
    print("MENU")
    if role=="admin":
        quizzes=createQuiz()
        saveQuiz(quizzes)
        print("Quiz saved")
    elif role=="student":
        takeQuiz(name)

# Additional exercises
def login() -> str:
    while True:
        print("LOGIN")
        userdata={
            "admin": ["teacher", "teacher_password"],
            "student": ["student", "student_password"]
        }
        username=input("Username: ")
        password=input("Password: ")
        for role, cred in userdata.items():
            if username==cred[0] and password==cred[1]:
                print("Login success. You are", role)
                return username, role
        else:
            print("Login failed")

def save_best(name:str, score:int):
    ls=[]
    with open("score.txt", "w+") as file:
        ls=file.readlines()
        for ind, data in enumerate(ls):
            if data.split("\t")[0]==name:
                if data.split("\t")[1] < score:
                    ls[ind]=f"{name}\t{score}"
                    file.writelines(ls)
                break
        else:
            ls.append(f"{name}\t{score}")
            file.writelines(ls)

menu()