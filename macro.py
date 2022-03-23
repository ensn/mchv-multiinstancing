import keyboard, time, readfiles
import pynput.mouse as pynm
import pynput.keyboard as pynk
import win32gui, win32con
global mouse, keys, focusedInstance

mouse = pynm.Controller()
keys = pynk.Controller()

toplist = []
winlist = []
def enum_callback(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
        
def getwinlist():
    win32gui.EnumWindows(enum_callback, toplist)
    window = [(hwnd, title) for hwnd, title in winlist if "minecraft" in title.lower()]
    return window

def focusWindow(indx, window):
    window = window[indx]
    win32gui.SetForegroundWindow(window[0])

def click(x, y):
    global mouse
    mouse.position = (x,y)
    time.sleep(DELAYS[6][0])
    mouse.press(pynm.Button.left)
    time.sleep(DELAYS[7][0])
    mouse.release(pynm.Button.left)

def send(x):
    global keys
    keys.press(x)
    time.sleep(DELAYS[8][0])
    keys.release(x)
    time.sleep(DELAYS[9][0])

def reset(minecrafts):
    global focusedInstance
    send(pynk.Key.esc)
    time.sleep(DELAYS[0][0])
    click(CLICKS[0][0], CLICKS[0][1])
    time.sleep(DELAYS[1][0])
    click(CLICKS[1][0], CLICKS[1][1])
    time.sleep(DELAYS[2][0])
    click(CLICKS[2][0], CLICKS[2][1])
    time.sleep(DELAYS[3][0])
    click(CLICKS[3][0], CLICKS[3][1])
    time.sleep(DELAYS[4][0])
    if focusedInstance==instances-1:
        focusedInstance=0
    else:
        focusedInstance+=1
    focusWindow(focusedInstance, minecrafts)
    time.sleep(DELAYS[5][0])
    send(pynk.Key.esc)
            
class GameMacro:
    def __init__(this, key, action):
        this.step=0
        this.key=key
        this.action=action
        this.start_time_sec=0
    def periodic_call(this):
        if this.step==0:
            if keyboard.is_pressed(this.key):
                this.start_time_sec = time.perf_counter()
                send(this.action)
                this.step += 1
        if this.step==1:
            if time.perf_counter() > this.start_time_sec + DELAYS[10][0]:
                this.step=0

DELAYS=readfiles.readfile("delays.txt", 1, "f")
CLICKS=readfiles.readfile("clicks.txt", 2, "i")
minecrafts=getwinlist()
instances=len(minecrafts)
focusedInstance=0
focusWindow(focusedInstance, minecrafts)
ingamemacros=[GameMacro("t", "7"), GameMacro("g", "8"), GameMacro("v", "9"), GameMacro("c", pynk.Key.f5)]
while True:
    if keyboard.is_pressed("y"):
        reset(minecrafts)
    for gamemacro in ingamemacros:
        gamemacro.periodic_call() 
