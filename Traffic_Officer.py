import datetime
from ClassQuestions import Class_Questions


class TrafficOfficer:
    def __init__(self, name, badge_number, password):
        self.name = name
        self.badge_number = badge_number
        self.password = password
        self.logged_in = False
        self.class_questions = Class_Questions()  # Create an instance of Class_Questions

    def login(self, badge_number, password):
        if badge_number == self.badge_number and password == self.password:
            self.logged_in = True
            print(f"Welcome, {self.name}! You are now logged in as Traffic Officer {self.badge_number}.\n")
            self.class_questions.vehicleClass()  # Call the method using the instance
        else:
            print("Login failed. Please check your badge number and password.")

# Load traffic officer data from a text file
def load_traffic_officers(filename):
    officers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split()  
                if len(data) == 3:
                    name, badge_number, password = data
                    officer = TrafficOfficer(name, badge_number, password)
                    officers.append(officer)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return officers




class OfficerQuestions(TrafficOfficer):
        
    def vehicleClass(self):
        license_plate = input("Please enter your license plate number: ")
        filename = f"txt_data/number_plates/{license_plate}.txt"

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
            question_instance.bike()
        elif answer == "2":
            selected_class = "Car"
            question_instance.car()
        elif answer == "3":
            selected_class = "Bakkie"
            question_instance.bakkie()
        elif answer == "4":
            selected_class = "Truck"
            question_instance.truck()

        with open(filename, "w") as file:
            file.write(f"License Plate: {license_plate}\n")
            file.write(f"Vehicle Class: {selected_class}\n")


question_instance = Class_Questions()


