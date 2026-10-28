import os
import pylnk3
from colorama import Fore, Back, Style
from pathlib import Path
apps=[]
count=0
inpt=0
def settings():
    global artcolor, menucolor
    with open("settings.conf","r",encoding="UTF-8") as conf:
        artcolor= getattr(Fore, conf.readline().strip(), Fore.WHITE)
        menucolor= getattr(Fore, conf.readline().strip(), Fore.WHITE)

def art():
    with open("art.dat","r", encoding="UTF-8") as art:
        for i in art:
            i = i.strip().split(";")
            for thing in i:
                print(artcolor + thing)
def launchlist():
    global count
    for file in Path("apps").glob("*lnk"):
        pic=pylnk3.parse(str(file))
        cut=pic.path
        print(f"[{count}] ", end="")
        for i in str(file.name):
            if i == ".":
                break
            else:
                print(i, end="")
        print(end="\n")
        count+=1
        valid=False
    while valid == False:
        try:
            inpt=int(input(""))
            valid=True
            print("Launching...")
        except(ValueError):
            print("Please enter a number... ")


settings()
art()
launchlist()