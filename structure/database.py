#! usr/bin/env python3
import psycopg2 as postgre


class DataBaseManager:
	def __init__(self, db_name, ):
		self.name = db_name

	def connection(self, content, values=None):
		connect = postgre.connect(f'dbname={self.name}')
		with connect:
			curr = connect.cursor()
			curr.execute(content, values or [])
		return curr

	def data_select(self, table_name, card_name, player_count=None):
		query = f'''SELECT card_name FROM {table_name} WHERE card_name='{card_name}'  '''
		if player_count:
			query = f'''
			SELECT {player_count} FROM {table_name} WHERE card_type='{card_name}' '''

		query_fetch = self.connection(query).fetchone()
		return query_fetch
