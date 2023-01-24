from rich.console import Console
from rich.table import Table
import pickle
from structure.commands import PercentsSelectCommand as PerComm


class Tools:
	@staticmethod
	def is_valid(value, data):
		return value in data or value.upper() in data

	def user_inputs(self, label, criteria=None):
		value = input(f'{label}')
		if criteria:
			while not self.is_valid(value=value, data=criteria):
				value = input(f'{label}')
		return value.upper()

	@staticmethod
	def print_positions_list():
		table = Table(title="Positions list")
		table.add_column("Symbol", justify="right", style="cyan", no_wrap=True)
		table.add_column("Designation", style="magenta")

		table.add_row("D ", "Dealer | Small Blind | Big Blind")
		table.add_row("E ", "Early Position | Middle Position")
		table.add_row("L ", "Last Position")

		console = Console()
		console.print(table)

	@staticmethod
	def serialize(data):
		with open('serialized_dump', 'wb') as file:
			pickle.dump(data, file)

	@staticmethod
	def deserialize():
		with open('serialized_dump', 'rb') as file:
			d_file = pickle.load(file)
		return d_file

	@staticmethod
	def value_len_correction(data):
		value = data['Cards']
		try:
			if len(value) != 2:
				raise ValueError()
			return data
		except ValueError:
			return None

	@staticmethod
	def corrector(data):
		data['Cards'] = data['Cards'][::-1]
		return data

	@staticmethod
	def s_cards(data):
		value = data['Cards']
		suite = value + 's'
		data['Cards'] = suite
		return data


class PercentChance(Tools):
	def __init__(self, data: dict):
		self.data = data
		self.cards = [i for i in data['Cards']]

	def extract(self):
		percent = ''.join(
			[str(value) for value in PerComm().execute(self.data) or PerComm().execute(super().corrector(self.data))])
		if len(self.cards) == len(set(self.cards)):
			suit_cards = self._modify()
			return [percent, suit_cards]
		return percent

	def _modify(self):
		suit = ''.join(
			[str(value) for value in PerComm().execute(super().s_cards(self.data)) or PerComm().execute(
				Tools.s_cards(super().corrector(self.data)))])
		return suit
