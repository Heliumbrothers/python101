import random, sys, os
while True:
    moves = ['R', 'P', 'S']
    print('Try your luck (and skill) in this RPS simulator!')
    player_move = input('Type \"R\" for Rock, \"P\" for Paper and \"S\" for Scissor\n').upper()
    error_count = 0
    for i in range(0, len(moves) - 1):
        if player_move != moves[i]:
            error_count += 1
    if error_count == 3:
        print('You lose!')
        sys.exit('Enter a valid letter')

    if player_move == 'R':
        player_move_full = 'Rock'
    elif player_move == 'S':
        player_move_full = 'Scissor'
    else:
        player_move_full = 'Paper'
    print(f'You chose {player_move_full}!')
    for i in range(len(moves) - 1):
        if moves[i] == player_move:
            player_move = i
            print(player_move)

    computer_move = random.randint(0, 2)
    if  computer_move == 0:
        computer_move_full = 'Rock'
    elif computer_move == 2:
        computer_move_full = 'Scissor'
    elif computer_move == 1:
        computer_move_full = 'Paper'
    print(f'The computer chose {computer_move_full}!')
    print(computer_move)
    
    if (player_move == 0 and computer_move == 1) or (player_move == 1 and computer_move == 2) or (player_move == 2 and computer_move == 0):
        print('You lose!')
    elif player_move == computer_move:
        print('It\'s a draw!')
    else:
        print('You win!')
    error_count = 0
    if input('Type \"Yes\" to continue or \"No\" to exit\n').lower() == 'no':
        sys.exit('This game has terminated')
    else:
        os.system['cls' if os.name == 'sts' else 'clear']