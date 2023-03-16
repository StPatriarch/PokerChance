from rich.console import Console
from rich.table import Table
import pickle
from structure.commands import PercentSelectCommand as PerComm
from itertools import cycle
from collections import deque


class Validators:
	@staticmethod
	def is_valid(value, data):
		return value in data or value.upper() in data

	@staticmethod
	def user_inputs(label, criteria=None, length=None):
		value = input(f'{label}')
		if length:
			while len(value) != 2:
				value = input(f'{label}')
		if criteria:
			while not Validators.is_valid(value=value, data=criteria):
				value = input(f'{label}')
		return value.upper()


class Serialization:
	def __init__(self, data: dict):
		self.data = data

	def serialize(self):
		with open('temp', 'wb') as file:
			pickle.dump(self.data, file)

	@staticmethod
	def deserialize():
		with open('temp', 'rb') as file:
			dumped_file = pickle.load(file)
		return dumped_file


class Corrections:
	def __init__(self, data: dict):
		self.data = data

	def reverse_corrector(self):
		self.data['Cards'] = self.data['Cards'][::-1]
		return self.data

	def s_cards(self):
		suits = self.data['Cards'] + 's'
		self.data['Cards'] = suits
		return self.data

	def correct_position_by_players(self):
		_list = ['D', 'D_0', 'D_1']
		_dict = {
			6: ['E', 'E_0', 'L'],
			7: ['E', 'E_0', 'E_1', 'L'],
			8: ['E', 'E_0', 'E_1', 'L', 'L_0'],
			9: ['E', 'E_0', 'E_1', 'L', 'L_0', 'L_1']
		}
		if int(self.data['Players']) >= 6:
			_count = _dict.get(int(self.data['Players']))
			_list = _list + _count
		return _list


class Cycles:
	def __init__(self, data):
		self.position = data['Position']

	def queue_cycle(self,  p_list: list):
		deq = deque(p_list)
		try:
			idx = deq.index(self.position)
		except ValueError:
			idx = deq.index('D')
		deq.rotate(-idx)
		cycle_ = cycle(deq)
		return cycle_

	@staticmethod
	def position_(data):
		for i in data:
			return next(data)


class PercentChance(Corrections):
	def __init__(self, data: dict):
		super().__init__(data)
		self.data = data
		self.cards_ = [i for i in data['Cards']]

	def extract(self):
		percent = ''.join(
			[str(value) for value in PerComm().execute(self.data) or PerComm().execute(self.reverse_corrector())])
		if len(self.cards_) == len(set(self.cards_)):
			suit_cards = self._modify()
			return [percent, suit_cards]
		return percent

	def _modify(self):
		suit = ''.join(
			[str(value) for value in PerComm().execute(self.s_cards())])
		return suit


class Tools(Validators, Serialization, Corrections, Cycles):
	def __init__(self, data: dict):
		super().__init__(data)
		self.data = data
		self.position = data['Position']

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