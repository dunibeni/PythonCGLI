import os
from colorama import Fore, Back, Style
def showart():
    with open("art.dat","r", encoding="UTF-8") as f:
        for i in f:
            i = i.strip().split(";")
            for elem in i:
                print(Fore.RED + elem)
showart()

