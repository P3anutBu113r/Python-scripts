import random
mainloop = True
guesses = 10
wantedlength = int(input("Enter the length of the word you want: "))
if wantedlength <= 0:
    print("invalid length")

findloop = True
with open(<your wordlist>, "r") as everyword:
    potential_words = everyword.read().splitlines()


while findloop == True:
    secret_word = potential_words[random.randint(0,len(potential_words)-1)]
    if len(secret_word) == wantedlength:
        findloop = False

letters = 0
def break_string_to_list(word):
    wordcharacters = []
    for char in word:
        char = char.lower()
        wordcharacters.append(char)
    return wordcharacters
secretwordlist = break_string_to_list(secret_word)
print(f"The length of the word is: {len(secret_word)}")
print ("Dont guess higher then this")

while mainloop:
    if guesses >= 1:
        print("you have ", guesses, " guesses left")
        guesses -= 1
        guess = input("what's your guess: ")
        if len(guess) > len(secret_word):
            print("invalid length")
            guess = ""

        guesslist = break_string_to_list(guess)
        if guess == secret_word:
            print("you win!")
            mainloop = False
        else:
            for char in set(secretwordlist) & set(guesslist):
                print(f"{char} is in both words")

    else:
        print("you lose!")
        print(f"The word was {secret_word}")
        mainloop = False