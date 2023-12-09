#Step 5
import random, sys, os, time

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
'coyote crow deer dog donkey duck eagle ferret fox frog goat '
'goose hawk lion lizard llama mole monkey moose mouse mule newt '
'otter owl panda parrot pigeon python rabbit ram rat raven '
'rhino salmon seal shark sheep skunk sloth snake spider '
'stork swan tiger toad trout turkey turtle weasel whale wolf '
'wombat zebra ').split(' ')
guessed_letters = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print('''_                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/    ''')
print(f'You have {lives} lives.')
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  guess = input("Guess a letter: ").lower()
  
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      continue
      
    if guess in guessed_letters:
      print(f'You have already guessed {guess}.')
      break
        

    #Check if user is wrong.
    if guess not in chosen_word:
      print(f'{guess.capitalize()} is not in the solution.')
      lives -= 1
      print(hangman_pics[6 - lives])
      if lives == 0:
        end_of_game = True
        print(f"You lose!\nThe solution was {chosen_word}!")
        sys.exit()
      elif lives != 1:
        print(f'You have {lives} lives left...')
        break
      else:
        print(f'You have {lives} life left...')
  
    #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  guessed_letters.append(guess)
    #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("You win!")
    sys.exit()