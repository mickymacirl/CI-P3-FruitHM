# HANGMAN: The Fruit Edition(TM)

In this game, HANGMAN: The Fruit Edition(TM), players try to guess all letters of a word based on the different types of fruit.

This game is based on the Hangman, pen and paper game that possibly stretches back to the 1890s.

Stories claim that criminals sentenced to death by hanging could demand the *"Rite of Words and Life."*

First, the Executioner would pick a five-letter word, marking correctly guessed letters on the dashes of a board. Then, at every incorrect guess, the Executioner would use a sledgehammer or axe to knock away a single leg of the stand. With five wrong guesses, the criminal was hung.
If the entire word were filled in correctly or guessed, the condemned would be set free from that sentence and not tried again for that crime. The irony was that almost all of those criminals were illiterate.

The TV show Wheel of Fortune, based on the game, has been broadcast worldwide since the 1960s.

View the live project here

## How to Play

Players guess the letters of an unrevealed fruit-themed word and then draw a head, torso, arms, legs and ears of a stick figure hanging from gallows for every incorrect guess.

If the player draws all body parts and the word still hasn't been found, the player loses.

* A hangman board displays the number of guesses left.
* Players have eight attempts to guess the fruit word. Players are asked for their guesses in single letter format.
* After every attempt (unless successful), the player is asked to guess a letter contained in the fruit word.
* Every incorrect guess adds to the letters tried, and a correct guess adds to the hidden word, revealing the location of the correctly guessed letter in the fruit word.

![Main Board](./assets/readme/maingamerm.jpg)

## User Stories

This game aims to give the user a straightforward, attractive, understandable, and repeatedly playable experience.

As a User, I want to:

* play the game clearly across different devices
* play an attractive game
* understand how to play the game
* have the choice to easily play again or quit
* alert to incorrect input
* know what incorrect input has been input
* know how many attempts are left
* play a game that is not timed

As a Site Administrator I want to:

* have the random text file, player messages, and images separated into different files to facilitate easy editing
* offer the player a straightforward and understandable game

## Features

### Logo

* Pyfiglet is installed and used to import pyfiglet, which generates the Hangman text using the standard font. The cybersmall font was used for the secondary text, with centred yellow text. A logo-display function was created and stored within the art.py file and imported for use when needed.

![Logo Readme](./assets/readme/logorm.jpg)

### Game Title

* Game Title is split into a function and imported from messages.py to play in the game loading function.

![Game Title Readme](./assets/readme/gametitlerm.jpg)

### Game Loading

* Game Loading uses the time function in conjunction with the delete last line function to display a game loading screen on the welcome screen.

![Please Wait](./assets/readme/pqrm1.jpg)

        def game_loading():
            ''' This function produces a Game Loading time moving text line '''
            clear()
            logo_display()
            print(f"{Fore.YELLOW}Welcome to Hangman, the Fruit Edition(TM)\n")
            game_title()
            print("Please Wait! Game Loading.")
            time.sleep(1)
            delete_last_line()
            print(f"{Fore.RED}Drawing HANGMAN Board.")
            time.sleep(0.5)
            delete_last_line()
            print(f"{Fore.RED}Drawing HANGMAN Board..")
            time.sleep(1)
            delete_last_line()
            print(f"{Fore.RED}Drawing HANGMAN Board...")
            time.sleep(0.5)
            delete_last_line()
            print(f"{Fore.RED}Drawing HANGMAN Board....")
            time.sleep(0.5)
            delete_last_line()
            print(f"{Fore.MAGENTA}HANGMAN Board Done!")
            time.sleep(1)
            delete_last_line()
            print("Game Loading..")
            time.sleep(0.5)
            delete_last_line()
            print(f"{Fore.RED}Calculating draw distance.")
            time.sleep(1)
            delete_last_line()
            print("Game Loading...")
            time.sleep(1)
            delete_last_line()
            print(f"{Fore.RED}Generating Random Fruit Word.")
            time.sleep(1.0)
            delete_last_line()
            print("Game Loading....")
            time.sleep(0.2)
            delete_last_line()
            print(f"{Fore.MAGENTA}Fruit Word Selected!")
            time.sleep(0.5)
            delete_last_line()
            print("Game Loading.....")
            time.sleep(0.5)
            delete_last_line()
            print("Game Loading......")
            time.sleep(0.5)
            delete_last_line()
            print("Game Loading.......")
            time.sleep(0.2)
            delete_last_line()
            print(f"{Fore.MAGENTA}Complete! Game Ready!")
            print("")

![Complete](./assets/readme/pqrm2.jpg)

### Read Instructions

* Game displays the message, "Do you want to read the instructions? Y, N or Q.
* Choosing Y brings you to view the instructions.
* Choosing N brings you to the main game.
* Choosing Q quits the game.

![Instructions](./assets/readme/instrm.jpg)

### Game Instructions

* Game displays the game instructions, including the number of guesses a player gets.
* Game displays, "Do you want to play? Y, N, Q.
* Choosing Y brings you to the main game.
* Choosing N or Q quits the game.

![Game Instructions](./assets/readme/gameinstrm.jpg)

### Main Game

* The main game screen displays the hangman board, with current hangman position and number of tries left. (1 and 2)
* Letters tried supplies the already and incorrect tried letters. (3)
* The number of letters in the fruit word is displayed. (4)
* '~' is used to space out the missing and already guessed letters. (4)
* Game displays a message asking the player to Pick a letter of a fruit. (5)

![Main Game Board](./assets/readme/mainboardrm.jpg)

## Features to Implement

## Design

### Flow Chart

![Flow Chart](./assets/readme/hangmanfc.jpg)

## Technologies

## Python Libraries

### Built-in Python Libraries

* OS was imported to create a clear function to clear the terminal. Both system and name being imported for use in the clear function. The clear function improves the user experience when replaying games by removing the previous game and previous menus and making the screen clearer and more structured.

* random was imported to access the random built-in method for random numbers using randint() method. This is used to generate the random pick of the fruit words from the words.py file.

* sys was imported to use in the delete last line function.

* time was imported to use in the time.sleep commands in the game loading screen and various other places.

### Others

* Colorama was imported for use in coloring fonts and game bars in python fuctions.
* Pyfiglet was used for adding ascii art to logo.
* termcolor was used to highlight both win and loss message.py functions.

## Testing

* Lines that were excessively long, abnormalities with spacing, and single- or double-line spacing were all addressed as they surfaced. As a consequence, the code was generally clean and devoid of errors and defects when final testing began.

* Techniques like print() were used to check for flaws as the code was being created. It was possible to verify that everything was operating as it should and that functions like selecting a random word from words.py were correctly displayed as a result.

* To enable the player understand why their decision was incorrect, all user inputs were validated and printed back to the screen.

### Instructions Option Screen

Input is from the question, Do you want to want to read the instructions? Y, N, or Q.

**Expected:** Any input outside of Y for Yes, No for No, or Quit for Quit returns an error.

**Actual:** Any input out Y for Yes, No for No, or Q for Quit returned an error.

#### nn text string

![Instructions Option Testing Text](./assets/readme/readinstestrm.jpg)

#### @@ symbols

![Instructions Option Testing symbol](./assets/readme/readinstest1rm.jpg)

### Play Again Option Screen

Input is from the question, Do you want to Play Again?

**Expected:** Any input outside of Y for Yes, No for No, or Quit for Quit returns an error.

**Actual:** Any input out Y for Yes, No for No, or Q for Quit returned an error.

#### Play Again nn text string

![Play Again Option Testing Text](./assets/readme/readinstest2rm.jpg)

#### Play Again @@ symbols

![Play Again Option Testing symbol](./assets/readme/readinstest3rm.jpg)

### Main Game Input Error Checking

Input is a single letter in the alphabet.

**Expected:** Any input outside of a single letter of the alphabet returns an error.

**Actual:** A input outside of a single letter of the alphabet returned an error.

#### Main Game Input Single Letter

![Game Input Single Letter Testing](./assets/readme/readinstest4rm.jpg)

#### Main Game Input Already Guessed

Input is a letter already guessed from the correct guessed letter display.

**Expected:** Any correctly guessed letter returns an error.

**Actual:** The correctly guessed letter returned an error.

![Game Input Already Guessed Testing](./assets/readme/readinstest5rm.jpg)

#### Main Game Not In The Alphabeta

Input is a special character, or a number.

**Expected:** Any input that is a special character or a number returns an error.

**Actual:** The special character returned an error.

![Game Input Already Guessed Testing](./assets/readme/readinstest6rm.jpg)

### Validator Testing

The python files were verified using pep8 online. Every Python file was examined, and there were no mistakes found.

![PIP8 Read Me](./assets/readme/pip8rm.jpg)

## Bugs and Fixes

### PYLINT Error when using range length line 176

Error was "Consider using enumerate instead of iterating with range and lenpylint((consider-using-enumerate))"

            for i in range(len(random_word_from_list)):
                if random_word_from_list[i] not in correct_guess:
                    have_all_letters = False
                    break

There is no need to use range length, can just use enumerate to iterate over it.

Using for k_r, v_r because enumerate returns the count and the value, not just the current index.

            for k_r, v_r in enumerate(random_word_from_list):
                if v_r not in correct_guess:
                    print(k_r)  # print then clear
                    clear()
                    have_all_letters = False
                    break

### Color Bleed

The main fuction user input color was bleeding into the instructions function
logo-display, causing the logo to be yellow.

![Color Bleed](./assets/readme/colorbleedrm.jpg)

        def instructions():
            clear()
            logo_display()
            game_rules()
            user_input = input(
            f"{Fore.YELLOW}" + f"Do you want to play? Y, N or Q:{Fore.RESET}\n"
            ).lower()
            if user_input == "y":
                clear()
                main_game()

            elif user_input == "n":
                clear()
                print(Fore.RESET)  # reset color
                delete_last_line()
                logo_display()
                exit_message()
                exit()    

Added a Fore.RESET print and created a delete_last_line fuction to delete last line to clear color bleed.

![Color Bleed Fixed](./assets/readme/colorbleedfixedrm.jpg)

    print(Fore.RESET)  # reset color
    delete_last_line()

## Deployment

### Template

* A repository called 'CI-P3-FruitHM' was created using the *[Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template)*.

## Version Control

## Credits

### History of Hangman

* Used *[History of Hangman](https://www.ludozofi.com/home/games/hangman/)* for information on the history of Hangman.

### Python Formatter

* Used *[Online Python Formatter](https://www.tutorialspoint.com/online_python_formatter.htm)* to correctly format python code.

### Python Reference

* Used *[W3Schools Python](https://www.w3schools.com/python/default.asp)* for reference with python use.

### Pyfiglet

* Used *[Pyfiglet](https://github.com/pwaller/pyfiglet/)* to create ascii art for the logo.
* Used *[Code Speedy](https://www.codespeedy.com/pyfiglet-in-python/)* for code example of pyfiglet.

### Colorama

* Used *[Colorama](https://pypi.org/project/colorama/)* to produce colored terminal text.
* Used *[Stackoverflow](https://stackoverflow.com/questions/43649051/a-way-to-not-have-to-reset-the-color-style-in-colorama-every-time)* to troubleshoot colorama color reset.

### Termcolor

* Used *[Termcolor](https://pypi.org/project/termcolor/)* to create ascii art for the logo.
* Used *[TowardsDataScience](https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b)* to create termcolor background.

### pylint

* Used *[pylint](https://pypi.org/project/pylint/)* to check for errors, enforce a coding standard, and refactoring.

### Command Line Interfaces with Python

* Used *[Code Burst.io](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df)* for reference.

### Tutorials

Some helpful tutorials that were reference to help with coding some of the design and structure:

* *[Data Flair Hangman Game Python](https://data-flair.training/blogs/hangman-game-python-code/)*
* *[Geeks for Geeks Hangman Game Python](https://www.geeksforgeeks.org/hangman-game-python/)*
* *[Invent with Python Hangman Game Python](https://inventwithpython.com/invent4thed/chapter8.html)*
* *[Medium.com Hangman Game with Python](https://medium.com/@branzoldecode/hangman-game-with-python-fbd64e99a96f)*

### Clear Screen Function

* Used *[Geeks for Geeks Clear Screen Python](https://www.geeksforgeeks.org/clear-screen-python/)* to help create the clear screen function.

### Fruit Names

* Used *[7esl.com](https://7esl.com/fruits-vocabulary-english/)* for fruit words to use in words.py.

### Flow Chart Creation

* Used *[Lucidchart](https://www.lucidchart.com/pages/)* to create flow chart.

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the *Settings* tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a *Config Var* called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another *Config Var* called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.
