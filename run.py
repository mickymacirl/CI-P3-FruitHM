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


def get_guess():
    print("Get Player Guess")


def play_again():
    print("Play Again")


def main_game():
    print("Main Game")
