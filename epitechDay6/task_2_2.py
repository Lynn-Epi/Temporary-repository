text = input("Enter your sentence/word: ")
text = text.lower()

word = ""

for character in text:
    if character.isalpha():
        word += character


def palindrome(word):

    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        return False

    return palindrome(word[1:-1])


print(palindrome(word))