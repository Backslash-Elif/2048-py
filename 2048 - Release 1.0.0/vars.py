#================================imports, checks and pre-configs================================
import os, platform
print("vars.py: os and platform were imported.")

osName = platform.system()
print("vars.py: Operating system was detected as: \""+osName+"\".")

if osName == "Windows":
    path = '%s\\2048_game\\' %  os.environ['APPDATA']

else:
    print("vars.py: ERR: Your operating system currently isn't supported. Sorry.")
    import sys
    sys.exit("Unsupported OS")

pathToSave = path+"score.ini"
pathToSettings = path+"settings.ini"

#global variables

colorList = {" ": "black", 0: "royalblue", 2: "turquoise", 4: "SpringGreen", 8: "lime", 16: "yellowgreen", 32: "orange", 64: "darkorange", 128: "orangered", 256: "red", 512: "deeppink", 1024: "darkviolet", 2048: "mediumblue", 4096: "mediumblue", 8192: "mediumblue", 16384: "mediumblue", 32768: "mediumblue", 65536: "mediumblue", 131072: "red", "Enter": "black", "=": "black", "Start": "black", " Game": "black", "[T]": "black", "  Tuto": "black", "rial  ": "black"}
game = []
gameRunning = True
gameOver = True
titleScreenActive = True
points = 0
soundPlaying = False

def setVal():#loads the score and the settings from the files and makes them if they are not present
    global high_score, high_score_points, loadSecret, path, music, sound, colors, motion
    try: 
        os.mkdir(path)
        print("vars.py: WARN: 2048 directory does not exist.")
        print("vars.py: NOTE: 2048 directory created successfully.")
    except OSError as error: 
        print("vars.py: 2048 directory exists.")
    print("vars.py: 2048 directory is: \""+path+"\"")

    while True:
        try:
            scoreFile = open(pathToSave)
            print("vars.py: Save file exists and has been successfully opened.")
        except:
            scoreFile = open(pathToSave, "w")
            scoreFile.write("Backslash 2400 1723-9642-5792-1075")
            print("vars.py: WARN: Save file does not exist.")
            print("vars.py: NOTE: Save file successfully created with default values.")
            continue
        break

    scoreContents = scoreFile.read()
    tempScore = scoreContents.split(" ")
    high_score = tempScore[0]
    high_score_points = int(tempScore[1])
    loadSecret = tempScore[2]
    scoreFile.close()
    scoreFile = open(pathToSave)

    while True:
        try:
            settingsFile = open(pathToSettings)
            print("vars.py: Settings file exists and has been successfully opened.")
        except:
            settingsFile = open(pathToSettings, "w")
            settingsFile.write("1 True True True")
            print("vars.py: WARN: Settings file does not exist.")
            print("vars.py: NOTE: Save file successfully created with default values.")
            continue
        break

    settingsContents = settingsFile.read()
    tempSet = settingsContents.split(" ")
    tempMusic = str(tempSet[0])
    tempSound = str(tempSet[1])
    tempColors = str(tempSet[2])
    tempMotion = str(tempSet[3])
    settingsFile.close()
    settingsFile = open(pathToSettings)

    resetSettings = False
    music = int(tempMusic)
    if tempSound == "True":
        sound = True
    elif tempSound == "False":
        sound = False
    else:
        resetSettings = True
    if tempColors == "True":
        colors = True
    elif tempColors == "False":
        colors = False
    else:
        resetSettings = True
    if tempMotion == "True":
        motion = True
    elif tempMotion == "False":
        motion = False
    else:
        resetSettings = True
    
    if resetSettings == True:
        settingsFile = open(pathToSettings, "w")
        settingsFile.write("True True True True")
        settingsFile.close()
        settingsFile = open(pathToSettings)