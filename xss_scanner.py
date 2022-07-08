import requests
from os import system

Red = "\033[1;31;40m"
Blue = "\033[1;36;40m"
White="\033[0;37m"
green = '\033[1;32;40m'

system(f"title Basic Tool To looking for xss in Site")
system('cls||clear')
target = input(f"""{green}
For example: https://xss-game.appspot.com/level1/frame?query=



Enter your url please: """)

file = input("\nEnter your file please: ")
with open(file, 'r') as files:
    payload = files.read().splitlines()

system('cls||clear')
for lists in payload:
    req = requests.get(f'{target}{payload}',"html.parser").text
    if lists in req:
        print(f"\n{Blue}Found XSS: {target}{lists}")
        with open("Vailed_xss.txt", 'a') as vailed:
            vailed.write(f"{target}{lists}\n")

    else:
        print(f"{Red}Not Found {target}{lists}")
input(f"{White}\n\n\nFinished......")