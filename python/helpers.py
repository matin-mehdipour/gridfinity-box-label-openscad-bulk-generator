
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
    
def createCSVTemplate():
    import csv
    with open('template.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Label Text', 'Font Size', 'Show Screw Icon', 'Output File Name'])
        writer.writerow(['Example Label', '12', 'True', 'example_label.stl'])