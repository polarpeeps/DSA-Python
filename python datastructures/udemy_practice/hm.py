import random

lst = ["robot","cat","batman","optimus prime","bat","dog"]

chosen_word = random.choice(lst)
print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display.append("_")
# print(display)




end_of_game = False
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

while not end_of_game:
    guess = input("Guess a letter:").lower()

    for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
    print(display)
    if guess not in chosen_word:
         lives -= 1
         print(stages[lives])
         if lives == 0:
              end_of_game = True
              print("You lost!!!")
    
    

    

    if "_" not in display:
         end_of_game= True
         print("You Won!!!")
    