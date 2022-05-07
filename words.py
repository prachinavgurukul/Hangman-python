import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    # word_list = ["navgurukul", "learning", "kindness"]
    # return word_list
    w="/home/jijasarak/Desktop/Hangman.python/words.py/words.txt"
    infile=open(w,"r")
    line=infile.readline()
    word_list=str.split(line)
    print(" ",len(word_list),"words loaded.\n")
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word