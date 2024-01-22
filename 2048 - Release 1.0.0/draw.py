#================================imports, checks and pre-configs================================

#main importing
import turtle, time, threading, vars, misc
print("draw.py: turtle, time, vars(.py), misc(.py) have been imported.")
from turtle import *
print("draw.py: additional turtle resources have been imported.")
from game import swipeUp, swipeLeft, swipeRight, swipeDown
print("draw.py: swipeUp, swipeLeft, swipeRight, swipeDown have been imported.")

#python configure
t = turtle
window = turtle.Screen()
t.speed(0)
t.delay(0)

#check if required modules are installed
try:
    from pydub import AudioSegment
    from pydub.playback import play
    t.forward(30)
except:
    from install import installModules
    print("draw.py: installModules was imported.")
    installModules("draw")
    from pydub import AudioSegment
    from pydub.playback import play
print("draw.py: AudioSegment, play have been imported.")

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


def drawField(): #draws the playing field
    fs = 150 #field size
    t.pu()
    t.color("gray")
    t.pencolor("white")

    t.width(5)
    t.home()
    t.goto(fs*2, fs*2)
    begin_fill()
    t.goto(fs*2, fs*-2)
    t.goto(fs*-2, fs*-2)
    t.goto(fs*-2, fs*2)
    end_fill()

    t.goto(fs*2, fs*2)
    t.pd()
    t.goto(fs*2, fs*-2)
    t.goto(fs, fs*-2)
    t.goto(fs, fs*2)
    t.goto(0, fs*2)
    t.goto(0, fs*-2)
    t.goto(fs*-1, fs*-2)
    t.goto(fs*-1, fs*2)
    t.goto(fs*-2, fs*2)
    t.goto(fs*-2, fs*-2)
    t.goto(fs*2, fs*-2)
    t.goto(fs*2, fs*-1)
    t.goto(fs*-2, fs*-1)
    t.goto(fs*-2, 0)
    t.goto(fs*2, 0)
    t.goto(fs*2, fs)
    t.goto(fs*-2, fs)
    t.goto(fs*-2, fs*2)
    t.goto(fs*2, fs*2)

    t.width(1)
    

def fillboard(content2): #fills the values from "game" into the table created by "drawField()"
    content = []
    for i in range(16):
        if content2[i] != 0:
            content.append(content2[i])
        else:
            content.append(" ")
    fs = 150
    fs2 = fs*2
    t.pu()
    colors = vars.colorList
    xTab = [225, 75, -75, -225]
    yTab = [150, 0, -150, -300]
    for i1 in range(4):
        for i2 in range(4):
            t.goto((xTab[i2])*-1, (yTab[i1])+(len(str(content[i1*4+i2]))-1)*11)
            t.color(colors[content[i1*4+i2]])
            t.write(content[i1*4+i2], False, "center", font=("Consolas", round(80/len(str(content[i1*4+i2])))+20, "normal"))

def tutorial(): #the tutorial
    t.clear()
    t.home()
    t.color("white")
    t.write("This game is best enjoyed in fullscreen.", False, "center", font=("Consolas", 30, "normal"))
    winWidth = window.window_width()
    winHeight = window.window_height()
    t.goto((winWidth/-2)+10, (winHeight/-2)+10)
    t.color("white")
    t.write("Press [enter] or (A) to continue.", False, "left", font=("Consolas", 20, "normal"))
    while misc.lastKey != "Key.enter": #wait for user input
        time.sleep(0.1)
        t.update()
    playSound("sounds/accepted.wav")
    temp = []
    vars.game = [0, 0, 0, 2, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0]
    misc.lastKey = ""
    while len(temp)<4:
        t.clear()
        drawField()
        fillboard(vars.game)
        t.goto(0, 400)
        t.color("white")
        t.write("Move the numbers with the arrow keys,\n[W], [A], [S], [D] or the left joystick.\nTry it out! ("+str(len(temp))+"/4)", False, "center", font=("Consolas", 30, "normal"))
        validKey = False
        while validKey == False: #wait for user input
            t.update()
            if misc.lastKey=="w" or misc.lastKey=="a" or misc.lastKey=="s" or misc.lastKey=="d" or misc.lastKey=="Key.up" or misc.lastKey=="Key.left" or misc.lastKey=="Key.down" or misc.lastKey=="Key.right":
                validKey = True
        if misc.lastKey=="w" or misc.lastKey=="Key.up":
            swipeUp()
        if misc.lastKey=="a" or misc.lastKey=="Key.left":
            swipeLeft()
        if misc.lastKey=="s" or misc.lastKey=="Key.down":
            swipeDown()
        if misc.lastKey=="d" or misc.lastKey=="Key.right":
            swipeRight()
        temp.append(misc.lastKey)
        misc.lastKey = ""
        t.clear()
        drawField()
        fillboard(vars.game)
        t.goto(0, 400)
        t.color("white")
        t.write("Move the numbers with the arrow keys,\n[W], [A], [S], [D] or the left joystick.\nTry it out! ("+str(len(temp))+"/4)", False, "center", font=("Consolas", 30, "normal"))
    time.sleep(1)
    temp = []
    vars.game = [0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
    misc.lastKey = ""
    while len(temp)<1:
        t.clear()
        drawField()
        fillboard(vars.game)
        t.goto(0, 400)
        t.color("white")
        t.write("You can combine two numbers of the same value.\nTry it out by pressing [W], [up key]\nor moving the left joystick up.", False, "center", font=("Consolas", 30, "normal"))
        validKey = False
        while validKey == False:
            t.update()
            if misc.lastKey=="w" or misc.lastKey=="Key.up":
                validKey = True
        if misc.lastKey=="w" or misc.lastKey=="Key.up":
            swipeUp()
        temp.append(misc.lastKey)
        misc.lastKey = ""
        t.clear()
        drawField()
        fillboard(vars.game)
        t.goto(0, 400)
        t.color("white")
        t.write("You can combine two numbers of the same value.\nTry it out by pressing [W], [up key]\nor moving the left joystick up.", False, "center", font=("Consolas", 30, "normal"))
    time.sleep(1)
    t.clear()
    t.goto(0,400)
    t.write("The 5 rules fo 2048:", False, "center", font=("Consolas", 50, "normal"))
    t.goto(0, 300)
    t.color("royalblue")
    t.write("The main objective of the game is to merge tiles with the same number\nto create a tile with a higher number. (2&2 -> 4)", False, "center", font=("Consolas", 24, "normal"))
    t.goto(0, 100)
    t.color("turquoise")
    t.write("You can slide the tiles in four directions: up, down, left, and right.\nAll tiles will slide as far as possible in the chosen direction\nuntil they reach the edge of the grid or collide with another tile", False, "center", font=("Consolas", 24, "normal"))
    t.goto(0, -50)
    t.color("SpringGreen")
    t.write("After each slide, a new tile with the number 2 or 4 will appear in\nan empty random spot on the grid.", False, "center", font=("Consolas", 24, "normal"))
    t.goto(0, -250)
    t.color("lime")
    t.write("The game continues until the grid is completely filled and there are\nno more possible moves, or until you reach\nthe tile with the number 2048.", False, "center", font=("Consolas", 24, "normal"))
    t.goto(0, -450)
    t.color("yellowgreen")
    t.write("Planning and strategy are key to achieving a high score in 2048.\nYou need to think ahead and consider the consequences of each move,\nas merging tiles in the wrong order can block other\npotential merges and limit your options.", False, "center", font=("Consolas", 24, "normal"))
    winWidth = window.window_width()
    winHeight = window.window_height()
    t.goto((winWidth/-2)+10, (winHeight/-2)+10)
    t.color("white")
    t.write("Press [enter] or (A) to end the tutorial.", False, "left", font=("Consolas", 20, "normal"))
    misc.lastKey = ""
    while misc.lastKey != "Key.enter": #wait for user input
        time.sleep(0.1)
        t.update()
    playSound("sounds/accepted.wav")
    transition(0)
    titleScreen(4)

def titleScreen(length): #the titlescreen
    length = length*20
    t.clear()
    t.pu()
    t.goto(-75, 150)
    t.color("deepskyblue")
    t.write("0", False, "center", font=("Consolas", 100, "normal"))
    vars.game = [2, 0, 4, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fillboard(vars.game)
    t.goto(300, 300)
    t.pd()
    t.color("white")
    t.width(5)
    t.goto(-300, 300)
    t.goto(-300, 150)
    t.goto(300, 150)
    t.goto(300, 300)
    t.goto(300, 150)
    t.goto(150, 150)
    t.goto(150, 300)
    t.goto(0, 300)
    t.goto(0, 150)
    t.goto(-150, 150)
    t.goto(-150, 300)
    pu()
    if vars.motion == True:
        t.goto(-300, 300)
        t.pd()
        t.left(45)
        t.forward(length)
        t.right(45)
        for i in range(4):
            t.forward(150)
            t.left(45)
            t.back(length)
            t.forward(length)
            t.right(45)
        t.right(90)
        t.forward(150)
        t.right(45)
        t.forward(length)
        t.pu()
    t.home()
    t.goto(0, -70)
    t.write("Press [ENTER] or (A) to start a new Game.", False, "center", font=("Consolas", 30, "normal"))
    t.goto(0, -150)
    t.write("Press [T] or (Y) for a tutorial.", False, "center", font=("Consolas", 20, "normal"))
    t.goto(0, -200)
    t.write("Press [S] or (X) for settings.", False, "center", font=("Consolas", 20, "normal"))

def transition(mode): #the transition between screens
    if vars.motion == True:
        winWidth = window.window_width()
        winHeight = window.window_height()
        if winWidth>winHeight:
            scr = winWidth
        else:
            scr = winHeight
        scr= scr*1.3
        t.right(90)
        multi = 40
        if mode==1:
            multi=50
        t.width(scr/multi)
        pu()
        if mode !=1:
            t.color(0.1, 0.1, 0.1)
            for i in range(multi):
                a = i+1
                t.goto(scr*-0.5/(multi/(multi+1-a)), 0)
                t.pd()
                t.circle(scr*0.5/(multi/(multi+1-a)))
                t.pu()
            t.bgcolor(0.1, 0.1, 0.1)
            t.clear()
        if mode == 2:
            if vars.colors == True:
                t.color(100/255, 0, 0)
            else:
                t.color(0.2, 0.2, 0.2)
        else:
            t.color(0.2, 0.2, 0.2)

        a = multi +1
        time.sleep(0.1)
        for i in range(multi):
            a = a-1
            t.goto(scr*-0.5/(multi/(multi+1-a)), 0)
            t.pd()
            t.circle(scr*0.5/(multi/(multi+1-a)))
            t.pu()
        if mode == 2:
            if vars.colors == True:
                t.bgcolor(100/255, 0, 0)
            else:
                t.bgcolor(0.2, 0.2, 0.2)
        else:
            t.bgcolor(0.2, 0.2, 0.2)
        t.clear()
        t.home()
        if mode==1:
            multi=40

def setBGColor(): #sets the backgroundcolor during gameplay
    if vars.colors == True:
        value = vars.points%1200/2

        if value<=99:
            t.bgcolor(100/255, value%100/255, 0)#100, up, 0

        elif value>=100 and value<=199:
            t.bgcolor((100-value%100)/255, 100/255, 0)#down, 100, 0

        elif value>=200 and value<=299:
            t.bgcolor(0, 100/255, value%100/255)#0, 100, up

        elif value>=300 and value<=399:
            t.bgcolor(0, (100-value%100)/255, 100/255)#0, down, 100

        elif value>=400 and value<=499:
            t.bgcolor(value%100/255, 0, 100/255)#up, 0, 100

        elif value>=500:
            t.bgcolor(100/255, 0, (100-value%100)/255)#100, 0, down
    else:
        t.bgcolor(0.2, 0.2, 0.2)

def settings(): #the settings page
    misc.lastKey = ""
    cur = 0
    resetGame = False
    description = [
        "Turns the music on or off.",
        "Turns the sounds on or off.",
        "Turns the ambient colors (background during gameplay) on or off.",
        "Enables or disables motion. (e.g. screen-transitions)",
        "See who made this game.",
        "Reset all the settings back to the default values.",
        "Did someone get a higher score than you? (RESETS ALL SETTINGS AND SCORES. BE CAREFUL!!!)"
    ]
    while misc.lastKey != "Key.esc":
        t.clear()
        t.pu()
        t.goto(190, 190)
        t.right(90)
        begin_fill()
        t.color(0.1, 0.1, 0.1)
        for i in range(2):
            t.forward(300)
            t.left(90)
            t.forward(125)
            t.left(90)
        end_fill()
        t.home()
        #option values
        t.color("white")
        
        t.goto(-410, 200-(cur*50))
        t.color(1, 0.3, 0)
        t.width(3)
        t.pd()
        for i in range(2):
            t.forward(820)
            t.left(90)
            t.forward(40)
            t.left(90)
        t.pu()
        t.home()

        t.goto(-420, 250)
        t.color("white")
        t.pd()
        t.goto(-420, -110)
        t.goto(420, -110)
        t.goto(420, 250)
        t.goto(-420, 250)
        t.pu()
        t.width(1)

        winWidth = window.window_width()
        winHeight = window.window_height()
        t.goto((winWidth/-2)+10, (winHeight/-2)+10)
        t.color("white")
        t.write(description[cur], False, "left", font=("Consolas", 12, "normal"))
        t.goto((winWidth/2)-15, (winHeight/2)-25)
        t.write("[ESC], (B): Go back", False, "right", font=("Consolas", 12, "normal"))
        

        t.color("white")
        t.goto(-400, 280)
        t.write("Settings", False, "left", font=("Consolas", 50, "normal"))
        #option names
        t.goto(-400, 200)
        t.write("Music", False, "left", font=("Consolas", 24, "normal"))
        t.goto(-400, 150)
        t.write("Sound", False, "left", font=("Consolas", 24, "normal"))
        t.goto(-400, 100)
        t.write("Ambient colors", False, "left", font=("Consolas", 24, "normal"))
        t.goto(-400, 50)
        t.write("Reduced motion", False, "left", font=("Consolas", 24, "normal"))
        t.goto(-400, 0)
        t.write("Credits", False, "left", font=("Consolas", 24, "normal"))
        t.goto(-400, -50)
        t.write("Reset settings", False, "left", font=("Consolas", 24, "normal"))
        t.color("red")
        t.goto(-400, -100)
        t.write("Reset game", False, "left", font=("Consolas", 24, "normal"))
        t.color("white")

        
        #values (formating: "xxxxxx"+" "+"xxxxxx")
        t.goto(380, 200)
        if vars.music == 0:
            t.write("off", False, "right", font=("Consolas", 24, "normal"))
        elif vars.music == 1:
            t.write("Scourge of the Universe", False, "right", font=("Consolas", 24, "normal"))
        elif vars.music == 2:
            t.write("Unholy Ambush", False, "right", font=("Consolas", 24, "normal"))
        elif vars.music == 3:
            t.write("sanctuary", False, "right", font=("Consolas", 24, "normal"))
        if vars.sound == True:
            t.goto(200, 150)
        else:
            t.goto(75, 150)
        t.write("on     off    ", False, "left", font=("Consolas", 24, "normal"))
        if vars.colors == True:
            t.goto(200, 100)
        else:
            t.goto(75, 100)
        t.write("on     off    ", False, "left", font=("Consolas", 24, "normal"))
        if vars.motion == True:
            t.goto(75, 50)
        else:
            t.goto(200, 50)
        t.write("on     off    ", False, "left", font=("Consolas", 24, "normal"))
        t.goto(200, 0)
        t.write("select", False, "left", font=("Consolas", 24, "normal"))
        t.goto(200, -50)
        t.write("select", False, "left", font=("Consolas", 24, "normal"))
        t.goto(200, -100)
        if resetGame == True:
            t.color("red")
            t.write("REALLY", False, "left", font=("Consolas", 24, "normal"))
        else:
            t.write("select", False, "left", font=("Consolas", 24, "normal"))
        misc.lastKey = ""
        while not misc.lastKey.startswith("Key"):
            time.sleep(0.1)
            t.update()

        #curser movement
        if misc.lastKey == "Key.up":
            if cur != 0:
                cur = cur - 1
            else:
                playSound("sounds/critical.wav")
        if misc.lastKey == "Key.down":
            if cur != 6:
                cur = cur + 1
            else:
                playSound("sounds/critical.wav")
        
        #option actions
        if misc.lastKey == "Key.enter":
            if cur == 0:
                playSound("sounds/select.wav")
                if vars.music != 3:
                    vars.music = vars.music + 1
                else:
                    vars.music = 0
            if cur == 1:
                playSound("sounds/select.wav")
                if vars.sound == True:
                    vars.sound = False
                else:
                    vars.sound = True
            if cur == 2:
                playSound("sounds/select.wav")
                if vars.colors == True:
                    vars.colors = False
                else:
                    vars.colors = True
            if cur == 3:
                playSound("sounds/select.wav")
                if vars.motion == True:
                    vars.motion = False
                else:
                    vars.motion = True
            if cur == 4:
                playSound("sounds/accepted.wav")
                t.clear()
                t.goto(0, 250)
                t.write("Game by:", False, "center", font=("Consolas", 24, "normal"))
                t.goto(0, 150)
                t.write("Backslash", False, "center", font=("Consolas", 50, "normal"))
                t.goto(0, 130)
                t.write("================ aka Neo ================", False, "center", font=("Consolas", 12, "normal"))
                t.goto(0, -50)
                t.write("Music by:", False, "center", font=("Consolas", 24, "normal"))
                t.goto(0, -80)
                t.write("DM DOKURO (youtube.com/@DMDOKURO)", False, "center", font=("Consolas", 12, "normal"))
                t.goto(0, -110)
                t.write("Wels (welsmusic.ch)", False, "center", font=("Consolas", 12, "normal"))
                t.goto(0, -200)
                t.write("Sounds by:", False, "center", font=("Consolas", 24, "normal"))
                t.goto(0, -230)
                t.write("freesounds.org, pixabay.com", False, "center", font=("Consolas", 12, "normal"))
                misc.lastKey = ""
                while misc.lastKey == "":
                    time.sleep(0.1)
                    t.update()
                misc.lastKey = ""
                playSound("sounds/accepted.wav")
            if cur == 5:
                playSound("sounds/select.wav")
                vars.music = True
                vars.sound = True
                vars.colors = True
                vars.motion = True
            
            if cur == 6:
                if resetGame == True:
                    resetGame = False
                    vars.music = True
                    vars.sound = True
                    vars.colors = True
                    vars.motion = True
                    vars.high_score = "Backslash"
                    vars.high_score_points = 2400
                    misc.saveScore()
                    misc.saveSettings()
                    playSound("sounds/critical.wav")
                else:
                    playSound("sounds/information.wav")
                    resetGame = True
        if cur != 6:
            if resetGame == True:
                resetGame = False
                playSound("sounds/select.wav")
    misc.saveSettings()
    playSound("sounds/accepted.wav")
    transition(0)
    titleScreen(4)
