import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_cat():
    cat = [
        r"     /\_/\ ",
        r"   =( ' ' )=",
        r"    (,) (,)",
        r"     >' '<",
        r"    /_' '_\ ",
        r"   /_______\ "
    ]
    for line in cat:
        print(line)

while True:
    
    draw_cat()
    time.sleep(5)