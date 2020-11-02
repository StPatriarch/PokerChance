import version_info
import json


def greetings():
    print('''
Hello, this is simple poker Starting hands chance calculator | version {}. 
You should just enter your position, your starting hands and number of players.
Program is't take into consideration card suits.  \U00002660  \U00002665  \U00002666  \U00002663
    '''.format(version_info.version))


def position():
    greetings()
    print('''
 .-.-.-.-.-.-.-.-.-.-.-.-.    
 | D -> Dealer           |
 | SB -> Small Blind     |
 | BB -> Big Blind       |
 | EP -> Early Position  |
 | MP -> Middle Position |
 | LP -> Last Position   |
 .-.-.-.-.-.-.-.-.-.-.-.-. \n''')

    pos = input('Please enter your Position \t').upper()

    while True:

        if pos == 'D' or pos == 'SB' or pos == 'BB':
            small_big_dealer()
        elif pos == 'EP'or pos == 'MP':
            early_middle()
        elif pos == 'LP':
            last_position()
        else:
            print('Chosen position is not valid. Please try again.')
            break


def percents(card, player):
    with open('chance_in_percents.json') as json_file:
        file = json.load(json_file)
        return file[card][player]


def small_big_dealer():
    cards = input('Please enter your cards\t').upper()
    print('\n1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9')
    players = input('\nPlease enter number of Players\t')

    card_combinations = dict.fromkeys([
        'AA', 'AK', 'KQ', 'QJ', 'J9',
        'KK', 'AQ', 'KJ', 'QT', 'T9',
        'QQ', 'AJ', 'KT', 'JT',
        'JJ', 'AT',
        'TT',
        '99',
        '88',
        '77'], '\nRecommended for your Position.')

    try:
        finder = card_combinations[cards]
        print(finder,)
        try:
            print('The possibility of winning your cards is {}%'.format(percents(cards, players)))
        except KeyError:
            print('But the winning percentage is very low.')
    except KeyError:
        try:
            rev = cards[::-1]
            finder_2 = card_combinations[rev]
            print(finder_2,)
            try:
                print('The possibility of winning your cards is {}%'.format(percents(rev, players)))
            except KeyError:
                print('But the winning percentage is very low.')
        except KeyError:
            print('Card not found. Not Recommended Combination for your Position.')


def early_middle():
    cards = input('Please enter your cards\t').upper()
    print('\n1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9')
    players = input('\nPlease enter number of Players\t')

    card_combinations = dict.fromkeys([
        'AA', 'AK', 'KQ', 'JT',
        'KK', 'AQ', 'KJ', 'J9',
        'QQ', 'AJ', 'KT', 'J8',
        'JJ', 'AT', 'K9', 'T9',
        'TT', 'A9', 'QJ', 'T8',
        '99', 'A8', 'QT', '98',
        '88', 'A7', 'Q9',
        '77', 'A6', 'Q8',
        '66',
        '55', ], '\nRecommended for your Position.')

    try:
        finder = card_combinations[cards]
        print(finder,)
        try:
            print('The possibility of winning your cards is {}%'.format(percents(cards, players)))
        except KeyError:
            print('But the winning percentage is very low.')
    except KeyError:
        try:
            rev = cards[::-1]
            finder_2 = card_combinations[rev]
            print(finder_2,)
            try:
                print('The possibility of winning your cards is {}%'.format(percents(rev, players)))
            except KeyError:
                print('But the winning percentage is very low.')
        except KeyError:
            print('Card not found. Not Recommended Combination for your Position.')


def last_position():
    cards = input('Please enter your cards\t').upper()
    print('\n1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9')
    players = input('\nPlease enter number of Players\t')

    card_combinations = dict.fromkeys([
        'AA', 'AK', 'KQ', 'QJ', 'T7',
        'KK', 'AQ', 'KJ', 'QT', '98',
        'QQ', 'AJ', 'KT', 'Q9', '97',
        'JJ', 'AT', 'K9', 'Q8', '96',
        'TT', 'A9', 'K8', 'JT', '87',
        '99', 'A8', 'K7', 'J9', '86',
        '88', 'A7', 'K6', 'J8', '76',
        '77', 'A6', 'K5', 'J7', '75',
        '66', 'A5', 'K4', 'T9', '65',
        '55', 'A4', 'K3', 'T8',
        '44', 'A3', 'K2',
        '33', 'A2',
        '22', ], '\nRecommended for your Position.')

    try:
        finder = card_combinations[cards]
        print(finder,)
        try:
            print('The possibility of winning your cards is {}%'.format(percents(cards, players)))
        except KeyError:
            print('But the winning percentage is very low.')
    except KeyError:
        try:
            rev = cards[::-1]
            finder_2 = card_combinations[rev]
            print(finder_2,)
            try:
                print('The possibility of winning your cards is {}%'.format(percents(rev, players)))
            except KeyError:
                print('But the winning percentage is very low.')
        except KeyError:
            print('Card not found. Not Recommended Combination for your Position.')
