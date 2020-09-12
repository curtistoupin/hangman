# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:07:15 2020

@author: kehly
"""

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


def is_word_guessed(secret_word,letters_guessed):
    letters_guessed = ''.join(letters_guessed)
    for i in secret_word:
        for j in letters_guessed:
            if i == j:
                flag = True
                break
        if i != j:
            flag = False
            break
    return flag
    

def get_guessed_word(secret_word,letters_guessed):
    letters_guessed = ''.join(letters_guessed)
    letters = ''
    for i in secret_word:
        for j in letters_guessed:
            if i == j:
                letters += i
                break
        else:
            letters += " _ "
    return letters
    

def get_available_letters(letters_guessed):
    letters_remaining = list(string.ascii_lowercase)
    for i in letters_guessed:
        letters_remaining.remove(i)
    return(''.join(letters_remaining))


def unique_letters(secret_word):
    alphabet = list(string.ascii_lowercase)
    for i in secret_word:
        if i in alphabet:
            alphabet.remove(i)
    return 26-len(alphabet)


def hangman(secret_word):
    letters_guessed = []
    number_guesses = 6
    warnings = 3
    vowels = ["a","e","i","o","u"]
    print("--------------------------------------------------------")
    print("Welcome to the game Hangman!")
    print("I am thinking of a secret word that is",len(secret_word),"letters long.")
    print("You have",number_guesses,"guesses.")
    print("You have",warnings,"warnings.")
    print("Available letters:",get_available_letters(letters_guessed))
    
    while number_guesses != 0:
        guess = (str(input("Please guess a letter: ")))
        if guess in list(string.ascii_uppercase):
            guess = guess.lower()
        print("")
                
        if guess in get_available_letters(letters_guessed):
            letters_guessed += guess
       
            if guess in secret_word:
                print("--------------------------------------------------------")
                print("Fan-freaking-tastic! That letter is in the secret word!")
                print(get_guessed_word(secret_word,letters_guessed))
                     
                if is_word_guessed(secret_word,letters_guessed) == True:
                    print("Hotdog we have a weiner!")
                    total_score = number_guesses*unique_letters(secret_word)
                    print("Total Score:",total_score)
                    break
                    
                else:
                    print("You have",number_guesses,"guesses left.")
                    print("Available letters:",get_available_letters(letters_guessed))
                    
            else:
                if guess in vowels:
                    number_guesses -= 2
                else:
                    number_guesses -= 1
                print("--------------------------------------------------------")
                print("Oops! That letters is not in my secret word.")
                print(get_guessed_word(secret_word,letters_guessed))
                print("You have",number_guesses,"guesses left.")
                print("You have",warnings,"warnings left.")
                print("Available letters:",get_available_letters(letters_guessed))
         
        else:
            if warnings > 0:
                warnings -= 1
            else:
                number_guesses -= 1
            if guess in string.ascii_lowercase:
                print("--------------------------------------------------------")    
                print("Hey dumby, you've already guessed that letter.")
            else:
                print("--------------------------------------------------------")
                print("Hey dumby, that's not a valid letter.")
            print("You have",number_guesses,"guesses left.")
            print("You have",warnings,"warnings left.")
            print("Available letters:",get_available_letters(letters_guessed))
            
    else:
        print("Well. You officially suck at Hangman. The secret word was",secret_word+".")
   
    
wordlist = load_words()

if __name__ == "__main__":   
     secret_word = choose_word(wordlist)
     hangman(secret_word)