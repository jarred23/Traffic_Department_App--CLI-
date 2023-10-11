import os

folder_path = "txt_Data/number_plates"

def get_data_for_license_plate(license_plate):
    # Construct the file path
    file_path = os.path.join(folder_path, license_plate + ".txt")

    # Check if the file exists
    if os.path.isfile(file_path):
        # If the file exists, read and return its content
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    else:
        # If the file does not exist, return a message indicating that the license plate is not found
        return "License plate not found in the system."

def mainUser():
    if __name__ == "__main__":
        while True:
            license_plate = input("Enter a license plate number (or 'exit' to quit): ")
            if license_plate.lower() == 'exit':
                break
            else:
                result = get_data_for_license_plate(license_plate)
                print(result)
