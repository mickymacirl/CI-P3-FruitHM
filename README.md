# HANGMAN: The Fruit Edition(TM)

The origins of the game Hangman are unclear but could stretch back
to the 1890s. Players guess letters of an unrevealed word and then
draw an arm, leg, head or torso of a stick figure hanging from
gallows for every incorrect guess.

If players draw all body parts and the word still hasnt
been spelled out, the players lose.

# How to Play

#  User Experience

# Features

# Features to Implement

# Design

## Flow Chart

![Flow Chart](./assets/readme/hangmanfc.jpg)
# Technologies


# Python Libraries

# Testing


# Bugs and Fixes

# Deployment

# Version Control

# Credits


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
