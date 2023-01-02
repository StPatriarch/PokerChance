import subprocess
import os

folder = os.path.dirname(os.path.abspath(__file__))
dump = os.path.join(folder, 'postgres_2_dump.sql')


class DumpRestore:
	def __init__(self, dump_name=None):
		self.dump = dump_name
		self.user = os.getlogin()
		self.base = 'poker_chance_base'

	def create_base(self):
		return subprocess.call(f'psql -U {self.user} -c "create DATABASE {self.base};"', shell=True)

	def file_dump(self):
		return subprocess.call(f'psql  {self.base} < {self.dump}', shell=True)


if __name__ == '__main__':
	DR = DumpRestore(dump_name=dump)
	DR.create_base()
	DR.file_dump()

