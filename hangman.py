import random
words = ["mouse", "beekeeper", "rail"]

# choose a random word
rando_word = random.choice(words)
print(f"the chosen word is: {rando_word}")

# create an empty list
i = 1
empty_list = []
for i in range(len(rando_word)):
    empty_list += "_"


print(empty_list)

while "_" in empty_list:
    # choose a letter
    lette = input("choose a aletter? ")

    for position in range(len(rando_word)):
        letter = rando_word[position]
        if letter == lette:
            empty_list[position] = letter

    print(empty_list)
print("you win!")

list2 = [
    """
    +---+
    |   |
        |
    |   |"""empty_list

]