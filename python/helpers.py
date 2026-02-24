
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