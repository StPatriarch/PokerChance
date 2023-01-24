from structure.commands import PercentsSelectCommand as PerComm
from language.languages import ArmenianLanguage, RussianLanguage, EnglishLanguage
from joint.toolbox import Tools, PercentChance


class Interface:
	def __init__(self, language_name, language):
		self.lang = language_name
		self.language = language

	def choose(self):
		print(self.language.greeting)
		Tools.print_positions_list()
		self.data_serialize()
		return self.data_deserialize()

	def data_serialize(self):
		data = self.language.positions_data()
		Tools.serialize(data=data)

	def data_deserialize(self):
		dump = Tools.deserialize()
		while True:
			data = {
				'Position': dump['Position'],
				'Players': dump['Players'],
				'Cards': self.language.card_data()
			}
			extras = self.processing_additional_data(data=data)
			return self.language(data).positions_choose(extras)

	def percent_validation(self, data):
		try:
			dat = Tools.value_len_correction(data=data.copy())
			if not dat:
				self.data_deserialize()
			percents = PercentChance(data=dat).extract()
			if isinstance(percents, list):
				chances = ' - '.join(i for i in percents)
				return chances
			return percents
		except TypeError:
			return None

	def processing_additional_data(self, data):
		chance_value = self.percent_validation(data)
		extras = self.user_input_results(chance_value)
		return extras

	def user_input_results(self, chance_value):
		return {
			'answer_one': self.language.other_data('answer_one', chance_value),
			'answer_two': self.language.other_data('answer_two')
		}

	def additional(self, data, percent=None):
		return self.language.other_data(data, percent)

	def __str__(self):
		return self.lang


languages_list = {
	'H': Interface('ՀԱՅԵՐԵՆ ԼԵԶՈՒ ', ArmenianLanguage),
	'R': Interface('РУССКИЙ ЯЗЫК', RussianLanguage),
	'E': Interface('ENGLISH LANGUAGE', EnglishLanguage),
}


def user_choice(option):
	choice = input('մուտքագրեք։  |  input:  |  введите: \n ')
	while not Tools.is_valid(choice, option):
		choice = input('incorrect')
	return option[choice.upper()]


def print_languages(languages):
	for key, value in languages.items():
		print(f'{key} - {value}')
	print()
