# mchv-multiinstancing
Multi-Instance Macro for Historical Versions of Minecraft: Java Edition

## how to use
- [download and install python](https://www.python.org/downloads/)<br />
- install from pip: 'keyboard', 'pynput', 'pywin32' (look up a tutorial if you dont know how to install packages from pip)<br />
- run as many minecraft instances as you want<br />
- close Minecraft launcher<br />
- run macro.py with python.exe<br />
- reset using y (this can be changed in line 82 of macro.py (you can open it with Notepad))<br />
- whenever an instance is closed or opened, restart macro.py<br />

## in-game-macros
for custom key-to-key macros like rebinding f5, 9, etc. to other keys<br />
how to customize: open macro.py with Notepad, edit macros in line 81 like this:<br />
ingamemacros=[GameMacro(key, action), GameMacro("t", "7"), GameMacro("c", pynk.Key.f5)]<br />
numbers and letters have to be written in "", special keys like this: pynk.Key.shift, pynk.Key.return. A list of special key names can be found [here]( https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key)<br />
ingamemacros=[] if you want no in game macros<br />

## it doesnt work
- make sure your pc is running windows<br />
- make sure macro.py, readfiles.py, delays.txt, clicks.txt are all there and in the same directory<br />
- run readfile.py - if it fails, there is a mistake one of the text files<br />
- macro doesnt click/clicks before gui loads - increase delays in the delays.txt file<br />
- macro clicks in the wrong spots - adjust coordinates in the clicks.txt file (deafault is for 1080x1920 monitors, maximized (not fullscreen), Large GUI, Beta 1.8.1)<br />
- macro runs in game - only start the macro when you are NOT paused<br />
- macro focuses on non-Minecraft windows - there is the word 'minecraft' in that window's title. Close or rename the window and restart macro.py
- macro doesnt focus on instance - there has to be the word 'minecraft' (not case sensitive) in the window's title
- open macro.py with Python/Lib/idlelib/idle.bat and run using f5 to see error message
