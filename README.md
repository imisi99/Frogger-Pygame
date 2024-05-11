# Frogger-Pygame
This is an objective game built using pygame and pyinstaller.  
The game requires the player to move to the top of the maps across the roads while avoiding cars     
The project can be cloned [here]()    
What the game entails:
 - The game can be played by using the keyboard direction buttons
 - Players can move the avatar anywhere on the screen to avoid the oncoming vehicles 
 - There is a total of 1 life for a player at the beginning of the game but this can go down: 
   - If the player collides with a vehicle there is a life deduction
 - Throughout the event of the game the player can have a max of 1 life only
    -
 - Once a plAyer life is below zero then it is game-over for the player and the player can do the following:
   - Press the p button to restart the game
   - Press the q button to quit the game 
 - If a player successfully reaches the end of the game, He can decide to play again or quit the game
 - There is a timer for how long it took to complete the game if the player did complete the game

The game has been made into an executable file using pyinstaller therefore there is no need for any package installation to run the game, It can be downloaded [here]()    
This is the installation Process:
 - After downloading the zip folder extract it. 
 - After extraction navigate to the app folder and you will find an executable file frogger.
 - You can create a shortcut of the game to your desktop for easy access.
 - After extraction, the folder order should be left as the game depends on all the data and would not run if the order isn't set well.

To run the game on your terminal however, you would have to clone the project and run this command on your terminal:
 -      pip install requirements.txt
 -      cd app
 -      python main.py

It was fun creating the game and I hope you enjoy it if you did, you can star the repository
