# Messages Python File
''' Messages.py holds all messages returned to user '''

from os import system, name
import colorama
from colorama import Fore
from termcolor import colored
from art import logo_display

colorama.init(autoreset=True)


def clear():
    """Function to clear the console screen"""

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def exit_message():
    """This function is used to display exit message"""
    print(Fore.YELLOW + "~---------------------------~".center(80))
    print(Fore.YELLOW + "HANGMAN:Fruit Edition(TM)\n".center(80))
    print(Fore.YELLOW + "Thank you for playing!\n".center(80))
    print(Fore.YELLOW + "Please come back soon!".center(80))
    print(Fore.YELLOW + "~---------------------------~\n".center(80))


def game_title():
    """ This function has the text for the game title"""
    print(
        "The origins of the game Hangman are unclear but could stretch back\n"
        "to the 1890s. Players guess letters of an unrevealed word and then \n"
        "draw an arm, leg, head or torso of a stick figure hanging from \n"
        "gallows for every incorrect guess.\n\nIf players draw all body "
        "parts and the word still "
        "hasnt\nbeen spelled out, the player loses.\n"
    )


def game_rules():
    """ This function displays the gamer instuctions """
    print(f"{Fore.YELLOW}HANGMAN: The Fruit Edition(TM) Game Instructions")
    print()
    print("The hangman consists of a head, a body, 2 arms, 2 legs, and ears.")
    print("If you correctly guess the puzzle or fill in all of the letters")
    print("before the hangman is complete, you WIN!")
    print()
    print("You have 8 chances to guess the correct fruit letters!")
    print()


def game_pick():
    """ This function displays the pick a letter of a fruit question"""
    print(f"{Fore.YELLOW}\n~-----------------------~")
    print(f"{Fore.MAGENTA}Pick a letter of a fruit?   ")
    print(f"{Fore.YELLOW}~-----------------------~")


def game_yn():
    """ This fuction displays the yes or no option """
    print(f"{Fore.YELLOW}~----------------------------------~\n".center(85))
    print(f"{Fore.RED}Please choose Y to play or N to quit.\n".center(86))
    print(f"{Fore.YELLOW}~----------------------------------~\n".center(85))


def instructions_yn():
    """ This fuction displays the yes or no option to view
    instructions"""
    print(f"{Fore.YELLOW}~----------------------------------~\n".center(85))
    print(f"{Fore.RED}Please choose Y to read or N to play\n".center(86))
    print(f"{Fore.RED}or Q to quit.\n".center(86))
    print(f"{Fore.YELLOW}~----------------------------------~\n".center(85))


def game_win():
    """ This function displays the WIN page """
    clear()
    logo_display()
    print(Fore.YELLOW + "+-------------------------+".center(80))
    text = colored("WON!".center(80), "magenta", attrs=["reverse", "blink"])
    print(text)
    print(Fore.YELLOW + "+-------------------------+".center(80))


def game_loss():
    """ This function displays the LOST page """
    clear()
    logo_display()
    print(Fore.YELLOW + "+-------------------------+".center(80))
    text = colored("LOST!".center(80), "red", attrs=["reverse", "blink"])
    print(text)
    print(Fore.YELLOW + "+-------------------------+".center(80))
