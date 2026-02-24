from helpers import *
import sys


def main():
    print("Checking for OpenSCAD path...")
    if checkOpenSCADPathExists() == 0:
        print("OpenSCAD path exists.")
    else:        
        print("OpenSCAD path does not exist. Please install OpenSCAD and ensure it is in the default location.")
        sys.exit(1)
    pass



if __name__ == "__main__":
    main()