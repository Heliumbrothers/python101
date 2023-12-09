print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
if input('You\'re at a crossroad. Where do you want to go? Type \'left\' or \'right\'\n').lower() == 'left':
    if input('You come to a lake. There is an island in the middle of the lake. Type \'wait\' to wait for a boat, or \'swim\' to swim across\n').lower() == 'wait':
        if int(input('You arrive at the island unharmed. There is a house with 100 doors. One leads to the treasure. 99 lead to death. Type the number of the door you want to open\n')) == 24:
            print('You found the treasure!!!')
        else:
            print('I warned you... You died :(')
    else:
        print('You start to swim, but you get too tired and then drown. Better luck next time!')
else:
    print('You fell into a hole and broke your legs. Try again')