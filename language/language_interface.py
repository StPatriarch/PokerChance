from structure.commands import CardsSelectCommand


class LocalInterface():
	def __init__(self, data):
		self.data = data
		self.position = data['Position'].lower()
		self.players = data['Players']
		self.cards = data['Cards']

	def positions_choose(self, extras):
		try:
			card_value = CardsSelectCommand().execute(self.data)
			if not card_value:
				self.data['Cards'] = self.data['Cards'][::-1]
				card_value = CardsSelectCommand().execute(self.data)
				if not card_value:
					raise TypeError()

			message = extras['answer_one']
			print(message)
		except TypeError:
			print(extras['answer_two'])

