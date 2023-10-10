from os import system


class TrafficOfficer:
    def __init__(self, name, badge_number, password):
        self.name = name
        self.badge_number = badge_number
        self.password = password



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


def add_traffic_officer(filename, officer):
    with open(filename, 'a') as file:
        file.write(f"{officer.name} {officer.badge_number} {officer.password}\n")

if __name__ == "__main__":
    filename = "txt_Data/Traffic_Officer_Data/traffic_officers.txt"  
    traffic_officers = load_traffic_officers(filename)


    new_name = input("Enter the new officer's name: ")
    new_badge_number = input("Enter the new officer's badge number: ")
    new_password = input("Enter the new officer's password: ")

    new_officer = TrafficOfficer(new_name, new_badge_number, new_password)
    add_traffic_officer(filename, new_officer)

    traffic_officers.append(new_officer)  

    print(f"New officer '{new_name}' has been added to the file.")
    system("clear")
