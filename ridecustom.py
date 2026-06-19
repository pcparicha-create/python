# Transport Selection System using Nested Conditions

print("===== TRANSPORT BOOKING SYSTEM =====")
print("1. Bike")
print("2. Car")
print("3. Bus")
print("4. Train")

transport = int(input("Select a transport type: "))

if transport == 1:
    print("\nBike Options")
    print("1. Standard Bike")
    print("2. Sports Bike")

    bike = int(input("Choose a bike: "))

    if bike == 1:
        print("You selected a Standard Bike.")
    else:
        print("You selected a Sports Bike.")

elif transport == 2:
    print("\nCar Options")
    print("1. Sedan")
    print("2. SUV")

    car = int(input("Choose a car: "))

    if car == 1:
        print("You selected a Sedan.")
    else:
        print("You selected an SUV.")

elif transport == 3:
    print("\nBus Options")
    print("1. City Bus")
    print("2. Express Bus")

    bus = int(input("Choose a bus: "))

    if bus == 1:
        print("You selected a City Bus.")
    else:
        print("You selected an Express Bus.")

elif transport == 4:
    print("\nTrain Options")
    print("1. Metro Train")
    print("2. High-Speed Train")

    train = int(input("Choose a train: "))

    if train == 1:
        print("You selected a Metro Train.")
    else:
        print("You selected a High-Speed Train.")

else:
    print("Invalid choice.")