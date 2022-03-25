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
    time.sleep(settings.delays[13])
    mouse.press(pynm.Button.left)
    time.sleep(settings.delays[14])
    mouse.release(pynm.Button.left)

def send(x):
    global keys
    keys.press(x)
    time.sleep(settings.delays[15])
    keys.release(x)
    time.sleep(settings.delays[16])

def reset(minecrafts):
    global focusedInstance
    starttime=time.perf_counter()
    send(pynk.Key.esc)
    time.sleep(settings.delays[0])
    click(settings.clicks[0])
    if settings.saving_world_skip and len(minecrafts)>=3:
        time.sleep(settings.delays[2])
        focusWindow((focusedInstance-1)%len(minecrafts), minecrafts)
        time.sleep(settings.delays[3])
    else:
        time.sleep(settings.delays[1])
    click(settings.clicks[1])
    time.sleep(settings.delays[4])
    click(settings.clicks[2])
    if settings.seed!=0:
        time.sleep(settings.delays[6])
        click(settings.clicks[3])
        time.sleep(settings.delays[7])
        click(settings.clicks[4])
        time.sleep(settings.delays[8])
        for char in str(settings.seed):
            send(char)
        time.sleep(settings.delays[9])
    else:
        time.sleep(settings.delays[5])
    click(settings.clicks[5])
    time.sleep(settings.delays[10])
    focusedInstance=(focusedInstance+1)%len(minecrafts)
    focusWindow(focusedInstance, minecrafts)
    time.sleep(settings.delays[11])
    send(pynk.Key.esc)
    if settings.livesplit:
        time.sleep(settings.delays[12])
        send(settings.timer_start)
    print(time.perf_counter()-starttime)

def timeestimate(minecrafts):
    tclick=settings.delays[13]+settings.delays[14]
    tsend=settings.delays[15]+settings.delays[16]
    est=settings.delays[0]+settings.delays[4]+settings.delays[10]+settings.delays[11]+4*tclick+2*tsend
    if settings.saving_world_skip and len(minecrafts)>=3:
        est=est+settings.delays[2]+settings.delays[3]
    else:
        est=est+settings.delays[3]
    if settings.seed!=0:
        est=est+settings.delays[6]+settings.delays[7]+settings.delays[8]+settings.delays[9]+2*tclick+len(str(settings.seed))*tsend
    else:
        est=est+settings.delays[5]
    if settings.livesplit:
        est=est+settings.delays[12]
    return est
      
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
            if time.perf_counter() > this.start_time_sec + settings.delays[17]:
                this.step=0

minecrafts=getwinlist()
instances=len(minecrafts)
print("Instances: "+str(instances))
print("Seconds/Reset: "+str(timeestimate(minecrafts)))
focusedInstance=0
focusWindow(focusedInstance, minecrafts)
ingamemacros=[GameMacro("t", "7"), GameMacro("g", "8"), GameMacro("v", "9"), GameMacro("c", pynk.Key.f5)]
while True:
    if keyboard.is_pressed(settings.reset_key):
        reset(minecrafts)
    for gamemacro in ingamemacros:
        gamemacro.periodic_call()
    time.sleep(0.01)
