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
		Tools(data).serialize()

	def data_deserialize(self):
		tool = Tools(Tools.deserialize())
		p_list = tool.correct_position_by_players()
		while True:
			data = {
				'Position': tool.data['Position'],
				'Players': tool.data['Players'],
				'Cards': self.language.card_data()
				}
			Tools({
				'Position': tool.position_(p_list),
				'Players': tool.data['Players'],
			}).serialize()
			print(data)
			extras = self.processing_additional_data(data=data)
			return self.language(data).positions_choose(extras)

	@staticmethod
	def percent_validation(data):
		try:
			percents = PercentChance(data=data.copy()).extract()
			if isinstance(percents, list):
				percents = ' - '.join(i for i in percents)
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
