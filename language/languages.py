from language.language_interface import LocalInterface
from joint.toolbox import Tools
valid_positions = ['D', 'E', 'L']
valid_players = [f'{i}' for i in range(1, 10)]


class ArmenianLanguage(LocalInterface):
	greeting = '''
Ողջույն, սա պարզ պոկերային նախնական ձեռքի հնարավորության հաշվիչ է | վերսիա 0.1.0. 
Դուք ընդհամենը պետք է մուտքագրեք ձեր խաղային դիրքը, խաղացողների քանակը  և նախնական խաղաքարտերը։ Այն կհաշվի
ձեր քարտերի հաղթելու հավանականությունը տոկոսներով։
Ծրագիրը հաշվի չի առնում խաղաքարտերի մաստային պատկանելությունը։ \U00002660  \U00002665  \U00002666  \U00002663
'''

	@staticmethod
	def positions_data():
		return {
			'Position': Tools().user_inputs('Մուտքագրեք ձեր դիրքը: ', valid_positions),
			'Players': Tools().user_inputs('Մուտքագրեք մրցակիցների քանակը: ', valid_players),
		}

	@staticmethod
	def card_data():
		return Tools().user_inputs('Մուտքագրեք ձեր խաղաքարտերը: ')

	@staticmethod
	def other_data(data, percent=None):
		answers = {
			'answer_one': f'Ձեր խաղաքարտերի հաղթելու հավանականությունը՝ {percent} % է',
			'answer_two': 'Խաղաքարտերը չեն գտնվել։ Քարտերը խորհուրդ չեն տրվում ձեր դիրքի համար։'
		}
		return answers.get(data)


class RussianLanguage(LocalInterface):
	greeting = '''
Приветствую, это простой калькулятор для начальних рук в покере | версия 0.1.0. 
Вы просто должны ввести вашу позоцию, число играков и начальные руки. Оно посчитает вероятность 
выигрыша ваших карт в процентах. 
Программа не принимает во внимание масти карт. \U00002660  \U00002665  \U00002666  \U00002663
'''

	@staticmethod
	def positions_data():
		return {
			'Position': Tools().user_inputs('Введите вашу позицию: ', valid_positions),
			'Players': Tools().user_inputs('Введите число оппонентов: ', valid_players),
		}

	@staticmethod
	def card_data():
		return Tools().user_inputs('Введите ваши карты: ')

	@staticmethod
	def other_data(data, percent=None):
		answers = {
			'answer_one': f'Возможность выигрыша ваших карт составляет {percent}%',
			'answer_two': 'Карты не найдены. Не рекомендованная комбинация карт для вашего позиции.'
		}
		return answers.get(data)


class EnglishLanguage(LocalInterface):
	greeting = '''
Hello, this is simple poker Starting hands chance calculator | version 0.1.0. 
You should just enter your position, your starting hands number of players and your starting hands. 
It calculates the probability winning your cards in percentage.
Program it's take into consideration card suits. \U00002660  \U00002665  \U00002666  \U00002663
'''

	@staticmethod
	def positions_data():
		return {
			'Position': Tools().user_inputs('Enter your Position: ', valid_positions),
			'Players': Tools().user_inputs('Enter number of Players: ', valid_players),
		}

	@staticmethod
	def card_data():
		return Tools().user_inputs('Enter your cards: ')

	@staticmethod
	def other_data(data, percent=None):
		answers = {
			'answer_one': f'The possibility of winning your cards is {percent}%',
			'answer_two': 'Cards not found. Not recommended combination of cards for your position.'
		}
		return answers.get(data)
