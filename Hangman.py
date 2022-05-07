
from words import choose_word
from images import IMAGES
import random


def ifValid(user_input):
    if len(user_input) != 1:
        return False
    if not user_input.isalpha():
        return False


    return True

def is_word_guessed(secret_word, letters_guessed):
    if secret_word==get_guessed_word(secret_word,letters_guessed):
        return True
    return False









def get_guessed_word(secret_word, letters_guessed):







    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):






    import string
    letters_left = string.ascii_lowercase
    for i in letters_guessed:
        letters_left=letters_left.replace(i,"")
    return letters_left

def get_hint(secret_word,letters_guessed):
    letter_not_guessed=[]
    for i in secret_word:
        if i not in letters_guessed:
            if i not in letter_not_guessed:
                letter_not_guessed.append(i)
    return random.choice(letter_not_guessed)

def hangman(secret_word):












    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    letters_guessed = []
    total_lives=remaining_lives=8
    images_selection_list_indices=[0,1,2,3,4,5,6,7]
    user_difficulty_choise=input("aap kitne level pe game play karna chate hain?\na)\tEasy\nb)\tMedium\nc)\tHard\n\n\Apni choice a,b or c ki term mein btayein\n")
    
    
    
    if user_difficulty_choise=="b":
        total_lives=remaining_lives=6
        images_selection_list_indices=[0,2,3,5,6,7]
    elif user_difficulty_choise=="c":
        total_lives=remaining_lives=4
        images_selection_list_indices=[1,3,5,7]
    else:
        if user_difficulty_choise not in ["a","b","c"]:
            print("your choise is invalid\ngame is start in easy mode")


    while(remaining_lives>0):
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)
        guess = input("Please guess a letter: ")
        letter = guess.lower()

        if guess=="hint":
            letter=get_hint(secret_word,letters_guessed)
        else:
            letter=guess.lower()
        
        
        if (not ifValid(letter)):
            print("invalid input")
            continue
        if letter in secret_word:
            letters_guessed.append(letter)
            print(letters_guessed)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")
            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            remaining_lives-=1
            print(IMAGES[images_selection_list_indices[total_lives-remaining_lives]])
            print ("remaining_lives",str(remaining_lives))
            print("")
    else:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")
secret_word = choose_word()
hangman(secret_word)