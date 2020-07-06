# Creates a dictionary called 'score' where each letter has been assigned its corresponding value
score = {"a": 1, "b": 3, "c": 3, "d": 2,
         "e": 1, "f": 4, "g": 2, "h": 4,
         "i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3,
         "q": 10, "r": 1, "s": 1, "t": 1,
         "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4, "z": 10}


# Creates a function which takes 1 argument, in this case it is the input word that will be entered.
def scrabble_score(word):
    # Initial value for total scores is initially an empty list
    total = []
    # Looks at every letter in the 'word'
    for letter in word
        # scrabble words has to be lowered because capitals aren't included
        letter = letter.lower()

        # Adds the score of each letter into the total
        total.append(score[letter.lower()])
    # returns the list as a singular number
    return sum(total);


# Input your own word to calculat the score
your_word = input("Word score: ");

# Last line congrats. Prints of your score!!
print(scrabble_score(your_word));
