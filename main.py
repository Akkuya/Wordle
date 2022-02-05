from termcolor import colored
import random
import sys
import os

os.system('color')

def generate():
    wordFile = open('words.txt', "r")
    words = wordFile.read().splitlines()
    generate.word = words[random.randint(0, len(words))].lower()
    generate.guessed = False

generate()


while generate.guessed == False:
    colours = ['on_grey', 'on_grey', 'on_grey', 'on_grey', 'on_grey']
    count = 0
    guess=input("Guess the word!\n")


    if len(guess) != 5:
        print('Not a 5 Letter Word!')
        continue
    
    
    
    for i in range(5):
        for j in range(5):
            if guess[i] == generate.word[j]:
                colours[i] = "on_yellow"

    for i in range(5):
        if guess[i] != generate.word[i]:
            continue
        colours[i] = "on_green"
        count+=1

    
    
    print(f"{colored(guess[0], 'white', colours[0])} {colored(guess[1], 'white', colours[1])} {colored(guess[2], 'white', colours[2])} {colored(guess[3], 'white', colours[3])} {colored(guess[4], 'white', colours[4])}")
    if count == 5:
        guessed = True
        print(f'Good Job!')
        play = input('Play Again? y/n')
        if play.lower() == 'y':
            generate.guessed = False
            generate()
            continue
        sys.exit(0)
    