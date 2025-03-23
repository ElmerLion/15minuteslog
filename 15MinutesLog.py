import tkinter as tk
from tkinter import simpledialog
import csv
from datetime import datetime
import schedule
import time
import pandas as pd
import matplotlib.pyplot as plt

# Create one persistent Tk instance
root = tk.Tk()
root.withdraw()  

def get_user_input():
    # Use the persistent root instance as the parent for the dialog
    activity = simpledialog.askstring("Time Tracker", "What are you working on right now?", parent=root)
    return activity

def log_to_csv(activity):
    with open("time_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), activity])

def track_time():
    activity = get_user_input()
    if activity:
        log_to_csv(activity)
        print(f"Logged: {activity} at {datetime.now().strftime('%H:%M:%S')}")

# Schedule to run every 15 minutes
schedule.every(15).minutes.do(track_time)

print("Time Tracker is running... Press Ctrl+C to stop.")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nTime Tracker stopped.")
    root.destroy()  # Properly close the Tk instance when exiting

