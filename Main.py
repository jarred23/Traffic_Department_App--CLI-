from Traffic_Officer import load_traffic_officers
from Users import *
from os import system
system("clear")
print("Please enter 1 if you are a Traffic Officer")
print("Please enter 2 if you are a User\n")

answer = int(input("Please enter your choice: "))

if answer == 1:
    system("clear")
    filename = "txt_data/Traffic_Officer_Data/traffic_officers.txt"  # Change to the path of your data file
    traffic_officers = load_traffic_officers(filename)

    print("Welcome Traffic Officer")
    print("-------------------------------------------\n")
    
    badge_number = input("Enter your badge number: ")
    password = input("Enter your password: ")
    
    matched_officer = next((officer for officer in traffic_officers if officer.badge_number == badge_number), None)
    
    if matched_officer:
        matched_officer.login(badge_number, password)
    else:
        print("No matching officer found. Please check your badge number and password.")
    
elif answer == 2:
    system("clear")
    if __name__ == "__main__":
        while True:
            license_plate = input("Enter a license plate number (or 'exit' to quit): ")
            if license_plate.lower() == 'exit':
                break
            else:
                result = get_data_for_license_plate(license_plate)
                print(result)
                print("\nPLEASE GET THIS SORTED OUT BY YOUR CLOSETEST TRAFFIC DEPARTMENT!")

else:
    
    print("Please enter the correct number!")
