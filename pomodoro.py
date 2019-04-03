#!/usr/bin/env python3

import time
import sys
import tkinter as tk
from tkinter import messagebox

minute = 1 


def breakpnt(breaktime):
    messagebox.showwarning("Time is up!", "Please take a " + str(breaktime) + " minute break starting now")
    root.update
    x = breaktime
    for i in range(breaktime):
        print(str(x) + " minutes remaining")
        x -= 1
        time.sleep(minute)
    messagebox.showwarning("Back to work!", "Please resume your work")
    root.update
    print("\n\n\nResuming...\n\n\n")


print("Welcome to Pomodoro Timer!")

try:
    count = int(sys.argv[1])
except (ValueError, IndexError):
    print("The number is null or invalid\nDefault Number is 25")
    count = 25

mins = 1
breakcnt = 0
root = tk.Tk()
root.withdraw()
print("\n\n Starting.... \n\n")
while True:
    if mins <= count:
        print(">>>>>>>>>>>> " + str(mins))
        time.sleep(minute) #60 = 1 min
        mins += 1
    elif breakcnt < 3:
        breakpnt(5) 
        mins = 1
        breakcnt += 1
    elif breakcnt >= 3:
        breakpnt(25) 
        mins = 1
        breakcnt = 0
