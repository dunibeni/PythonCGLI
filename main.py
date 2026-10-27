import os
from colorama import Fore, Back, Style

def settings():  # settings from settings.conf
    global artcolor, menucolor
    with open("settings.conf","r",encoding="UTF-8") as f:
        artcolor= getattr(Fore, f.readline().strip(), Fore.WHITE) # Getattr: Fore color from 1. line
        menucolor= getattr(Fore, f.readline().strip(), Fore.WHITE)

def art(): # Print art
    with open("art.dat","r", encoding="UTF-8") as f:
        for i in f:
            i = i.strip().split(";")
            for thing in i:
                print(artcolor + thing)


settings()
art()