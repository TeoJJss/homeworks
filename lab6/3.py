def main():
    print("Enter 1 to read from file\nEnter 2 to add new records")
    opt=input("Your option: ")
    match(opt):
        case "1": read()
        case "2": write()
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

main()