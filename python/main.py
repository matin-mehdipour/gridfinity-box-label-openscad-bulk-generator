from helpers import *
import sys


def main():
    
    #check if OpenSCAD path exists
    print("Checking for OpenSCAD path...")
    if checkOpenSCADPathExists() == 0:
        print("OpenSCAD path exists.")
    else:        
        print("OpenSCAD path does not exist. Please install OpenSCAD and ensure it is in the default location.")
        sys.exit(1)
    
    #open menu
    while True:
        showMenu()

def showMenu():
    print("Menu:")
    print("1. Create CSV Template")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        createCSVTemplate()
        print("CSV template created successfully.")
    elif choice == "2":
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")
        showMenu()

if __name__ == "__main__":
    main()