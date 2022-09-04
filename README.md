# HANGMAN: The Fruit Edition(TM)

In this game, HANGMAN: The Fruit Edition(TM), players try to guess all letters of a word based on the different types of fruit.

This game is based on the Hangman, pen and paper game that possibly stretches back to the 1890s.

Stories claim that criminals sentenced to death by hanging could demand the "Rite of Words and Life."

First, the Executioner would pick a five-letter word, marking correctly guessed letters on the dashes of a board.
At every incorrect guess, the Executioner would use a sledgehammer or axe to knock away a single leg of the stand. Five wrong guesses, thus, meant that the criminal was hung.

If the entire word were filled in correctly or guessed, the condemned would be set free from that sentence and not tried again for that crime. The irony was that almost all of those criminals were illiterate.

The TV show Wheel of Fortune, based on the game, has been broadcast worldwide since the 1960s.

View the live project here

## How to Play

Players guess letters of an unrevealed fruit-themed word and then draw an arm, leg, head or torso of a stick figure hanging from gallows for every incorrect guess.

If the player draws all body parts and the word still hasn't been found, the player loses.

## User Experience

## Features

### Logo

* Pyfiglet is installed and used to import pyfiglet, which generates the Hangman text using the standard font. The cybersmall font was used for the secondary text, with centred yellow text. A logo-display function was created and stored within the messages.py file and imported for use when needed.

![Logo Readme](./assets/readme/logorm.jpg)

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

## Bugs and Fixes

### PYLINT Error when using range length line 176

Error was "Consider using enumerate instead of iterating with range and lenpylint((consider-using-enumerate))"

            for i in range(len(random_word_from_list)):
                if random_word_from_list[i] not in correct_guess:
                    have_all_letters = False
                    break

No need to use range length, can just use enumerate to iterate over it.

Using for k_r, v_r because enumerate returns the count and the value, not just the current index.

            for k_r, v_r in enumerate(random_word_from_list):
                if v_r not in correct_guess:
                    print(k_r)  # print then clear
                    clear()
                    have_all_letters = False
                    break

### Color Bleed

The see_instructions fuction user input color was bleeding into the instructions function
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
            logo_display()
            exit_message()
            exit()

        elif user_input == "q":
            clear()
            logo_display()
            exit_message()
            exit()

        else:
            clear()
            logo_display()
            game_yn()
            see_instructions()

Added a Fore.RESET print and created a delete_last_line fuction to delete last line to clear color bleed.

![Color Bleed Fixed](./assets/readme/colorbleedfixedrm.jpg)

    print(Fore.RESET)  # reset color
    delete_last_line()

## Deployment

## Version Control

## Credits

### History of Hangman

* Used *[History of Hangman](https://www.ludozofi.com/home/games/hangman/)* for information on the history of Hangman.

### Pyfiglet

* Used *[Pyfiglet](https://github.com/pwaller/pyfiglet/)* to create ascii art for the logo. 

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.
