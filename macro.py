import keyboard, time, os, settings
import pynput.mouse as pynm
import pynput.keyboard as pynk
try:
    import win32gui
except:
    import win32.win32gui as win32gui
global mouse, keys, focusedInstance

mouse=pynm.Controller()
keys=pynk.Controller()

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

def click(pos):
    global mouse
    mouse.position = (pos[0], pos[1])
    time.sleep(settings.delays[11])
    mouse.press(pynm.Button.left)
    time.sleep(settings.delays[12])
    mouse.release(pynm.Button.left)

def send(x):
    global keys
    keys.press(x)
    time.sleep(settings.delays[13])
    keys.release(x)
    time.sleep(settings.delays[14])

def reset(minecrafts):
    global focusedInstance
    send(pynk.Key.esc)
    time.sleep(settings.delays[0])
    click(settings.clicks[0])
    time.sleep(settings.delays[1])
    click(settings.clicks[1])
    time.sleep(settings.delays[2])
    click(settings.clicks[2])
    if settings.seed!=0:
        time.sleep(settings.delays[4])
        click(settings.clicks[3])
        time.sleep(settings.delays[5])
        click(settings.clicks[4])
        time.sleep(settings.delays[6])
        for char in str(settings.seed):
            send(char)
        time.sleep(settings.delays[7])
    else:
        time.sleep(settings.delays[3])
    click(settings.clicks[5])
    time.sleep(settings.delays[8])
    focusedInstance=(focusedInstance+1)%len(minecrafts)
    print(focusedInstance)
    focusWindow(focusedInstance, minecrafts)
    time.sleep(settings.delays[9])
    send(pynk.Key.esc)
    if settings.livesplit:
        time.sleep(settings.delays[10])
        send(settings.timer_start)
            
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
            if time.perf_counter() > this.start_time_sec + settings.delays[15]:
                this.step=0

minecrafts=getwinlist()
instances=len(minecrafts)
print("Instances: "+str(instances))
#print("Seconds/Reset: "+str((settings.delays[6]+settings.delays[7])*4+DELAYS[0][0]+DELAYS[1][0]+DELAYS[2][0]+DELAYS[3][0]+DELAYS[4][0]+DELAYS[5][0]+DELAYS[8][0]+DELAYS[9][0]))
focusedInstance=0
focusWindow(focusedInstance, minecrafts)
ingamemacros=[GameMacro("t", "7"), GameMacro("g", "8"), GameMacro("v", "9"), GameMacro("c", pynk.Key.f5)]
while True:
    if keyboard.is_pressed(settings.reset_key):
        reset(minecrafts)
    for gamemacro in ingamemacros:
        gamemacro.periodic_call()
    time.sleep(0.01)
