import snowflake.connector
import configparser

config=configparser.ConfigParser()

config.read('config.ini')

account=config['SNOWFLAKE']['account']
user=config['SNOWFLAKE']['user']
password=config['SNOWFLAKE']['password']
warehouse=config['SNOWFLAKE']['warehouse']
database=config['SNOWFLAKE']['database']
schema=config['SNOWFLAKE']['schema']

conn=snowflake.connector.connect(account=account,user=user,password=password,warehouse=warehouse,database=database,schema=schema)

print('connection scussefully')

conn.close()
