from logger import logger
from extract import extractdata,get_connection
from transform import transform_customer
from load import load_customer
from last_version import get_last_version


def main():
    conn=None

    try:

        conn=get_connection()

        logger.info('Get last version')
        last_version = get_last_version(conn)
        logger.info(f'Update last version is {last_version}')
        
        cursor=conn.cursor()
        cursor.execute("SELECT CHANGE_TRACKING_CURRENT_VERSION()")
        new_version=cursor.fetchone()[0]
        logger.info(f'new version is {new_version}')


        logger.info('data extract function start')
        df=extractdata(conn,last_version)
        logger.info('data extract function end')

        logger.info('data transform function start')
        df=transform_customer(df)
        logger.info('Data transform function end')
        
        logger.info('Data Load Function Start')

        df=load_customer(df)

        logger.info('Data load function End')

        logger.info('ETL process complited')

        cursor.execute("""update ETL_WATERMARK set LAST_VERSION=? WHERE PROCESS_NAME = 'CUSTOMERS'""",(new_version,))

        logger.info(f'New version updated id {new_version}')
        conn.commit()
        
        conn.close()

    except Exception as e:

        logger.error(f'ETL process fail {e}')

        raise

if __name__=="__main__":
    main()

