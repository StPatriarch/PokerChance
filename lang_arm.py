import version_info
import json


def greeting():
    print('''
Ողջույն, սա պարզ պոկերային նախնական ձեռքի հնարավորության հաշվիչ է։ version {}. 
Դուք ընդհամենը պետք է մուտքագրեք ձեր խաղային դիրքը, նախնական խաղաքարտերը և խաղացողների քանակը։
Ծրագիրը հաշվի չի առնում խաղաքարտերի մաստային պատկանելությունը։ \U00002660  \U00002665  \U00002666  \U00002663
'''.format(version_info.version))


def position():
    greeting()
    print('''
 .-.-.-.-.-.-.-.-.-.-.-.-.    
 | D -> Dealer           |
 | SB -> Small Blind     |
 | BB -> Big Blind       |
 | EP -> Early Position  |
 | MP -> Middle Position |
 | LP -> Last Position   |
 .-.-.-.-.-.-.-.-.-.-.-.-. \n''')

    pos = input('Խնդրում եմ մուտքագրեք ձեր դիրքը \t').upper()

    if pos == 'D' or pos == 'SB' or pos == 'BB':
        small_big_dealer()
    elif pos == 'EP'or pos == 'MP':
        early_middle()
    elif pos == 'LP':
        last_position()
    else:
        print('Մուտքագրված դիրքը սխալ է։ Խնդրում եմ կրկին փորձեք։')


def percents(card, player):
    with open('chance_in_percents.json') as json_file:
        file = json.load(json_file)
        return file[card][player]


def small_big_dealer():
    cards = input('Խնդրում եմ մուտքագրեք ձեր խաղաքարտերը\t').upper()
    print('\n1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9')
    players = input('\nԽնդրում եմ մուտքագրեք խաղացողների քանակը\t')

    card_combinations = dict.fromkeys([
        'AA', 'AK', 'KQ', 'QJ', 'J9',
        'KK', 'AQ', 'KJ', 'QT', 'T9',
        'QQ', 'AJ', 'KT', 'JT',
        'JJ', 'AT',
        'TT',
        '99',
        '88',
        '77'], '\nԹույլատրված է ձեր դիրքի համար։')

    try:
        finder = card_combinations[cards]
        print(finder,)
        try:
            print('Ձեր խաղաքարտերի հաղթելու հավանականությունը՝ {}% է։'.format(percents(cards, players)))
        except KeyError:
            print('Բայց հաղթեանակի Տոկոսը շատ ցածր է։')
    except KeyError:
        try:
            rev = cards[::-1]
            finder_2 = card_combinations[rev]
            print(finder_2,)
            try:
                print('Ձեր խաղաքարտերի հաղթելու հավանականությունը՝ {}% է։'.format(percents(rev, players)))
            except KeyError:
                print('Բայց հաղթեանակի Տոկոսը շատ ցածր է։')
        except KeyError:
            print('Խաղաքարտը չի գտնվել։ Տվյալ կոմբինացիան խորհուրդ չի տրվում ձեր դիրքի համար։')


def early_middle():
    cards = input('Խնդրում եմ մուտքագրեք ձեր խաղաքարտերը\t').upper()
    print('\n1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9')
    players = input('\nԽնդրում եմ մուտքագրեք խաղացողների քանակը\t').capitalize()

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
        '55', ], '\nԹույլատրված է ձեր դիրքի համար։')

    try:
        finder = card_combinations[cards]
        print(finder,)
        try:
            print('Ձեր խաղաքարտերի հաղթելու հավանականությունը՝ {}% է։'.format(percents(cards, players)))
        except KeyError:
            print('Բայց հաղթեանակի Տոկոսը շատ ցածր է։')
    except KeyError:
        try:
            rev = cards[::-1]
            finder_2 = card_combinations[rev]
            print(finder_2,)
            try:
                print('Ձեր խաղաքարտերի հաղթելու հավանականությունը՝ {}% է։'.format(percents(rev, players)))
            except KeyError:
                print('Բայց հաղթեանակի Տոկոսը շատ ցածր է։')
        except KeyError:
            print('Խաղաքարտը չի գտնվել։ Տվյալ կոմբինացիան խորհուրդ չի տրվում ձեր դիրքի համար։')


def last_position():
    cards = input('Խնդրում եմ մուտքագրեք ձեր խաղաքարտերը\t').upper()
    print('\n1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9')
    players = input('\nԽնդրում եմ մուտքագրեք խաղացողների քանակը\t').capitalize()

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
        '22', ], '\nԹույլատրված է ձեր դիրքի համար։')

    try:
        finder = card_combinations[cards]
        print(finder,)
        try:
            print('Ձեր խաղաքարտերի հաղթելու հավանականությունը՝ {}% է։'.format(percents(cards, players)))
        except KeyError:
            print('Բայց հաղթեանակի Տոկոսը շատ ցածր է։')
    except KeyError:
        try:
            rev = cards[::-1]
            finder_2 = card_combinations[rev]
            print(finder_2,)
            try:
                print('Ձեր խաղաքարտերի հաղթելու հավանականությունը՝ {}% է։'.format(percents(rev, players)))
            except KeyError:
                print('Բայց հաղթեանակի Տոկոսը շատ ցածր է։')
        except KeyError:
            print('Խաղաքարտը չի գտնվել։ Տվյալ կոմբինացիան խորհուրդ չի տրվում ձեր դիրքի համար։')
