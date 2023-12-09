import random, sys

class GuessingNumbers:

    guesses_remaining = 10
    turns = 0
    number_range = [int(input('What is the smallest number in your range of numbers (ie. 100 for range 100-200): ')),int(input('What is the largest number in your range of numbers: '))]
    target_number = random.randint(number_range[0], number_range[1])
    
    
    def __init__(self, difficulty, single_player = bool):
        self.difficulty = difficulty
        self.single_player = single_player

    def check_number(self, user_number, target_number):
        '''Returns True if user_number > target_number, elif user_number < target_number return False else print 'YOU WIN' and exit game.'''
        if user_number > target_number:
            return True
        elif user_number < target_number:
            return False
        else:
            print('You Win!')
            sys.exit()

    def check_guesses_remaining(self):
        if self.difficulty == 'Easy':
            self.guesses_remaining = self.turns - self.guesses_remaining
            if self.guesses_remaining == 0:
                print('You Lose!')
            else:
                return self.guesses_remaining
            
    def play_turn(self):
        self.guessed_number = int(input('What number do you guess?'))
        if self.check_number(self.guessed_number, self.target_number) == True:
            print('Too High')
        elif self.check_number(self.guessed_number, self.target_number) == False:
            print('Too Low')

            if self.single_player == False:
                self.computer_guessed_number = random.randint(self.number_range[0], self.number_range[1])
                self.check_number(self.computer_guessed_number)

    def play(self):
        while self.check_guesses_remaining() > 0:
            self.play_turn(self)

    def generate_number(self):
        return random.randint(self.number_range[0], self.number_range[1])



if __name__ == "__main__":
    if input('Type \'yes\' for single-player and \'no\' for multiplayer').lower() == 'yes':
        is_single_player = True
    else:
        is_single_player = False
    user = GuessingNumbers(input('What difficulty setting do you want to play? Type \'Easy\' for easy and \'Hard\' for hard: '), is_single_player)
    
    user.play()


            


                
            