Ubuntu Audio Jack Indicator
===============
Adds an indicator menu to Ubuntu that switches between front and rear audio jacks.

The actual hardware scripts were generated using HDA-Analyzer; refer to <a href="http://askubuntu.com/questions/225017/how-do-i-change-which-audio-jacks-are-used-for-input-and-output">this question</a> for more info.

This just adds a GUI that you can add to your startup script like so:
<img src="http://i.imgur.com/7avTQxX.png"/>

Usage
=====
Run in background with
```
nohup python audio-indic.py $
```


