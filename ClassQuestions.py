class Class_Questions:
    def __init__(self):
        self.offenses = []
        self.total_fine = 0

    def offensesList(self, offense, fined):
        self.offenses.append((offense, fined))
        self.total_fine += fined
        print(f"{offense}: Fine - {fined}")

    def save_to_file(self, license_plate, selected_class):
        filename = f"txt_data/number_plates/{license_plate}.txt"
        with open(filename, 'w') as file:
            file.write(f"License Plate: {license_plate}\n")
            file.write(f"Vehicle Class: {selected_class}\n")
            file.write("Offenses:\n")
            for idx, (offense, fined) in enumerate(self.offenses, 1):
                file.write(f"Offense {idx}: {offense}, Fine: {fined}\n")
            file.write(f"Total Fine: {self.total_fine}\n")

    def bike(self, license_plate):
        global_func(self)
        A = input("Was He / She Speeding: (yes|no) ")
        if A.lower() == "yes":
            offense = "Speeding Violation"
            fine = 1500
            self.offensesList(offense, fine)
        B = input("Did He / She Run a red light: (yes|no) ")
        if B.lower() == "yes":
            offense = "Have run a Red Light"
            fine = 1000
            self.offensesList(offense, fine)
        C = input("Did He / She Run a stop sign: (yes|no) ")
        if C.lower() == "yes":
            offense = "Have run a Stop Sign"
            fine = 1000
            self.offensesList(offense, fine)
        D = input("Did He / She drive recklessly: (yes|no) ")
        if D.lower() == "yes":
            offense = "Driving recklessly"
            fine = 3250
            self.offensesList(offense, fine)
        self.save_to_file(license_plate, "Bike")

    def car(self, license_plate):
        A = input("")
        if A.lower() == "yes":
            offense = ""
            fine = 2000
            self.offensesList(offense, fine)
        B = input("")
        if B.lower() == "yes":
            offense = ""
            fine = 2000
            self.offensesList(offense, fine)
        C = input("")
        if C.lower() == "yes":
            offense = ""
            fine = 2000
            self.offensesList(offense, fine)
        D = input("")
        if D.lower() == "yes":
            offense = ""
            fine = 2000
            self.offensesList(offense, fine)
        self.save_to_file(license_plate, "car")

    def bakkie(self, license_plate):
        A = input("")
        if A.lower() == "yes":
            offense = ""
            fine = 2000
            self.offensesList(offense, fine)
        B = input("")
        if B.lower() == "yes":
            offense = ""
            fine = 2000
            self.offensesList(offense, fine)
        C = input("")
        if C.lower() == "yes":
            offense = ""
            fine = 2000
            self.offensesList(offense, fine)
        D = input("")
        if D.lower() == "yes":
            offense = ""
            fine = 2000
            self.offensesList(offense, fine)
        self.save_to_file(license_plate, "Bakkie")

    def truck(self, license_plate):
        A = input("Does the license of the driver have the right license for this vehicle? (Yes/No): ")
        if A.lower() == "yes":
            offense = "Not having the right license for this vehicle"
            fine = 1500
            self.offensesList(offense, fine)
        B = input("Is the vehicle overloaded? (Yes/No): ")
        if B.lower() == "yes":
            offense = "Vehicle is overloaded"
            fine = 2000
            self.offensesList(offense, fine)
        C = input("")
        if C.lower() == "yes":
            offense = ""
            fine = 2000
            self.offensesList(offense, fine)
        self.save_to_file(license_plate, "Truck")









    def vehicleClass(self):
        license_plate = input("Please enter your license plate number: ")

        print("Press 1 for bike")
        print("Press 2 for car")
        print("Press 3 for bakkie")
        print("Press 4 for truck")

        while True:
            answer = input("Please enter your choice: ")

            if answer in ["1", "2", "3", "4"]:
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

        selected_class = None

        if answer == "1":
            selected_class = "Bike"
            self.bike(license_plate)
        elif answer == "2":
            selected_class = "Car"
            self.car(license_plate)
        elif answer == "3":
            selected_class = "Bakkie"
            self.bakkie(license_plate)
        elif answer == "4":
            selected_class = "Truck"
            self.truck(license_plate)


def global_func(self):
    A = input("1111Does the license of the driver have the right license for this vehicle? (Yes/No): ")
    if A.lower() == "yes":
        offense = "Not having the right license for this vehicle"
        fine = 1500
        self.offensesList(offense, fine)
    B = input("I11111s the vehicle overloaded? (Yes/No): ")
    if B.lower() == "yes":
        offense = "Vehicle is overloaded"
        fine = 2000
        self.offensesList(offense, fine)
    C = input("")
    if C.lower() == "yes":
        offense = ""
        fine = 2000
        self.offensesList(offense, fine)

    