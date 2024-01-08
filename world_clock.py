import tkinter as tk
from datetime import datetime
import pytz
import time

# Define the time zones
time_zones = ['Australia/Sydney', 'Asia/Tokyo', 'Asia/Singapore', 'Asia/Seoul', 'Europe/London', 'America/New_York', 'America/Los_Angeles']

def update_times():
    for i, tz in enumerate(time_zones):
        # Get the current time in the time zone
        now = datetime.now(pytz.timezone(tz))
        # Format the time as a string
        time_str = now.strftime('%H:%M:%S')
        # Update the label for the time zone
        labels[i].config(text=f'{tz.split("/")[-1]}: {time_str}')
    # Schedule the function to run again after 1 second
    root.after(1000, update_times)

# Create the main window
root = tk.Tk()
root.title('World Clock')
root.configure(background='black')  # Set the background color of the window to black

# Create a label for each time zone
labels = [tk.Label(root, font=('Helvetica', 20), 
                   foreground='green', background='black') 
                   for _ in time_zones]
# Set the text color to green and the background color to black
for label in labels:
    label.pack()

# Start the clock
update_times()

# Start the main loop
root.mainloop()
