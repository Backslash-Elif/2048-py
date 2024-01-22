#================================imports, checks and pre-configs================================

#turtle configuration
import turtle
print("main.py: turtle has been imported.")
from turtle import *
print("main.py: additional turtle resources have been imported.")
t = turtle
t.title("2048")
window = turtle.Screen()
t.speed(0)
t.delay(0)
t.ht()

root = window._root
root.iconbitmap("icon/cube.ico")

#loading screen
t.bgcolor(1, 1, 1)
t.color("black")
t.write("Loading.", False, "center", font=("Consolas", 20, "normal"))
t.pu()
t.goto(0, -100)
t.write("If this is the first time running this game, loading might take longer.", False, "center", font=("Consolas", 15, "normal"))
t.goto(-200, -300)
t.color("black")
t.width(28)
t.pd()
t.goto(200, -300)
t.width(20)
t.color("white")
t.goto(-200, -300)
t.width(17)
t.color(1, 0, 0)
t.forward(30)

#main importing
import time, threading, math, misc, vars
print("main.py: time, threading, math, misc(.py), vars(.py) have been imported.")
t.forward(10)
from draw import *
print("main.py: draw(.py) has been imported.")
t.forward(10)
from game import *
print("main.py: draw(.py) has been imported.")
t.forward(10)
from misc import startKeyDetect, startGamepad
print("main.py: startKeyDetect, startGamepad have been imported.")
t.forward(10)
from vars import setVal
print("main.py: setScore has been imported.")
t.forward(10)
from sound import *
print("main.py: sound(.py) has been imported.")
t.forward(10)

#check if required modules are installed
try:
    from pydub import AudioSegment
    from pydub.playback import play
    import pyaudio #pydub uses pyaudio which, must be installed.
    t.forward(30)
except:
    from install import installModules
    print("main.py: installModules was imported.")
    installModules("main")
    from pydub import AudioSegment
    from pydub.playback import play
print("main.py: AudioSegment, play have been imported.")

#important functions that must start/run
startKeyDetect()
setVal()
startSound()
startGamepad()

#sound system
def playS():
    while vars.soundPlaying == True:
        time.sleep(0.01)
    if vars.sound == True:
        vars.soundPlaying = True
        play(AudioSegment.from_wav(musicFile))
        vars.soundPlaying = False

def playSound(sound):
    global musicFile
    musicFile = sound
    thread = threading.Thread(target=playS)
    thread.start()

#anticheat
if vars.high_score_points%2==1 or len(vars.high_score)>16 or vars.loadSecret!=(misc.cy(vars.high_score_points)):
    t.bye()
    playSound("sounds/game_over.wav")
    print("\033[1;31;40m")
    for i in range(666):
        print("CHEATER!!!")
    vars.titleScreenActive = False
    import shutil
    shutil.rmtree(vars.path)
    print("YOU CAN RESTART THE GAME BUT THE SETTINGS AND SCORES HAVE BEEN RESET.")
    import sys
    sys.exit("DO NOT CHEAT!!!")

t.forward(30)
transition(1)
dev = False

#================================Main game loop================================
while True:
    vars.titleScreenActive = True
    if dev:
        t.title("2048 [DEVELOPER OPTIONS ENABLED]")
    else:
        t.title("2048")
    t.bgcolor(0.2, 0.2, 0.2)
    titleScreen(4)
    lastTSnum = 4
    misc.lastKey = ""
    ee = ["aaa"]
    lastWinW = 0
    lastWinH = 0
    while misc.lastKey != "Key.enter": #wait for user to start the game
        try:
            lastTSnum = int(misc.lastKey)
            lastWinW = 0
            lastWinH = 0
        except:
            misc.lastKey = misc.lastKey
        if misc.lastKey != "":
            if len(ee)>2:
                ee.pop(0)
                ee.append(misc.lastKey)
                if ee[0]+ee[1]+ee[2]=="dev":
                    if dev:
                        dev = False
                        t.title("2048")
                    else:
                        dev = True
                        t.title("2048 [DEVELOPER OPTIONS ENABLED]") #dev options ("dev" on start screen) puts game into debug mode
                if ee[0]+ee[1]+ee[2]=="hii":
                    t.goto(0, -400)
                    t.write("Hewwwo! :3", False, "center", font=("Consolas", 100, "normal")) #easter egg :3
            else:
                ee.append(misc.lastKey)
        if misc.lastKey == "t" or misc.lastKey == "T": #tutorial
            playSound("sounds/accepted.wav")
            transition(0)
            tutorial()
            lastWinW = 0
            lastWinH = 0
        if misc.lastKey == "s" or misc.lastKey == "S": #settings
            playSound("sounds/accepted.wav")
            transition(0)
            settings()
            lastWinW = 0
            lastWinH = 0
        misc.lastKey = ""
        winWidth = window.window_width()
        winHeight = window.window_height()
        if lastWinW != winWidth or lastWinH != winHeight: #update if windows size changed
            t.clear()
            titleScreen(lastTSnum)
            t.goto((winWidth/-2)+10, (winHeight/-2)+10)
            t.write("HI: "+vars.high_score+" -> "+str(vars.high_score_points), False, "left", font=("Consolas", 20, "normal"))
            t.goto((winWidth/2)-10, (winHeight/-2)+10)
            t.write("-2023 Backs\\ash Studios-", False, "right", font=("Consolas", 20, "normal"))
            lastWinW = winWidth
            lastWinH = winHeight
        t.update()
    
    #game loading
    playSound("sounds/accepted.wav")
    vars.titleScreenActive = False
    transition(2)
    vars.gameOver = False
    startime = round(time.time())
    timeDifference = -1

    vars.game = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    setupGame()
    if dev:
        vars.game = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512 ,1024 ,2048 ,4096 ,8192 ,16384 ,32768]
        vars.points = 9999999
    gameBackup = vars.game
    vars.gameRunning = True
    t.clear()
    drawField()

    #gameplay loop
    while vars.gameRunning == True: #the main game
        winWidth = window.window_width()
        winHeight = window.window_height()
        t.pu()
        t.goto((winWidth/-2)+10, (winHeight/-2)+10)
        t.color("white")
        t.write("SCORE: "+str(vars.points), False, "left", font=("Consolas", 20, "normal"))
        fillboard(vars.game)
        setBGColor()
        vars.gameOver = checkGameOver()
        if vars.gameOver==True:
            #game over screen
            t.pu()
            t.color("white")
            t.goto(5, 305)
            t.write("GAME OVER", False, "center", font=("Consolas", 150, "normal"))
            t.goto(-5, 305)
            t.write("GAME OVER", False, "center", font=("Consolas", 150, "normal"))
            t.goto(5, 295)
            t.write("GAME OVER", False, "center", font=("Consolas", 150, "normal"))
            t.goto(-5, 295)
            t.write("GAME OVER", False, "center", font=("Consolas", 150, "normal"))
            t.color("red")
            t.goto(0, 300)
            t.write("GAME OVER", False, "center", font=("Consolas", 150, "normal"))
            vars.gameRunning = False
            playSound("sounds/game_over.wav")
        misc.lastKey=""
        validKey = False
        if vars.gameRunning==True:
            playSound("sounds/click.wav")
            while validKey == False: #wait for user input
                t.update()
                if misc.lastKey=="w" or misc.lastKey=="a" or misc.lastKey=="s" or misc.lastKey=="d" or misc.lastKey=="Key.up" or misc.lastKey=="Key.left" or misc.lastKey=="Key.down" or misc.lastKey=="Key.right":
                    validKey = True
                #playtime counter
                currentTime = round(time.time())
                sec = (currentTime - startime)
                if timeDifference != sec:
                    timeDifference = sec
                    min = sec/60
                    hrs = min/60
                    sec = sec%60
                    min = math.floor(min%60)
                    hrs = math.floor(hrs%24)
                    if len(str(sec)) == 1:
                        sec = "0"+str(sec)
                    if len(str(min)) == 1:
                        min = "0"+str(min)
                    if len(str(hrs)) == 1:
                        hrs = "0"+str(hrs)
                    t.title("2048 - [Highscore: "+str(vars.high_score_points)+"] [Playtime: "+str(hrs)+":"+str(min)+":"+str(sec)+"]") #window title
            #game actions
            if misc.lastKey=="w" or misc.lastKey=="Key.up":
                swipeUp()
            if misc.lastKey=="a" or misc.lastKey=="Key.left":
                swipeLeft()
            if misc.lastKey=="s" or misc.lastKey=="Key.down":
                swipeDown()
            if misc.lastKey=="d" or misc.lastKey=="Key.right":
                swipeRight()
            for i in range(12*4+1):
                t.undo()

    #"kayote time" (to prevent a user to accidentally skip the game over screen)
    time.sleep(1)
    misc.lastKey = ""
    while misc.lastKey == "":
        t.update()
        time.sleep(0.1)
    
    t.clear()
    if vars.points > vars.high_score_points: #asks for a username if the score was higher than the highscore
        playSound("sounds/win.wav")
        user = ""
        misc.lastKey = ""
        while misc.lastKey != "Key.enter" or user == "":
            t.clear()
            t.goto(0, 200)
            t.color("white")
            t.write("Your score: "+str(vars.points), False, "center", font=("Consolas", 40, "normal"))
            t.home()
            t.write("Your name: "+user, False, "center", font=("Consolas", 70, "normal"))
            misc.lastKey = ""
            while misc.lastKey == "":
                time.sleep(0.01)
            if misc.lastKey.startswith("Key") == False and len(user) < 16:
                user = user + misc.lastKey
            if misc.lastKey == "Key.backspace" and len(user)!=0:
                user = user[0:(len(user)-1)]
            t.update()
    
        vars.high_score_points = vars.points
        vars.high_score = user
        misc.saveScore()
    vars.points = 0
    transition(0)  
