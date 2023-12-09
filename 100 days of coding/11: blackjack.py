import random, sys, os
os.system('cls' if os.name == 'sts' else 'clear')


class BlackJack:
    '''Requires 2 uses: computer and player to work'''
    def __init__(self, score):
        self.score = score

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    card_names = ['Ace', '2', '3' '4', '5', '6', '7', '8', '9', '10']
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    turns = 0
    #Flags:
    is_player_bust = False
    is_computer_bust = False
    is_computer_standing = False
    is_player_standing = False
    is_player_starting = True
    
    
    def deal_card(self):
        '''Deals random cards'''
        dealt_card = random.choice(self.cards)
        try:
            return [dealt_card, self.card_names[int(self.cards[int(self.cards.index(int(dealt_card)- 1))])]]
        except:
            return dealt_card, self.card_names[self.cards[len(self.cards) + 2]]


    def deal_multiple_cards(self, number_of_cards):
        '''Deals random cards'''
        for i in range(0, number_of_cards + 1):
            dealt_card = random.choice(self.cards)
            return [dealt_card, self.card_names[self.cards.index(dealt_card)]]

    def calculate_score(self, score_list):
        '''Calculates scores of players'''
        if score_list != [11, 10] or [10, 11]: # BlackJack
            return sum(score_list)

    def check_blackjack(self, score_list, user_name):
        '''Checks for blackjack in list of cards'''
        if score_list == [11, 10] or [10, 11]:
            user_name
            print(f'{user_name} has blackjack! {(user_name).upper()} wins!')
            sys.exit()
        else:
            return False
        
    def compare(self):
        '''Checks for win or loss'''
        if 21 - self.user_score < (21 - self.computer_score):
            print('You win!')
            sys.exit()
        elif 21 - self.user_score > (21 - self.computer_score):
            print('You lose!')
            sys.exit()
        elif 21 - self.user_score == (21 - self.computer_score):
            print('It\'s a draw!')
            sys.exit()
        elif self.is_player_bust == True:
            print('You went over 21! You lose!')
            sys.exit()
        elif self.is_computer_bust == True:
            print('The computer went over 21! You win!')

    def check_turn(self):
        '''Checks whose turn it is to play. Returns True if is user's turn'''
        if self.is_player_bust and self.is_player_standing == False:
            if self.is_player_starting == True:
                if self.turns % 2 == 1:
                    return True
            else:
                if self.turns % 2 == 0:
                    return False
                
    def convert(self, card_drawn):
        '''Converts value of card_drawn into card_name and returns name of card'''
        for i in range(0, len(self.cards)):
            if self.cards[i] == self.card_names[i] and self.cards[i] != 11:
                return self.card_names[i]
            else:
                return 'Ace'
    
    def change_card(self, card_to_change, card_to_replace):
        if card_to_change.lower() == 'ace':
            self.score[self.score.index(card_to_replace)] = 11
        else:
            self.score[self.score.index(card_to_change)] = card_to_replace
        return self.score
    
    def computer_turn(self):
        if self.computer_score <= 17:
            computer.deal_card()
            if sum(computer) > 21:
                self.is_computer_bust = True
            else:
                return self.computer_cards


    
user = BlackJack(score=0)
user.deal_card()
user.deal_card()
computer = BlackJack(score=0)
computer.deal_card()
computer.deal_card()



print('Welcome to BlackJack!')
if input('Do you want to play? Type \'yes\' to play: ').lower == 'yes':
    while True:
        # if user.turns == 1:
        if user.check_turn == True or user.is_player_starting:
            if input('Do you want to \'Stand\' or \'Draw\'').lower() == 'Draw':
                deal_card = user.deal_card
                user.compare()
            else:
                user.is_player_standing = True
        else:
            computer.computer_turn()
            computer.compare()


