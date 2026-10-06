import snowflake.connector
import configparser
from snowflake.connector.pandas_tools import write_pandas
from logger import logger

try:
    def load_customer(df):
        logger.info('Snowflake Database connection start')

        config=configparser.ConfigParser()

        config.read('config.ini')

        account=config['SNOWFLAKE']['account']
        user=config['SNOWFLAKE']['user']
        password=config['SNOWFLAKE']['password']
        warehouse=config['SNOWFLAKE']['warehouse']
        database=config['SNOWFLAKE']['database']
        schema=config['SNOWFLAKE']['schema']

        conn=snowflake.connector.connect(account=account,
                                    user=user,
                                    password=password,
                                    warehouse=warehouse,
                                    database=database,
                                    schema=schema)

        df.columns = df.columns.str.upper()

        success,chunks,rows,output=write_pandas(conn,df,table_name='STG_CUSTOMERS',database=database,schema=schema,auto_create_table=False)

        logger.info(f'load sccussful {success}')
        logger.info(f'row loadded {rows}')

        
        
except Exception as e:
    logger.error(f'Snowflake connection failed {e}')
