import Information


def greeting():
    print('''
Ողջույն, սա պարզ պոկերային նախնական ձեռքի հնարավորության հաշվիչ է։ version {}. 
Դուք ընդհամենը պետք է մուտքագրեք ձեր խաղային դիրքը և նախնական խաղաքարտերը։
Ծրագիրը հաշվի չի առնում խաղաքարտերի մաստային պատկանելությունը։ \U00002660  \U00002665  \U00002666  \U00002663
'''.format(Information.version))


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

    pos = str.upper(input('Խնդրում եմ մուտքագրեք ձեր դիրքը \t'))

    if pos == 'D':
        small_big_dealer()
    elif pos == 'SB':
        small_big_dealer()
    elif pos == 'BB':
        small_big_dealer()
    elif pos == 'EP':
        early_middle()
    elif pos == 'MP':
        early_middle()
    elif pos == 'LP':
        last_position()
    else:
        print('Մուտքագրված դիրքը սխալ է։ Խնդրում եմ կրկին փորձեք։')


def small_big_dealer():
    first_card = input('Խնդրում եմ մուտքագրեք ձեր խաղաքարտերը\t')

    cards = str.upper(first_card)

    card_combinations = {

        'AA': 'Recommended', 'AK': 'Recommended', 'KQ': 'Recommended', 'QJ': 'Recommended', 'J9': 'Recommended',
        'KK': 'Recommended', 'AQ': 'Recommended', 'KJ': 'Recommended', 'QT': 'Recommended', 'T9': 'Recommended',
        'QQ': 'Recommended', 'AJ': 'Recommended', 'KT': 'Recommended', 'JT': 'Recommended',
        'JJ': 'Recommended', 'AT': 'Recommended',
        'TT': 'Recommended',
        '99': 'Recommended',
        '88': 'Recommended',
        '77': 'Recommended',

    }

    try:
        finder = card_combinations[cards]
        print(finder)
    except KeyError:
        try:
            rev = cards[::-1]
            finder_2 = card_combinations[rev]
            print(finder_2)
        except KeyError:
            print('Խաղաքարտը չի գտնվել։ Տվյալ կոմբինացիան խորհուրդ չի տրվում ձեր դիրքի համար։')


def early_middle():
    first_card = input('Խնդրում եմ մուտքագրեք ձեր խաղաքարտերը\t')

    cards = str.upper(first_card)

    card_combinations = {

        'AA': 'Recommended', 'AK': 'Recommended', 'KQ': 'Recommended', 'JT': 'Recommended',
        'KK': 'Recommended', 'AQ': 'Recommended', 'KJ': 'Recommended', 'J9': 'Recommended',
        'QQ': 'Recommended', 'AJ': 'Recommended', 'KT': 'Recommended', 'J8': 'Recommended',
        'JJ': 'Recommended', 'AT': 'Recommended', 'K9': 'Recommended', 'T9': 'Recommended',
        'TT': 'Recommended', 'A9': 'Recommended', 'QJ': 'Recommended', 'T8': 'Recommended',
        '99': 'Recommended', 'A8': 'Recommended', 'QT': 'Recommended', '98': 'Recommended',
        '88': 'Recommended', 'A7': 'Recommended', 'Q9': 'Recommended',
        '77': 'Recommended', 'A6': 'Recommended', 'Q8': 'Recommended',
        '66': 'Recommended',
        '55': 'Recommended',


    }

    try:
        finder = card_combinations[cards]
        print(finder)
    except KeyError:
        try:
            rev = cards[::-1]
            finder_2 = card_combinations[rev]
            print(finder_2)
        except KeyError:
            print('Խաղաքարտը չի գտնվել։ Տվյալ կոմբինացիան խորհուրդ չի տրվում ձեր դիրքի համար։')


def last_position():
    first_card = input('Խնդրում եմ մուտքագրեք ձեր խաղաքարտերը\t')

    cards = str.upper(first_card)

    card_combinations = {

        'AA': 'Recommended', 'AK': 'Recommended', 'KQ': 'Recommended', 'QJ': 'Recommended', 'T7': 'Recommended',
        'KK': 'Recommended', 'AQ': 'Recommended', 'KJ': 'Recommended', 'QT': 'Recommended', '98': 'Recommended',
        'QQ': 'Recommended', 'AJ': 'Recommended', 'KT': 'Recommended', 'Q9': 'Recommended', '97': 'Recommended',
        'JJ': 'Recommended', 'AT': 'Recommended', 'K9': 'Recommended', 'Q8': 'Recommended', '96': 'Recommended',
        'TT': 'Recommended', 'A9': 'Recommended', 'K8': 'Recommended', 'JT': 'Recommended', '87': 'Recommended',
        '99': 'Recommended', 'A8': 'Recommended', 'K7': 'Recommended', 'J9': 'Recommended', '86': 'Recommended',
        '88': 'Recommended', 'A7': 'Recommended', 'K6': 'Recommended', 'J8': 'Recommended', '76': 'Recommended',
        '77': 'Recommended', 'A6': 'Recommended', 'K5': 'Recommended', 'J7': 'Recommended', '75': 'Recommended',
        '66': 'Recommended', 'A5': 'Recommended', 'K4': 'Recommended', 'T9': 'Recommended', '65': 'Recommended',
        '55': 'Recommended', 'A4': 'Recommended', 'K3': 'Recommended', 'T8': 'Recommended',
        '44': 'Recommended', 'A3': 'Recommended', 'K2': 'Recommended',
        '33': 'Recommended', 'A2': 'Recommended',
        '22': 'Recommended',



    }

    try:
        finder = card_combinations[cards]
        print(finder)
    except KeyError:
        try:
            rev = cards[::-1]
            finder_2 = card_combinations[rev]
            print(finder_2)
        except KeyError:
            print('Խաղաքարտը չի գտնվել։ Տվյալ կոմբինացիան խորհուրդ չի տրվում։')
