points = {
    1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}

word = input("type your word: ").upper()
score = 0
for letter in word:
    for value in points:
        if letter in points[value]:
            score += value



print(score)