
def main():
    print("Checking for OpenSCAD path...")
    if checkOpenSCADPathExists() == 0:
        print("OpenSCAD path exists.")
    else:        print("OpenSCAD path does not exist. Please install OpenSCAD and ensure it is in the default location.")
    pass

def checkOS():
    import platform
    os_name = platform.system()
    return os_name

def checkOpenSCADPathExists():
    os = checkOS()
    if os == "Windows":
        import os
        path = "C:\\Program Files\\OpenSCAD\\openscad.exe"
    elif os == "Linux":
        import os
        path = "/usr/bin/openscad"
        
    elif os == "Darwin":  # macOS
        import os
        path = "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"
    else:
        return -1  # Unsupported OS
    if os.path.exists(path):
        return 0  # Path exists

if __name__ == "__main__":
    main()