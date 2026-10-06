import pandas as pd	
from logger import logger


def transform_customer(df):
    logger.info('ETL start')

    orignal_count=len(df)
    df=df.drop_duplicates()
    duplire=orignal_count-len(df)
    logger.info(f'total records is {orignal_count}')
    logger.info(f'duplicate records deleted is {duplire}')

    missing_cust=df['customer_id'].isnull().sum()
    df=df.dropna(subset='customer_id')
 
    logger.info(f'total remove null records is {missing_cust}')

    logger.info(f'final total records is {len(df)}')

    return df
