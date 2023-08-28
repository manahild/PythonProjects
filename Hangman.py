import random

lis = ["apple", "mango", "banana"]
lis2 = []
lives = 6
word = random.choice(lis)

for x in word:
    lis2.extend("_")

print(lis2)

game_over = False
while not game_over:
    guess = input("Enter your guess: ")

    for i in range(len(word)):
        letter = word[i]
        if guess == letter:
            lis2[i] = guess
            print(lis2)

    if guess not in word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")
            print(stages[0])

    if "_" not in lis2:
        print("You won")
        game_over = True

stages = [
    '''
    --------
    |
    |
    |
    |
    |
    ''',
    '''
    --------
    |      |
    |
    |
    |
    |
    ''',
    '''
    --------
    |      |
    |      O
    |
    |
    |
    ''',
    '''
    --------
    |      |
    |      O
    |     /|\\
    |
    |
    ''',
    '''
    --------
    |      |
    |      O
    |     /|\\
    |      |
    |
    ''',
    '''
    --------
    |      |
    |      O
    |     /|\\
    |      |
    |     / \\
    '''
]

stages.reverse()

