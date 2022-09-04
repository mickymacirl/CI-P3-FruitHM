# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from os import system, name
import sys
import random
import time
from colorama import init
from colorama import Fore
from board import board  # import board from board.py
from words import words  # import words from words.py
from art import logo_display  # import logo_display from art.py
from messages import exit_message  # import exit_message from message.py
from messages import game_title  # import game_title from messages.py
from messages import game_rules  # import game_rules from messages.py
from messages import game_pick  # import game_rules from messages.py
from messages import game_yn  # import game_yn from messages.py
from messages import instructions_yn  # import instructions from messages.py
from messages import game_win  # import game_win from messages.py
from messages import game_loss  # import game_loss from messages.pyS

init(autoreset=True)  # auto reset colorama


# define our clear function
def clear():
    """This function uses the os import and assigns clear
    to clear the screen"""

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def get_random_word(words_list):
    """Get Random Word Function
    This function uses the random import to get a random word from the
    words.py file.
    """
    list_of_words = random.randint(0, len(words_list) - 1)
    return words_list[list_of_words]


def display_the_board(missing_letter, correct_guess, random_word_from_list):
    # pass
    """This function builds the game board from board.py and displays the
    length of the missing letter variable"""
    print(Fore.YELLOW + "HANGMAN: Fruit Edition(TM)")
    print(board[len(missing_letter)])
    print(f"{Fore.YELLOW}~-----------------------------------------~")
    print("Letters tried:", end=" ")
    for letter in missing_letter:
        print(letter, end=" ")
    print()
    print(f"{Fore.YELLOW}~-----------------------------------------~")

    empty = "~" * len(random_word_from_list)  # create empty and build from

    for k_r, v_r in enumerate(random_word_from_list):
        if v_r in correct_guess:
            empty = empty[:k_r] + random_word_from_list[k_r] + empty[k_r + 1:]

    word_length = len(random_word_from_list)
    print(f"The word has {word_length} letters:")
    for letter in empty:
        # Display random word from the words
        print(letter, end=" ")
    print("\n")
    print(random_word_from_list)


def get_guess(already_guessed):
    """This function askes for guess, and checks that guess is
    not greater than 1, display error message
    must be equal to letter
    must not equal an already guessed letter"""
    while True:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        game_pick()
        guessed = input()  # Get player guess
        guessed = guessed.lower()  # Force guessed lowercase
        clear()  # Clear Screen
        if len(guessed) != 1:
            clear()  # Clear Screen
            logo_display()  # Display Logo
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
            check_guess = f"{Fore.RED}'" + guessed + "' checking."
            i = check_guess.center(79, " ")
            print(i)
            time.sleep(1)
            delete_last_line()
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
            time.sleep(1)
            delete_last_line()
            clear()
            logo_display()
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
            check_guess = f"{Fore.RED}'" + guessed + "' checking.."
            i = check_guess.center(79, " ")
            print(i)
            time.sleep(1)
            delete_last_line()
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
            check_guess = f"{Fore.RED}'" + guessed + "' isn't acceptable!"
            i = check_guess.center(79, " ")
            print(i)
            print(f"{Fore.RED}Enter a single fruit letter only!".center(80))
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
        elif guessed not in alphabet:
            clear()
            logo_display()
            print(f"{Fore.YELLOW}~------------------------------~".center(80))
            check_guess = f"{Fore.RED}'" + guessed + "' is not a letter!"
            i = check_guess.center(79, " ")
            print(i)
            print(f"{Fore.RED}Enter a LETTER only!".center(80))
            print(f"{Fore.YELLOW}~------------------------------~".center(80))
        elif guessed in already_guessed:
            logo_display()
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
            check_guess = f"{Fore.RED}'" + guessed + "' is already used!"
            i = check_guess.center(79, " ")
            print(i)
            print(f"{Fore.RED}Choose another letter!".center(80))
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
        else:

            return guessed


def play_again():
    """This function askes the player do they want to play again"""
    player_choice = input(
        f"{Fore.YELLOW}" + f"Do you want to play again? Y or N:{Fore.RESET}\n"
    ).lower()
    if player_choice == "y":
        clear()
        main_game()

    elif player_choice == "n":
        clear()
        logo_display()
        exit_message()
        exit()

    else:
        clear()
        logo_display()
        game_yn()
        play_again()


def main_game():
    print("Main Game")
