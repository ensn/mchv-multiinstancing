seed=123456789          #put 0 for random seed
livesplit=True          #Starts the timer as soon as the instance is unpaused (having this falsely turned on does usually not cause any harm)
reset_key="y"           #Set this as your livesplit reset key too (numbers and letters have to be written in "", special keys like this: pynk.Key.shift, pynk.Key.return. A list of special key names can be found at https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key)
timer_start="x"         #Set this as your livesplit start/stop key too (Same rules as above apply)
saving_world_skip=True  #Skips the 'Saving Chunks' screen by switching the instance. Set this to False (case sensitive) if there are issues. This feature is automatically disabled for 2 or less instances

delays=[
    0.08,               #esc - save and quit
    0.6,                #saving world (only saving_world_skip=False)
    0.03,             #save and quit - focus previous instance (only saving_world_skip=True)
    0.15,             #focus instance - singleplayer (only saving_world_skip=True)
    0.03,               #singleplayer - create new world 1
    0.03,               #create new world - create new world (only Random Seed)
    0.03,               #create new world - more world options (only Set Seed)
    0.03,               #more world options - seed box (only Set Seed)
    0.03,               #seed box - start typing seed (only Set Seed)
    0.03,               #finish typing seed - create new world 2 (only Set Seed)
    0.03,               #create new world - focus next instance
    0.15,               #unpausing after focus
    0,                  #start livesplit 10
    0.03,               #mouse delay in between moving and pressing button
    0.02,               #mouse delay in between pressing and releasing button
    0,                  #keyboard delay in between pressing and releasing key
    0,                  #keyboard delay after relasing key
    0.25]               #double tap prevention for in-game-macros.

clicks=[
    [950, 623],         #save and quit
    [950, 450],         #singleplayer
    [1200, 900],        #create new world
    [950, 570],         #more world options (set seed)
    [950, 230],         #seed box (set seed)
    [700, 970]]         #create new world

import macro            #ignore this, dont delete
rebinds=[               #for rebinding key-key f5, 9, etc. to other keys. Change this to rebinds=[] if you dont want any rebinded keys and delete all following lines
    macro.GameMacro("t", "7"), #numbers and letters have to be written in "", special keys like this: pynk.Key.shift, pynk.Key.return. A list of special key names can be found at https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
    macro.GameMacro("g", "8"), 
    macro.GameMacro("v", "9"),
    macro.GameMacro("c", pynk.Key.f5)]
