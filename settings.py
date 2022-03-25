seed=0                  #put 0 for random seed
reset_key="y"           #Set this as your livesplit reset key too
timer_start="x"         #Set this as your livesplit start/stop key too
saving_world_skip=True  #Skips the 'Saving Chunks' screen by switching the instance. Set this to False (case sensitive) if there are issues. This feature is automatically disabled for 2 or less instances

delays=[
    0.08,               #esc - save and quit
    0.6,                #saving world (only saving_world_skip=False)
    0.03,               #singleplayer - create new world 1
    0.03,               #create new world - create new world (only Random Seed)
    0.03,               #create new world - focus next instance
    0.15,               #unpausing after focus
    0.03,               #mouse delay in between moving and pressing button
    0.02,               #mouse delay in between pressing and releasing button
    0,                  #keyboard delay in between pressing and releasing key
    0,                  #keyboard delay after relasing key
    0.25]               #double tap prevention for in-game-macros.

clicks=[
    [950, 623],         #save and quit
    [950, 450],         #singleplayer
    [1200, 900],        #create new world
    [700, 970]]         #create new world

if __name__ == "__main__":
    print(seed)
    print(reset_key)
    print(timer_start)
    print(saving_world_skip)
    print(delays)
    print(clicks)
    input()
    input()
