seed=0                  #seed=0 for random seed
reset_key="z"           #Timer reset key / macro trigger (numbers and letters have to be written in "", special keys like this: pynk.Key.shift, pynk.Key.return. A list of special key names can be found at https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key)
timer=True              #Starts the timer after unpausing
timer_start="x"         #Timer start key (Same rules as above)

visual_cue=False        #Looks at the screen to determine whether the 'Saving Chunks' screen has ended, requires 'pyautogui' from pip
seed_clipboard=True     #Copies seed for SS from clipboard instead of typing it out (automatically puts seed into clipboard when 'clipboard' from pip is installed)
saving_world_skip=False #Skips 'Saving World' when >=3 instances are active (always False)

delays=(
    0.1,                #esc - save and quit
    0.7,                #saving world
    0.05,               #saving_world_skip before focus
    0.1 ,               #saving_world_skip after focus
    0.2,                #visual_cue delay before checking pixel
    0.03,               #singleplayer - create new world
    0.03,               #create new world - create new world (RS)
    0.03,               #create new world - more world options (SS)
    0.05,               #more world options - click seed box (SS)
    0.05,               #click seed box - start typing seed (SS)
    0.1,                #finish typing seed - create new world 2 (SS)
    0,                  #create new world - focus next instance
    0.15,               #unpausing after focus
    0,                  #start timer
    0.03,               #mouse moving - pressing
    0.03,               #mouse pressing - releasing
    0,                  #keyboard pressing - releasing
    0,                  #keyboard after relasing
    0.25)               #double tap prevention for rebinds

clicks=(
    (950, 623),         #save and quit
    (950, 450),         #singleplayer
    (1200, 900),        #create new world
    (950, 570),         #more world options (set seed)
    (950, 230),         #seed box (set seed)
    (700, 970))         #create new world

pixeldata=(             #for visual_cue setting
    (1918, 24),         #position (top right, windowed)
    (46, 33, 23))       #rgb colour

import pynput.keyboard as pynk #dont delete this line
rebinds=(               #for rebinding key-key [key, action]. Change this to rebinds=[] if you dont want any rebinded keys and delete all following lines
    ("t", "7"),         #same rules as in line 2 apply
    ("g", "8"), 
    ("v", "9"),
    ("c", pynk.Key.f5))
