#!/usr/bin/env python3

import time
import sys
from tkinter import messagebox


print("Welcome to Pomodoro Timer!")

try:
    count = int(sys.argv[1])
except (ValueError, IndexError):
    print("The number is null or invalid\nDefault Number is 25")
    count = 25

mins = 0

print("\n\n Starting.... \n\n")
while mins != count:
    print(">>>>>>>>>>>> " + str(mins))
    time.sleep(60)
    mins += 1

messagebox.showinfo("Time is up!", "Please take a 5 minute break. If this is your 4th break, take a 25 minute break")
exit(0)
