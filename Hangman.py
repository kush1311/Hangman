import random
word=["kushal","bhavik","dharmil"]
import random
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

chosen_word = random.choice(word)
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)
end_of_the_game=False
lives=6
while not end_of_the_game:
    
    guess = input("Guess a letter: ").lower()

    for possition in range(word_length):
        latter=chosen_word[possition]
        if latter == guess:
            display[possition]=latter
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_the_game=True
            print("you lose")
    print(display)
    if "_" not in display:
        end_of_the_game=True
        print("you won")
    print(stages[lives])
