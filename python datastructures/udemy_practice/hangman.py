import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# print(f'Pssst, the solution is {chosen_word}.')

display = []

# display = []
for _ in range(len(chosen_word)):
    display += "_"

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(display)
    if guess not in chosen_word:
        lives = lives - 1
        if lives == 0:
            end_of_game= True
            print("You Lose!!!")
        print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("Game Over!!!!")
    

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")


