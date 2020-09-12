# -*- coding: utf-8 -*-
"""
Created on Wed May 13 19:07:15 2020

@author: kehly
"""

import string

#TODO CT 2020-09-12 next assignment: have the program ask the user to choose their own secret word but have it not show up on screen. 
#Helpful googling term is "secure input python". Try checking out the getpass package
#https://stackoverflow.com/questions/9202224/getting-command-line-password-input-in-python
secret_word = 'lollipop'
number_guesses = 6
warnings = 3
letters_guessed = []
vowels = ["a","e","i","o","u"]

#TODO CT 2020-09-12 a word is guessed if each of the unique letters in the word have been guessed
#You can retrieve the unique letters from your secret word and letters guessed using the set() function
#Then if the unique letters in secret_word is a subset of the unique letters in letters_guessed, you know the word has been guesed.
#You can use the inbuilt .issubset() method for this
#return set(secret_word).issubset(set(letters_guessed))
def is_word_guessed(secret_word,letters_guessed):
    letters_guessed = ''.join(letters_guessed)
    for i in secret_word:
        for j in letters_guessed:
            if i == j:
                flag = True
                break   #CT 2020-09-12 This function will return true if at least one letter in letters_guessed is in the secret_word. is this intended? CT
        if i != j: #CT 2020-09-12 indent here is too short, from here j will only ever be the last letter in letters_guessed because the loop over j has already finished 
            flag = False 
            break
    return flag
    

def get_guessed_word(secret_word,letters_guessed):
    letters_guessed = ''.join(letters_guessed)
    alphabet = ''
    for i in secret_word:
        for j in letters_guessed: #CT 2020-09-12 this loop can be replaced by a check for "if i in letters_guessed:"
            if i == j:
                alphabet += i
                break
        else:
            alphabet += " _ " #CT 2020-09-12 this will put two spaces between consecutive underscores, you might want to consider changing to " _" 
    return alphabet
    

def get_available_letters(letters_guessed):
    letters_remaining = list(string.ascii_lowercase) #CT 2020-09-12 instead of doing this every time, consider keeping a single list of available letters, and when a letter is guessed used the .pop() method to pull it into the letters_guessed list
    for i in letters_guessed: # Details on the .pop() method: https://www.geeksforgeeks.org/python-list-pop/ - the .pop() method removes a chosen member of a list and returns that member so that you could, for example, append it to antoher list
        letters_remaining.remove(i) #i.e. letters_guessed.append(letters_remaining.pop('a')) will remove the letter 'a' from letters_remaining and add it to letters_guessed
    return(''.join(letters_remaining))


def unique_letters(secret_word):
    alphabet = list(string.ascii_lowercase) 
    for i in secret_word: #CT 2020-09-12 len(set(secret_word)) returns the number of unique letters in secret word. You can use this and shorten this to return 26-len(set(secret_word))
        if i in alphabet:
            alphabet.remove(i)
    return 26-len(alphabet)


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
    print("Well. You officially suck at Hangman. The secret word was",secret_word) #rude :(