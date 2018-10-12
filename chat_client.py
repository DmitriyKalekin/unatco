import requests
from datetime import datetime
import json
from pathlib import Path
from threading import Thread
from functools import partial
from random import choice, uniform, randint
from time import sleep, time
from flask import jsonify
import colorama
from colorama import Fore, Back, Style, init
from random import randint, choice
from string import printable
import sys
import os
import time
import textwrap

#import random
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
STYLES = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]
# This assumes your terminal is 80x24. Ansi minimum coordinate is (1,1).
MINY, MAXY = 1, 10
MINX, MAXX = 1, 80
init()

TREE = Back.GREEN + Fore.LIGHTGREEN_EX + "F"
WATER = Back.CYAN + Fore.BLUE + "~"

def echo(s):
    for character in s:
        print(Fore.GREEN + character, end="")
        time.sleep(0.005)
    print(Fore.RESET)



def make_request(url, params):
    params["ts"] = time.time()
    try:
        # print(url)
        # print(params)
        r = requests.get(url=url, params=params)
        # print(r.status_code, r.reason)
        data = r.json()
        # print(data)
    except:
        return ("{NOT_CONNECTED}", "[?]", "default")


    try:
        return data["answer"]
    except:
        return ("{ERROR}", "[?]")


url = 'http://127.0.0.1:5001/'
params = {
    "message_text": "123",
    "chat_id": "555"
}



print("Input sentence. Type \"exit\" to exit.")
sentence = input(">>> ")
while sentence!="exit":
    params["message_text"]= sentence
    r = make_request(url, params)
    echo(r)
    # print(r)

    # print("[NiaML:%s]: " % mood, class_marks)
    # print("         ", ans)
    sentence = input(">>> ")
print("exiting")
