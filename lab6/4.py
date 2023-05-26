def main():
    print("Enter 1 to read from file\nEnter 2 to add new records\nEnter 3 to search flight")
    opt=input("Your option: ")
    match(opt):
        case "1": read()
        case "2": write()
        case "3": search()
        case _: print("Invalid option")

def write():
    def questions():
        flight=input("Enter flight number: ")
        depart=input("Enter departure time: ")
        arrive=input("Enter arrival time: ")
        airport=input("Enter departure airport: ")
        dest=input("Enter destination: ")

        return [flight, depart, arrive, airport, dest]

    master=[]

    for i in range(3):
        master.append(questions())

    with open("details.txt", "a") as file:
        for detail in master:
            file.write("\t".join(detail))
            file.write("\n")

def read():
    with open("details.txt", "r") as file:
        print(file.read())

def search():
    flight=input("Enter flight number to search: ")
    with open("details.txt", "r") as file:
        for line in file.readlines():
            if line[0]==flight[0]:
                print(line)
                break
        else:
            print("Record not exist! ")

main()