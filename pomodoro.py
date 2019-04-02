#!/usr/bin/env python3

import time
import sys
import tkinter as tk
from tkinter import messagebox

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
        time.sleep(60) #60 = 1 min
        mins += 1
    elif breakcnt < 3:
        messagebox.showwarning("Time is up!", "Please take a 5 minute break starting now")
        root.update
        x = 5
        for i in range(5):
            print(str(x) + " minutes remaining")
            x -= 1
            time.sleep(60)
        messagebox.showwarning("Back to work!", "Please resume your work")
        root.update
        mins = 1
        breakcnt += 1
        print("\n\nResuming...\n\n\n")
    elif breakcnt >= 3:
        messagebox.showwarning("Time is up!", "Please take a 25 minute break, you've earned it.'")
        root.update
        x = 25
        for i in range(25):
            print(str(x) + " minutes remaining")
            x -= 1
            time.sleep(60)
        messagebox.showwarning("Back to work!", "Please resume your work")
        root.update
        mins = 1
        breakcnt = 0
        print("\n\nResuming...\n\n\n")
