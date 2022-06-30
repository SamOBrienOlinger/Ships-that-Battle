#Ships that Battle

# **Ships that Battle**

For my third Portfolio Project submitted as part of the Code Institute's Diploma in full-stack software development course, I created a board game, commonly known as battleship, called ' Ships that Battle'. This is a Python terminal that runs using the Code Institute mock terminal on Heroku.   

![Website on multiple screens](assets/README.md-images/README.md-multiple-screens.png)

- **[Click Here]( https://ships-that-battle.herokuapp.com/)** to see the deployed website. 

- To view the repository on Github **[Click Here](https://github.com/SamOBrienOlinger/Ships-that-Battle)**.


## **Summary**
  This interactive game provides users with an easy way to 'fire cannonballs' at a computer ‘enemy’s fleet of ships’. The game is based on the well-known board game ‘Battleship’, to learn more about this game [Click Here]( https://en.wikipedia.org/wiki/Battleship_(game).



## **[Contents](#contents)**

1.	**[How to Play](#how-to-play)**
2.	**[Features](#features)**
3.	**[Features Left to Implement](#features-left-to-implement)**
4.	**[Data Model](#data-model)**
5.	**[Testing](#testing)**
6.	**[Bugs](#bugs)**
7.	**[Deployment](#deployment)**
8.	**[Credits](#credits)**
9.	**[Acknowledgements](#acknowledgements)** 

## **[How to Play](#how-to-play)**

In this version of the classic Battleship game, the player enters their name and an empty board is displayed. Five randomly located ships are generated which the player cannot see. 

The player must guess the coordinates of the hidden ships by choosing a row number and a column letter. The player has ten ‘cannonballs’ or turns to take in order to ‘hit’ the hidden ships. 

Hits are indicted by ‘X’ and misses ‘-‘

If the player hits all of the computer’s ships they win the game. If they fire all of their cannonballs and fail to do so, they lose the game.  

## **[Features](#features)**

# Existing features
* Random board generation
  * Ships are randomly placed on the board by the computer so that the player cannot see where they are (change code on line 101)


  ![player board](images/README.md-player-board.png)

  * Accepts player’s input

  * Validates coordinates input by player

  * Tells player if they input invalid values or the same values more than once

  ![inout validation](images/README.md-input-validation.png)

  


