import os
from colorama import Fore, Back, Style

def settings():  # settings from settings.conf
    global artcolor, menucolor
    with open("settings.conf","r",encoding="UTF-8") as conf:
        artcolor= getattr(Fore, conf.readline().strip(), Fore.WHITE) # Getattr: Fore color from 1. line
        menucolor= getattr(Fore, conf.readline().strip(), Fore.WHITE)

def art(): # Print art
    with open("art.dat","r", encoding="UTF-8") as art:
        for i in art:
            i = i.strip().split(";")
            for thing in i:
                print(artcolor + thing)
def launchlist():
    with open("apps.conf","r",encoding="UTF-8") as apps:
        for app in apps:
            None

settings()
art()

print("═══════════════════════════════════════════════════════════════════════")