# mchv-multiinstancing
Multi-Instance Macro for Historical Versions of Minecraft: Java Edition for Windows

## how to use
- [download and install python](https://www.python.org/downloads/)<br />
- install from pip: 'keyboard', 'pynput', 'pywin32' ([tutorial](https://www.youtube.com/watch?v=jnpC_Ib_lbc))<br />
- run as many minecraft instances as you want<br />
- close Minecraft launcher<br />
- run macro.py with python.exe<br />
- reset using y, use x as your livesplit start/stop key<br />
- whenever an instance is closed or opened, restart macro.py<br />

## customisation
- edit settings.py in Notepad while keeping the syntax the same

## it doesnt work
- macro doesnt click/clicks before gui loads - increase delays in the settings.py file<br />
- macro clicks in the wrong spots - adjust coordinates in the settings.txt file (default is for 1080x1920 monitors, maximized (not fullscreen), Large GUI, Beta 1.8.1)<br />
- macro focuses on non-Minecraft windows - Close this window and restart macro.py
- macro doesnt recognize instance - there has to be the word 'minecraft' (not case sensitive) in the window's title
