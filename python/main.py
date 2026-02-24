from helpers import *
import sys


def main():
    
    #check if OpenSCAD path exists
    print("Checking for OpenSCAD path...")
    os = checkOpenSCADPathExists()
    if os != -1:
        print(f"OpenSCAD path exists on {os}.")
    else:        
        print("OpenSCAD path does not exist. Please install OpenSCAD and ensure it is in the default location.")
        sys.exit(1)
    
    #open menu
    while True:
        showMenu()

def showMenu():
    print("Menu:")
    print("1. Create CSV Template")
    print("2. Generate STL Files from CSV")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        createCSVTemplate()
        print("CSV template created successfully.")
    elif choice == "2":
        print("Generating STL files from CSV...")
        filePath = input("Enter the path to the CSV file: ")
        data = parseCSV(filePath)
        print("************************************************************")
        print("Data from CSV:")
        for row in data:
            print(row)
        print("************************************************************")
        # Call the function to generate STL files from CSV here
        
        print("STL files generated successfully.")
    elif choice == "4":
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")
        showMenu()

if __name__ == "__main__":
    main()