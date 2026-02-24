import platform
import os
import csv
    
#determines OS the script is running on
def checkOS():

    os_name = platform.system()
    return os_name

#checks for presence of OpenSCAD in default location based on OS
def checkOpenSCADPathExists():
    osName = checkOS()
    if osName == "Windows":
        path = "C:\\Program Files\\OpenSCAD\\openscad.exe"
    elif osName == "Linux":
        path = "/usr/bin/openscad"     
    elif osName == "Darwin":  # macOS
        path = "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"
    else:
        return -1  # Unsupported OS
    if os.path.exists(path):
        return osName
    
#parses CSV file and add to array of dicts
def parseCSV(fileName):
    data = []
    with open(fileName, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

    
    
#create csv template for user input
def createCSVTemplate():
    import csv
    with open('template.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Label Text', 'Font Size', 'Show Screw Icon', 'Output File Name'])
        writer.writerow(['Example Label', '12', 'True', 'example_label.stl'])
        
        