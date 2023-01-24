from structure.database import DataBaseManager
from abc import ABC, abstractmethod


DB = DataBaseManager('poker_chance_base')


class Command(ABC):
	@abstractmethod
	def execute(self, data):
		pass


class PercentsSelectCommand(Command):
	def execute(self, data):
		return DB.data_select('players', data['Cards'], f'p_{data["Players"]}')


class CardsSelectCommand(Command):
	def execute(self, data):
		return DB.data_select(data['Position'], data['Cards'])
