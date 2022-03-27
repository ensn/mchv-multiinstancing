seed=0                  #put 0 for random seed
livesplit=True          #Starts the timer as soon as the instance is unpaused
reset_key="y"           #Set this as your livesplit reset key too (numbers and letters have to be written in "", special keys like this: pynk.Key.shift, pynk.Key.return. A list of special key names can be found at https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key)
timer_start="x"         #Set this as your livesplit start/stop key too (Same rules as above apply)
saving_world_skip=False #Attempt to skip the 'Saving Chunks' screen when 3 or more instances are active

delays=[
    0.1,                #esc - save and quit
    0.8,                #saving world (only saving_world_skip=False)
    0.1,                #save and quit - focus previous instance (only saving_world_skip=True)
    0.05,               #focus instance - singleplayer (only saving_world_skip=True)
    0.05,               #singleplayer - create new world 1
    0.07,               #create new world 1 - create new world 2 (only Random Seed)
    0.05,               #create new world - more world options (only Set Seed)
    0.05,               #more world options - click seed box (only Set Seed)
    0.05,               #click seed box - start typing seed (only Set Seed)
    0.3,                #finish typing seed - create new world 2 (only Set Seed)
    0.1,                #create new world - focus next instance
    0.2,                #unpausing after focus
    0,                  #start livesplit
    0.05,               #mouse moving - pressing
    0.05,               #mouse pressing - releasing
    0,                  #keyboard pressing - releasing
    0,                  #keyboard after relasing
    0.25]               #double tap prevention for rebinds

clicks=[
    [950, 623],         #save and quit
    [950, 450],         #singleplayer
    [1200, 900],        #create new world
    [950, 570],         #more world options (set seed)
    [950, 230],         #seed box (set seed)
    [700, 970]]         #create new world

import pynput.keyboard as pynk #ignore this, dont delete
rebinds=[               #for rebinding key-key [key, action]. Change this to rebinds=[] if you dont want any rebinded keys and delete all following lines
    ["t", "7"],         #same rules as in line 3 apply
    ["g", "8"], 
    ["v", "9"],
    ["c", pynk.Key.f5]]
