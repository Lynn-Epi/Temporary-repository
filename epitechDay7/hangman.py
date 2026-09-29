

import random
from english_words import english_words_lower_set

def randomWord():
        return random.choice(list(english_words_lower_set))

mysteryWord = randomWord()
guessedLetters = set()
penalties = 0
maleableWord = ""

for letter in mysteryWord:
    maleableWord += "_"

print(*maleableWord, sep=" ")
while maleableWord != mysteryWord and penalties < 12:

    guess = input("Guess a letter or word: ")
    if len(guess) == 1:
        if guess not in mysteryWord:
            penalties += 1

        for letterIndex in range(len(mysteryWord)):
            if mysteryWord[letterIndex] == guess:
                guessedLetters.add(guess)

        maleableWord = ""

        for letter in mysteryWord:
            if letter in guessedLetters:
                maleableWord += letter
            else:
                maleableWord += "_"
    else:

        if guess == mysteryWord:
            maleableWord = mysteryWord
        else:
            penalties += 5



    print(mysteryWord)
    print(*maleableWord, sep=" ")   
    print("mistakes", penalties,"/12" )
    #print(*maleableWord, sep=" ")
if penalties >= 12:
    print("You lose!")
else:
    print("You win!")