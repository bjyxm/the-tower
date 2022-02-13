# The Tower Automation

## Environment
- Python 3.10
- BlueStacks 5 (Portrait / 720x1280)
- Android Debug Bridge (from platform-tools_r32.0.0-windows)

## Python packages
- pure-python-adb 0.3.0.dev0
- Pillow 9.0.1

## ADB ?
- All python automation scripts in this project use Android Debug Bridge(ADB) which is officially provided by Google.
- By using ADB, we can capture screenshot, check running activity, send touch input, etc...

## Prerequisites
- Set up python environment
- Install BlueStacks 5 and set display settings to 'portrait', '720x1280'

# Setup ADB
- There are two ways of running adb on Windows.
1. (LOCAL) Place adb.exe where .py script exists
   1. Download platform tools from [official Android Developer website](https://developer.android.com/studio/releases/platform-tools)
   2. Unzip two files (adb.exe, AdbWinApi.dll) to target path (where you're going to place .py files)
2. (GLOBAL) Set environment variable of your system to run adb.exe globally
   1. Download platform tools from [official Android Developer website](https://developer.android.com/studio/releases/platform-tools)
   2. Unzip two files (adb.exe, AdbWinApi.dll) to your desired path (e.g. 'C:/adb/')
   3. Add your desired path to environment variables' Path

# How to run the script
1. Clone or download the source as ZIP and unzip it.
2. Install necessary packages
```shell
pip install -r requirements.txt
```
3. Run your 'The Tower' app on your BlueStacks 5.
4. Run state checking script to see everything is okay.
```shell
python run_state_check.py
```
5. Run automation script and have fun.
```shell
python run_automation.py
```

## Demo Video
To be updated

## Instruction Video
To be updated