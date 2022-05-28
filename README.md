# mchv-multiinstancing (b1.8)
Multi-Instance Macro for Historical Versions of Minecraft: Java Edition for Windows 11

## how to use
- [download and install python](https://www.python.org/downloads/)<br />
- install from pip: 'keyboard', 'pynput', 'pywin32' ([tutorial](https://www.youtube.com/watch?v=jnpC_Ib_lbc))<br />
- run as many instances as you want<br />
- close Minecraft launcher<br />
- run macro.py with python.exe<br />
- reset using z, use x as your timer start key<br />
- whenever an instance is closed or opened, restart macro.py<br />
- if you need help with anything, join the [mchv discord](https://discord.com/invite/SdCStmwJ46)<br />

## customisation
- edit settings.py in Notepad while keeping the syntax the samey<br />
- many common settings for FHD screens can be found in commonsettings.py. Replace the corresponding line(s) into settings.py<br />

## it doesnt work
- focus all instances manually, then restart macro.py<br />
- doesnt click or clicks before gui loads - increase delays in settings.py file<br />
- clicks in the wrong spots - adjust coordinates in settings.py file (default is for 1080x1920 monitors, maximized (not fullscreen), Large GUI, Beta 1.8.1)<br />
- focuses on non-Minecraft windows - Close this window and restart macro.py<br />
- doesnt recognize instance - there has to be the word 'minecraft' (not case sensitive) in the window's title<br />
- crashes or doesnt start - run macro.py in Python/Lib/idlelib/idle.bat using f5 to see error message<br />
