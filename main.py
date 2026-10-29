import os
import pylnk3
from colorama import Fore, Back, Style
from pathlib import Path
valid=False
suc= False
itsanumber=False
count=1
apps=[]
app=[]
m=45
with open("settings.conf","r",encoding="UTF-8") as conf:
    artcolor= getattr(Fore, conf.readline().strip(), Fore.WHITE)
    menucolor= getattr(Fore, conf.readline().strip(), Fore.WHITE)

with open("art.dat","r", encoding="UTF-8") as art:
    for i in art:
        i = i.strip().split(";")
        for thing in i:
            print(artcolor + thing)
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
    print(" " * ((m-3)-len(app)), end="")
    print("║")
    app=[]
    count+=1
print("╚", m*"═","╝")
while valid == False:
    try:
        inpt=int(input("\nChoice: "))
        if inpt < 1 or inpt >= count+1:
            if itsanumber == True:
                print("Yes, it's finally a number, BUT NOT AN OPTION")
                itsanumber = False
            else:
                print("Please enter a Valid Option")
        else:
            valid=True
            print("Launching...")   
    except(ValueError):    
        print("Please enter a N-U-M-B-E-R... ")
        itsanumber=True
try:
    os.startfile(apps[inpt-1])
except:
    print("Unexpected Error")
