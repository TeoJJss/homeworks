import math

PI=math.pi
def calculate_diameter(r):
    return 2*r

def calculate_circumference(r):
    return 2*PI*r

def calculate_area(r):
    return PI*r*r

def display_menu():
    print("Enter 1 to calculate Diameter\nEnter 2 to calculate Circumference\nEnter 3 to calculate Area")
    option=int(input("Enter your choice: "))
    r=result=o=""
    if option in range(1, 4):
        r=float(input("Enter the radius of the circle: "))

        match (option):
            case 1:
                o="diameter"
                result=calculate_diameter(r)
            case 2:
                o="circumference"
                result=calculate_circumference(r)
            case 3:
                o="area"
                result=calculate_area(r)
            case _:
                print("Invalid option")
        if result:
            print(f"The {o} of the circle is {round(result, 2)}")
    else:
        print("Invalid option")

if __name__=='__main__':
    display_menu()