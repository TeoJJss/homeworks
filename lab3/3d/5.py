num=int(input("Enter the number of students: "))
score_ls=[]

for i in range(1, num+1):
    score_ls.append(int(input(f"Enter the score for student {i}: ")))

avg=int((sum(score_ls))/num)
print("The average score is:",avg)