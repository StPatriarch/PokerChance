from language.language_interface import LocalInterface
from joint.toolbox import Tools
VALID_POSITIONS = ['D', 'E', 'L']
VALID_PLAYERS_COUNT = [f'{i}' for i in range(1, 10)]
VERSION_NUMBER = '0.1.1'


class ArmenianLanguage(LocalInterface):
	greeting = f'''
Ողջույն, սա պարզ պոկերային նախնական ձեռքի հնարավորության հաշվիչ է | վերսիա {VERSION_NUMBER}. 
Դուք ընդհամենը պետք է մուտքագրեք ձեր խաղային դիրքը, խաղացողների քանակը  և նախնական խաղաքարտերը։ Այն կհաշվի
ձեր քարտերի հաղթելու հավանականությունը տոկոսներով։
Ծրագիրը հաշվի չի առնում խաղաքարտերի մաստային պատկանելությունը։ \U00002660  \U00002665  \U00002666  \U00002663
'''

	@staticmethod
	def positions_data():
		return {
			'Position': Tools.user_inputs('Մուտքագրեք ձեր դիրքը: ', VALID_POSITIONS),
			'Players': Tools.user_inputs('Մուտքագրեք խաղացողների քանակը: ', VALID_PLAYERS_COUNT),
		}

	@staticmethod
	def card_data():
		return Tools.user_inputs('Մուտքագրեք ձեր խաղաքարտերը: ', length=True)

	@staticmethod
	def other_data(data, percent=None):
		answers = {
			'answer_one': f'Ձեր խաղաքարտերի հաղթելու հավանականությունը՝ {percent} % է',
			'answer_two': 'Խաղաքարտերը չեն գտնվել։ Քարտերը խորհուրդ չեն տրվում ձեր դիրքի համար։'
		}
		return answers.get(data)


class RussianLanguage(LocalInterface):
	greeting = f'''
Приветствую, это простой калькулятор для начальних рук в покере | версия {VERSION_NUMBER}. 
Вы просто должны ввести вашу позоцию, число играков и начальные руки. Оно посчитает вероятность 
выигрыша ваших карт в процентах. 
Программа не принимает во внимание масти карт. \U00002660  \U00002665  \U00002666  \U00002663
'''

	@staticmethod
	def positions_data():
		return {
			'Position': Tools.user_inputs('Введите вашу позицию: ', VALID_POSITIONS),
			'Players': Tools.user_inputs('Введите число игрокив: ', VALID_PLAYERS_COUNT),
		}

	@staticmethod
	def card_data():
		return Tools.user_inputs('Введите ваши карты: ', length=True)

	@staticmethod
	def other_data(data, percent=None):
		answers = {
			'answer_one': f'Возможность выигрыша ваших карт составляет {percent}%',
			'answer_two': 'Карты не найдены. Не рекомендованная комбинация карт для вашего позиции.'
		}
		return answers.get(data)


class EnglishLanguage(LocalInterface):
	greeting = f'''
Hello, this is simple poker Starting hands chance calculator | version {VERSION_NUMBER}. 
You should just enter your position, your starting hands number of players and your starting hands. 
It calculates the probability winning your cards in percentage.
Program it's take into consideration card suits. \U00002660  \U00002665  \U00002666  \U00002663
'''

	@staticmethod
	def positions_data():
		return {
			'Position': Tools.user_inputs('Enter your Position: ', VALID_POSITIONS),
			'Players': Tools.user_inputs('Enter number of Players: ', VALID_PLAYERS_COUNT),
		}

	@staticmethod
	def card_data():
		return Tools.user_inputs('Enter your cards: ', length=True)

	@staticmethod
	def other_data(data, percent=None):
		answers = {
			'answer_one': f'The possibility of winning your cards is {percent}%',
			'answer_two': 'Cards not found. Not recommended combination of cards for your position.'
		}
		return answers.get(data)
