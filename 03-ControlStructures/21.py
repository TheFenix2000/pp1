def addSpace(var):
    spaceWord = ""
    for letter in var:
        spaceWord += letter + " "
    spaceWord = spaceWord[:-1]
    print(spaceWord)

university = "University of Economics in Cracow"

addSpace(university)