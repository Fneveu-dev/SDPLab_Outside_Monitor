import time
import os
from datetime import datetime, timedelta
import tkinter as tk

# =====================================================================
# TO CHANGE THE NUMBER OF TOTAL COUNTDOWN DAYS EDIT THE BELOW VARIABLE
# =====================================================================

TOTAL_DAYS = 7   # <-- SET NUMBER OF DAYS HERE

# File to store start time
START_FILE = "/home/hallmonitor/countdown_start.txt"


# Title text (what countdown is for)
TITLE_TEXT = "HALL PASS SYSTEM RESET"   # <-- EDIT THIS


# ==============================
# Setup start time
# ==============================

if not os.path.exists(START_FILE):
    with open(START_FILE, "w") as f:
        f.write(str(time.time()))

with open(START_FILE, "r") as f:
    start_time = float(f.read())

start_datetime = datetime.fromtimestamp(start_time)


# ==============================
# UI Setup
# ==============================

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(background="black")



title_label = tk.Label(
    root,
    text=TITLE_TEXT,
    font=("Helvetica", 50),
    fg="white",
    bg="black"
)
title_label.pack(pady=40)

# Main countdown number
countdown_label = tk.Label(
    root,
    font=("Helvetica", 120),
    fg="white",
    bg="black"
)
countdown_label.pack(expand=True)

# Optional footer text
footer_label = tk.Label(
    root,
    text="Please take necessary action",
    font=("Helvetica", 30),
    fg="gray",
    bg="black"
)
footer_label.pack(pady=40)


# ==============================
# Countdown Logic
# ==============================

def update_countdown():
    now = datetime.now()
    elapsed = now - start_datetime
    days_passed = elapsed.days
    days_remaining = TOTAL_DAYS - days_passed

    if days_remaining <= 0:
        countdown_label.config(
            text="TIME EXPIRED",
            fg="red",
            bg="black"
        )
    else:
        # Warning color levels
        if days_remaining <= 2:
            color = "red"
        elif days_remaining <= 4:
            color = "orange"
        else:
            color = "white"

        countdown_label.config(
            text=f"{days_remaining} DAYS REMAINING",
            fg=color
        )

    root.after(60000, update_countdown)  # update every 60 seconds


update_countdown()
root.mainloop()
