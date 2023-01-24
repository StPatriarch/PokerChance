from structure.commands import CardsSelectCommand
from joint.toolbox import Tools


class LocalInterface:
	def __init__(self, data):
		self.data = data
		self.position = data['Position'].lower()
		self.players = data['Players']
		self.cards = data['Cards']

	def positions_choose(self, extras):
		try:
			card_value = CardsSelectCommand().execute(self.data) or CardsSelectCommand()\
				.execute(Tools.corrector(self.data))
			if not card_value:
				raise TypeError
			print(extras['answer_one'])
		except TypeError:
			print(extras['answer_two'])
