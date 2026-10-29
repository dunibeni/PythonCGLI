import os
import pylnk3
from colorama import Fore, Back, Style
from pathlib import Path
valid=False
itsanumber=False
count=1
apps=[]
app=[]
m=50
with open("settings.conf","r",encoding="UTF-8") as conf:
    artcolor= getattr(Fore, conf.readline().strip(), Fore.WHITE)
    menucolor= getattr(Fore, conf.readline().strip(), Fore.WHITE)

with open("art.dat","r", encoding="UTF-8") as art:
    for i in art:
        print(artcolor + i.rstrip("\n"))
print(menucolor+"\n╔", m*"═","╗")
for file in Path("apps").glob("*lnk"):
    pic=pylnk3.parse(str(file))
    cut=pic.path
    apps.append(cut)
    print(f"║ [{count}] ", end="")
    for i in str(file.name):
        if i == ".":
            break
        else:
            print(i, end="")
            app.append(i)
    print(" " * (((m-2)-(len(str(count))))-len(app)), end="")
    print("║")
    app=[]
    count+=1
print("╚", m*"═","╝")
while valid == False:
    try:
        inpt=int(input(menucolor+"\nChoice: "))
        if inpt < 1 or inpt >= count:
            if itsanumber == True:
                print(Fore.LIGHTRED_EX +"Yes, it's finally a number, BUT NOT AN OPTION")
                itsanumber = False
            else:
                print(Fore.LIGHTRED_EX +"Please enter a Valid Option")
        else:
            print(Fore.LIGHTRED_EX +"Trying to launch...")
            try:
                os.startfile(apps[inpt-1])
                valid=True
            except OSError as e:
                print(Fore.RED +f"Failed to launch: {e}")
    except(ValueError):    
        print(Fore.LIGHTRED_EX +"Please enter a N-U-M-B-E-R... ")
        itsanumber=True

