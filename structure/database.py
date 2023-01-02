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

	def data_select(self, table_name, criteria_1, criteria_2=None):
		query = f'''SELECT card_name FROM {table_name} WHERE card_name='{criteria_1}'  '''
		if criteria_2:
			query = f'''
			SELECT {criteria_2} FROM {table_name} WHERE card_type='{criteria_1}' '''

		query_fetch = self.connection(query).fetchone()
		return query_fetch
