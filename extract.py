import pandas as pd
import pyodbc
import configparser
from logger import logger

def get_connection():
    try:
        config=configparser.ConfigParser()

        config.read('config.ini')
	
        logger.info('connection start')
        server=config['SQL_SERVER']['server']
        database=config['SQL_SERVER']['database']
        username=config['SQL_SERVER']['username']
        password=config['SQL_SERVER']['password']
    
        conn=pyodbc.connect(f"driver=ODBC Driver 17 for SQL Server;"
                           f"server={server};"
                           f"database={database};"
                           f"uid={username};"
                           f"pwd={password};")

        return conn

    except Exception as e:
        logger.error(f'Sql connection fail{e}')

def get_last_version(conn):

    try:
        query="""SELECT LAST_VERSION FROM ETL_WATERMARK WHERE PROCESS_NAME = 'CUSTOMERS'"""

        cursor=conn.cursor()

        cursor.excute(query)

        row=cursor.fetchone()

        if row is None:
            raise Exception('Watermark not found')

        last_version=row[0]

        logger.info(f'last version is f{last_version}')

        return last_version

    except exception as e:
        logger.Exception(f'Error getting last version {e}')

        raise
    


def extractdata(conn,last_version):
    try:
        
        query= """
        SELECT
            ct.customer_id,
            c.customer_unique_id,
            c.customer_zip_code_prefix,
            c.customer_city,
            c.customer_state,
            ct.SYS_CHANGE_OPERATION AS choperation,
            ct.SYS_CHANGE_VERSION AS change_version
        FROM CHANGETABLE(CHANGES customers, ?) AS ct
        LEFT JOIN customers c
            ON c.customer_id = ct.customer_id
        """

        df=pd.read_sql(query,conn,params=(last_version,))
	
        logger.info('connection End')
        return df

    except Exception as e:
        logger.error('error:',e)
        raise

def fullload(conn):
    query="""select  c.customer_id,
            c.customer_unique_id,
            c.customer_zip_code_prefix,
            c.customer_city,
            c.customer_state
            from customers c"""

    df=pd.read_sql(query,conn)

    logger.info(f'full data loaded len is {len(df)} rows')

    return df
