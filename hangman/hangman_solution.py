'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''

import random
import string

Hangman_images = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''']

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    check_word(word)
        Checks if the word guessed is correct.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.number_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_letters = []
        print(f"The mystery word has {len(self.word)} characters")
        print(f"You have {self.num_lives} lives to guess the word")
        print(f"If you want to guess the whole word, type * followed by the word e.g. *python")
        print(f"{self.word_guessed}")

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        if letter in self.word:
            print(f"Nice! {letter} is in the word!")
            self.number_letters -= 1
            for index in range(len(self.word)):
                if self.word[index] == letter:
                    self.word_guessed[index] = letter
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Sorry, {letter} is not in the word.\nYou have {self.num_lives} lives left.')
            print(Hangman_images[self.num_lives])
        if self.number_letters != 0:
            print(f"You have already tried: {self.list_letters}")

    def check_word(self, word) -> None:
        '''
        Checks if the word guessed is correct.
        If it is, it replaces all of the '_' in the word_guessed list with the correct letters.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        word: str
            The word to be checked

        '''
        if word == self.word:
            print(f"Nice! {word} is the word!")
            self.number_letters = 0
            print(list(word))
        else:
            self.num_lives -= 1
            print(f'Sorry, {word} is not the word.\nYou have {self.num_lives} lives left.')
            print(Hangman_images[self.num_lives])
        if self.number_letters != 0:
            print(f"You have already tried: {self.list_letters}")

    def ask_letter(self):
        '''
        Asks the user for a letter and checks three things:
        1. If the input is actually the user trying to guess a word (using *)
        2. If the letter has already been tried
        3. If the character is a single character
        If it passes check 1, it calls the check_word method.
        Else, if it passes checks 2 and 3, it calls the check_letter method.
        '''

        while True:
            letter = input("Please enter a letter: ").lower()
            if letter[0] == "*":
                word = letter[1:]
                if word == "":
                    print("No word detected")
                elif False in list(map(lambda x: x in string.ascii_lowercase, list(word))):
                    print("You can only use letters from the English alphabet")
                elif word in self.list_letters:
                    print(f"{word} was already tried")
                else:
                    self.list_letters.append(word)
                    Hangman.check_word(self, word=word)
                    break
            elif letter == "":
                print("No input detected")
            elif len(letter) != 1:
                print("Please, enter just one character")
            elif letter not in list(string.ascii_lowercase):
                print("You can only use letters from the English alphabet")
            elif letter in self.list_letters:
                print(f"{letter} was already tried")
            else:
                self.list_letters.append(letter)
                Hangman.check_letter(self, letter=letter)
                break

def play_game(word_list):
    game = Hangman(word_list)
    while True:
        game.ask_letter()
        if game.num_lives == 0:
            print(f"You ran out of lives. The word was {game.word}.")
            break
        if game.number_letters == 0:
            if game.num_lives == 5:
                print("Congratulations, you won without losing any lives!")
            else:
                print("Congratulations, you won!")
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
