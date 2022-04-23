import random
import hangman_life
import words

print(hangman_life.logo)
print("||-- WELCOME TO THE HANGMAN GAME --||\n\n")

word_chosen = random.choice(words.word_list)

#print(word_chosen)
length_word = len(word_chosen)

word_guessed = ''
for letter in range(length_word):
  word_guessed += '_'

print(f"Word to Guess: {word_guessed}")
game_is_over = False

vidas = 6
somador = 0
data_base = ''

while not game_is_over:

  letter_guessed = input("Guess the letter: ").lower()
  #print(data_base)

  if not letter_guessed in data_base:

    data_base += letter_guessed

    verifier = 0

    for iterator in range(len(word_chosen)):
      if letter_guessed == word_chosen[iterator]:
        word_guessed = word_guessed[:iterator] + letter_guessed + word_guessed[iterator+1:]
        somador += 1
        verifier = 1

    if verifier == 0:
      vidas -= 1
      print(f"You just lost one life. Now you have {vidas}")
      print(hangman_life.stages[vidas])

    print(f"Word: {word_guessed}\n")

    if somador == length_word:
      print("YOU WIN")
      game_is_over = True

    if vidas == 0:
      game_is_over = True
      print(f"The word was: {word_chosen}")
      print("GAME OVER")
      print

  else:
    print("Choose another letter, this one was already used!\n")
