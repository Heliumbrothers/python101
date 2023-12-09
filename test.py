import time, os
stop = False

('''def ripple():
    sleep = 1 / float(input('How many FPS: '))
    while stop == False:
        print('-----')
        time.sleep(sleep)
        print('----')
        time.sleep(sleep)
        print('---')
        time.sleep(sleep)
        print('--')
        time.sleep(sleep)
        print('-')
        time.sleep(sleep)
        print('--')
        time.sleep(sleep)
        print('---')
        time.sleep(sleep)
        print('----')
        time.sleep(sleep)
        ''')


def spin():
    stop = False
    sleep = 1 / float(input('How many FPS: '))
    while stop == False:
        print('|   \n\n\n\n\n\n        ')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('/          \n\n\n\n\n\n\n\n')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-         \n\n\n\n\n\n')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\          \n\n\n\n\n\n\n\n')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('|   \n\n\n\n\n\n        ')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('/          \n\n\n\n\n\n\n\n')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-         \n\n\n\n\n\n')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\          \n\n\n\n\n\n\n\n')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        if input('Press enter key to stop') == '':
            stop = True


def piston():
    stop = False
    sleep = 1 / float(input('How many FPS: '))
    while stop == False:
        print('-\n-')
        time.sleep(sleep)
        print('-\n-\n-')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-\n-\n-\n-')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-\n-\n-\n-\n-')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        if input('Press enter key to stop') == '':
            stop = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-\n-\n-\n-\n-\n-')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-\n-\n-\n-\n-')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-\n-\n-\n-')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-\n-\n-')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-\n-')
        time.sleep(sleep)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('-')
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(sleep)
        if input('Press enter key to stop') == '':
            stop = True
        else:
            continue


if input('Which animation do you want? Type s for spin and p for piston').lower() == 's':
    spin()
else:
    piston()