from structure.commands import CardsSelectCommand
from joint.toolbox import Tools


class LocalInterface:
	def __init__(self, data):
		self.data = data

	def positions_choose(self, extras):
		try:
			card_value = CardsSelectCommand().execute(self.data) or CardsSelectCommand()\
				.execute(Tools(self.data).reverse_corrector())
			if not card_value:
				raise TypeError
			print(extras['answer_one'])
		except TypeError:
			print(extras['answer_two'])
