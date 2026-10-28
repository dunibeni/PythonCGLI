import os
import pylnk3
from colorama import Fore, Back, Style
from pathlib import Path
apps=[]
count=1
inpt=0
itsanumber=False
with open("settings.conf","r",encoding="UTF-8") as conf:
    artcolor= getattr(Fore, conf.readline().strip(), Fore.WHITE)
    menucolor= getattr(Fore, conf.readline().strip(), Fore.WHITE)

with open("art.dat","r", encoding="UTF-8") as art:
    for i in art:
        i = i.strip().split(";")
        for thing in i:
            print(artcolor + thing)

for file in Path("apps").glob("*lnk"):
    pic=pylnk3.parse(str(file))
    cut=pic.path
    apps.append(cut)
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
        inpt=int(input("\nChoice: "))
        valid=True
        print("Launching...")
    except(ValueError):
        if inpt <= count:
            if itsanumber == True:
                print("Yes, it's a number, BUT NOT AN OPTION")
            else:
                print("Please enter a Valid Option")
        else:
            print("Please enter a N-U-M-B-E-R... ")
            itsanumber=True
try:
    os.system(apps[inpt-1])
except:
    print("Error")
