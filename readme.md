## lzy_fck
A simple script that will automate mouse and keyboard movements.

If you need to keep your computer awake for awhile and you don't feel like changing your system settings this is for you.

If you have a boring job and want to trick microsoft Teams or your boss into thinking that you are active then this is also for you.

## About
This app leverages the pyautogui api and all of its dependencies. It is minimal code and I aim to make it user friendly.

<ins>Why not write it in c/c++ and make an exe?</ins><br>
Not everyone will have c/c++ on their system and python is by far the easiest to install and run. Maybe I will re-make this in c/c++. For now a python version is dead easy to use without having to download a bunch of shit.

### OS Support
- Linux - Experimental
- Windows

They should work the same, but I have noticed that pyautogui doesn't play as nice in debian. Works fine in Windows.

<ins>Why is there not a MAC version.?</ins><br>
I don't have a MAC laying around to test with. According to the API author, pyautogui should work fine with MAC OS.

### Dependencies

```
pyautogui
wakepy
time
numpy
```

#### Install Packages
```pip3 install -r /path/requirements.txt```

## How it Works
run: ```python3 app.py```

Enter: ```[y/n]``` for sleep mode.

Enter: ```<number``` for sleepTime (seconds).

Quick Start: Press Enter Twice to skip all prompts and use defaults.

After launching the program successfully, the program will take control of your mouse and keyboard, but in a mostly non-intrusive way. 

### Debug Mode
At the start the user will be prompted if they want to enable ```debug mode``` at the start. Debug mode will log how the program interacts with your machine.

### Sleep Time
At start the user can set a ```sleepTime``` this tells the program how long to wait between each loop. Each loop contains a set of instructions. You can enter ```0``` if you want the program to run without pauses, or a value greater than ```0```. Currently the limit is 180 seconds. This value is arbitrary, but at this time values larger 180 seconds(3 minutes) have not been tested.

### Windows
On Windows, you will see your mouse move to a random location and drag to the bottom right, relative to its current position. Then the scroll wheel will be used to "scroll" ```UP``` and ```DOWN``` a few times. If your mouse is hovering a window then you'll see the window "scroll." Lastly, ```shift``` is pressed 3 times.

### Linux
The linux version works the same as the windows version, however the pyautogui api doesn't play nice with Debian. This isn't to suggest that this program doesn't work. The windows GUI API is win32. Many distros differ on what GUI API they use. The GUI found on most linux machines is ```X Window System```. 

```X Window System``` defines a device independent way of dealing with screens, keyboards, and pointer devices. Based on testing on my machine, the program keeps my cpu running, however, you cannot see the mouse visually moving. You can see the program scroll up and down if the mouse hovers over a scrollable window. The program successfully takes control of the mouse pointer, the user just can't see it move. 

This is why I will leave Linux as ```Experimental``` I need to do more tests in virtual machines to see how things behave in different distros.

## Uses
<ins>Prevent Sleep:</ins><br>
If you need to keep your system awake while you compile code, run a slow app, whatever. This can help out. Even if you lock your computer, the program will continue to run.

<ins>Fool Your Annoying Boss:</ins><br>
If you have a slow job and need to keep your system active. This is also great. In a lot of cases, work applications like "Microsoft Teams" checks for use inputs periodically to see if someone is "away" or not. Some managers check employee statuses regularly. Sometimes you step away for a brief amount of time, or you sitting and waiting for something to compile. You don't touch your mouse or keyboard while you wait. Your status changes to "away." Your manager then asks "why were you away for x amount of time." It's annoying. 

```lzy_fck``` prevents this. Even if you lock your computer, your mouse will still move and scroll, and the program will press shift. Your status will show "available."
