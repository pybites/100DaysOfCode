#!python3
#save_screenshot.py is a script to take a screenshot and save it to a specified directory.

import os
import pyscreeze

#the save path is only necessary if you need to save the file anywhere
#other than where the script is being run from
SAVE_PATH = "/Users/pybites/screenshots"

def change_dir():
    os.chdir(SAVE_PATH)

def take_screenshot():
    filename = input("What do you want to name the screenshot? ")
    pyscreeze.screenshot(filename + ".png")

if __name__ == '__main__':
    change_dir() #comment out if you don't need a specific path
    take_screenshot()
	
