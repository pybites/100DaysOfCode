#!python3
#pomodoro_timer.py is a simple script to set a pomodoro timer for yourself.

import time
import webbrowser

def choose_time():
    print("How long would you like to set for your Pomodoro?")
    p_time = input("Please enter a time in minutes: ")
    return int(p_time)

def timer(p_time):
    time.sleep((p_time * 60))   
    alarm()
    
def alarm():
    webbrowser.open("https://www.youtube.com/watch?v=vTVWGoQcn9Q")
    print("\n******** TIME UP ********\n")
    
if __name__ == "__main__":
    while True:
        p_time = choose_time()
        timer(p_time)