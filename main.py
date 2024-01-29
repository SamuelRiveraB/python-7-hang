import random

words = ["ardvark", "baboon", "camel"]
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
lives = len(stages)


print("HANGMAN")

word = words[random.randint(0,len(words)-1)]
guess = []
for g in range(0, len(word)):
    guess.append("_")
print(guess)
compl = len(word)
corr = False

lts = []

while lives > 0 and compl > 0:
    lett = input("Guess a letter: ").lower()
    if lett not in lts:
        for e in range(0, len(word)):
            if lett == word[e]:
                compl -= 1
                corr = True
                guess[e] = lett
                print(guess)
        if corr == False:
            print(stages[lives-1])
            print(guess)
            lives -= 1
        else:
            lts.append(lett)
            corr = False
    else:
        print(f"You already guessed {lett}")

if lives == 0:
    print("You lost")
    print(f"The word was {word}")
elif compl == 0:
    print("You won!")
