def findAverage(num1, num2, num3):
    return (num1+num2+num3)/3

avg=findAverage(int(input("Enter first number:")), 
                int(input("Enter second number:")), 
                int(input("Enter third number:"))
                )
print("Average of the given three numbers is:", avg)