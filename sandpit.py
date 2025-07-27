import re
import sys

def ask_start():
    while True:
        answer = input("\nAre you ready to begin your battle through the maze?\n")
        if re.fullmatch("yes|y", answer, flags = re.IGNORECASE):
            break
        elif re.fullmatch("no|n", answer, flags = re.IGNORECASE):
            sys.exit("Ok. Come back when you feel ready to ")
        else:
            continue
        
ask_start()