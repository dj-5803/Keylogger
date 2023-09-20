# Keylogger

This Python script is a basic keylogger that logs keypress events along with the active window's name. It's designed for educational purposes and to help you understand how keyloggers work.

## Features

1. Logs keypress events.
2. Tracks the active window's name.

## Prerequisites

Before using this keylogger, make sure you have the following dependencies installed:

- Python 3.x
- pyxhook (Python X Library Hook)
- Xlib (X Window System library for Linux)



## Usage

1. Clone or download this repository to your local machine.
	`git clone  https://github.com/dj-5803/Keylogger`

2. To download dependencies
	`pip install -r requirements.txt`
 
4. Run the script using Python:
`python3 keylogger.py`

5. The keylogger will start running and logging keypress events along with the active window's name.

6. Press `Ctrl + C` in the terminal where the keylogger is running to stop it.

## **To Run script in Background**
1. `python3 keylogger.py &`

2. To stop the program type `fg` and `CTRL + C` 

## Output

The keylogger logs events in a log file with a name based on the current date and time. The log files are created in the same directory as the script.

Sample log file format:
![image](https://github.com/dj-5803/Keylogger/assets/63869350/2fc79d35-b992-4f11-9da9-1745eb352ece)


## Disclaimer

This script is intended for educational and research purposes only. Be aware that using keyloggers without consent is illegal and unethical. Always respect privacy and the law.
