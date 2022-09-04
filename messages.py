# Messages Python File
''' Messages.py holds all messages returned to user '''

from os import system, name
import colorama
from colorama import Fore
from termcolor import colored
from art import logo_display

colorama.init(autoreset=True)

def clear():
    """this is"""

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")

