
Project Overview-
  This project is a text-based implementation of the classic Hangman Game, developed as part of the Python Programming Internship at CodeAlpha. The goal of the project is to demonstrate proficiency in Python fundamentals, including data structures, control flow, and user interaction.  
Task Description
  The objective of Task 1 is to create a functional console-based game where a player attempts to guess a secret word one letter at a time. To meet the specific requirements of the internship, the project follows these guidelines:  
 1.Word Selection: The game utilizes a predefined list of 5 words for selection.  
 2.Guess Limit: The player is restricted to a maximum of 6 incorrect guesses.  
 3.Interface: The game operates entirely through basic console input and output without external graphics.  
Technical Implementation
   The program is built using several key Python concepts to ensure efficient logic and clear gameplay:  
     1.Random Module: Used to select a secret word from the predefined list at the start of each session.  
     2.While Loops: Drives the main game engine, allowing the game to continue until the player wins or runs out of attempts.  
     3.Conditional Logic (if-else): Manages the comparison between user input and the secret word, determining if a guess is correct or incorrect.  
     4.Lists and Strings: Utilized to track the state of the word being guessed and to display progress to the player using underscores.  
How the Game Works
     1.Initialization: The program selects a random word and displays its length to the user using underscores.
     2.User Input: The player enters a single letter to guess part of the word.
     3.Verification: The system checks if the letter exists in the word. If found, the letter is revealed in its correct position. If not, the player loses one of          their 6 lives.
     4.End State: The game concludes when all letters are guessed (Win) or when the lives counter reaches zero (Loss).
Installation and Usage
     1.Ensure you have Python 3.14.2 installed on your system.
     2.Clone the repository: git clone https://github.com/YourUsername/CodeAlpha_HangmanGame.  
     3.Navigate to the directory and run the script: python main.py.