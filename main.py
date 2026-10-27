import os
from colorama import Fore, Back, Style

def setting_read():  # Reading settings from settings.conf
    global artcolor, menucolor
    with open("settings.conf","r",encoding="UTF-8") as f:
        artcolor= getattr(Fore, f.readline().strip(), Fore.WHITE) # Getattr: Reading Fore color from 1. line
        menucolor= getattr(Fore, f.readline().strip(), Fore.WHITE)

def show_art(): # Showing ASCII art
    with open("art.dat","r", encoding="UTF-8") as f:
        for i in f:
            i = i.strip().split(";")
            for thing in i:
                print(artcolor + thing)


setting_read()
show_art()