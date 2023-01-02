from rich.console import Console
from rich.table import Table


class IsValid:
	@staticmethod
	def is_valid(value, data):
		return value in data or value.upper() in data


class UserInputs:
	@staticmethod
	def user_inputs(label, criteria=None):
		value = input(f'{label}')
		if criteria:
			while not IsValid.is_valid(value=value, data=criteria):
				value = input(f'{label}')
		return value.upper()


class PositionsList:
	def print_positions_list(self):
		table = Table(title="Positions list")
		table.add_column("Symbol", justify="right", style="cyan", no_wrap=True)
		table.add_column("Designation", style="magenta")

		table.add_row("D ", "Dealer | Small Blind | Big Blind")
		table.add_row("E ", "Early Position | Middle Position")
		table.add_row("L ", "Last Position")

		console = Console()
		console.print(table)
