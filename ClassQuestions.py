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
        A = input("Is your motorcycle equipped with all the required safety equipment, including mirrors, lights, and turn signals? (yes|no): ")
        if A.lower() == "no":
            offense = "Motorcycle not equipped with all the required safety requirements"
            fine = 1500
            self.offensesList(offense, fine)
        B = input("Are your tires in good condition, with sufficient tread and proper inflation? (yes|no): ")
        if B.lower() == "yes":
            offense = "Motorcycle tired not in good condition"
            fine = 500
            self.offensesList(offense, fine)
            self.save_to_file(license_plate, "Bike")

    def car(self, license_plate):
        global_func(self)
        self.save_to_file(license_plate, "car")

    def bakkie(self, license_plate):
        global_func(self)
        A = input("Is the vehicle overloaded (yes|no): ")
        if A.lower() == "yes":
            offense = "Vehicle overloaded"
            fine = 2170
            self.offensesList(offense, fine)
        self.save_to_file(license_plate, "Bakkie")

    def truck(self, license_plate):
        global_func(self)
        A = input("Is the vehicle overloaded (yes|no): ")
        if A.lower() == "yes":
            offense = "Vehicle overloaded"
            fine = 3000
            self.offensesList(offense, fine)
        B = input("Has the driver checked the vehicle for any mechanical defects or safety issues today? (Yes/No): ")
        if B.lower() == "no":
            offense = "Drive failed to do daily inspection"
            fine = 1000
            self.offensesList(offense, fine)
        C = input("Do you have all the necessary safety equipment, such as reflective vests, warning triangles, and fire extinguishers? (yes|no)")
        if C.lower() == "no":
            offense = "Driver does not have all the necessary safety equipment"
            fine = 780
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
    A = input("Does the driver of the vehicle have the right license for the vehicle? (Yes/No): ")
    if A.lower() == "no":
        offense = "Driver does not have the right license for the vehicle class"
        fine = 1500
        self.offensesList(offense, fine)
    B = input("Was He / She Speeding (yes|no): ")
    if B.lower() == "yes":
        offense = "Speeding Violation"
        fine = 1500
        self.offensesList(offense, fine)
    C = input("Did He / She Run a red light (yes|no): ")
    if C.lower() == "yes":
        offense = "Have run a Red Light"
        fine = 1000
        self.offensesList(offense, fine)
    D = input("Did He / She Run a stop sign (yes|no): ")
    if D.lower() == "yes":
        offense = "Have run a Stop Sign"
        fine = 1000
        self.offensesList(offense, fine)
    E = input("Did He / She drive recklessly (yes|no): ")
    if E.lower() == "yes":
        offense = "Driving recklessly"
        fine = 3250
        self.offensesList(offense, fine)
    F = input("Was He / She driving under the Influence? (yes|no): ")
    if F.lower() == "yes":
        offense = "Driving under the Influence"
        fine = 2000
        self.offensesList(offense, fine)
    G = input("Was He / She using there cellphone while driving (yes|no): ")
    if G.lower() == "yes":
        offense = "Using cellphone while driving"
        fine = 1500
        self.offensesList(offense, fine)
    H = input("Was He / She driving with out insurance or registered vehicle? (yes|no): ")
    if H.lower() == "yes":
        offense = "Driving without Insurance or Registered vehicle"
        fine = 5000
        self.offensesList(offense, fine)
    I = input("Is He / She vehicle louder as normal? (yes|no): ")
    if I.lower() == "yes":
        offense = "Vehicle is louder as normal (Modified Exhaust)"
        fine = 1750
        self.offensesList(offense, fine)
    J = input("Was He / She parked illegally (yes|no): ")
    if J.lower() == "yes":
        offense = "Driver Parked Illegally"
        fine = 1000
        self.offensesList(offense, fine)
    K = input("Is the vehicle defected in anyway? (yes|no): ")
    if K.lower() == "yes":
        offense = "Vehicle defects"
        fine = 120
        self.offensesList(offense, fine)
    L = input("Was He / She Wearing a seatbelt (yes|no): ")
    if L.lower() == "yes":
        offense = "Vehicle defects"
        fine = 400
        self.offensesList(offense, fine)
    
   

    