import time
import subprocess
import os
import psutil
from tkinter import Tk, Label, Button, Toplevel

# Read the banned programs and their ban periods from a text file
def read_banned_programs(file_path):
    banned_programs = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                program_name, start_time, end_time = line.split(',')
                banned_programs[program_name] = [start_time, end_time]
    return banned_programs

# Function to check if a program is currently banned
def is_banned(program_name, banned_programs):
    current_time = time.strftime("%H:%M")
    ban_period = banned_programs.get(program_name, [])
    if ban_period:
        start_time, end_time = ban_period
        if start_time <= current_time < end_time:
            return True
    return False

# Function to get the list of currently running programs
def get_running_programs():
    running_programs = []
    for proc in psutil.process_iter(['name']):
        try:
            running_programs.append(proc.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return running_programs

# Function to launch a program
def launch_program(program_name, banned_programs):
    if is_banned(program_name, banned_programs):
        
        show_reminder_window(program_name, banned_programs)
    else:
        subprocess.Popen([program_name])

# Function to show the reminder window with the option to extend the usage time or close the program
def show_reminder_window(program_name, banned_programs):
    window = Toplevel()
    label = Label(window, text=f"{program_name} is currently banned.")
    label.pack()

    def extend_usage_time():
        # Extend the usage time for 5 minutes
        window.after(300000, lambda: check_running_programs(banned_programs))
        window.destroy()

    def close_program():
        # Implement your logic to close the program here
        print(f"Closing {program_name}")
        window.destroy()
        # Add code here to close the program

    extend_button = Button(window, text="Extend Usage Time (5 mins)", command=extend_usage_time)
    extend_button.pack(side="left", padx=5, pady=5)

    close_button = Button(window, text="Close Program", command=close_program)
    close_button.pack(side="left", padx=5, pady=5)

# Function to check for running programs that should be banned
def check_running_programs(banned_programs):
    running_programs = get_running_programs()
    for program in running_programs:
        if is_banned(program, banned_programs):
            show_reminder_window(program, banned_programs)

# Read the banned programs from the text file
banned_programs = read_banned_programs("banned_programs.txt")

# Check for running programs that should be banned
check_running_programs(banned_programs)

# Example usage
# launch_program("program1.exe", banned_programs)
# launch_program("program2.exe", banned_programs)