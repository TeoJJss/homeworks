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