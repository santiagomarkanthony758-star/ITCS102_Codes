# JEEPNEY SIMULATOR (iteractive)
route = ["terminal", "perez park", "pacific mall"]
passenger = []
seats = 6
fare = 13
total = 0

while "true":
    print()
    print("sakay:", passenger)
    print(len(passenger), "of", seats, "seats")
    print("1 sakay 2 priority seat 3 para po!")
    print("4 Baba sa pinto 5 baba sa harap")
    print("6 seat check 7  balikan 8 exit")
    choice = input("choice:")

    if choice == "1":
        if len(passenger) == seats:
            print("puno na !")
        else:
            name = input("name:")
            passenger.append(name)
            total = total + fare
            print(name, "boarded at the back.")

    elif choice == "2":
        if len(passenger) == seats:
            print("puno na")
        else:
            name = input("name:")
            passenger.insert(0, name)
            total = total + fare 
            print(name, "took the priority seat.")

    elif choice == "3":
        name = input("who is getting off? ")
        if name in passenger:
            passenger.remove(name)
            print(name, "got off, ingat ka ha!")
        else:
            print(name, "its not on this jeep")

    elif choice == "4":
        if len(passenger) == 0:
            print("the jeep is empty.")
        else:
            left = passenger.pop()
            print(left, "got off at the door.")

    elif choice == "5":
        if len(passenger) == 0:
            print("the jeep is empty.")
        else:
            front = passenger.pop(0)
            print(front, "got off at the front." )

    elif choice == "6":
        for i in range(len(passenger)):
            print("seat", i + 1, passenger[i])

    elif choice == "7":
        route.reverse
        print("route:", route)
    elif choice == "8":
        print("total fare today:", total)
        break

    else: 
        print("invalid choice.")
    