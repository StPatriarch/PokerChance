from structure.commands import PercentsSelectCommand
from language.languages import ArmenianLanguage, RussianLanguage, EnglishLanguage
from joint.instruments import IsValid, PositionsList


class Interface:
	def __init__(self, language_name, language):
		self.lang = language_name
		self.language = language

	def choose(self):
		print(self.language.greeting)
		PositionsList().print_positions_list()
		data = self.language.positions_data()
		percent_value = self.percent_validation(data)
		extras = self.user_input_results(percent_value)
		return self.language(data).positions_choose(extras)

	@staticmethod
	def percent_validation(data):
		try:
			percent = ''.join([str(value) for value in PercentsSelectCommand().execute(data)])
		except TypeError:
			return None
		return percent

	def user_input_results(self, percent_value):
		return {
			'answer_one': self.additional('answer_one', percent_value),
			'answer_two': self.additional('answer_two')
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
	while not IsValid.is_valid(choice, option):
		choice = input('incorrect')
	return option[choice.upper()]


def print_languages(languages):
	for key, value in languages.items():
		print(f'{key} - {value}')
	print()


if __name__ == '__main__':
	print_languages(languages_list)
	chosen = user_choice(languages_list)
	chosen.choose()


