import random

from english_words import english_words_lower_set

def randomWord():
        return random.choice(list(english_words_lower_set))

test = randomWord()

print(test)
print(test)
print(test)
print(test)