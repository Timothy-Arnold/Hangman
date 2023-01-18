# Hangman Project

This is a project to make a fully playable version of hangman, which picks a random word from a list of words that the user then has to guess without losing too many lives. It is played through the terminal, and makes use of various features in python such as classes, loops, lambda functions, and even ascii art in order to run.

## Milestone 1

The code written in this milestone is designed to ask the user to input a letter (or a whole word if they specify so by adding a * to the front of the word). This input is then checked using a bunch of if/elif statements to make sure it is valid (making sure that letter inputs are only 1 character, they only contain letters of the English alphabet, the input hasn't already been picked etc.) I used a mapped lambda function to test if an inputed word had any non-letter characters. If the input is invalid, the while loop causes the user to iteratively be asked to enter a new input until the input is valid, in which case the while loop breaks and either the (soon to be built) check_letter or check_word methods are called.
  
```python
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
```

## Milestone 2

For this milestone I initialized the Hangman class which would set up the foundation of the Hangman game. I set up attributes which start off the game by randomly picking the word to guess from a list of word to be defined later (using the imported random package), and then setting up the blank-space word showing which letters needed to be guessed (in the form of a list of '_' strings). I made attributes for the number of (unique) letters in the word yet to be guessed, as well as the number of lives the user has remaining (since either of these reaching 0 would signify the game ending in a win or loss), and a list of already-tried inputs was also defined for use in the ask_letter method. Finally I printed out the starting message of the game, showing the user the blank spaces to fill.

```python
import random

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
```

## Milestone 3

In milestone 3 I built the check_letter and check_word methods which would be called by the ask_letter method upon receiving a valid input. For incorrect inputs I reduced the num_lives attribute by 1, and for correct inputs I either reduced the num_letters attribute by 1, or all the way down to 0 in the case of a correct word (signifying a win). In the ask_letter method I used a for loop to replace blank spaces with the inputed letter if said letter was in the word.

```python
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
```

## Milestone 4

For the final milestone I defined a function which would start an instance of the game by iteratively asking the user for a letter. I also coded the winning / losing conditions of the game which would break the while loop of asking for letters and print a winning / losing statement.

```python
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
```

## Conclusions

Writing this hangman project involved using loops, game logic etc. in order to define functions, all within the framework of a class to help carry out each instance of the game. In the future I would consider making a front end GUI for the game using Tkinter which would make it more accessible to the user.