global mouse, keys
import keyboard, time, settings
import pynput.mouse as pynm
import pynput.keyboard as pynk
if settings.visual_cue:
    import pyautogui
try:
    import clipboard
    if settings.seed!=0 and settings.seed_clipboard:
        clipboard.copy(str(settings.seed))
except:
    pass

mouse=pynm.Controller()
keys=pynk.Controller()

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


def reset():
    send(pynk.Key.esc)
    time.sleep(settings.delays[0])
    click(settings.clicks[0])           #Save and quit
        
    if settings.visual_cue:
        while pyautogui.screenshot(region=settings.pixeldata[0]+(1,1)).getcolors()[0][1]!=settings.pixeldata[1]:
            continue
        
    else:
        time.sleep(settings.delays[1])
        
    click(settings.clicks[1])           #singleplayer
    time.sleep(settings.delays[5])
    click(settings.clicks[2])           #create new world
    
    if settings.seed!=0:                #SS
        time.sleep(settings.delays[6])
        click(settings.clicks[3])       #more world options
        time.sleep(settings.delays[7])
        click(settings.clicks[4])       #seed box
        time.sleep(settings.delays[8])
        if settings.seed_clipboard:
            keys.press(pynk.Key.ctrl)
            time.sleep(settings.delays[15])
            send("v")
            keys.release(pynk.Key.ctrl)
        else:
            for char in str(settings.seed):
                send(char)
        time.sleep(settings.delays[9])
        
    else:                               #RS
        time.sleep(settings.delays[5])
        
    click(settings.clicks[5])           #create new world
    if settings.timer:
        time.sleep(settings.delays[12])
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
            if time.perf_counter() > this.start_time_sec + settings.delays[17]:
                this.step=0



ingamemacros=[]
for item in settings.rebinds:
    ingamemacros.append(GameMacro(item[0], item[1]))
while True:
    if keyboard.is_pressed(settings.reset_key):
        reset()
    for gamemacro in ingamemacros:
        gamemacro.periodic_call()
    time.sleep(0.01)
